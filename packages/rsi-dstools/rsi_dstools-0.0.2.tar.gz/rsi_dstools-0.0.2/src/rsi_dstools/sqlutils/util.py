'''A few homebrew speed-ups for implementing SQL Alchemy -based querying/insertion'''
import pandas as pd
# from debugpy import connect
import numpy as np
import os
# from matplotlib import pyplot as plt
# import pickle as pkl
from warnings import warn
import sqlalchemy as sql
from .sqlconfig import SQLConfig

'''
Example calls:
    with dbgen.gen_connection() as conn:
        datadf = pd.read_sql(('SELECT transactionId, Amount, Class FROM ccdata '
                            'WHERE Amount > 100 AND Class = 1'), 
            conn.connection)
    print(datadf.shape)
    datadf.head()
'''

def gettypes(_df):
    d = {}
    for k,val_type in zip(_df.dtypes.index,_df.dtypes):
        converts2flt = converts2int = False
        try:
            converts2flt = all([isinstance(float(v),float) for v in _df[k].values])
        except ValueError:
            pass
        if converts2flt:
            try:
                converts2int = all([isinstance(int(v),int) for v in _df[k].values])
            except ValueError:
                pass
        print(val_type, type(val_type))
        if ('object' in str(val_type)) and not(converts2flt):
            maxlen = _df[k].str.len().max()
            d[k] = sql.types.VARCHAR(10 if maxlen == 0 else maxlen)
        elif ('float' in str(val_type)) or (converts2flt and not(converts2int)):
            d[k] = sql.types.FLOAT(126)
        elif ('int' in str(val_type)) or converts2int:
            d[k] = sql.types.INTEGER()
        else:
            raise Exception(f'unknown handling of input type: {v}')
    return d

class ConnectCommand(object):
    def __init__(self,engine,meta,conn,parent=None):
        self.engine = engine
        self.meta = meta
        self.connection = conn
        self.parent_context = parent

    def close(self):
        if self.connection is not None:
            try:
                self.connection.close()
                self.connection = None
            except:
                pass

    def connect(self, new=False):
        if (self.connection is None) or new:
            self.connection = self.engine.connect() # pull metadata of a table

    def execute_query(self,query,values=None):
        ''' form query with one of below
                sql.select([<sql table object>])
                sql.insert([<sql table object>]).values(col0=val0,col1=val1,...)
                sql.update([<sql table object>]).values(attribute = new_value)
                sql.delete([<sql table object>])
            
            optionally adding 
                .where(condition)
                
            with 'insert' of many records, must provide secondary argument 
            to pass records along with query 'insert' method, i.e., as 
                execute(sql.insert(tbl), values_list)
            where
                values_list = [dict(col0=val0,col1=val1,...),dict(),...]


        '''
        ResultConn = self.connection.execute(query)
        ResultSet = None
        if True:
            # standard fetch execution
            ResultSet = ResultConn.fetchall()
        else:
            # better for large datasets
            flag = True
            while flag:
                partial_results = ResultConn.fetchmany(50)
                if(partial_results == []): 
                    flag = False
        # close query connection
        ResultConn.close()
        # convert SQL data query result to dataframe
        if ResultSet is None:
            return
        if sql.insert.__name__ != query.__class__.__name__ and 'selected_columns' in query.__dict__:
            return pd.DataFrame(ResultSet, columns=[c.name for c in query.selected_columns])

    def drop_table(self,table):
        tbl = self.get_table(table)
        return tbl.drop(self.engine)
    
    def drop_all_tables(self):
        return self.meta.drop_all(self.engine)
    
    def get_table(self,table):
        if isinstance(table,list):
            tbls = []
            for tbl in table:
                tbls.append(self.get_table(tbl))
            return tbls
        else:
            return sql.Table(table, self.meta, autoload=True, autoload_with=self.engine)
            
    def table_names(self):
        insp = sql.inspect(self.engine)
        return insp.get_table_names()
        
    def table_names_from_meta(self):
        return [t.name for t in self.meta.sorted_tables]
    
    def columns(self,table):
        tbl = sql.Table(table, self.meta, autoload=True, autoload_with=self.engine)
        return [c.name for c in tbl.columns]
    
    def insert_into_table(self,values,table):
        ''' this one is better for existing tables with complex/unique data types
            (the implicit types will be interpreted into the correct type)
        '''
        if isinstance(values,pd.DataFrame):
            ddata = values.to_dict()
            row_indices = list(list(ddata.values())[0].keys())
            recs = []
            for row in row_indices:
                recs.append({k:v[row] for k,v in ddata.items()})
            values = recs
        elif isinstance(values,dict):
            values = [values]
        elif isinstance(values,list):
            if len(values) == 0:
                return
            elif ~isinstance(values[0],dict):
                raise NotImplemented(f'list element type "{type(values[0])}" not handled')
        else:
            raise NotImplemented(f'values type "{type(values)}" not handled')
        _table = self.get_table(table)
        # insert_cmd = sql.insert(table).values(**values)
        # ResultConn = self.connection.execute(insert_cmd)
        return self.connection.execute(_table.insert(),values)


    def upload_df_to_table(self,df,tablename,if_exists='append', index=False, dtypes=None):
        ''' this one is better for creating/appending tables with no existing data 
            or having only simple data types
        '''
        if dtypes is None:
            coltypes = gettypes(df)
        else:
            coltypes = dtypes
        # print(f'\nCol types: {coltypes}')
        df.to_sql(name=tablename, con=self.engine, 
          if_exists=if_exists, # 'replace' / 'append'
          index=index, dtype=coltypes)
    
