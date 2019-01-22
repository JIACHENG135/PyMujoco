
from pyh import *
import time
from MjMap import *
class Print(object):
	def __init__(self):
		if hasattr(self,"name"):
			print(type(self).__name__,self.__getattribute__("name"),"has attributes as below: ")
		else:
			print(type(self).__name__,"has attributes as below: ")
		for i in dir(self):
			# print(i)
			if '_' not in i:
				print(i,":",self.__getattribute__(i))

		print("\n")
			# print(i,":",self.__getattribute__(i))

class Write(object):
	def __init__(self,name,body):

		page = PyH("Author: Jiacheng Liu")
		page<<body
		GEN_HTML = name + ".html"  #命名生成的html
		f = open(GEN_HTML,'w')
		message = page.render()
		f.write(message)
		f.close()




class Change(object):
	def change(self,attrname,value):
		if type(self).__name__ == "Body":
			print("yihoo")
			self.body.attributes[attrname] = value
			setattr(self.body,attrname,value)
		else:
			setattr(self,attrname,value)
	def add(self,attrname,value):
		setattr(self, attrname, value)

	def addAtt(self):
		selfname = type(self).__name__
		selfname = chr(ord(selfname[0])+32) + selfname[1:]
		# obname = type(ob).__name__
		# obname = chr(ord(obname[0])+32) + obname[1:]
		# self.size = size(nconmax = self.nconmax,)

		strogeom = selfname + '('
		for i in dir(self):
			if '_' not in i and i not in ['add','change','fstr','addAtt',selfname]:
				strogeom += i+'=' + 'self' + '.'+i + ','
		strogeom += ')'
		print(strogeom)
		tmp = eval(strogeom)
		# eval
		setattr(self,selfname,tmp)



	def fstr(self,ob):
		# this method is a build-in function to add some attr to self.body
		obname = type(ob).__name__
		# print(obname)
		obname = chr(ord(obname[0])+32) + obname[1:]
		strogeom = 'self.body<<' + 'self.' + obname 
		# for i in dir(ob):
		# 	if '_' not in i and i not in ['add','change','fstr','addAtt']:
		# 		strogeom += i+'=' + 'ob' + '.'+i + ','
		# strogeom += ')'
		eval(strogeom)
		# return strogeom




class Option(Change):
	def __init__(self,timestep = "0.005",iterations="50",solver="Newton",tolerance="1e-10",gravity= "0 0 0",collision = "predefined"):
		self.timestep = timestep
		self.iterations = pos
		self.solver = size
		self.tolerance = tolerance
		self.gravity = gravity
		self.collision = collision
		self.addAtt()
		Print.__init__(self)

class Size(Change):
	def __init__(self,njmax = "500",nconmax = "100",nstack = "2000"):
		# self.size = size()
		self.njmax = njmax
		self.nconmax = nconmax
		self.nstack = nstack
		self.addAtt()
		Print.__init__(self)



class Rgba(Change):
	def __init__(self,haze = ".3 .3 .3 1"):
		self.haze = haze
		self.addAtt()
		Print.__init__(self)

class Visual(Change):
	def __init__(self):
		orgba = Rgba()
		self.visual = visual()
		self.visual<<rgba(haze=orgba.haze)
		Print.__init__(self)


class Muscle(Change):
	def __init__(self,ctrllimited = "true",ctrlrange="0 1"):
		self.ctrlrange = ctrlrange
		self.ctrllimited = ctrllimited

		self.addAtt()

		Print.__init__(self)

class Default(Change):
	def __init__(self):
		selfname = type(self).__name__
		# eval('self')
		self.default = default()
		# selfname = chr(ord(selfname[0]+32))
		dbar = getattr(MjMap,'dbar')
		# print(dir(MjMap))
		for v in dbar[selfname]:
			tmp = eval(v+'()')
			if v == 'Joint':
				ojoint = joint(type="hinge",pos="0 0 0",axis="1 0 0",limited="false",range="-180 180",damping="1000")
				self.default<<ojoint
			# tampname = type(tmp)
			else:
				eval('self.default<<tmp.'+chr(ord(v[0])+32)+v[1:])
		Print.__init__(self)









class Site(Change):
	def __init__(self,name="s2",pos="0 1 0",size="0.1"):
		self.name = name
		self.pos = pos
		self.size = size
		self.addAtt()

		Print.__init__(self)

class Geom(Change):
	def __init__(self,fromto="0 0 0  0 1 0",name="bar",rgba=".5 .1 .1 1",size="0.04",type="capsule"):
		self.name = name
		self.type = type
		self.size = size
		self.fromto = fromto
		self.rgba = rgba
		self.addAtt()

		Print.__init__(self)

class Joint(Change):
	def __init__(self,name="center2",range="-90 90"):
		self.name= name
		self.range = range
		self.addAtt()

		Print.__init__(self)

class Light(Change):
	def __init__(self,directional="true",diffuse=".8 .8 .8",specular = ".2 .2 .2",pos="0 0 5",dir="0 0 -1"):
		# Body.__init__(self,pos)
		self.directional = directional
		self.diffuse = diffuse
		self.specular = specular
		self.pos = pos
		self.dir = dir
		self.addAtt()
		Print.__init__(self)



class Body(Change):
	# def __init__
	def __init__(self,pos):
		self.body = body(pos=pos)
		Print.__init__(self)


if __name__ == '__main__':
	ogeom = Geom("steel","barmoohow","1000","1 0 0  0 100 0")
	ojoint = Joint()
	osite = Site()
	olight = Light()
	b = Body("0 0 1000",ogeom,ojoint,osite)
	d = Body("0 10 0",ogeom,ojoint,osite)

	print(b.body.attributes['pos'])

	b.change("pos","0 0 3")
	for i in dir(b):
		if '_' not in i:
			print(i)
	print(b.body.attributes['pos'])
	print(b.body.pos)
	page = PyH('My wonderful PyH page')
	page<<b.body
	print(page.render())