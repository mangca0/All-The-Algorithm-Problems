
**Taylor's Theorem with Peano Remainder**

Suppose $f$ is $n$ times differentiable at $x_{0}$. Then we have

$$
f(x)=f(x_{0})+\frac{f'(x_{0})}{1!}(x-x_{0})+\frac{f''(x_{0})}{2!}(x-x_{0})^2+\dots+\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^n+R_{n}(x).
$$

Where $R_{n}(x)=o[(x-x_{0})^n](x\to x_{0})$ is called the Peano remainder.

This expansion is called $n$ -th order Taylor formula with Peano remainder for $f(x)$ in a neighborhood of $x_{0}$.

**Taylor's Mean Value Theorem with Lagrange Remainder**

Suppose $f$ is $n+1$ times differentiable on the open interval $(a,b)$ containing $x_{0}$, and has continuous derivatives up to order $n$ on the closed interval $[a,b]$. Then for any $x \in [a,b]$, we have:

$$
f(x)=f(x_{0})+\frac{f'(x_{0})}{1!}(x-x_{0})+\frac{f''(x_{0})}{2!}(x-x_{0})^2\dots+\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^n+R_{n}(x).
$$

Where $R_{n}(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_{0})^{(n+1)}$ for some $\xi$ between $x_{0}$ and $x$, is called the Lagrange remainder.

This expansion is called $n$ -th order Taylor formula with Lagrange remainder for $f$ on $[a,b]$.

> Comparison:
> 
> |                                | **Taylor's Formula with Peano Remainder**                                        | **Taylor's Formula with Lagrange Remainder**                                                               |
> | ------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
> | **Prerequisites**              | **Weaker**. $f(x)$ only needs to be $n$ times differentiable at the point $x_0$. | **Stronger**. $f(x)$ must be $n+1$ times differentiable on the interval containing $x_0$.                  |
> | **Nature and Scope**           | **Qualitative (Limit-based).**<br>Rely on the condition that $x\to x_{0}$.       | **Quantitative (Equation-based).**<br>$x$ can be chosen within the given interval $[a,b]$.                 |
> | **Remainder and Applications** | $R_n(x) = o((x-x_0)^n)$<br>Evaluating limits.                                    | $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$<br>Numerical approximation and proving inequalities. |
> 

**Maclaurin Series**

$$
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\dots+\frac{x^n}{n!}+\begin{cases}
o(x^n) \\
\frac{e^\xi}{(n+1)!}x^{n+1},\xi=\theta x(0<\theta<1)
\end{cases}.
$$

$$
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}+\dots+(-1)^{n}\frac{x^{2n+1}}{(2n+1)!}+R_{2n+1}(x).
$$

$$
\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}+\dots+(-1)^n \frac{x^{2n}}{(2n)!}+R_{2n}(x).
$$

$$
\frac{1}{1-x}=1+x+x^2+\dots+x^n+R_{n}(x).
$$

$$
\frac{1}{1+x}=1-x+x^2+\dots+(-1)^nx^n+R_{n}(x).
$$

$$
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}+...+ (-1)^{n-1} \frac{x^{n}}{n}+R_{n}(x).
$$

$$
(1+x)^\alpha = 1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2+\dots+ \frac{{\alpha(\alpha-1)\dots(\alpha-n+1)}}{n!}x^n+R_{n}(x).
$$

