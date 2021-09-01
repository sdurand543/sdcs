# Linear Dependence

## Linear Dependence

Informally, linear dependence refers to redundancy within data.

> Somewhat formally, a set of $$n$$ vectors $$\vec{v} = \begin{bmatrix} \vec{v}_1 \ \vec{v}_2, \ \dots \ \vec{v}_n \end{bmatrix}$$are **linearly dependent** iff
>
> 1. $$\exists$$ scalars $$\alpha_1, \alpha_2, \dots, \alpha_n$$$$s.t.$$$$\alpha_1 \vec{v}_1 + \alpha_2 \vec{v}_2 + \dots + \alpha_n \vec{v}_n = \vec{0}$$ and $$\exists$$ at least one $$\alpha_i \ne 0$$ \($$\exists$$ means "there exists" and $$s.t.$$ is short for "such that"\)
> 2. $$\exists \ i \ \ s.t. \ \ \vec{v}_i = \sum_{j \ne i}{\alpha_j v_j}$$ \(one of the vectors is a linear combination of the others\)
>
> Either condition is sufficient to prove linear independence and also to imply the other.
>
> **Linearly independent** vectors are those that are not linearly dependent.

### Examples

$$\vec{v}_1 = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$and $$\vec{v}_2 = \begin{bmatrix} -6 \\ -9 \end{bmatrix}$$ are linearly dependent for either / both of the following:

1. $$\alpha_1 = 3$$ and $$\alpha_2 = -1$$ yields $$\alpha_1 \vec{v}_1 + \alpha_2 \vec{v}_2 = \vec{0}$$
2. $$i = 2$$ and $$\alpha_1 = -3$$ $$s.t.$$ $$\vec{v}_i = \sum_{j \ne i}{\alpha_j v_j}$$

$$\vec{v}_1 = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$and $$\vec{v}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$ are linearly independent for either / both of the following:

1. $$2\alpha_1 + \alpha_2 = 0$$ and $$3\alpha_1 + 0\alpha_2 = 0$$ has unique solution $$\alpha_1 = \alpha_2 = 0$$.
2. \($$2 \alpha_1 = 1$$ and $$ 3 \alpha_1 = 0$$\) has no solution and \($$1 \alpha_1 = 2$$ and  $$ 0 \alpha_1 = 3$$\) has no solution.

## Orthogonality

Informally, orthogonal vectors are perpendicular, They are completely unrelated / unaligned \(not even inverted / negative alignment\). In English, we often refer to unrelated concepts as orthogonal. This carries over into linear algebra.

If you recall, the informal interpretation of the [inner product](vector-operations.md#inner-product) involved how similar two vectors were, and the geometric interpretation of the [dot product](vector-operations.md#euclidian-inner-product-dot-product-scalar-product) incorporated the angle between them. 

$$
\vec{u} \cdot \vec{v}
= \lVert u \rVert \lVert v \rVert cos(\theta)
$$

Since we know that perpendicular lines form a $$90 \degree$$angle, we can determine exactly what the dot product between two orthogonal vectors should be.

$$
cos(90 \degree) = 0
$$

> Formally, vectors $$\vec{u}$$ and $$\vec{v}$$ are orthogonal iff
>
> $$
> \vec{u} \cdot \vec{v} = 0
> $$

### Proof of Linear Independence

A set of nonzero orthogonal vectors are necessarily linearly independent.

Let $$\vec{x}$$ be a set / vector of vectors where $$\vec{x}_i \cdot \vec{x}_j = 0 \ \  \forall i \neq j$$. Consider the following expression:

$$
\alpha_1 \vec{x}_1 + \alpha_2 \vec{x}_2 + \dots + \alpha_n \vec{x}_n
$$

Multiply the whole expression by $$\vec{x}_i$$.

$$
\vec{x}_i \cdot (\alpha_1 \vec{x}_1 + \alpha_2 \vec{x}_2 + \dots + \alpha_n \vec{x}_n)
$$

$$
\alpha_1 \vec{x}_i  \cdot \vec{x}_1 + \alpha_2 \vec{x}_i  \cdot \vec{x}_2 + \dots + \alpha_n \vec{x}_i  \cdot \vec{x}_n
$$

All terms will be annihilated except for $$\alpha_i \vec{x}_i \cdot \vec{x}_i$$.

$$
\alpha_i \lVert \vec{x}_i \rVert ^2
$$

Hence, in order to achieve $$\alpha_1 \vec{x}_1 + \alpha_2 \vec{x}_2 + \dots + \alpha_n \vec{x}_n = \vec{x}_i * \vec{0} = \vec{0}$$, $$\alpha_i$$ must be $$0$$.

This holds for all $$i$$, so linear dependence \($$\exists$$ scalars $$\alpha_1, \alpha_2, \dots, \alpha_n$$$$s.t.$$$$\alpha_1 \vec{v}_1 + \alpha_2 \vec{v}_2 + \dots + \alpha_n \vec{v}_n = \vec{0}$$ and $$\exists$$ at least one $$\alpha_i \ne 0$$\) does not hold.

