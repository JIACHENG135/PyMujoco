
from main import *
from MjMap import *

# print(MjMap.dbar)
ogeom = Geom("steel","barmoohow","1000","1 0 0  0 100 0")

ojoint = eval("Joint()")
osite = Site()
olight = Light()
size = Size()
omuscle = Muscle()
odef = Default()
print(odef.default.render())
# osite<<olight
# olight.addAtt(osite)
b = Body("0 0 1000")
omuscle.muscle<<size.size
b.body<<ojoint.joint
b.body<<omuscle.muscle
b.body<<odef.default

Write("Dbar_wirte_test",b.body)
