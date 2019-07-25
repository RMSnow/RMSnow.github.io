---
layout:     single
title:      "C语言中补码的整数运算特性"
excerpt:   " "
date:       2017-11-06 17:04:00
toc: true
categories:
- Programming Language
tags:
- C
- Complement
---

### 前言

本篇博客以**“SSD6-Exercise2-Data Lab: Manipulating Bits”**为例，分析在对C语言中的整数采用**补码（two's-complement）**编码的机器上，其整数运算的特性。

----------
### 补码

#### 定义
> 最常见的有符号数的计算机表示方式就是*补码（two's-complement）*形式。在这个定义中，将字的最高有效位解释为负权（negative weight），我们用函数*B2T（Binary to Two's-complement的缩写，长度为 w）*来表示。

如：

B2T ([0001]) = -0 + 0 + 0 + 1 = 1
B2T ([0101]) = -0 + 4 + 0 + 1 = 5
B2T ([1011]) = -8 + 0 + 2 + 1 = -5
B2T ([1111]) = -8 + 4 + 2 + 1 = -1

#### 定理1
> B2T ([11···1]) = -1

证明：假设B2T ([11···1]) 共有w位，则其值为 `-2^(w-1) + 2^(w-2) + ··· +  2^0`. 根据等比数列求和公式，易证该值为-1.

#### 定理2
> 对于`w`位的补码B2T来说，其边界值Tmax与Tmin分别为：
> 
> Tmax = B2T ([01···1])  = 2^(w-1) - 1
> 
> Tmin  = B2T ([10···0])  = -2^(w-1)
> 
> 即有：~Tmax = Tmin

----------
### 整数运算

我们先以表格的形式，宏观介绍C语言中的位级运算、逻辑运算和移位运算。

|运算种类|运算符|主要说明|
|:-|:-|:-|
|位级运算|\|, &, ~, ^|对应于**布尔运算**中的OR, AND, NOT, EXCLUSIVE-OR|
|逻辑运算|\|\|, &&, !|对应于**命题逻辑**中的OR, AND, NOT|
|移位运算|<<, >>|分为左移与右移，右移运算包括逻辑右移与算数右移|

#### `!`与`~`有什么区别？

注意：逻辑运算很容易和位级运算相混淆，但是它们的功能是完全不同的。

 - 逻辑运算中认为所有非零的参数都表示`TRUE`，而参数0表示`FALSE`.

 - 逻辑运算的结果为一个**布尔值**，而位级运算的结果依然为一个**数**.

 - 逻辑运算的运算符常称为`与`、`或`、`非`，而位级运算的运算符常称为`与`、`或`、`取反`、`异或`.

因此，`!`是逻辑运算中的`非`运算符，而`~`是位级运算中的`取反`运算符。

#### 逻辑右移与算术右移

我们先来看左移运算`<<`.
> 对操作数`x`执行`x<<k`运算，即`x`向左移动`k`位。此运算会丢弃最高的`k`位，并在右端补`k`个`0`.

相应而言的右移运算`>>`.
> 对操作数`x`执行`x>>k`运算，即`x`向右移动`k`位。此运算会丢弃最低的`k`位，那么在左端需要补充的`k`个位是什么呢？

> 若执行**逻辑右移**，则补充`k`个`0`，这类似于左移运算.

> 若执行**算术右移**，则补充`k`个`最高有效位`的值。

且几乎所有的编译器／机器组合都对有符号数使用算术右移，对无符号数采用逻辑右移。

----------
### 运算特性

我们通过完成这下面这10个函数，来体会补码的整数运算特性。

