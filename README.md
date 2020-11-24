## Machine Learning without using any library, not even math. K-Means applied on random trigonometrically scattered and clustered data points

_Reading level: average/high_

**Article overview**

-   How this idea came to be. Why should you care. Personal thoughts.
-   We want to understand how things work.
-   We will implement a machine learning algorithm without using any library.
-   We will implement random, sqrt, sine, cosine without using any library
-   The mental steps to implement everything you need both DATA and Algorithm.
-   Lack of data doesn't stop algorithms. Sometimes you don't have data but you can make it so that it tests what you want.
-   **_Where there is a will there is a way._**

**Introduction**

In my opinion everyone should see what's under the bonnet of your car, at least one in a lifetime. You should be curious to know how things work. Explore TVs, video games consoles, mobile phones, mould, yeast, eggs! I did all these and I suggest you doing it too... I never opened up a human being, yet... don't worry.

One of the most beautiful things I know is the so called logical thinking, or algorithmic thinking, if you want to make it sound cooler. I see algorithms as a synonym of logic. Unlike other sciences, in mathematics et similia, you don't really need to memorise things by heart, even if you don't remember anything, you can derive it.

In machine learning one of the easiest and yet most powerful algorithms for unsupervised learning is K-Means, which essentially groups things that are closer for one reason, call it similar shape, colour, geometrical distance. K-Means also has the great advantage of being very easy to implement.

**In this article, we will walk through the implementation of K-Means and we will apply in on data we will generate: a scattered trigonometric random function. All this will be done without importing ANY library, not even to calculate sine, cosine, square roots and so on.**

To perform K-Means we need two things: the algorithms and the data, in the following paragraph I will describe my reasoning, if you just want the code, scroll down to the dedicated section.

**Let's reason together**

I will use a mind-map to help me walk you though this beautiful journey under the bonnet of mathematical calculation and machine learning which lead to creating a data set and the implementation of K-Means. This is how I broke down the problem:

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/K-means%20without%20libs.png" width=700>


**The Algorithm: K-Means**

Believe it or not, this is the easy part: [**K-Means**](https://en.wikipedia.org/wiki/K-means_clustering). The algorithm is based on [**clustering**](https://en.wikipedia.org/wiki/Cluster_analysis) (A) things together according to some property. For the sake of this article, we are using geometrical distance, the [**Euclidean distance**](https://en.wikipedia.org/wiki/Euclidean_distance) (B).

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/algo_flow.png" width=400>

Euclidean distance depends on [**square root**](https://en.wikipedia.org/wiki/Square_root)  (C ) which is part of the **math** library we do not want to use, thus, we are going to implement one possible way to calculate it. We will implement the [**Heron's methods**](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots) (D) which I like because it somewhat reminds me of [**back propagation**](https://en.wikipedia.org/wiki/Backpropagation): it makes a guess, estimates and errors, and feeds it back to the formula until it gets close to the real value.

This is all, the algorithm is a piece of cake.

**Input Data**

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/points_flow.png" width=400>

To test our implementation of K-Means, we want to generate a data set which contains scattered, grouped points (A). The choice is completely arbitrary so we choose to implement a generative function (B) which has two properties: periodicity, using trigonometric functions (C ), and randomness (D).

_Randomness_

To generate random numbers we needed, of course, a random number generator (A). Also in this case the first idea would be to import **random** library but well, we do not want to use it. Never mind, we can implement it using different techniques: [**bit-shifting**](https://en.wikipedia.org/wiki/Xorshift), an easy xor-based trick, or better, use a [**linear congruential generator**](https://en.wikipedia.org/wiki/Linear_congruential_generator) (C ) which is what C and other popular programming languages use. We will go for the latter, LCG, just because C is C.

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/random_flow.png" width=400>

At this point if we randomly generate points, let's say with -1<x<1 and -1<y<1, we will get a rectangle but, ideally, we want to create rounded shapes (clusters) thus we will bound (B) our generator with a [**circumference**](https://en.wikipedia.org/wiki/Circumference)  (D) x^2+y^2<r^2. In this way we will obtain sparse clumps of random dots.

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/scatter.png" width=400>

With this trick we could lay out clumps along a line or any curve but what would be the fun then? We are now going to implement some trigonometric functions (A) to distribute our clumps along some patterns. There are easier ways but I want to deliver the message that you can develop everything if you want and you can understand everything if you want.

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/trigo_flow.png" width=400>

Sine (C) and cosine (D) are implemented in the **math** library which once again, we do not want to use. Nevertheless, we can implement sine and cosine using our **_powerful friend_** [**Taylor series**](https://en.wikipedia.org/wiki/Taylor_series) (B) which actually require the [**factorial**](https://en.wikipedia.org/wiki/Factorial) (D) operations, which we can be easily implemented with [**recursion**](https://en.wikipedia.org/wiki/Recursion_(computer_science)) (there exist other ways but I like recursion).

We are done, we have understood what we need, let's see how to implement every bit.

**The shopping list**

1.  **Square root**: Heron's method (Back propagation?)
2.  **Euclidean distance**
3.  **Randomness**: linear congruential generator
4.  **Factorial**
5.  **Sine**: Taylor series
6.  **Cosine**: Taylor series
7.  **Random trigonometrically scattered and clustered points**
8.  **K-Means loop**

**Implementations**

REMARK: ll following code snippets are not "perfect" in terms of speed and memory usage, they are implemented to be easy to understand.

_Square root: Heron's method (Back propagation?)_

    def sqrt(s):
        x = s/2 # initial guess
        # Iterate until error is small
        while x**2 - s > 0.01  or x**2 - s < -0.01:
            x = ((s/x)+x)/2
        return x
<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/sqrt.png" width=400>

_Euclidean distance_

    def distance(v1,v2):
        # If one cluster is empty
        if len(v1)==0 or len(v2)==0:
            return 1000 # distance is infinite
        sum = 0
        for i in range(len(v1)):
            sum += ((v2[i]-v1[i])**2)
        return sqrt(sum)

_Randomness: linear congruential generator_

    # linear congruential method
    # x_i+1 = (a*X_n + c) mod m
    def myrand(x):
        x = hash(str(x)) # using a hash to have a large starging number
        c = 1013904223
        a = 1664525
        m = 2**32
        x = (a*x+c) % m
        return x/m # to get number between 0 and 1
        
<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/random.png" width=400>

_Factorial_

    # Recursive factorial
    def factorial(n):
        if n < 0:
            return -1 # Error, defined only for positive numbers
        if n == 1 or n == 0:
            return 1
        return n*factorial(n-1)

_Taylor sine series (input degrees)_

    # Tylor sin x in degrees
    def sin(x):
        x = (x*3.1416)/180 # assuming degrees as input
        s = 0
        for n in range(0,10):
            alpha = 2*n+1
            s = s + (((-1)**n)*(x**alpha))/factorial(alpha)
        return s
        
<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/sine.png" width=400>

_Taylor cosine series (input degrees)_

    # Tylor cos x in degrees
    def cos(x):
        x = (x*3.1416)/180
        s = 0
        for n in range(0,10):
            alpha = 2*n
            s = s + (((-1)**n)*(x**alpha))/factorial(alpha)
        return s
        
<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/cosine.png" width=400>

_Random trigonometrically scattered and clustered points_

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/trigo_pattern.png" width=400>

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

_K-Means loop_

Example with 8 clusters

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/c1.png" width=400>

Example with 12 clusters

<img src="https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/c2.png" width=400>

    new_assignment = []
    for n in range(iterations):
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

