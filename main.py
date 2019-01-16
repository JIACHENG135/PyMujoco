
from pyh import *



class Site(object):
	def __init__(self,name="s2",pos="0 1 0",size="0.1"):
		self.name = name
		self.pos = pos
		self.size = size
class Geom(object):
	def __init__(self,name="bar",types="capsule",size="0.04",fromto="0 0 0  0 1 0",rgba=".5 .1 .1 1"):
		self.name = name
		self.type = types
		self.size = size
		self.fromto = fromto
		self.rgba = rgba
class Joint(object):
	def __init__(self,name="center2",ranges="-90 90"):
		self.name= name
		self.range = ranges


class Light(object):
	def __init__(self,directional="true",diffuse=".8 .8 .8",specular = ".2 .2 .2",pos="0 0 5",dir="0 0 -1"):
		Body.__init__(self,pos)
		self.directional = directional
		self.diffuse = diffuse
		self.specular = specular
		self.pos = pos
		self.dir = dir
class Change(object):
	def change(self,ob,attrname,value):
		ob.attributes[attrname] = value
		return ob
class Body(object):
	def __init__(self,pos,ogeom,ojoint,osite):
		self.body = body(pos=pos)
		# self.body<<h1('nihao',cl='123')
		# print(self)
		# self.body<<worldbody('hellow',name='floor')
		# ogeom = Geom()
		self.body<<geom(name=ogeom.name,type=ogeom.type,size=ogeom.size,fromto=ogeom.fromto,rgba=ogeom.rgba)
		self.body<<joint(name=ojoint.name,range=ojoint.range)
		self.body<<site(name=osite.name,pos=osite.pos,size=osite.size)
		self.body<<light(name='ljc')
		# self.pos = pos
	# def __repr__(self):
	# 	return self.render()
	# def change(self,strpos):
	# 	self.body.attributes['pos'] = strpos
		# for i in self.body.attributes.items():
		# 	print(i)


if __name__ == '__main__':
	ogeom = Geom("steel","barmoohow","1000","1 0 0  0 100 0")
	ojoint = Joint()
	osite = Site()
	# olight = Light()
	b = Body("0 0 1000",ogeom,ojoint,osite)
	d = Body("0 10 0",ogeom,ojoint,osite)
	# b.body<<d.body
	# print(b.body.attributes['pos'])
	# b.change('123 12 456')
	mchange = Change()
	print(b.body.attributes["pos"]) 
	b.body = mchange.change(b.body,'pos','12 3 2 5 6')
	print(b.body.attributes["pos"]) 

	for i in b.body.geom.attributes:
		print(i,)
	page = PyH('My wonderful PyH page')
	page<<b.body
	# print(page.render())