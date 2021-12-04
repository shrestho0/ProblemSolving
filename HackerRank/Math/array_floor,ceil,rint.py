


#@ LEARNING PART
import numpy
numpy.set_printoptions(sign=' ')
my_array = numpy.array([input().split()], float)
print(numpy.floor(*my_array))
print(numpy.ceil(*my_array))
print(numpy.rint(*my_array))