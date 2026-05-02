
According to the data ranges of $n$ and $k$, and the number of queries, there are mainly the following four methods for calculating.

---

**Directly Compute**

- Core formula:
	$$
	C(n, k) = \frac{n \times (n - 1) \times \dots \times (n - k + 1)}{k \times (k - 1) \times \dots \times 1}.
	$$

- **Use case: Modulo is not required,  usually $n\leq 60$ around** (to prevent exceed the 64-bit integer range).

- Time complexity: $O(k)$; Space complexity: $O(1)$.

- Template:
	
	```java
	public static long C(int n, int k) {
		if (k < 0 || k < n) return 0;
		
		k = Math.min(k, n - k); // Pick smaller value
		long res = 1;
		
		for (int i = 1; i <= k; i++) {
			// Must first multiply and the divide
			res *= (n - i + 1) / i;
		}
	}
	```

---

**DP (Yang Hui Triangle / Recursive)**

- Core formula:
	
	$$
	C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
	$$

- **Use case: $n$ and $k$ is smaller, usually $n \leq 2000$. Where you need to frequently query. Modulus can be non-prime number**.

- Time complexity: preprocessing $O(n^2)$, query $O(1)$; Space complexity: $O(n^2)$.

- Template:
	
	```java
	public static void init() {
		c[0][0] = 1;
		for (int i = 1; i <= n; i++) {
			c[i][0] = 1;
			for (int j = 1; j <= i; j++) {
				c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % p;
			}
		}
	}
	
	public static int C(int n, int k) {
		if (k < 0 || k > n) return 0;
		return c[n][k];
	}
	```

---

**Preprocessing the Factorial with Quick Power**

- Core formula:

	$$
	C(n, k)=\frac{n!}{(n-k)!\cdot k!}
	$$
	
	Under modulo：
	
	$$
	C(n, k) \equiv n! \times (k!)^{-1} \times ((n - k)!)^{-1} \pmod p
	$$

- **Use case: $n$ is larger, usually $n \leq 10^6$, and $p$ is prime.**

- Time complexity: preprocessing $O(n)$, query $O(1)$; Space complexity $O(n)$.

- Template:
	
	```java
	public static void build() {
		// Preprocessing factorial
		fac[0] = 1;  
		for (int i = 1; i < MX; i++) {  
		    fac[i] = fac[i - 1] * i % p;  
		}  
		// Preprocessing inverse factorial
		inv_fac[MX - 1] = qpow(fac[MX - 1], (int) p - 2); // 费马小定理
		for (int i = MX - 2; i >= 0; i--) {  
		    inv_fac[i] = inv_fac[i + 1] * (i + 1) % p;  
		}
	}
	
	// Quick power
	public static long qpow(long a, int b) {  
	    long res = 1L;  
	    while(b > 0) {  
	        if ((b & 1) == 1) {  
	            res = res * a % p;  
	        }  
	        a = a * a % p;  
	        b >>= 1;  
	    }  
	    return res;  
	}
	
	public static long C(int n, int k) {  
		if (m < 0 || m > n) return 0;
	    return fac[n] * inv_fac[m] % p * inv_fac[n - m] % p; // Care about modulo
	}
	```

---

**Lucas Theorem**

When it $n$ is extremely large but the modulus $p$ is small, it is calculated by converting it into $p$ a decimal form.

- Core formula:    
	
	$$
	C(n, k) \equiv C(n \bmod p, k \bmod p) \times C(n / p, k / p) \pmod p
	$$

- **Use case: $n$ and $k$ maximum (e.g. $10^{18}$ ), but modulus $p$ is a smaller prime number** (usually $p \le 10^5$ ).

- Time complexity: $O(p \log_p n)$ .

- Template:
	
	```java
	public class LucasTheorem {
	    
	    // 快速幂
	    public static long qmi(long a, long b, long p) {
	        long res = 1;
	        while (b > 0) {
	            if ((b & 1) == 1) res = res * a % p;
	            a = a * a % p;
	            b >>= 1;
	        }
	        return res;
	    }
	
	    // 计算内部的小组合数 (基于直接定义或逆元)
	    public static long C(long n, long k, long p) {
	        if (k > n) return 0;
	        long res = 1;
	        for (int i = 1, j = (int) n; i <= k; i++, j--) {
	            res = res * j % p;
	            res = res * qmi(i, p - 2, p) % p;
	        }
	        return res;
	    }
	
	    // Lucas 递归调用
	    public static long lucas(long n, long k, long p) {
	        if (n < p && k < p) return C(n, k, p);
	        return C(n % p, k % p, p) * lucas(n / p, k / p, p) % p;
	    }
	}
	```

## Problems

**入门**

- [牛客 130226 B](https://ac.nowcoder.com/acm/contest/130226/B)

- [力扣 62. 不同路径](https://leetcode.cn/problems/unique-paths/)

- [力扣 357. 统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits/) 

- [力扣 1175. 质数排列](https://leetcode.cn/problems/prime-arrangements/) 

**基础**

- [力扣 3179. K 秒后第 N 个元素的值](https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/) 递推 组合数

- [力扣 1359. 有效的快递序列数目](https://leetcode.cn/problems/count-all-valid-pickup-and-delivery-options/) 

**进阶**

- [洛谷 P2822 [NOIP2016 提高组] 组合数问题] DP法 + 前缀和
