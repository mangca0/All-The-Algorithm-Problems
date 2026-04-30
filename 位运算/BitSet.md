Replace a `boolean[]` with Java's `BitSet`.

**Basic Operations**

```java
BitSet f = new BitSet(Pre-sized); // Default capacity is 64

f.set(i); // Set to true
f.set(i, j); // Set [i, j) to true
f.clear(i); // Set to false
f.flip(i); // Flip value
boolean val = f.get(i);
f.clear();
```

**Get the `true` Index**

```java
// Starting from fromIndex, search backwards for the index of the first set bit
// If not found, it will return -1
id = f.nextSetBit(fromIndex); 
```

Iterate:

```java
// Skip chunks of zeros instantly
// nextSetBit() will return -1 when 
for (int i = f.nextSetBit(0); i >= 0; i = f.nextSetBit(i + 1)) {
	System.out.println("Bit " + i + " is true);
}
```

Analogously, there is a method called `BitSet.nextClearBit(int fromIndex)`.

**Counting and Sizes**

- Find the highest `true` index:

```java
f.length(); // Return the index of the hightest bit + 1
```

- Find the physical memory capacity:

```java
f.size(); // usually a multiple of 64
```

- Count the `true` value:

```java
f.cardinality() // O(1)
```

**Bulk Operations**

```java
f1.or(f2);
f1.and(f2);
f1.andNot(f2);
f1.xor(f2);
```

**Cloning**

```java
newF = (BitSet) f.clone();
```

