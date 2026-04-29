**In what follows, we will focus on convex functions. The case for concave functions follows simply by reversing the inequalities.**

## Definition

**Midpoint Convex Function**

Let $f$ be a function defined on an interval $I$. Suppose that $\forall x, y \in I$, we have:

$$f\left( \frac{{x+y}}{2} \right)\leq \frac{{f(x)+f(y)}}{2}.$$

Midpoint Convexity $\centernot\implies$ Convexity.

**Convex Function**

Let $f$ be a function defined on an interval $I$. Suppose that $\forall x, y \in I, 0<r<1$, we have:

$$f(rx+(1-r)y) \leq rf(x)+(1-r)f(y).$$

Then $f$ is said to be a convex function on the interval $I$.

**Equivalent Definition**

A continuous function that satisfies midpoint convexity is a convex function.

(i.e., Midpoint Convexity + Continuity $\implies$ Convexity).

## Property

A convex function is not necessarily differentiable.

if it is differentiable, then its derivative is monotonically increasing.

A convex function is not necessarily twice differentiable.

if it is twice differentiable, then its second derivative is $\geq 0$.

**Tangent Line Property**: if $f$ is a convex function on an interval $I$, and is differentiable at $x_{0}$, then $\forall x \in I$, we have:

$$f(x) \geq f(x_{0}) + f'(x_{0}) \cdot (x-x_{0}).$$

> **Proof:**
> 
> By the definition of convexity, for $\forall x \in I,t \in (0,1)$, we have:
> 
> $$ f((1-t)x_{0} + tx) \leq (1-t)f(x_{0}) + tf(x).$$
> 
> Rearranging the terms, we have:
> 
> $$ f(t(x-x_{0}) + x_{0}) \leq t[f(x)-f(x_{0})] + f(x_{0}).$$
> 
> and then we have:
> 
> $$\frac{{f(t(x-x_{0})+x_{0})-f(x_{0})}}{t} \leq f(x)-f(x_{0}). $$
> 
> For the case where $x=x_{0}$, the inequality holds trivially.
> 
> For the case where $x>x_{0}$, we have:
> 
> $$\frac{{f(t(x - x_{0}) + x_{0}) - f(x_{0})}}{t(x-x_{0})} \leq \frac{{f(x)-f(x_{0})}}{x-x_{0}}$$
> 
> Now, we take the limit as $t(x-x_{0})\to 0^+$, we have:
> 
> $$f'(x_{0}) \leq \frac{{f(x) - f(x_{0})}}{(x-x_{0})}. $$
> 
> Namely,
> 
> $$f(x) \geq f(x_{0}) + f'(x_{0}) \cdot (x-x_{0}).$$
> 
> For the case Where $x < x_{0}$, the proof follows analogously.
> 
> Therefore, in all cases, we conclude that:
> 
> $$f(x) \geq f(x_{0}) + f'(x_{0}) \cdot (x-x_{0}).$$
> 
> Which completes the proof.

## Theorem

**Jensen's Inequality**

Let $f$ be a convex function defined on interval $I$. Suppose that $x_{i}\in I,w_{i}\geq 0, \sum_{i}w_{i}=1$, we have:

$$f\left( \sum_{i=1}^nw_{i}\cdot x_{i} \right) \leq \sum_{i=1}^nw_{i}\cdot f(x_{i}).$$

Note: The weighted inequality also holds under midpoint convexity, under the additional assumption that $w_{i} \in \mathbb{Q}$.

## Corollary

**Unweighted Version of Jensen's Inequality**

In particular, for uniform weights $w_{i}=\frac{1}{n}$, we obtain the unweighted version:

$$f\left( \frac{1}{n}\sum_{i=1}^nx_{i} \right) \leq \frac{1}{n} \sum_{i = 1}^n f(x_{i})$$

Note: The unweighted inequality holds even if $f$ only satisfies midpoint convexity.

## Proposition

**Criteria for Convexity**

