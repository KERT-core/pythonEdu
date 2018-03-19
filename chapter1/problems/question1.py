#/usr/bin/python3


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	WARNING = '\033[93m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'	


def question1():
	print(bcolors.HEADER + "Enter String you want to print inverted" + bcolors.ENDC)
	a = input()
	print('\n\n\n')
	print(bcolors.OKBLUE + "inveretd string is" + bcolors.ENDC)
	print(a[::-1])
	print('\n\n\n')

def question2():
	print(bcolors.WARNING + "Input the word that you want to change from txt file" + bcolors.ENDC)
	initWord = input()
	print('\n')
	print(bcolors.WARNING + "Input the word that you want the word to be changed to" + bcolors.ENDC)
	newWord = input()
	
	print('\n\n\n')
	print(bcolors.OKGREEN + "Finished" + bcolors.ENDC)
	print('\n\n')

	with open('input.txt', 'r') as f:
		with open('inputchanged.txt', 'w') as fc:
			contents = f.readlines()
			for lines in contents:
				fc.write(lines.replace(initWord, newWord))
				


if __name__ == '__main__':
	question2()
