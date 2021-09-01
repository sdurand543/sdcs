# Rigid Transformations

Recall that a [transformation](../../../cs/programming/functions.md#transformations) is a function from Type space $$T$$ to Type space $$T$$.

A rigid transformation / Euclidian transformation is an affine transformation that preserves the distance between all points.

> Somewhat formally, a rigid body transformation $$g : \mathbb{R^3} \rightarrow \mathbb{R^3}$$ preserves
>
> 1. Length: $$\lVert g(\vec{p}) - g(\vec{q}) \rVert = \lVert \vec{p} - \vec{q} \rVert$$
> 2. Orientation: $$g(\vec{v} \times \vec{w}) = g(\vec{v}) \times g(\vec{w})$$

## Special Orthogonal Matrices \(SO\(n\)\)

Recall that a square matrix $$A$$ is considered orthogonal / orthonormal iff $$A^T A = I$$ or / equivalently iff $$A^{-1} = A$$. Orthonormal matrices in $$\mathbb{R^{n \times n}}$$ are considered part of $$O(n)$$.

The subclass **special orthogonal matrices** \($$SO(n)$$\) also have the following 'special' property.

$$
det(A) = 1
$$

{% hint style="info" %}
Recall that matrices in $$O(n)$$ have the following property $$det(A) = \pm 1$$. In euclidian space, an orthonormal matrix $$A$$ with $$det(A) = -1$$ corresponds to a reflection.
{% endhint %}

A rotation can be defined by a $$SO(3)$$ matrix.

## Group

> Formally, a group is a Type-Operation pair $$(G, \circ)$$ with the following properties:
>
> 1. Closure: $$a \circ b \in G$$  $$\forall a, b \in G$$ 
> 2. Identity: $$\exists ! e \in G$$  $$s.t.$$  $$  a \circ e = e \circ a = a$$  $$\forall a \in G$$ 
> 3. Inverse: $$\exists ! a^{-1} \in G$$  $$s.t.$$  $$  a \circ a^{-1} = e$$  $$\forall a \in G$$ 
> 4. Associativity: $$ a \circ (b \circ c) = (a \circ b) \circ c$$  $$\forall a, b, c \in G$$
>
> @source [Wikipedia](https://en.wikipedia.org/wiki/Group_%28mathematics%29)

## Hat Map

$$ \hat{\cdot} : \mathbb{R^3} \rightarrow so(3)$$

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

#### Properties

> 1. Scalar Triple Product: $$\vec{a} \cdot (\vec{b} \times \vec{c}) = \vec{c} \cdot (\vec{a} \times \vec{b}) = \vec{b} \cdot (\vec{c} \times \vec{a})$$
> 2. Vector Triple Product: $$\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c}) \vec{b} - (\vec{a} \cdot \vec{b}) \vec{c}$$
> 3. Jacobi Identity \($$\vec{a} \times (\vec{b} \times \vec{c}) + \vec{c} \times (\vec{a} \times \vec{b}) + \vec{b} \times (\vec{c} \times \vec{a}) = \vec{0}$$\)
> 4. $$ \widehat{R \vec{v}} = R \hat{v} R^T $$

For notational purposes, let's define the group of skew symmetric matrices as \(little\)$$so(3)$$.

> Somewhat formally, the group of $$so(n)$$ matrices satisfy the following:
>
> $$so(n) \equiv \{ S \in \mathbb{R^{n \times n}}$$  $$s.t.$$  $$ S^T = -S \}$$

## Rotation

### Group

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

### Rigid Transformation

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
R \hat{p} R^T R q
$$

$$
\widehat{(Rp)} R q
$$

## Rodrigues Formula

Let's consider a rotation of a point about an axis $$w$$. We wish to express the position of the point at parameter $$t$$.

{% hint style="info" %}
While we will be discussing the Rodrigues Formula in terms of $$t$$, this does not mean that rotations must be parameterized over time. However, for simplicity of discussion, I will make this language simplification.
{% endhint %}

At any given point in time, the trajectory of the point can be described by its velocity / derivative, which is in the direction orthogonal to both:

* The axis of rotation $$w$$
* The radial position vector of the rotating point

For simplicity, let's discuss all vectors with respect to the center of rotation. To express the orthogonality just described, we can use the cross product between the axis of rotation and the radial position vector of the rotating point.

$$
\dot{r}(t) = w \times r(t)
$$

Using our new tools from the **hat map**, we can express the position in terms of $$\hat{w}$$.

$$
\dot{r}(t) = \hat{w} r(t)
$$

Now solving the differential equation:

$$
r(t) = e^{\hat{w}t} + r(0)
$$

Using Taylor Series expansion, we can work towards an explicit formula for the radial position vector of the rotating point at time $$t$$. 

Recall the following three Taylor Series.

$$
e^{xt} =
$$

