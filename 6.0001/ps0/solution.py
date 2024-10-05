import math
import numpy

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

# Math.pow returns a float and ** keep the original types
print("X**y = ", math.pow(x, y))

# Is numpy.log2 more accurate than math.log?
# Or does it just automatically round which makes it more user-friendly
print("log(x) = ", numpy.log2(x))
