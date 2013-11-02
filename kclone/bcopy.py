import sys, string, os

fin = open(sys.argv[1],'r')
fout = open('test.dat','w')

data = []

for line in fin.readlines():
	data.append(line)

fin.close()

for i in range(len(data)):
	fout.write(data[i])

fout.close()
	
