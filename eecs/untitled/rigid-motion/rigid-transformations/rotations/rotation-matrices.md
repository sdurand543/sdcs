# Rotation Matrices

## Rotation Matrix

### Definition

A rotation can be represented by an$$SO(3)$$ matrix $$R_{ab} = \begin{bmatrix} x_{ab} \ y_{ab} \ z_{ab} \end{bmatrix}$$.

This rotation matrix represents the configuration of a rigid body in frame $$B$$ $$w.r.t$$ the initial frame $$A$$.

The rotation matrix can also be used as a transformation to convert vectors from frame $$B$$ to frame $$A$$. Because $$R_{ab}$$ is invertible, and, more precisely, $$R_{ab}^{-1} = R_{ab}^T$$ \(because $$R_{ab}$$ is orthonormal\), we can easily find a transformation from frame $$A$$ to frame $$B$$.

$$
q_a = R_{ab} q_b
$$

$$
q_b = R_{ab}^T q_a
$$

The vector components of $$R_{ab} = \begin{bmatrix} x_{ab} \ y_{ab} \ z_{ab} \end{bmatrix}$$ can be found by representing the coordinate axes of the rotated frame \($$B$$\) in terms of the original frame \($$A$$\).

### Explanation

It may seem at first unintuitive to transform elements of the **target** frame $$B$$ to the **initial** frame $$A$$ using this matrix. However, we can illustrate the validity of this transform with a simple example:

Let's say we wish to represent a point on the $$i$$th coordinate axis of our target frame $$B$$. In frame $$B$$, the point is represented by the unit vector along the $$i$$th axis:$$e_i = \begin{bmatrix} 0 \ \dots \ 1 \dots \ 0\end{bmatrix}$$

If you want to represent this coordinate in your initial frame $$A$$, it will be represented by $$r_i$$, where $$r_i$$ is the axis represented in frame $$A$$. Hence, we get that $$q_a = R_{ab} q_b$$ \(and not the other way around\).

## Group

Rotation \($$SO(3)$$\) is a group under matrix multiplication.

Closure: $$ R_1 * R_2 \in SO(3)$$

$$
(R_1 R_2)^T (R_1 R_2) = 
R_2 ^T R_1 ^T R_1 R_2 =
R_2^T I R_2 =
R_2^T R_2 =
I
$$

$$
det(R_1 R_2) = det(R_1) * det(R_2) = 1 * 1 = 1
$$

Identity: $$ R * I = R$$

Inverse: $$ R * R^T = I$$

Associativity: $$ R_1 (R_2 R_3) = (R_1 R_2) R_3$$

## Rigid Transformation

Rotation \($$SO(3)$$\) is a rigid transformation.

Length: $$\lVert R(p - q) \rVert = \lVert p - q \rVert$$

$$
(R (p - q))^T (R (p - q))
$$

$$
(p - q)^T R^T R (p - q)
$$

$$
(p - q)^T (p -q)
$$

Orientation: $$ R(p \times q) = (Rp) \times (Rq)$$

$$
R(\hat{p}q)
$$

$$
R \hat{p} I q
$$

$$
R \hat{p} R^T R q
$$

$$
\widehat{(Rp)} R q
$$

