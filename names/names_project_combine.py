import os

'''
path = 'namesbystate/'

names_file = open("namesbystate.txt","w+")

names_file.truncate(0)

files = os.listdir(path)

for x in files:

	if x.endswith('.TXT'):

		file = path + x
		open_file = open(file,"r")
		for x in open_file:
			names_file.write(x)
'''

###########################################################


# path = 'namesbystate/'
path = 'names/'

# names_file = open("namesbystate.txt","w+")
names_file = open("names.txt","w+")

names_file.truncate(0)

files = os.listdir(path)

for x in files:
	year = x[3:7]
	if x.endswith('.txt'):
		file = path + x
		# print(file)
		open_file = open(file,"r")
		for x in open_file:
			names_file.write(year + ',' + x)


###########################################################


		# print(open_file)

# directory = os.listdir(path)

# for x in directory:
	# if x.endswith('.TXT'):

	# 	f = open(path+'/'+x)
	# 	lines = f.read()
	# 	print(lines[1:50])
	# print(x)

# file = open(path + 'AK.TXT','r')

# for x in file:
# print(file.readlines())


# for line in file:
# 	print(line, end = "")

# print(y)

