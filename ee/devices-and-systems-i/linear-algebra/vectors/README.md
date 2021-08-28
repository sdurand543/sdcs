# Vectors

## Intro

A vector is a list of scalar values.

Here is an example of a vector$$\vec{u} = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}$$.

It is very common for vectors and matrices to be described using indices that start from one. For instance, $$\vec{u}_1$$ would give us the value 2, the first value in our vector. In a language that starts with the zero-index \(like Python\), we could use `u[0]` to get the same value.

## Coordinate Space

Vectors are often used as implicit mappings of index to property value. 

For example, the three elements of the aforementioned $$\vec{u}$$ might describe the three dimensional coordinates of an object located somewhere in the physical world.

**Statement:** The coordinate space of $$\vec{u}$$ is in $$\mathbb{R^3}$$ \(meaning the three dimensional space of real numbers\).

While the above statement is not wrong, I would argue that it really doesn't add too much clarity to what on earth we are talking about / our **coordinate space**. 

* By convention, you probably assumed that the coordinate ordering was $$x \ y \ z$$, but it may be something else \(ex. $$ z \ x \ y $$\). 
* Another consideration is where the axes derive. There are no inherent $$x \ y \  z$$ axes given by the universe, so we will have to decide on our own where these axes lie. 

As an EECS designer, it is important to have a complete understanding of the coordinate space you are working in at all times. 

**Revised Statement:** The coordinate space of $$\vec{u}$$ is in $$\mathbb{R^3}$$ defined by the $$ x \ y \ z $$ unit vector describing my line of sight \(a specific vector in $$\mathbb{R^3}$$\), measured in meters.

As a bit of a teaser, $$\mathbb{R^3}$$ is the [vector space](vector-space.md) \(forward link\) of our model.

> Summary: Coordinate spaces are the link between your mathematical representation and the world space you are representing. In some ways, you can consider them as definitional and descriptive \(even when they seem intangible\), adding specific meaning to your vector and matrix data.

## Orientation

Once we get into matrices, it will be very important to distinguish between the two possible orientations of vectors \(because they will be treated like a matrix with width 1\). 

Since all vectors and matrices contain logical state for their coordinate space, operations on them have logical meaning. If the dimensions of your data don't match your coordinate space you will run into problems performing vector and matrix operations or you will be unable to interpret your numerical results.

1. Row-Vectors / Horizontal Vectors

{% tabs %}
{% tab title="Vector" %}
$$
\vec{u} = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}
$$
{% endtab %}

{% tab title="LaTeX" %}
\vec{u} = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}
{% endtab %}

{% tab title="numpy" %}
```python
u = np.array([1, 2, 3])
```
{% endtab %}
{% endtabs %}

1. Column-Vectors / Vertical Vectors

{% tabs %}
{% tab title="Vector" %}
$$
\vec{v} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
$$
{% endtab %}

{% tab title="LaTeX" %}
\vec{v} = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}
{% endtab %}

{% tab title="numpy" %}
```python
v = np.array([[1], [2], [3]])
```
{% endtab %}
{% endtabs %}

There is a common mathematical markup language known as LaTeX. While it may seem somewhat tedious to write out vectors in this, it is standard and produces polished results. In the above examples, I provided you with both so you could appreciate its design.

