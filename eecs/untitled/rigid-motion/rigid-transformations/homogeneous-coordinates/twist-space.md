# Twist Space

## Intro

Let's consider some possible trajectories that our rigid body could take.

### Purely Rotational

$$
\dot{p}(t) = w \times (p(t) - q)
$$

$$
\begin{bmatrix}
\dot{p} \\ 0
\end{bmatrix}
=
\begin{bmatrix}
\hat{w} & -\hat{w}q \\ 
0 & 0
\end{bmatrix}
\cdot
\begin{bmatrix}
p \\ 1
\end{bmatrix}
$$

### Purely Translational

$$
\dot{p} = v
$$

$$
\begin{bmatrix}
\dot{p} \\ 0
\end{bmatrix}
=
\begin{bmatrix}
0 & v \\ 
0 & 0
\end{bmatrix}
\cdot
\begin{bmatrix}
p \\ 1
\end{bmatrix}
$$

We will call this space, made of matrix trajectories for $$SE(3)$$, $$se(3)$$.

{% hint style="info" %}
Going forward, we will denote these trajectories in $$se(3)$$using the symbol $$\hat{\xi}$$.
{% endhint %}

We define the hat map from $$\mathbb{R^6} \rightarrow se(3)$$ as follows:

$$
\begin{bmatrix}
v \\ w
\end{bmatrix}
\rightarrow
\begin{bmatrix}
\hat{w} & v \\
0 & 0
\end{bmatrix}
$$

