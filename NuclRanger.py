import sys
import itertools

# input file from command line arguments
input_file = sys.argv[1]

input_file_pointer = open(input_file, 'r')

lines = input_file_pointer.readlines()

list_of_numbers=[]

for line in lines:
	line = line.strip() # strip whitespace
	if line: # only go on if the line was not blank
		list_of_numbers.append(int(line))
		print(list_of_numbers)
		
input_file_pointer.close()


# Utility Generator Function
def groupc(list_of_numbers):
    for x, y in itertools.groupby(enumerate(list_of_numbers), lambda (a, b): b - a):
        y = list(y)
        yield y[0][1], y[-1][1]

# printing original list
print("The original list is : " + str(list_of_numbers))

# Consecutive elements grouping list
# using enumerate() + groupby() + generator function + lambda
res = list(groupc(list_of_numbers))

# printing result
print("Grouped list is : " + str(res))

#writing pitput to file
output_file_pointer = open(input_file+".output", "a")
for row in res:
	print(str(row[0])+'\t'+str(row[1]))
	output_file_pointer.write(str(row[0])+'\t'+str(row[1])+'\n')
output_file_pointer.close()
