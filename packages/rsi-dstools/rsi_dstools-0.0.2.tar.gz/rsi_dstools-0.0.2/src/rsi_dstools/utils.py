''' Utility routines.'''
import sys
from io import StringIO


class Capturing(list):
    # Capture stdout print() statements into object for logging
    #
    # Usage: (use `with` context modifier)
    #     with Capturing(<prev_lines>) as output:
    #         do_something(my_object)
    #     print(output)
    #
    # Args:
    #   previous_lines (optional List(str))
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

    def __str__(self):
        return '\n'.join(self)

