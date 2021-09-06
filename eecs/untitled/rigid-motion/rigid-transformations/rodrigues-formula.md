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

Now solving the differential equation:

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
\phantom{--} 0 \
\phantom{-} -w_3 \
\phantom{-} w_2 \\
\phantom{--} w_3 \
\phantom{--} 0 \
\phantom{-} -w_1\\
\phantom{} -w_2\
\phantom{--} w_1\
\phantom{--} 0
\end{bmatrix}
$$

$$
\hat{w}^2 
= 
\begin{bmatrix}
\phantom{} -(w_3^2 + w_2^2) \ 
\phantom{--} w_1w_2 \ 
\phantom{---} w_1w_3 \\
\phantom{-} w_1 w_2 \
\phantom{-} -(w_1^2 + w_3^2) \
\phantom{--} w_2 w_3 \\
\phantom{--} w_1 w_3 \ 
\phantom{---} w_2 w_3 \ 
\phantom{-} -(w_2^2 + w_3 ^2)
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

