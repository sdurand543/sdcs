# Rigid Motion

## Structures

In this series, we will be careful with our language in order to be explicit about the real-world interpretation of the Linear Algebra \(LA\) structures we are dealing with. 

In particular, while LA [vectors](../../../ee/devices-and-systems-i/linear-algebra/#vector) are general and multi-purpose, we will start by denoting the interpretive difference between points and vectors.

### Point

A point describes the location of an object. Below is a **trajectory**, a point as a function of $$t$$.

$$
p(t) = \begin{bmatrix} x(t) \\ y(t) \\ z(t) \end{bmatrix}
$$

### Vector

A vector describes the difference / displacement between two points.

$$
\vec{v} = p - q
$$

### Matrix

A matrix is a 2D collection of values.

$$
A \in \mathbb{R^{n \times m}} \ \ \ \ \ \
A = \begin{bmatrix}
r_{11} \ r_{12} \ \dots \ \ r_{1m} \\
r_{21} \ r_{22} \ \dots \ r_{2m} \\
\vdots \\
r_{n1} \ r_{n2} \ \dots \ \ r_{nm}
\ \end{bmatrix}
$$

