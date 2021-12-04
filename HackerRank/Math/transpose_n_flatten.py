import numpy



#$Transpose

my_array = numpy.array([
    [1,2,3],
    [4,5,6]
])
print(numpy.transpose(my_array))


#@Flatten

my_array = numpy.array([
    [1,2,3],
    [4,5,6]
])
print(my_array.flatten())




#@TASK
listo = []
n, m = [int(x) for x in input().split()]

for i in range(n):
    listo.append([int(x) for x in input().split()])


print(numpy.transpose(listo))
print(numpy.array(listo).flatten())