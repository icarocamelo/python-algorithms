
sequence = [5,3,2,6,7,8,22,1]
unsorted = True
length = len(sequence) - 1

while unsorted:	
	unsorted = False
	for i in range(0,length):
			if sequence[i] > sequence[i+1]:								
				temp = sequence[i+1]
				sequence[i+1] = sequence[i]
				sequence[i] = temp
				unsorted = True

print sequence