```c
/* 
 * bitAnd - x&y using only ~ and | 
 *   Example: bitAnd(6, 5) = 4
 *   Legal ops: ~ |
 *   Max ops: 8
 *   Rating: 1
 */
int bitAnd(int x, int y) {
    return ;
}

/* 
 * bitOr - x|y using only ~ and & 
 *   Example: bitOr(6, 5) = 7
 *   Legal ops: ~ &
 *   Max ops: 8
 *   Rating: 1
 */
int bitOr(int x, int y) {
    return ;
}

/*
 * isZero - returns 1 if x == 0, and 0 otherwise 
 *   Examples: isZero(5) = 0, isZero(0) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 2
 *   Rating: 1
 */
int isZero(int x) {
    return ;
}

/* 
 * minusOne - return a value of -1 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 2
 *   Rating: 1
 */
int minusOne(void) {
    return ;
}

/* 
 * TMax - return maximum two's complement integer 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 4
 *   Rating: 1
 */
int tmax(void) {
    return ;
}

/* 
 * bitXor - x^y using only ~ and & 
 *   Example: bitXor(4, 5) = 1
 *   Legal ops: ~ &
 *   Max ops: 14
 *   Rating: 2
 */
int bitXor(int x, int y) {
    return ;
}

/* 
 * getByte - Extract byte n from word x
 *   Bytes numbered from 0 (LSB) to 3 (MSB)
 *   Examples: getByte(0x12345678,1) = 0x56
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2
 */
int getByte(int x, int n) {
    return ;
}

/* 
 * isEqual - return 1 if x == y, and 0 otherwise 
 *   Examples: isEqual(5,5) = 1, isEqual(4,5) = 0
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int isEqual(int x, int y) {
    return );
}

/* 
 * negate - return -x 
 *   Example: negate(1) = -1.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int negate(int x) {
    return ;
}

/* 
 * isPositive - return 1 if x > 0, return 0 otherwise 
 *   Example: isPositive(-1) = 0.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 3
 */
int isPositive(int x) {
    return ;
}
```

下面则分模块讨论：每个函数所代表的补码的整数运算特性。

#### 逻辑运算与位级运算
这两个函数要分别实现位级运算中的`与`和`或`操作。

由于二进制表示的数位只有0与1，所以我们在思考位级运算的时候，可以借助逻辑运算／命题逻辑中的一些重要定律，即：把位级运算中的0想象成逻辑运算中的FALSE，把1想象成TRUE.

在命题逻辑中，有重要的**德摩根律**：
> 对命题p、q，有：
> 
> （1）p `∧` q `↔` `﹁`(`﹁`p `∨` `﹁`q)
> （2）p `∨` q `↔` `﹁`(`﹁`p `∧` `﹁`q)

相应地，可以很快地推导出位级运算中的`与`和`或`操作。

```c
/* 
 * bitAnd - x&y using only ~ and | 
 *   Example: bitAnd(6, 5) = 4
 *   Legal ops: ~ |
 *   Max ops: 8
 *   Rating: 1
 */
int bitAnd(int x, int y) {
    return ~(~x | ~y);
}

/* 
 * bitOr - x|y using only ~ and & 
 *   Example: bitOr(6, 5) = 7
 *   Legal ops: ~ &
 *   Max ops: 8
 *   Rating: 1
 */
int bitOr(int x, int y) {
    return ~(~x & ~y);
}
```

那么对于异或操作，命题逻辑中又是怎么定义的呢？
> 对命题p、q，有：
> p `⊕` q `↔` (`﹁`p `∧` q) `∨` (p `∧` `﹁`q)

故相应的：

```c
/* 
 * bitXor - x^y using only ~ and & 
 *   Example: bitXor(4, 5) = 1
 *   Legal ops: ~ &
 *   Max ops: 14
 *   Rating: 2
 */
int bitXor(int x, int y) {
    return (x & ~y) | (~x & y);
}
```

#### 异或的用途

从上面关于`异或`的定义中我们也可以看到：
> p `⊕` q `↔` (`﹁`p `∧` q) `∨` (p `∧` `﹁`q)

即：只有当`p`和`q`取值不同时，`p ⊕ q` 才为1（TRUE）.

那么同样地，在位级运算中，我们可以通过异或的这一性质，用来**判断两个数值是否相等**。

