
from pyh import *
import time
import collections
from MjMap import *


__mem__ = []

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


class Dfs(object):
	def __init__(self):
		self.mem=[]
	def changename(self):
		selfname = type(self).__name__
		fname = chr(ord(selfname[0])+32) + selfname[1:]
		return fname,selfname

	def dfs(self,path=[]):

		def changenameany(classname):
			fname = chr(ord(classname[0])+32) + classname[1:]
			return fname
		def genetag(tagname):
			if tagname == "site":
				tag = site(site = "s0")
			tag = eval(tagname+"()")
			tag = eval('tag.'+changenameany(tagname))
			return tag


		fname,selfname =self.changename()
		dbar = getattr(MjMap,'dbar')
		if "customize" in dbar[selfname]:
			customize = dbar[selfname][1][1]
			eval(fname + '(customize)')
		else:
			q = collections.deque()
			q.append([selfname,[[]]])
			while q:
				cur,paths= q.popleft()
				tmp = list(paths)
				Flag = False
				for e in dbar[cur]:
					tmp.append([e[0],e[1]])
					q.append([e[0],tmp])
					tmp = list(paths)
					Flag = True
				if not Flag:
					# self.mem.append(paths)
					__mem__.append(paths)
					path.append(paths)
			tags,num = [],[]
			for i in path:
				for e in i:
					print(e,'edges')
					if e:
						tags.append(genetag(e[0]))
						num.append(e[1])
			# print(self.mem)
			while len(tags)>=2:
				parent = tags[-2]
				kid = tags[-1]
				while num[-1]>0:
					parent<<kid
					num[-1]-=1
				tags.pop()
				num.pop()
			tmp = eval(fname+'()')
			while num[-1]>0:
				tmp<<tags[0]
				num[-1]-=1
			setattr(self,fname,tmp)




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
		# print(strogeom)
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
		self.iterations = iterations
		self.solver = solver
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

class Default(Change,Dfs):
	def __init__(self):
		# selfname = type(self).__name__
		self.mem = []
		self.default = default()
		# dbar = getattr(MjMap,'dbar')
		# for v in dbar[selfname]:
		# 	tmp = eval(v+'()')
		# 	if v == 'Joint':
		# 		ojoint = joint(type="hinge",pos="0 0 0",axis="1 0 0",limited="false",range="-180 180",damping="1000")
		# 		self.default<<ojoint
		# 	else:
		# 		eval('self.default<<tmp.'+chr(ord(v[0])+32)+v[1:])
		self.dfs()
		# Print.__init__(self)


class Texture(Change):
	def __init__(self,name="texplane",type="2d",builtin="checker",rgb1=".25 .25 .25",rgb2=".3 .3 .3",width="512",height="512",mark="cross",markrgb=".8 .8 .8"):
		self.name = name 
		self.type = type
		self.builtin = builtin
		self.rgb1 = rgb1
		self.rgb2 = rgb2
		self.width = width
		self.height = height
		self.mark = mark
		self.markrbg = markrgb 
		self.addAtt()
		Print.__init__(self)

class Material(Change):
	def __init(self,name="matplane",reflectance="0.3",texture="texplane",texrepeat="1 1",texuniform="true"):
		self.name = name
		self.reflectance = reflectance
		self.texture = texture
		self.texrepeat = texrepeat
		self.texuniform = texuniform
		self.addAtt()
		Print.__init__(self)




class Asset(Change):
	def __init__(self):
		selfname = type(self).__name__
		self.Asset = asset()
		dbar = getattr(MjMap,'dbar')
		for v in dbar[selfname]:
			if not dbar[v]:
				tmp = eval(v+'()')
				# if v == 'Joint':
				# 	ojoint = joint(type="hinge",pos="0 0 0",axis="1 0 0",limited="false",range="-180 180",damping="1000")
				# 	self.default<<ojoint
				# else:
				eval('self.default<<tmp.'+chr(ord(v[0])+32)+v[1:])
		Print.__init__(self)

class Connect(Change):
	def __init__(self,active="true", name='1bar34', body1='bar3', body2='bar4', anchor='-0.05 -1 -1'):
		# self.connect = connect()
		self.active = active
		self.name =  name
		self.body1 = body1
		self.body2 = body2
		self.anchor =  anchor
		self.addAtt()
		Print.__init__(self)

class Equality(Change,Dfs):
	def __init__(self):
		self.equality = equality()
		self.mem = []
		# selfname = type(self).__name__
		# for v in dbar[selfname]:
		# 	tmp = eval(v+'()')
		# 	# if v == 'Joint':
		# 	# 	ojoint = joint(type="hinge",pos="0 0 0",axis="1 0 0",limited="false",range="-180 180",damping="1000")
		# 	# 	self.default<<ojoint
		# 	# else:
		# 	eval('self.default<<tmp.'+chr(ord(v[0])+32)+v[1:])
		self.dfs()
		Print.__init__(self)

class Spatial(Change,Dfs):
	def __init__(self,name="S1" ,width="0.02"):
		# is very special because there are several sites there but they cann't set name tag
		self.name = name
		self.width = width
		self.mem = []
		self.dfs()

		# self.addAtt()

class Tendon(Change,Dfs):
	def __init__(self):
		self.tendon = tendon()
		self.mem = []
		self.dfs()
class Actuator(Change,Dfs):
	def __init__(self):
		self.actuator = actuator()
		self.mem = []
		self.dfs()


class Site(Change):
	def __init__(self,customize = 0,name="s2",pos="0 1 0",size="0.1"):
		if not customize:
			self.name = name
			self.pos = pos
			self.size = size
			# self.mem = []
			# self.dfs()
			self.addAtt()
		else:
			for att,value in customize:
				setattr(self,att,value)
			self.addAtt()
		# Print.__init__(self)










class Geom(Change,Dfs):
	def __init__(self,fromto="0 0 0  0 1 0",name="bar",rgba=".5 .1 .1 1",size="0.04",type="capsule"):
		self.name = name
		self.type = type
		self.size = size
		self.fromto = fromto
		self.rgba = rgba
		# self.addAtt()
		self.mem = []
		self.dfs()

		Print.__init__(self)

class Joint(Change,Dfs):
	def __init__(self,name="center2",range="-90 90"):
		self.name= name
		self.range = range
		# self.addAtt()
		self.mem = []
		self.dfs()

		Print.__init__(self)

class Light(Change,Dfs):
	def __init__(self,directional="true",diffuse=".8 .8 .8",specular = ".2 .2 .2",pos="0 0 5",dir="0 0 -1"):
		# Body.__init__(self,pos)
		self.directional = directional
		self.diffuse = diffuse
		self.specular = specular
		self.pos = pos
		self.dir = dir
		self.mem = []
		self.dfs()
		# self.addAtt()
		Print.__init__(self)



class Body(Change,Dfs):
	# def __init__
	def __init__(self,pos):
		self.body = body(pos=pos)
		self.mem = []
		self.dfs()
		Print.__init__(self)


# if __name__ == '__main__':
	# ogeom = Geom("steel","barmoohow","1000","1 0 0  0 100 0")
	# ojoint = Joint()
	# osite = Site()
	# olight = Light()
	# b = Body("0 0 1000")
	# d = Body("0 10 0")

	# print(b.body.attributes['pos'])

	# b.change("pos","0 0 3")
	# for i in dir(b):
	# 	if '_' not in i:
	# 		print(i)
	# print(b.body.attributes['pos'])
	# print(b.body.pos)
	# page = PyH('My wonderful PyH page')
	# page<<b.body
	# print(page.render())