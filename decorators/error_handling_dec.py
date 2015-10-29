__author__ = 'dmakstc'


class ErrorHandlerPO(object):
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        def wr(*args):
            try:
                return func(*args)
            except Exception:
                    raise AssertionError(self.message)

        return wr
