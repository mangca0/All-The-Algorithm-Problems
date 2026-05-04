
Half-folded reverse order.

## Template

```java
public static boolean isPalindrome(long x) {  
    if (x < 0 || (x % 10 == 0 && x != 0)) {  
        return false;  
    }  
    long revertedHalf = 0;  
    while (x > revertedHalf) {  
        revertedHalf = revertedHalf * 10 + x % 10;  
        x /= 10;  
    }  
    return x == revertedHalf || x == revertedHalf / 10;  
}
```