If $f''(x)\geq 0$ on $I$ , or $f'(x)$ is monotonically increasing on $I$, then $f$ is convex on $I$.

**The Reverse of Jensen's Inequality**

Let $f$ be a convex function defined on interval $I$. Suppose that $x_{1}, x_{2}, y_{1}, y_{2} \in I$ satisfy:

$$
y_{1}\leq x_{1}\leq y_{2}
$$

$$
y_{1}\leq x_{1}\leq y_{2}
$$

$$
x_{1}+x_{2}=y_{1}+y_{2}. 
$$

then we have:

$$f(x_{1})+f(x_{2}) \leq f(y_{1})+f(y_{2}).$$

_This conclusion typically requires an independent proof as a lemma._

> **Proof:**
> 
> Assuming $y_{1} < y_{2}$. Let:
> 
> $$x_{1}=\frac{{y_{2}-x_{1}}}{y_{2}-y_{1}}y_{1}+\frac{{x_{1}-y_{1}}}{y_{2}-y_{1}}y_{2}$$
> 
> $$ x_{2}=\frac{{y_{2}-x_{2}}}{y_{2}-y_{1}}y_{1}+\frac{{x_{2}-y_{1}}}{y_{2}-y_{1}}y_{2}.$$
> 
> Applying the definition of convexity to both equations, we obtain:
> 
> $$ f(x_{1}) \leq \frac{{y_{2}-x_{1}}}{y_{2}-y_{1}}f(y_{1})+\frac{{x_{1}-y_{1}}}{y_{2}-y_{1}}f(y_{2})$$
> 
> $$ f(x_{2}) \leq \frac{{y_{2}-x_{2}}}{y_{2}-y_{1}}f(y_{1})+\frac{{x_{2}-y_{1}}}{y_{2}-y_{1}}f(y_{2}).$$
> 
> Summing these two inequalities, the coefficients for $f(y_{1})$ add up to $1$, and the coefficients for $f(y_{2})$ also add up to $1$. Thus, it simplifies to:
> 
> $$f(x_{1})+f(x_{2})\leq f(y_{1})+f(y_{2}).$$
> 
> Which completes the proof.

## Remarks

- **Example:**
    
    - Convex functions: $x^2, x^4, e^x, \sqrt{ x^2+1 },|x|,x^{-1}(x>0), (1+x)^{-1}(x>-1).$
        
    - Concave functions: $\sqrt{ x }, \sqrt{ 1+x }, \ln x.$
        
    - Convex on some intervals, concave on others: $\sin x, \cos x.$
        
