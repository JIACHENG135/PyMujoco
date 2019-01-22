from collections import *
class MjMap(object):
    dbar = defaultdict(list)
    dbar["Mujoco"] = ["Option","Size","Visual","Defaul","Asset","Worldbody","Equality","Tendon","Actuator"]
    dbar['Default'] = ['Joint','Muscle','Site']



    def __init__(self):
        print(self.dbar.items())
    def get(self,mapname):
        return self.__getattribute__(mapname)

    def add(self,mapname,attrname):
        self.__getattribute__(mapname)[attrname] = sefl.__getattribute__(attrname)

