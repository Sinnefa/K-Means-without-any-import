import matplotlib.pyplot as plt
import math
import random
from decimal import Decimal

# Recursive factorial
def factorial(n):
	if n < 0:
		return -1 # Error, defined only for positive numbers
	if n == 1 or n == 0:
		return 1
	return n*factorial(n-1)

# Heron's method
def sqrt(s):
	x = s/2 # initial guess
	# Iterate until error is small
	while x**2 - s > 0.01  or x**2 - s < -0.01:
		x = ((s/x)+x)/2
	return x

# Tylor sin x in degrees
def sin(x):
	x = (x*3.1416)/180 # assuming degrees as input
	s = 0
	for n in range(0,10):
		alpha = 2*n+1
		s = s + (((-1)**n)*(x**alpha))/factorial(alpha)
	return s

# Tylor cos x in degrees
def cos(x):
	x = (x*3.1416)/180
	s = 0
	for n in range(0,10):
		alpha = 2*n
		s = s + (((-1)**n)*(x**alpha))/factorial(alpha)
	return s

# linear congruential method
# x_i+1 = (a*X_n + c) mod m
def myrand(x):
	x = hash(str(x)) # using a hash to have a large starging number
	c = 1013904223
	a = 1664525
	m = 2**32
	x = (a*x+c) % m
	return x/m # to get number between 0 and 1

# Euclidean distance
def distance(v1,v2):
	# If one cluster is empty 
	if len(v1)==0 or len(v2)==0:
		return 1000 # distance is infinite
	sum = 0
	for i in range(len(v1)):
		sum += ((v2[i]-v1[i])**2)
	return sqrt(sum)





fig = plt.figure()
t = []
for i in range(0,360):
	t.append(sin(i))

s = []
for i in range(0,360):
	s.append(math.sin(math.radians(i)))

plt.plot(t,"-",c="blue", label="Without import")
plt.plot(s,":", linewidth=3,c="red", label="With import")
plt.title("Sine")
plt.xlabel("Degree")
plt.ylabel("Sine")
plt.legend(loc="upper left")
plt.show()



fig = plt.figure()
t = []
for i in range(0,360):
	t.append(cos(i))

s = []
for i in range(0,360):
	s.append(math.cos(math.radians(i)))

plt.plot(t,"-",c="blue", label="Without import")
plt.plot(s,":", linewidth=3,c="red", label="With import")
plt.title("Cosine")
plt.xlabel("Degree")
plt.ylabel("Cosine")
plt.legend(loc="upper left")
plt.show()



fig = plt.figure()
t = []
for i in range(0,100):
	t.append(sqrt(i))

s = []
for i in range(0,100):
	s.append(math.sqrt(i))

plt.plot(t,"-",c="blue", label="Without import")
plt.plot(s,":", linewidth=3,c="red", label="With import")
plt.title("Square root")
plt.xlabel("Value")
plt.ylabel("Square root")
plt.legend(loc="upper left")
plt.show()



fig = plt.figure()
x = []
for j in range(0,50):
	for i in range(0,50):
		x.append(myrand(i+myrand(j)))

y = []
for j in range(0,50):
	for i in range(0,50):
		y.append(myrand(j+myrand(i)))

x1 = []
for j in range(0,50):
	for i in range(0,50):
		x1.append(random.random())

y1 = []
for j in range(0,50):
	for i in range(0,50):
		y1.append(random.random())

plt.scatter(x,y,c="blue",marker="o", label="Without import")
plt.scatter(x1,y1,c="red",marker="x", label="With import")
plt.title("Random")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.legend(loc="upper left")
plt.show()


