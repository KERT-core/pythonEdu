import hashlib

def solution(text):
	hashcode = hashlib.md5()
	hashcode.update(text)
	password = hashcode.hexdigest()
	return password

if __name__ == "__main__":
	a = solution("therearenoone")
	print(a)