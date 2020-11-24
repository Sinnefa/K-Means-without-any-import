# algorithm initialization
iterations = 20
nclusters = 12

nelms = 2000
ncoords = 2 

spreading = 0.3
clumpiness = 4

############ Math Functions ##############

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

# Taylor sin x in degrees
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

######## END Math Functions ##############

############ Algo Functions ##############
	
def centroid(l):
	if len(l)==0:
		return [0,0]
	res = [0,0]
	for i in range(len(res)):
		for a in l:
			res[i]+=elms[a][i]
	for i in range(len(res)):
		res[i]/=len(l)
	return res

def calculateCentroids(l):
	res = []
	for i in l:
		res.append(centroid(i))
	return res

def printClusters(l):
	for n,c in enumerate(l):
		print("cluster: "+str(n))
		for x in c:
			print(elms[x])
		print()
	print()
	
###############
# random points

elms = []
for i in range(nelms):
	v = []
		
	if ncoords > 2: # If more than two coordinates just random
		for n in range(ncoords):
			val = int(cos(n)+i)%clumpiness # Random function
			if myrand(i+myrand(n))>0.5: 
				val = -val
			else:
				val = +val
		
			if myrand(i+myrand(n))>0.5: 
				noise = sin(myrand(i+myrand(n)))*spreading
			else:
				noise = -sin(myrand(i+myrand(n)))*spreading
				
			v.append(val+noise)
	elif ncoords==2: # Two coordinates
		center = []
		for n in range(ncoords):
			val = int(cos(n)+i)%clumpiness # Random function
			if myrand(i+myrand(n))>0.5: 
				val = -val
			else:
				val = +val
			center.append(val)

		for n in range(ncoords):
			for a in range(1,1000): # attempting many times to get a good point
				x = myrand(i+myrand(n)*a) # just creating a random starting point
				y = myrand(n+myrand(i)/a) # depending on the two indices so that
							  # it is different
				# Randomly moving point in the 4 sections of a circle
				x = x if myrand(i+myrand(n))>0.5 else -x
				y = y if myrand(n+myrand(i))>0.5 else -y
				# Check if it is wthin the radius
				if x**2 + y**2 < spreading:
					center[0] = center[0]+x
					center[1] = center[1]+y
					break # as soon as we have a good point beak the loop

		v = center
	elms.append(v)

# Random assignment toclusters
clusters= []
for i in range(nclusters):
	clusters.append([])
for i in range(len(elms)):
	pos = i%nclusters
	clusters[pos].append(i)

print("kmeans")
print("clustering "+str(nelms)+" vectors with "+str(ncoords)+" components in "+str(nclusters)+" clustets")
centroids = calculateCentroids(clusters)
print("centroids")
print(centroids)
#print("elements")
#print(elms)
print()

#algorithm
print("-----")
	
new_assignment = []
for n in range(iterations):
	#print("Iteration: "+str(n))
	#printClusters(clusters)
	#print()


	centroids=calculateCentroids(clusters) # calculate centroids
	for i in range(nclusters):
		clusters[i]=[]
	for e in range(len(elms)): #loop all points
		best = 0
		bestd = 1000
		for c in range(nclusters): #loop over centroids
			d = distance(centroids[c],elms[e])
			if d < bestd:
				best = c
				bestd = d
		if len(clusters[best])==0:
			clusters[best]=[]
		clusters[best].append(e)

printClusters(clusters)
print()
