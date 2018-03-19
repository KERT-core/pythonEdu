with open("input.txt", "r") as f:
	contents = f.readlines()
	for lines in contents:
		print(lines.replace('Protocol', 'protocol'))
