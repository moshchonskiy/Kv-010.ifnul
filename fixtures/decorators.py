from functools import wraps

__author__ = 'Den'


class ErrorHandler(object):
    def __init__(self, message):

        self.message = message

    def __call__(self, func):
        def wr(*args):
            try:
                return func(*args)
            except Exception:
                raise AssertionError(self.message)
        return wr


def dec(error):
    def my_dec(func):
        @wraps(func)
        def wr(*args):
            res = func(*args)

            print args
            print res
            if res > 0:
                return res
            else:
                print "error = " + error
        return wr
    return my_dec
