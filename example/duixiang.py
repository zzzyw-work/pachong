"""
面向对象的实践
"""
class people:
	name = 'zzz'
	age = 0
	__weight = 0

	#构造方法
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
	def work(self):
		print("%s talk : i am %d old."%(self.name,self.age))

class student(people):
	grade = ''
	def __init__(self, n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade = g
	def work(self):
		print("%s talk: i am %d old,in %d rank"%(self.name,self.age,self.grade))

if __name__ == '__main__':
	s = student('ken',10,60,3)
	s.work()

		

