# Linear Dependence

## Linear Dependence

Informally, linear dependence refers to redundancy within data.

> Somewhat formally, a set of $$n$$ vectors $$\vec{v} = \begin{bmatrix} \vec{v}_1 \ \vec{v}_2, \ \dots \ \vec{v}_n \end{bmatrix}$$are **linearly dependent** if
>
> 1. $$\exists$$ scalars $$\alpha_1, \alpha_2, \dots, \alpha_n$$$$s.t.$$$$\alpha_1 \vec{v}_1 + \alpha_2 \vec{v}_2 + \dots + \alpha_n \vec{v}_n = \vec{0}$$ and $$\exists$$ at least one $$\alpha_i \ne 0$$ \($$\exists$$ means "there exists" and $$s.t.$$ is short for "such that"\)
> 2. $$\exists \ i \ \ s.t. \ \ \vec{v}_i = \sum_{j \ne i}{\alpha_j v_j}$$ \(one of the vectors is a linear combination of the others\)
>
> Either condition is sufficient to prove linear independence and also to imply the other.
>
> **Linearly independent** vectors are those that are not linearly dependent.

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

Orthogonal vectors are necessarily linearly independent. 

