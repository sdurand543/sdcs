# Rigid Transformations

Recall that a [transformation](../../../../cs/programming/functions.md#transformations) is a function from Type space $$T$$ to Type space $$T$$.

A rigid transformation / Euclidian transformation is an affine transformation that preserves the distance between all points.

> Somewhat formally, a rigid body transformation $$g : \mathbb{R^3} \rightarrow \mathbb{R^3}$$ preserves
>
> 1. Length: $$\lVert g(\vec{p}) - g(\vec{q}) \rVert = \lVert \vec{p} - \vec{q} \rVert$$
> 2. Orientation: $$g(\vec{v} \times \vec{w}) = g(\vec{v}) \times g(\vec{w})$$

All rigid transformations are composed of two rigid transformation primitives:

1. Rotation
2. Translation

