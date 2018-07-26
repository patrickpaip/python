class bacteria():
	def __init__(self,power):
		self.power=power
	def run():
		print("I am bacteria")

class animal(bacteria):
	__noofanimals=0
	def __init__(self,texture,legs,nose,tail):
		self.texture=texture
		self.legs=legs
		self.nose=nose
		self.tail=tail
		animal.noofanimals+=1
		super().__init__()
	def run(self,speed):
			pass
	def walk(self):
		pass
	def sleep(self):
		pass
	def aboutme(self):
		print (self.texture,self.legs)


lion.run(60)
lion=animal("liontype",6,1,1)
lion.aboutme()
print (animal.noofanimals)
print (lion.noofanimals)
tiger=animal("tigertype",4,1,1)
tiger.aboutme()
tiger.noofanimals=4
print (animal.noofanimals)
print (tiger.noofanimals)
delattr(lion,"legs")
lion.wings=10
print (lion.wings)
print ("legs:",hasattr(lion,"legs"))
print ("tail:",tiger.tail)


hasattr()
delattr()
getattr()