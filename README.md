## Machine Learning without using any library, not even math. K-Means applied on random trigonometrically scattered and clustered data points.

_Reading level: average/high_

**Article overview**

-   How this idea came to be. Why should you care. Personal thoughts.
-   We want to understand how things work.
-   We will implement a machine learning algorithm without using any library.
-   The mental steps to implement everything you need both DATA and Algorithm.
-   Lack of data doesn't stop algorithms. Sometimes you don't have data but you can make it so that it tests what you want.
-   **_Where there is a will there is a way._**

  

**Introduction**

In my opinion everyone should see what's under the bonnet of your car, at least one in a lifetime. You should be curious to know how things work. Open TVs, video games consoles, mobile phones are things! I did all these and I suggest you doing it too... I never opened up a human being, yet... don't worry.

One of the most beautiful things I know is the so called logical thinking, or algorithmic thinking, if you want to make it sound cooler. I see algorithms as a synonym of logic. Unlike other sciences, in mathematics et similia, you don't really need to memorise things by heart, even if you don't remember something, you can derive it.

In machine learning one of the easiest and yet most powerful algorithms for unsupervised learning is K-Means, which essentially groups things that are closer for one reason, call it similar shape, colour, geometrical distance. K-Means also has the great advantage of being very easy to implement.

In this article I will guide you through the implementation of K-Means applied over a scattered trigonometric random function without importing ANY library, not even to calculate sine, cosine, square roots and so on.

To perform K-Means we need two things: the algorithms and the data, in the following paragraph I will describe my reasoning, if you want to just to the code, go to the next session.

**Let's reason together**

I will use a mind-map to help me walk you though this beautiful journey under the bonnet of mathematical calculation and machine learning. This is how I broke down the problem:
![mindmap](https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/K-means%20without%20libs.png)

**Algorithms (K-Means)**

Believe it or not, this is the easy part: [**K-Means**](https://en.wikipedia.org/wiki/K-means_clustering). The algorithm is based on [**clustering**](https://en.wikipedia.org/wiki/Cluster_analysis) (A) things together according to some property. For the sake of this article I chose to use geometrical distance calculated thought the [**Euclidean distance**](https://en.wikipedia.org/wiki/Euclidean_distance) (B).
![algoflow](https://github.com/Sinnefa/K-Means-without-any-import/blob/main/imgs/algo_flow.png)