```c
/*
 * isZero - returns 1 if x == 0, and 0 otherwise 
 *   Examples: isZero(5) = 0, isZero(0) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 2
 *   Rating: 1
 */
int isZero(int x) {
    return !(x^0);
}

/* 
 * isEqual - return 1 if x == y, and 0 otherwise 
 *   Examples: isEqual(5,5) = 1, isEqual(4,5) = 0
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int isEqual(int x, int y) {
    return !(x^y);
}
```

需要注意的是：这里的`!`不能改为`～`，因为这个函数所做的是一个逻辑运算：判断某个数`是不是` 0（或x与y`是不是`相等）.（从函数的名字`isZero`、`isEqual`就可以看的出来：最外层进行的必须是一个逻辑运算）


#### 特别的数：`-1`

在最上方的时候我们已经提过了补码中的一个重要定理：

> B2T ([11···1]) = -1

那么如何取到`[11···1]`呢，很简单，因为数`0`可以表示为`[00···0]`，所以对`0`进行按位取反操作即可。

```c
/* 
 * minusOne - return a value of -1 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 2
 *   Rating: 1
 */
int minusOne(void) {
    return ~0;
}
```

#### 特别的数：`0`
我们来看`isPositive`函数：判断一个数是否为正，对正数，返回值为1；对非正数，返回值为0.

根据补码的定义，我们很容易知道：最高有效位为1的数是负数。

那么最高有效位是0的数是正数吗？

不然，因为对于`0`来说，它的每一位都是0.

“数`x`最高有效位是否为1”很好判断：让`x`的最高有效位先跑到最右边，也就是`x>>31`，然后在与`1`按位取或，若最终结果为1，说明最高有效位就是1.

所以`isPositive`函数需要满足两个命题：

（1）x的最高有效位是`0`，即`((x>>31) & 1) == 0`
（2）x不是0，即`x != 0`

即：函数的返回值为：`(((x>>31) & 1) == 0) && x `（记为式*），由于具有运算符号的限制，我们还要对它继续进行转化。

对于`((x>>31) & 1) == 0`来说，由于`(x>>31) & 1`的结果只有1位，所以这个逻辑运算可以表达成：`!((x>>31) & 1)`.

那么式*就变为了：`!((x>>31) & 1) && x`，由于命题`!((x>>31) & 1)`的值是0或1，命题`x`的值也是0或1，所以逻辑运算符`&&`可**退化**为：**两个只有一个数位的数值的按位取与运算**。

```c
/* 
 * isPositive - return 1 if x > 0, return 0 otherwise 
 *   Example: isPositive(-1) = 0.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 3
 */
int isPositive(int x) {
    return (!((x>>31) & 1)) & x;
}
```


#### 边界值：`Tmax`与`Tmin`

由补码的定义我们可以知道：
> 对于`w`位的补码B2T来说，其边界值Tmax与Tmin分别为：
> 
> Tmax = B2T ([01···1])  = 2^(w-1) - 1
> 
> Tmin  = B2T ([10···0])  = -2^(w-1)
> 
> 即有：~Tmax = Tmin

那么我们需要得到`Tmin`，即`[10···0`]呢？

只需要`[10···0] = 1<<31`即可，再对其按位取反，便得到了`Tmax`.

```c
/* 
 * TMax - return maximum two's complement integer 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 4
 *   Rating: 1
 */
int tmax(void) {
    return ~(1<<31);
}
```

#### 移位运算的潜在含义

下面我们来看getByte函数：
```c
/* 
 * getByte - Extract byte n from word x
 *   Bytes numbered from 0 (LSB) to 3 (MSB)
 *   Examples: getByte(0x12345678,1) = 0x56
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2
 */
int getByte(int x, int n) {
    return ;
}
```
其中，LSB（Least Significant Bit）是“最低有效位”，MSB（Most Significant Bit）是“最高有效位”。

举个例子：对于十六进制数`0x12345678`，其二进制表示为`[0001 0010 ··· 1000]`，其最低有效位是排列在最右那个0，而最高有效位是排列在最左边的那个0.