- **Problem:**
    
    - [[How to use Jensen's inequality1.png]]
        
    - [[How to use Jensen's inequality2.png]]

---

## Relationship
with - [[柯西函数方程]]

这是一个极其敏锐且极具数学直觉的问题。将“凸函数与琴生不等式”和“柯西函数方程”联系起来，意味着你的思考已经跨越了单一知识点的孤岛，开始触及**实分析（Real Analysis）**与**泛函方程（Functional Equations）**的底层逻辑。

这两者在高等数学和数学竞赛中都占据着核心地位。它们看似一个是“不等式”，一个是“等式”，但其底层的方法论和逻辑演进路径有着惊人的高度一致性。

以下是这两个知识点之间的深度结构对比：

---

## 1. 核心联系 (Deep Connections)

### A. $\mathbb{Q} \to \mathbb{R}$ 的跨越逻辑（最核心的联系）

无论是你的讲义还是柯西函数方程，最精妙的逻辑都在于**“如何从有理数系扩展到实数系”**。

- **在柯西函数方程中**：对于 $f(x+y) = f(x) + f(y)$，我们可以很容易地通过数学归纳法证明 $f(qx) = qf(x)$ 对所有 $q \in \mathbb{Q}$（有理数）成立。但要让它对所有 $r \in \mathbb{R}$（实数）也成立（即得出唯一连续解 $f(x)=cx$），就必须加上一个**正则性条件（Regularity Condition）**，比如“连续性”、“单调性”或“局部有界性”。
    
- **在你的凸函数讲义中**：请注意这句原话——_“The weighted inequality also holds under midpoint convexity, under the additional assumption that $w_{i} \in \mathbb{Q}$.”_ 同样地，中点凸性（Midpoint Convexity）只能保证有理数权重的琴生不等式成立。要想推广到实数域（即得出一般的凸函数定义 $0<r<1$），同样需要**连续性**（Midpoint Convexity + Continuity $\implies$ Convexity）。
    

### B. 凸性是柯西方程的“正则性解药”

这也是一个极其优美的数学结论：如果你已知一个函数 $f(x)$ 满足柯西加性方程 $f(x+y) = f(x) + f(y)$，并且它在某个区间上是**凸函数**（或凹函数），那么这个函数必定是连续的，进而必定是线性函数 $f(x) = cx$。在这里，凸性直接成为了破解柯西函数方程病态解的“钥匙”。

### C. 极限情况的交汇：仿射函数

如果一个函数既是凸函数又是凹函数，即它同时满足：

$$f(rx+(1-r)y) \leq rf(x)+(1-r)f(y)$$

$$f(rx+(1-r)y) \geq rf(x)+(1-r)f(y)$$

那么它必须满足等式 $f(rx+(1-r)y) = rf(x)+(1-r)f(y)$。这正是**仿射函数（Affine Functions）**的定义，而仿射函数 $f(x) = cx + d$ 的齐次版本（当 $d=0$ 时），正是柯西函数方程 $f(x+y)=f(x)+f(y)$ 的连续解。

---

## 2. 相同之处 (Similarities in Methodology)

- **抽象的函数视角**：两者都不研究具体的函数解析式（如 $\sin x$ 或 $e^x$），而是研究**函数类的结构特征**。它们都试图通过自变量的代数运算规则（如 $x+y$ 或 $tx+(1-t)y$）来约束函数值的代数结构。
    
- **代换与迭代技巧**：在证明过程中，两者都高度依赖于“特殊值代入”（如令 $x=y$，$x=0$）以及“递推迭代”（将 $n=2$ 的情况通过数学归纳法或柯西向前向后归纳法推广到 $n$ 的情况）。
    
- **对数与指数的同构变换**：在处理不同形式的柯西方程（如 $f(xy)=f(x)+f(y)$）时，常通过对数/指数变换将其化归为标准加性方程；而在凸函数中，我们同样利用 $\ln x$ 的凹性和 $e^x$ 的凸性，通过恒等变形来证明著名的均值不等式（AM-GM Inequality）。
    

---

## 3. 本质不同 (Key Differences)

### A. 研究对象：等式 vs. 不等式

- **柯西函数方程**研究的是**严格等式（$=$）**。它的目标是“求解”，即在特定的附加条件下，寻找出满足该等式的唯析函数形式（通常是线性、指数或对数形式）。
    
- **凸函数讲义**研究的是**不等式（$\leq$ 或 $\geq$）**。它的目标不是求解某一个具体的函数，而是界定一个**函数空间（Function Space）**。它描述的是一种“几何弯曲的趋势”，并利用这种趋势去进行放缩和极值估计。
    

### B. 几何直观：线性 vs. 曲率

- 柯西加性方程刻画的是**线性（Linearity）**与**叠加原理（Superposition）**。它的几何直观是穿过原点的直线。
    
- 凸函数刻画的是**曲率（Curvature）**与**下凸性**。它的几何直观是“弦在弧之上”或“切线在曲线之下”（正如你讲义中 Tangent Line Property 所证明的那样）。
    

---

这种将“结构特征”与“不等式放缩”结合起来的思维，在高等数学的进阶推演中极其强大。

既然我们聊到了凸性可以作为柯西方程的“正则性条件”，是否需要我为你严格推导一下，如何利用“函数 $f(x)$ 具有凸性”这一条件，直接证明柯西函数方程 $f(x+y)=f(x)+f(y)$ 的解必然是 $f(x)=cx$？