# Vectors

## Intro

A vector is the concise mathematical representation of a list of numerical values.

Here is an example of a vector$$u = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}$$.

It is very common for vectors and matrices to be described using indices that start from one. For instance, $$u_1$$ would give us the value 2. In a language like Python, we could use `u[1]` to acquire the same value.

## Coordinate Space

Vectors are often used as implicit mappings of index to property value. 

For example, the three elements of the aforementioned $$u$$ might describe the three dimensional coordinates of an object located somewhere in the physical world.

**Possible Statement:** The coordinate space of $$u$$ is in $$\mathbb{R^3}$$ \(meaning the three dimensional space of real numbers\).

While the above statement is not wrong, I would argue that it really doesn't add too much clarity to what on earth we are talking about / our **coordinate space**. 

* By convention, you probably assumed that the coordinate ordering was $$x \ y \ z$$, but it may be something else \(ex. $$ z \ x \ y $$\). 
* Another consideration is where the axes derive. There are no inherent $$x \ y \  z$$ axes given by the universe, so we will have to decide on our own where these axes lie. 

As an EECS designer, it is important to have a complete understanding of the coordinate space you are working in at all times. 

**Revised Statement:** The coordinate space of $$u$$ is in $$\mathbb{R^3}$$ defined by the $$ x \ y \ z $$ unit vector describing my line of sight \(a specific vector in $$\mathbb{R^3}$$\), measured in meters.

In Summary: Coordinate spaces are the link between your mathematical representation and the world space you are representing. In some ways, you can consider them as definitional and descriptive.

{% hint style="info" %}
It is very nice when our coordinate space is tangible and describes something we can clearly visualize. Later on, we will discuss coordinate space transforms that are more difficult to describe. Keep in mind that these spaces should still be thought of as descriptive environments mapping index to property value. This will make some things easier to grasp.
{% endhint %}

## Orientation

Once we get into matrices, it will be very important to distinguish between the two possible orientations of vectors \(because they will be treated like a matrix with width 1\). 

Since all vectors and matrices contain logical state for their coordinate space, operations on them have logical meaning. If the dimensions of your data are off you will run into problems due to a mismatch between your data and your coordinate space.

1. Row-Vectors / Horizontal Vectors

{% tabs %}
{% tab title="LaTeX" %}
$$
u = \begin{bmatrix} 2 \  3 \   4 \end{bmatrix}
$$
{% endtab %}

{% tab title="LaTeX Src" %}
```text
u = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}
```
{% endtab %}

{% tab title="numpy Src " %}
```text
u = np.array([2, 3, 4])
```
{% endtab %}
{% endtabs %}

1. Column-Vectors / Vertical Vectors

{% tabs %}
{% tab title="Latex" %}
$$
v = \begin{bmatrix} 2 \\   3 \\ 4 \end{bmatrix}
$$
{% endtab %}

{% tab title="Latex Src" %}
```text
v = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}
```
{% endtab %}

{% tab title="numpy Src" %}
```
v = np.array([[2],
          [3],
          [4]])
```
{% endtab %}
{% endtabs %}

To denote an element of a vector, 

There is a common mathematical markup language known as LaTeX. While it may seem somewhat tedious to write out vectors in this, it is standard and produces polished results. In the above examples, I provided you with both so you could appreciate its design.

## Operations

### Addition

Vector-vector addition is computed entry-wise, and is only defined for vectors of the same dimensions.

$$
\begin{bmatrix}  2 \\ 3 \\ 4 \end{bmatrix}
+
\begin{bmatrix} 7 \\ 4 \\ 10 \end{bmatrix}
=
\begin{bmatrix} 9 \\ 7 \\ 14 \end{bmatrix}
$$

Since we can negate all of the elements of a vector without any trouble, subtraction is can be reduced to element-wise addition after negating the subtrahend \(second argument\).

### Scaling

Vector-scalar multiplication is computed entry-wise.

$$
2
*
\begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}
=
\begin{bmatrix} 4 \\ 6 \\ 8 \end{bmatrix}
$$

### Multiplication

Vector-vector multiplication comes in several different flavors.

#### Dot Product

The dot product of two vectors is the sum of their element-wise products \(a scalar\).

$$
u * v = \sum_{i=1}^{n}{u_i * v_i}
$$

Dot products are useful for determining how similar two vectors / data points are \(more on this later\).

#### Cross Product

The cross product of two vectors $$u$$ and $$v$$ is the one that is perpendicular / orthogonal to both and whose magnitude is equal to the area of the parallelogram formed between them.

