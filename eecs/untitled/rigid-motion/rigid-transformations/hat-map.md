# Hat Map

## Intro

Before we get into rigid transformations, we will discuss a notational / functional tool that will help us represent [cross products](../../../../ee/devices-and-systems-i/linear-algebra/vectors/vector-operations.md#cross-product) in matrix form.

## Hat Map

$$\hat{} : \mathbb{R^3} \rightarrow so(3)$$

$$
\hat{a} = \begin{bmatrix}
\phantom{-} 0 \ -a_3 \ \phantom{-} a_2 \\
\phantom{-}a_3 \ \phantom{-} 0 \ -a_1 \\
-a_2 \ \phantom{-} a_1 \ \phantom{-}0
\end{bmatrix}
$$

The **hat map** operator maps a vector to a skew matrix. A matrix $$A$$ is considered **skew symmetric** if $$A^T = -A$$.

With this definition, we can redefine the cross product in terms of matrix multiplication.

$$
\vec{a} \times \vec{b} = \hat{a} \vec{b}
$$

For notational purposes, let's define the group of skew symmetric matrices as \(little\)$$so(3)$$.

> Somewhat formally, the group of $$so(n)$$ matrices satisfy the following:
>
> $$so(n) \equiv \{ S \in \mathbb{R^{n \times n}}$$  $$s.t.$$  $$ S^T = -S \}$$

## Cross Product Properties

> 1. Scalar Triple Product: $$\vec{a} \cdot (\vec{b} \times \vec{c}) = \vec{c} \cdot (\vec{a} \times \vec{b}) = \vec{b} \cdot (\vec{c} \times \vec{a})$$
> 2. Vector Triple Product: $$\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c}) \vec{b} - (\vec{a} \cdot \vec{b}) \vec{c}$$
> 3. Jacobi Identity \($$\vec{a} \times (\vec{b} \times \vec{c}) + \vec{c} \times (\vec{a} \times \vec{b}) + \vec{b} \times (\vec{c} \times \vec{a}) = \vec{0}$$\)

In addition, one could show the following property of the hat map:

$$
\widehat{R \vec{v}} = R \hat{v} R^T
$$

