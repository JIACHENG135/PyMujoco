from collections import *
class MjMap(object):
    dbar = defaultdict(list)
    dbar["Mujoco"] = [("Option",1),("Size",1),("Visual",1),("Defaul",1),("Asset",1),("Worldbody",1),("Equality",1),("Tendon",1),("Actuator",1)]
    dbar["Default"] = [("Joint",1),("Muscle",3),("Site",1)]
    dbar["Visual"] = [("Rgba",1)]
    dbar["Asset"] = [("Texture",2),("Material")]
    dbar["Equality"] = [("Connect",2)]
    dbar["Tendon"] = [("Spatial",3)]
    dbar["Spatial"] = ["customize",("customize",("site",[])),("Site",3)]
    dbar["Actuator"] = [("Muscle",2)]
    # dbar["Site"] = [()]


    def __init__(self):
        print(self.dbar.items())
    def get(self,mapname):
        return self.__getattribute__(mapname)

    def add(self,mapname,attrname):
        self.__getattribute__(mapname)[attrname] = sefl.__getattribute__(attrname)