因此，这个函数想要表达的意思就是说：`n`的值从0到3，且0代表最低有效位（可以理解为排在最右边的那个字节，也就是`0x78`），3代表最高有效位（可以理解为排在最左边的那个字节，也就是`0x12`），同理：1代表的就是`0x56`.

那么我们该如何实现这个函数的功能呢？

我们可以把这个问题分三个步骤考虑：

 1. 通过`n`的值，我们就得到了其所代表的两个数位（比如：当`n`为1时，我们就得到，这两个数位是`5 6`；当`n`为2时，这两个数位就是`3 4`）

 2. 我们又知道，最终得到的这两个数位，其实是在“最右边”的。依然拿`n`为1来举例子，我们在第一步得到了`5 6`，但我们得把这两个数放在最右边啊，否则不就成了`0x5600`吗，它一点都不等于`0x56`，即`0x0056`.

 3. 第三步，我们把这两个数位放到最右边以后，还得保证它的左侧全部是0。这要怎么做呢——只需要让它和`0x000000ff`进行按位与操作即可。

这样转化了问题之后，我们的难点只剩下一个了，也就是上述过程中的第二步：我们要把这两个数位向右移动几位呢？

由于 `1 byte = 8 bits`，所以这个问题也很简单了：当n=1时，向右8位；当n=2时，向右16位…也就是说，我们只需要向右移动`8n`位就好了。

那么这个函数就很好写了：
```c
/* 
 * getByte - Extract byte n from word x
 *   Bytes numbered from 0 (LSB) to 3 (MSB)
 *   Examples: getByte(0x12345678,1) = 0x56
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2
 */
int getByte(int x, int n) {
    int offset = 8 * n;
    int a = x >> offset;
    int b = 0x000000ff;
    return a & b;
}
```

细心的读者可能发现了，我们这个函数的实现是不符合题目要求的。题目中还有一个额外的要求，即：我们能够使用的运算符，只有`! ~ & ^ | + << >>`，这其中没有乘号`*`.

那么，`8 * n`又该怎么表示呢？

这个问题也很简单。我们都喜欢拿十进制来思考问题，就比如说：`100 * x`是多少呢？小学生都知道：在`x`的右边添上两个0啊！那`1000 * x`呢？添3个0啊！

好了，那么回到我们的二进制。`2 * x`是多少呢？大学生应该可以知道了：在`x`的右边添1个0啊！那`8 * x`呢？添3个0啊！

这也就是移位运算的潜在含义了，**我们把`x`向左移`k`位，其实就是在说：把`x * 2^k`**.

经过修正后的函数如下：

```c
/* 
 * getByte - Extract byte n from word x
 *   Bytes numbered from 0 (LSB) to 3 (MSB)
 *   Examples: getByte(0x12345678,1) = 0x56
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2
 */
int getByte(int x, int n) {
    int offset = n << 3;
    int a = x >> offset;
    int b = 0x000000ff;
    return a & b;
}
```

#### 补码中的“相反数”
```c
/* 
 * negate - return -x 
 *   Example: negate(1) = -1.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int negate(int x) {
    return ~x+1;
}
```

在补码中有这样一个定理：
> 对于数`x`来说，`-x = ~x + 1`.

我们考虑用数学归纳法来证明这个式子：

（1）考虑只有2位的补码。此时，只有`[00] = 0` 、`[01] = 1` 、`[10] = -2` 、`[11] = -1`这四个数，容易发现`-x = ~x + 1`.

（2）现假设此结论对于拥有`k`位的补码成立.

（3） 下面证明此结论对于拥有`k + 1`位的补码成立。

由于篇幅与表达所限，只提供证明思路如下：

 - 需要利用假设（2）的条件。

 - 需分别讨论：对于`k + 1`位的补码，当其最高有效位（即符号位）分别为0、1时的情况。 

----------
### 参考资料

[1]《深入理解计算机系统》（第3版）. Randal E. Bryant, David R.O'Hallaron 著.

[2] 博客：[SSD06 Exercise02 个人解答](http://qianjigui.iteye.com/blog/269501).
