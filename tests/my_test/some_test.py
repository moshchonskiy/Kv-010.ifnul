class ErrorIgnore(object):
    def __call__(self, function):
        def wr(*args, **kwargs):
            try:
                print "fuck1"
                return function(*args, **kwargs)

            except:
                print "fuck2"
        return wr




@ErrorIgnore()
def myfunction():
    print "myfunction"
    assert 1 == 2

myfunction()