class ContextConnect(object):
    '''ContextConnect
    
        Usage: 
            with conn:
                <do pandas sql stuff>
        OR
            cmd = conn()
    '''
    def __init__(self,engine,meta):
        self.engine = engine
        self.meta = meta
        self.open = False
        self.connection = None
        self.open_commands = []

    def connect(self, new=False):
        if not(self.open) or new:
            self.open = True
            self.connection = self.engine.connect() # pull metadata of a table

    def close(self):
        if self.open and self.connection is not None:
            self.connection.close()
            self.connection = None
        self.open = False

    def close_all(self):
        for cmd in self.open_commands:
            if cmd.connection is not None:
                cmd.connection.close()
                cmd.connection = None
        self.open_commands = []

    def __call__(self,new=False) -> ConnectCommand:
        self.connect(new)
        cmd = ConnectCommand(self.engine, self.meta, self.connection, parent=self)
        if not(any(conn == cmd.connection for conn in self.open_commands)):
            self.open_commands.append(cmd)
        return cmd
       
    def __enter__(self):
        self.connect()
        return ConnectCommand(self.engine, self.meta, self.connection)
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()
        if exc_type is not None:
            raise exc_type.with_traceback(exc_value, exc_traceback)
    
class DbConnectGenerator(object):
    def __init__(self, *args, config=None, **connect_config):
        if isinstance(config, SQLConfig):
            self._connection_str = config.get_conn_str()
        elif (isinstance(connect_config,dict) and len(connect_config)) or (
                isinstance(config,dict) and len(config)):
            if (isinstance(config,dict) and len(config)):
                connect_config = config
            assert all([k in connect_config for k in [
                'dialect_driver','user','password','port','database']]), (
                'insufficient data in connect config dict')
            # database connection url
            self._connection_str = (f'{connect_config["dialect_driver"]}://'
                f'{connect_config["user"]}:'
                f'{connect_config["password"]}@{connect_config["host"]}:'
                f'{connect_config["port"]}'
                f'{("/"+connect_config["database"] if ("database" in connect_config) and connect_config["database"] is not None else "")}')
        elif not(args or config or connect_config):
            warn('no input credentials, empty connector')
            return None
        else:
            connect_url = args[0]
            assert isinstance(connect_url,str), (
                'cannot connect with data provided as '
                f'type: {type(connect_url)}; use dict or str')
            self._connection_str = connect_url
        self.engine = sql.create_engine(self._connection_str)
        self.meta = sql.MetaData(bind=self.engine)

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.connection_str    
    
    @property
    def connection_str(self):
        # obfuscate the PW
        if len(self._connection_str.split('@')) > 2:
            warn(('password might have an @ in it. This could confuse '
            'the denoting of the hostname; obfuscation of PW will not '
            'work, not printing/returning the connection string'))
            return None
        front, host_db = self._connection_str.split('@')
        dialect, userpw = front.split('//')
        user, pw = userpw.split(':')
        return '@'.join(['//'.join([dialect,':'.join([user,'******'])]),
                host_db])

    def gen_connection(self):
        return ContextConnect(self.engine, self.meta)


def execute_query(query, conn):
    '''functional execution of queries with SQLAlchemy - requires connection object'''
    ResultConn = conn.execute(query)
    ResultSet = None
    if True:
        # standard fetch execution
        ResultSet = ResultConn.fetchall()
    else:
        # better for large datasets
        while flag:
            partial_results = ResultConn.fetchmany(50)
            if(partial_results == []): 
                flag = False

    # close query connection
    ResultConn.close()

    # convert SQL data query result to dataframe
    if ResultSet is None:
        return
#     print(query.__dict__)
    return pd.DataFrame(ResultSet, columns=[c.name for c in query.selected_columns])