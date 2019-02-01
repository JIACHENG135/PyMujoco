from collections import *
class MjMap(object):
    dbar = defaultdict(list)
    dbar["Mujoco"] = [("Option",1),("Size",1),("Asset",1),("Equality",1),("Default",1),("Tendon",1),("Actuator",1)]
    # ("Visual",1),
    dbar["Default"] = [("Joint",1),("Muscle",3),("Site",1)]
    dbar["Visual"] = [("Rgba",1)]
    dbar["Asset"] = [("Texture",2),("Material")]
    dbar["Equality"] = [("Connect",2)]
    dbar["Tendon"] = [("Spatial",3)]
    # dbar["Spatial"] = ["customize",("customize",["site","s1"]),("Site",2)]
    dbar["Spatial"] = [("Site",2)]

    # dbar["Actuator"] = ["customize",("customize",["name","s1","tendon","s1"]),("Muscle",2)]
    dbar["Actuator"] = [("Muscle",2)]
    # dbar["Site"] = [()]


    def __init__(self):
        print(self.dbar.items())
    def get(self,mapname):
        return self.__getattribute__(mapname)

    def add(self,mapname,attrname):
        self.__getattribute__(mapname)[attrname] = sefl.__getattribute__(attrname)

