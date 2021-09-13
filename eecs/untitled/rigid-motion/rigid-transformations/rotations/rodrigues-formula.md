# Rodrigues Formula

## Setup

Let's consider a rotation of a point $$p$$ about an axis $$w$$. We wish to express the position of the point at rotation $$\theta$$.

At any $$\theta$$ of rotation, the derivative of the radial position $$r$$ of point $$p$$ is in the direction orthogonal to both:

* The axis of rotation $$w$$
* The radial position vector of the rotating point

For simplicity, let's discuss all vectors with respect to the center of rotation. To express the orthogonality just described, we can use the cross product between the axis of rotation $$w$$ and the radial position vector $$r$$ of the rotating point.

$$
\dot{r}(\theta) = w \times r(\theta)
$$

Using our new tools from the **hat map**, we can express the position in terms of $$\hat{w}$$.

$$
\dot{r}(\theta) = \hat{w} r(\theta)
$$

Now solving the differential equation by using the exponential map:

$$
r(\theta) = e^{\hat{w}\theta} + r_0
$$

## Derivation

### Summation

Using Taylor Series expansion, we can work towards an explicit formula for the radial position vector of the point $$p$$ at rotation $$\theta$$.

$$
e^{x} = I + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots
$$

Thus:

$$
e^{\hat{w}\theta} = I + \hat{w}\theta + \frac{(\hat{w}\theta)^2}{2!} + \frac{(\hat{w}\theta)^3}{3!} + \dots
$$

### Factorization

We will show that $$\hat{w}^2 = ww^T - \lVert w \rVert ^2 I$$ \($$= ww^T - I$$ for normalized $$w$$\)

$$
\hat{w} = \begin{bmatrix}
0 & -w_3 & w_2 \\
w_3 & 0 & -w_1 \\
-w_2 & w_1 & 0
\end{bmatrix}
$$

$$
\hat{w}^2 
= 
\begin{bmatrix}
-(w_3^2 + w_2^2) &  w_1w_2 & w_1w_3 \\
w_1 w_2 & -(w_1^2 + w_3^2) & w_2 w_3 \\
w_1 w_3 & w_2 w_3 & -(w_2^2 + w_3 ^2)
\end{bmatrix}
$$

Because we know that $$w$$ is normalized, $$\sum_{i}{w_i^2} = 1$$. Each term on the diagonal of $$\hat{w}^2$$,$$\hat{w}^2_{ii}$$, is equal to $$w_i^2 - 1$$, where $$1$$ is expressed by the above summation. Then:

$$
\hat{w}^2 = ww^T - I
$$

We will show that $$\hat{w}^3 = - \lVert w \rVert ^ 2 \hat{w}$$ \($$ = -\hat{w}$$for normalized $$w$$\)

$$
\hat{w}^3 = \hat{w} w w^T - \hat{w}
$$

$$
\hat{w}^3 = 0 w^T - \hat{w}
$$

$$
\hat{w}^3 = - \hat{w}
$$

Using these, we can factor our summation:

$$
e^{\hat{w} \theta} = 
I + 
\hat{w} \theta + 
\frac{\hat{w}^2 \theta^2}{2!} - 
\frac{\hat{w} \theta^3}{3!} - 
\frac{\hat{w}^2 \theta^4}{4!} + 
\dots
$$

$$
e^{\hat{w}\theta} = 
I + 
\hat{w} (\theta  - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} + \dots) + 
\hat{w}^2 (\theta^2 - \frac{\theta^4}{4!} + \frac{\theta^6}{6!} + \dots)
$$

### Taylor Series

Recall the following two Taylor Series.

$$
sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots
$$

$$
cos(x) = 1 - x^2 + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots
$$

Using these, we can reduce our matrix rotation \($$e^{\hat{w}\theta}$$\) to $$sin$$ and $$cos$$ expressions.

## Formula

Finally we get the **Rodrigues Formula** for unit $$w$$ \($$\lVert w \rVert = 1$$\):

$$
R_{a\theta} = e^{\hat{w}\theta} = I + \hat{w} sin(\theta) + \hat{w}^2 (1 - cos(\theta))
$$



## Logarithmic Map

Given the relationship we have established between $$so(3)$$ and $$SO(3)$$ through the Rodrigues Formula, we can formalize our understanding of the **exponential map** for matrices in $$so(3)$$.

The exponential map from $$so(3)$$ to $$SO(3)$$, \($$exp : so(3) \rightarrow SO(3)$$\) is [onto](../../../../../cs/programming/functions.md#onto).

Using the Rodrigues Formula, we see that every rotation \(with unit $$w$$\) has trace:

$$
tr(R) = 1 + 2cos(\theta)
$$

Given this, we can formulate 3 partitioning cases for a rotation matrix $$R$$ in $$SO(3)$$, and show that all of them can be mapped from at least one element in $$so(3)$$ .

In the case that $$tr(R) = 3$$:

$$
\theta = 0
$$

In the case that $$-1 < tr(R) < 3$$:

$$
\theta = cos^{-1}(\frac{tr(R) - 1}{2})
$$

$$
w = \frac{1}{2sin(\theta)}
\begin{bmatrix}
r_{32} - r_{23} \\
r_{13} - r_{31} \\
r_{21} - r_{12}
\end{bmatrix}
$$

In the case that $$tr(R) = -1$$, $$cos(\theta) = -1$$:

$$
\theta = cos^{-1}(-1) = \pm \pi
$$

$$
w = 
\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
or
\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
or
\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

The above reverse mapping from $$log : SO(3) \rightarrow so(3)$$ is called the **logarithmic map.**

