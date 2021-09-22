# Homogeneous Coordinates

## Composite Transformations

A rigid transformation can be described completely as a composition of translations and rotations.

Given this, we wish to define a new group of matrices that describes fully a rigid transformation involving:

1. $$p_{ab} \in \mathbb{R^3}$$ : coordinates of the origin of $$B$$
2. $$R_{ab} \in SO(3)$$ : orientation of $$B$$ relative to $$A$$

We define a new space, $$SE(3)$$, as the concatenation of these two components.

$$
SE(3) : \{ (p, R) | p \in \mathbb{R^3}, R \in SO(3)\}
$$

We can also think of $$SE(3)$$ as a transformation $$g_{ab}$$.

$$
p_{a} = g_{ab} p_b = q_{ab} + R_{ab} p_b
$$

## Homogeneous Coordinates

In an effort to generalize our expressions to matrix multiplications, we describe $$SE(3)$$ in terms of **homogeneous coordinates**.

$$
g_{ab} = 
\begin{bmatrix}
R_{ab} & p_{ab} \\
0 & 1
\end{bmatrix}
$$

By adding this extra dimension  to our transformation, we can transform points through multiplication.

$$
p_b = g_{ab} p_b = 
\begin{bmatrix}
R_{ab} & p_{ab} \\
0 & 1
\end{bmatrix} 
\cdot
\begin{bmatrix}
p_b \\ 1
\end{bmatrix}
$$

It is important to note that the bottom row of a vector indicates whether or not it should be interpreted as a point or a vector. 

As we have already discussed, vectors do not have a starting position, and are only defined by their orientation. This is reflected in the above transformation, which would result in $$\begin{bmatrix} R_{ab} \vec{v}_b \\ 0 \end{bmatrix}$$ for an input vector $$\vec{v}_b$$.

## SE\(3\) \(Special Euclidian Group\)

We can now redefine $$SE(3)$$ :

$$
SE(3) : \{ 
\begin{bmatrix}
R & p \\
0 & 1
\end{bmatrix}
\in \mathbb{R^4},
p \in \mathbb{R^3}, R \in SO(3)
\}
$$

It can be shown that $$SE(3)$$ forms the \(special euclidian\) group:

> 1. Closed: $$ g_1 \cdot g_2 \in SE(3)$$
> 2. Identity: $$ I_4 $$
> 3. Inverse: $$ g^{-1} = \begin{bmatrix}  R^T & -R^Tp \\ 0 & 1 \end{bmatrix}$$
> 4. Associativity: \(follows from matrix multiplication\)

It can be shown that $$SE(3)$$ is a rigid transformation:

> 1. Lengths Preserved: $$\lVert gp - gq \rVert = \lVert p - q \rVert$$
> 2. Angles Preserved: $$g(\vec{u} \times \vec{v})  = g \vec{u} \times g \vec{v}$$

