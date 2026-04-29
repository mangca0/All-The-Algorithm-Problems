## Definition

**Periodicity**

Suppose $f(x+a)=f(x)$, then we have  $T = a$.

**Symmetry**



## Property

**Periodicity**

$f(x+a)=-f(x)\implies T=2a$

$f(x+a)=\frac{1}{f(x)} \implies T=2a$

$f(x+a)=-\frac{1}{f(x)} \implies T=2a$

$f(x+a)=f(x)+f(x+2a) \implies T=6a$

$f(x+a)=\frac{{1-f(x)}}{1+f(x)} \implies T=2a$

$f(x+a)=\frac{{1+f(x)}}{1-f(x)} \implies T=4a$

**Periodicity of Composite Function**

Consider a composite function $y=f(\varphi(x))$, where $f(u)$ is the outer function and the $\varphi(x)$ is the inner function.

1. **When the Inner Function is Periodic**

	- If the inner function $\varphi(x)$ is periodic with a period of $T$, then the composite function $y=f(\varphi(x))$ is also periodic with a period of $T$.

2. **When the Outer Function is Periodic & the Inner Function is Linear**

	- If the outer function is periodic with a period of $T$, and the inner function is a linear function (i.e., $\varphi(x)=ax+b$, where $a\neq 0$), the composite function is periodic with a period of $\frac{T}{|a|}$.

**Double Symmetry implies Periodicity**

If a continuous function $f(x)$ possesses **two distinct symmetries** (either axes or centers of symmetry), it is necessarily to be a **periodic function** (except the point 3 below).

1. **Two Axes of Symmetry**
	- Condition: $f(x)$ is symmetric about the line $x=a$ and $x=b$.
	- Period:
$$
T=2|a-b|.
$$
2. **One Axis & One Center Symmetry**
	- Condition: $f(x)$ is symmetric about the line $x=a$ and the point $(b,y_{b})$.
	- Period: 
$$
T=4|a-b|.
$$
3. **Two Centers of Symmetry**
	- Condition: $f(x)$ is symmetric about the points $(a, y_{a})$ and $(b, y_{b})$.
	- Period:
$$
T=2|a-b|.
$$
(strictly periodic only if $y_{a}=y_{b}$).


> Proof:
> 
> Considering symmetry, we have:
> $$f(a+x)+f(a-x)=2y_{a} \implies f(x)+f(2a-x)=2y_{a}.$$
>  and:
>  $$f(b+x)+f(b-x)=2y_{b} \implies  f(x)+f(2b-x)=2y_{b}.$$
>  Then:
> $$f(2b-x)+f(2a-(2b-x))=2y_{a}.$$
> $$f(x)=f(2(a-b)+x)-2(y_{a}-y_{b}).$$
> Namely, when $y_{a}=y_{b}$, $f(x)$ is a periodic function with a period of $2|a-b|$.
> 
> When $y_{a}\neq y_{b}$, the equation takes the form $f(x+T)=f(x)+\Delta y$.
> 
> let $f(x)=\varphi(x)+px+q$, $p$ and $q$ is constants, we have:
> 
> $$\varphi(x)+px+q=\varphi(2(a-b)+x)+p[2(a-b)+x]+q-2(y_{a}-y_{b}).$$
> By expanding and simplifying, we get：
> 
> $$\varphi(2(a-b)+x)-\varphi(x)=\frac{y_{a}-y_{b}}{p(a-b)}$$
> Therefore, taking $p=\frac{y_{a}-y_{b}}{{a-b}}$, then $\varphi(x)$ is a periodic function with a period of $2|a-b|$, and $f(x)$ is a sum of periodic function and linear function.