tower = [[None],
	 [176,None],
	 [80,None,112],
	 [36,None,None,60],
	 [16,None,None,None,32],
	 [7,None,None,None,None,None],
	 [3,None,None,None,None,None,None]
	]

# get the number of empty spaces
n = 0
for floor in tower:
	n += sum(x is None for x in floor)

while n > 0:
	for i in range(len(tower)-1):
		for j in range(len(tower[i])):
			triplet = [tower[i][j],tower[i+1][j],tower[i+1][j+1]]
			if (sum(x is None for x in triplet) > 1) or (sum(x is None for x in triplet) == 0):
				continue
			if triplet[0] == None:
				tower[i][j] = triplet[1] + triplet[2]
				n += -1
			if triplet[1] == None:
				tower[i+1][j] = triplet[0] - triplet[2]
				n += -1
			if triplet[2] == None:
				tower[i+1][j+1] = triplet[0] - triplet[1]
				n += -1

for floor in tower:
	print(floor)
