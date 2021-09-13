# Special Orthogonal Matrices

## Intro

Before we jump into rigid transformation matrices, we will briefly introduce group theory. By doing so, and then proving that different kinds of transformation matrices form algebraic groups, we can get a lot of insight into the algebraic properties of rigid transformations.

## Group

> Somewhat formally, a group is a type-operation pair $$(G, \circ)$$ with the following properties:
>
> 1. Closure: $$a \circ b \in G$$  $$\forall a, b \in G$$ 
> 2. Identity: $$\exists ! e \in G$$  $$s.t.$$  $$  a \circ e = e \circ a = a$$  $$\forall a \in G$$ 
> 3. Inverse: $$\exists ! a^{-1} \in G$$  $$s.t.$$  $$  a \circ a^{-1} = e$$  $$\forall a \in G$$ 
> 4. Associativity: $$ a \circ (b \circ c) = (a \circ b) \circ c$$  $$\forall a, b, c \in G$$
>
> @source [Wikipedia](https://en.wikipedia.org/wiki/Group_%28mathematics%29)

## Special Orthogonal Matrices \(SO\(n\)\)

Recall that a square matrix $$A$$ is considered orthogonal / orthonormal iff $$A^T A = I$$ or iff $$A^{-1} = A^T$$. Orthonormal matrices in $$\mathbb{R^{n \times n}}$$ are considered part of $$O(n)$$.

The subclass **special orthogonal matrices** \($$SO(n)$$\) also have the following 'special' property.

$$
det(A) = 1
$$

{% hint style="info" %}
Recall that matrices in $$O(n)$$ have the following property $$det(A) = \pm 1$$. In euclidian space, an orthonormal matrix $$A$$ with $$det(A) = -1$$ corresponds to a reflection.
{% endhint %}

