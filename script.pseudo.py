import random
seed = random.randint(400,500)
class enc:
	@classmethod
	def magic(cls,x,y):
		if x > y:
			 temp = x
		else:
			 temp = y
		while(True):
			 if((temp % x == 0) and (temp % y == 0)):
				  res = temp
				  break
			 temp += 1
		return res
	
	@classmethod
	def flawless_encryption(cls,string):
		string += 's'
		arr = []
		for i in enumerate(string):
            #ord(string) converts a string to ASCII
			arr.append(enc.magic(ord(string[i[0]]), seed))
		return arr

enc.flawless_encryption(<wechat number>) == [57385, 51896, 55389, 58383, 49401, 50898, 57385]
# True
