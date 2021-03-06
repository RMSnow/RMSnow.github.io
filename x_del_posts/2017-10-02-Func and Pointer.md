---
layout: single
title: "函数指针与函数指针数组应用总结"
excerpt: ""
date: 2017-10-02 21:54:00
toc: true
categories:
- Programming Language
tags:
- C
---

## 函数指针

**函数指针包含函数在内存中的地址**。数组名实际上就是数组的第一个元素在内存中的地址，类似地，函数名实际上也是执行这个函数任务的代码在内存中的起始地址。

函数指针可以传递给函数、从函数返回、保存在数组中、赋予另一个函数指针或者调用底层函数。

```c

#include <stdio.h>

/* 定义四则运算 */
double add(double a, double b);
double sub(double a, double b);
double mul(double a, double b);
double divi(double a, double b);

/* 声明函数指针 */
double (*foo)(double a, double b);

int main(int argc, const char * argv[]) {
    double num1, num2;
    num1 = 4;
    num2 = 2;
    
    /* 函数指针赋值 */
    foo = add;
    printf("%f + %f = %f\n", num1, num2, foo(num1, num2));
    
    /* 函数指针重载 */
    foo = sub;
    printf("%f - %f = %f\n", num1, num2, foo(num1, num2));

    return 0;
}

double add(double a, double b){
    return a+b;
}

double sub(double a, double b){
    return a-b;
}

//……

```
输出结果如下：
```c
4.000000 + 2.000000 = 6.000000
4.000000 - 2.000000 = 2.000000
Program ended with exit code: 0
```

----------


## 函数指针数组

函数指针数组在菜单驱动系统、启动消息的处理函数等领域，都有其独特的应用。下面列举了三个实际的应用场景：

### 场景1：有关积分计算
```c
#include <stdio.h>

/* 定义四个待积函数 */
double func1(double x){
    return x;
}
double func2(double x){
    return x*x;
}
double func3(double x){
    return x*x*x;
}

/* 定义积分运算 */
/* 1. func指向待积函数 */
/* 2. a表示积分下限，b表示积分上限 */
double calculation(double (*func)(double x), double a, double b){
    double dx = 0.001;
    double sum = 0;
    
    for(double i=a+dx; i<b; i+=dx){
        sum += func(i) * dx;
    }
    
    return sum;
}

int main(int argc, const char * argv[]) {
    /* 定义积分上限与下限 */
    double a=0;
    double b=1;
    
    /* 为函数指针数组赋值 */
    double (*foo[])(double x) = {func1, func2, func3};
    
    /* 计算三个函数的定积分 */
    for(int i=0; i<3; i++){
        printf("函数func%i在[0,1]上的定积分为：%f\n", i+1,
               calculation(foo[i], a, b));
    }
    
    return 0;
}


```
输出结果为：
```
函数func1在[0,1]上的定积分为：0.499500
函数func2在[0,1]上的定积分为：0.332834
函数func3在[0,1]上的定积分为：0.249500
Program ended with exit code: 0
```

### 场景2：Windows驱动编程
```c
# pragma INITCODE
extern "C" NTSTATUS DriverEntry (
            IN PDRIVER_OBJECT pDriverObject,
            IN PUNICODE_STRING pRegistryPath    ) 
{
    NTSTATUS status;
    /* 注册其他驱动调用函数入口 */
    pDriverObject->DriverUnload = HelloDDKUnload;
    pDriverObject->MajorFunction[IRP_MJ_CREATE] = MyDDKCreate;
    pDriverObject->MajorFunction[IRP_MJ_CLOSE] = MyDDKClose;
    pDriverObject->MajorFunction[IRP_MJ_WRITE] = MyDDKWrite;
    pDriverObject->MajorFunction[IRP_MJ_READ] = MyDDKRead;
    .........
    .........
}
```

### 场景3：处理标识类型的数据
假如现在需要处理一段二进制数据，输入参数为 `char* buffer`和 `int length`，`buffer`是数据的首地址，`length`表示这批数据的长度。

数据的特点是：长度不定，类型不定，由第一个字节（`buffer[0]`）标识该数据的类型，此时共有256 (2的8次方) 种可能性。

要求必须对每一种可能出现的数据类型都要作处理，并且模块包含若干个函数，在每个函数里面都要作类似的处理。

若按通常做法，会写出如下代码：
```c
/* 首先定义256个处理函数(及其实现) */
void funtion0( void );
//……
void funtion255(void );

/* 总处理函数如下： */
void MyFuntion( char* buffer, int length )
{
    __int8 nStreamType = buffer[0];
    
    switch( nStreamType )
    {
        case 0:
            function1();
            break;
        case 1:
        /* ...... */
        case 255:
            function255();
            break;
    }
}
```
若采用函数指针数组的方式代替switch语句，则可以改写为：
```c
/* 首先定义函数指针数组，并给数组赋值 */
void (*fun[256])(void);

fun[0] = function0;
/* …… */
fun[255] = function();

/* 之后，MyFunction()函数可以修改如下： */
void MyFuntion( char* buffer, int length )
{
    __int8 nStreamType = buffer[0];
    (*fun[nStreamType])();
}
```

只要2行代码，就完成了256条case语句要做的事，减少了编写代码时工作量，将nStreamType作为数组下标，直接调用函数指针，从代码执行效率上来说，也比case语句高。假如多个函数中均要作如此处理，函数指针数组更能体现出它的优势。

----------

## 应用及评价
### 优点
在绝大部分情况下，函数指针（数组）的功能都能够以其他方式实现，但使用函数指针数组也会有很多独特的优势。

优点一：编码美观,容易维护。
```c
typedef void (*FUN)();
/* 事件类型 */
enum EVENT_TYPE
{
    EVENT_TYPE_1 = 0,
    EVENT_TYPE_2,
    EVENT_TYPE_3,
    EVENT_TYPE_END,
};
/* 这里不是单纯的函数指针，稍微扩展成了一个STRUCT，为了阅读，维护更容易 */
struct EVENT_FUN_MAP
{
    EVENT_TYPE    eType;
    FUN        pFun;
};
/* 针对不同的事件，只需要修改这个就可以改变事件的动作 */
EVENT_FUN_MAP eFunMap[EVENT_TYPE_END] = {
    EVENT_TYPE_1,        &EventFun1,
    EVENT_TYPE_2,        &EventFun2,
    EVENT_TYPE_3,        &EventFun3,
}
 
/* .............................. */


void DoAction(EVENT_TYPE eType)
{
    (*eFunMap[eType].pFun)();
}
```

优点二：容易动态重载，某些事件有默认处理函数，只需要重载某些自定义的处理函数。
```c
void DoAction(EVENT_TYPE eType)
{
    (*eFunMap[eType].pFun)();
}
 
void ReloadEventFun()
{
    eFunMap[EVENT_TYPE_1].pFun = &MyEventFun1;
}
```

优点三：执行效率高。

如场景三中所示，函数指针数组可直接根据索引下标直接寻址，算法复杂度为O(1)，在多数情况下其执行效率高于switch语句，更远高于if-else语句。

### 局限性
函数指针数组的最大特点，就是对于这多个处理函数，每个函数的**参数个数及类型**必须相同。在实际场景中，对应用户操作的不同响应函数，当其所要求的参数不同时，就不能再使用函数指针数组，而只能通过如switch语句这样的常规方法来实现。
