

__mem__ = {}
class Magic(object):
    def __init__(self,*kw):
        self.attributes = kw
        __mem__['a'] = 1



if __name__ == "__main__":
    a = Magic('1')
    # print(a.a)
    print(dir(a))
    print(__mem__)