---
layout:     single
title:      "为C语言的动态内存分配添加出错预警"
excerpt:   "An Enhanced Allocator"
date:       2017-11-27 01:02:00
toc: true
categories:
- Programming Language
tags:
- C
- malloc
---

### 前言
本篇博客利用C标准库现有的`malloc`和`free`函数，在其基础之上编写一个更强大的动态内存分配器，它可以实现**出错预警**的功能。  

具体的出错预警功能描述，参见 **[SSD6 Exercise3——Debugging Malloc Lab: Detecting Memory-Related](http://qianjigui.iteye.com/blog/282706)** 的题目要求。

----------
### 基础知识

#### 背景

> 虽然可以使用低级的`mmap`和`munmap`函数来创建和删除虚拟内存的区域，但是C程序员还是会觉得当运行时需要额外虚拟内存时，用动态内存分配器 *(dynamic memory allocator)* 更方便，也有更好的可移植性。
> ……
> 显式分配器 *(explicit allocator)* ，要求应用显式地释放任何已分配的块。例如，C标准库提供一种叫做`mallo`c程序包的显式分配器，并通过调用`free`函数来释放一个块。C++中的`new`和`delete`操作符和C中的`malloc`和`free`相当。

本篇博客就利用C标准库提供的`malloc`和`free`函数，为其编写一个更强大的动态内存分配器，它可以实现**出错预警**的功能。  

下面我们先来看C标准库中`malloc`与`free`分别为我们提供了哪些功能。

#### malloc
```c
#include <stdlib.h>
void *malloc(size_t size);
```
`malloc`的参数就是需要分配的内存字节数，如果内存池中的可用内存可以满足这个需求，函数就返回一个指向被分配的内存块**起始位置**的指针。

#### free
```c
#include <stdlib.h>
void free(void *pointer);
```
`free`的参数要么是`NULL`，要么是一个之前从`malloc`、`calloc`或`realloc`函数得到的返回值。向`free`传递一个`NULL`参数不会产生任何效果。

#### 缺陷分析
在动态内存分析中，常常会出现许多错误，这些错误可能包括：

 1. 对NULL指针进行解引用操作
 2. 对分配的内存进行操作时越过边界
 3. 释放并非动态分配的内存
 4. 试图释放一块动态分配内存的一部分
 5. 一块动态内存被释放之后被继续使用

而正如我们所看到的，C标准库中原有的`malloc`、`calloc`、`realloc`与`free`函数，并不会对这些可能出现的错误进行相应的预警处理。  

因此我们试图通过编写一个Enhanced Allocator，来解决这一缺陷。

----------


### 方案设计

#### 数据抽象
我们对一个连续的虚拟内存片 *(chunk)* 进行下图所示的设计：  

![1](http://img.my.csdn.net/uploads/201711/26/1511710848_3664.png)  


 - 每个`chunk`由`Header`、`Payload`、`Footer`这三部分组成。
 - `Header`至少包括如下内容：
	 - `checkSum (int)`：一个`chunk`最前面的部分，通过检查`checkSum`的变化，可判断出`Header`有没有被错误更改。
	 - `size (size_t)`：`Payload`的大小
	 - `filename (char *)`：文件名
	 - `linenum (int)`：行号
 - `Fence`：为特定的常数值。在一个`chunk`的`Header`与`Footer`中各有一个`Fence`，通过检查其值的变化，可判断出`Payload`的前方与后方有没有被错误更改。
 - `Payload`：原应分配的内存块。
 - `Footer`：由一个`Fence`组成。

#### 错误处理
我们所完成的Enhanced Allocator，拟对如下5种错误进行捕获处理：

> Error #1: Writing past the beginning of the user's block (through the fence) 
Error #2: Writing past the end of the user's block (through the fence)
Error #3: Corrupting the header information
Error #4: Attempting to free an unallocated or already-freed block
Error #5: Memory leak detection (user can use ALLOCATEDSIZE to check for leaks at the end of the program)

#### 数据结构
下面我们来看具体的数据结构如何实现。  

我们可以看到，如果想要对上述的5种错误进行捕获，我们需要维护（记录）当前进程中所有**已经分配的内存片**，从而在释放内存时，判断出`free`的参数是否有效。  

那么我们就可以采用最简单，也是最直接的方式，就通过一个**单向链表**实现对所有**已经分配的内存片**的记录。  

```c
/* Define Header */
struct header{
    int checkSum;
    size_t size;
    char *filename;
    int linenumber;
    struct header *next;  //指向下一个分配的内存片
};
```

在具体的实现中，我们将`Fence`从`Header`中分离出来，从而将内存片的设计简化为`chunk = Header + Fence + Payload + Fence`.

----------
### 具体实现

#### 宏定义
```c
#define FENCE_VALUE 0xCCDEADCC
#define BASIC_SIZE_HEADER sizeof(struct header) / 4
#define BASIC_SIZE_FENCE sizeof(FENCE_VALUE) / 4
#define BASIC_SIZE_META BASIC_SIZE_HEADER + BASIC_SIZE_FENCE * 2
```
我们在通过一个`header`结构体获取`checkSum`、`size`等属性值时，要通过大量的**指针增减操作**（且多为**整型指针**的操作），因此我们通过定义上述宏，来使后续代码更加清晰直观。  

在上面的四个宏定义中：

 - `FENCE_VALUE`：取`0xCCDEADCC`这个常数值
 - `BASIC_SIZE_HEADER`：结构体`Header`的基本字长
 - `BASIC_SIZE_FENCE`：常数`FENCE_VALUE`的基本字长
 - `BASIC_SIZE_META`：一个内存片包含的所有**额外信息**的基本字长（`chunk = Header + Fence + Payload + Fence`，其中`Header`、`Fence`为额外信息）

#### 单向链表
```c
struct header *head_block = NULL;       //单向链表的表头结点
struct header *tail_block = NULL;       //单向链表的尾结点

/* 链表初始化 */
void initLinkedList(){
    if (head_block) {
        return;
    }
    
    head_block = malloc(sizeof(struct header));
    head_block->next = NULL;
    tail_block = head_block;
}
```
由于分配内存片操作，需要在链表的尾部不断增加新的结点，因此通过尾结点可实现分配操作在常数次时间内执行。为避免判断“删除（释放）的结点是不是头结点”，因此通过设置表头结点可简化操作步骤。

#### 获取`META`信息
我们把一个内存片`Heade`中的各属性，前后两个`Fence`，以及`Payload`的起始地址统称为它的`META`信息。

```c
int computeCheckSum(struct header *ptr) {
    return (ptr->size)|(ptr->linenumber);       //利用size与linenumber获取checksum
}

int *getHeaderFenceOfChunk(struct header *ptr){
    return (int*)((int*)ptr + BASIC_SIZE_HEADER);
};

int *getFooterFenceOfChunk(struct header *ptr){
    return (int*)((int*)ptr + BASIC_SIZE_HEADER + BASIC_SIZE_FENCE + ptr->size/4);
};

void *getPayloadAddress(struct header *ptr){
    return ((int*)ptr + BASIC_SIZE_HEADER + BASIC_SIZE_FENCE);
};
```
注：`checkSum`的定义可以有多种形式，这里采用通过块大小和行号来获取`checkSum`的方式

#### `MyMalloc()`——增加结点
```c
void *MyMalloc(size_t size, char *filename, int linenumber) {
    initLinkedList();
    
    struct header *new = malloc(BASIC_SIZE_META * 4 + size);
    new->size = size;
    new->filename = filename;
    new->linenumber = linenumber;
    new->checkSum = computeCheckSum(new);
    
    tail_block->next = new;
    tail_block = new;
    tail_block->next = NULL;
    
    *getHeaderFenceOfChunk(new) = FENCE_VALUE;
    *getFooterFenceOfChunk(new) = FENCE_VALUE;
    
    return getPayloadAddress(new);
}
```

#### `MyFree()`——删除结点
我们将所有的出错预警处理，均放在`Myfree()`函数里，也就是说：我们只有在执行释放内存的操作时，才去检查其参数的合理性，从而进行相应的错误提示。在分配内存时，没有出错预警。  

对于某个`header`参数，我们检查其`META`信息并获取出错码：
```c
/* 获取错误种类 */
int getErrorCode(struct header *ptr){
    if(ptr == NULL){
        return 0;
    }else{
        int flag;
        
        flag = (*getHeaderFenceOfChunk(ptr) == FENCE_VALUE);
        if(!flag){      //Starting edge of the payload has been overwritten
            return 1;
        }
        
        flag = (*getFooterFenceOfChunk(ptr) == FENCE_VALUE);
        if(!flag){      //Ending edge of the payload has been overwritten
            return 2;
        }
        
        flag = (ptr->checkSum == computeCheckSum(ptr));
        if(!flag){      //Header has been corrupted
            return 3;
        }
    }
    return 0;
};
```

下面是`MyFree()`函数的具体实现：
```c
void MyFree(void *ptr, char *filename, int linenumber) {
    if (!head_block) {      //链表不存在
        error(4, filename, linenumber);
    }
    
    struct header *preFree = head_block;
    struct header *toFree = preFree->next;
    
    while (toFree) {        //在链表中查找需要释放的块
        if(getPayloadAddress(toFree) == ptr){
            int errorCode = getErrorCode(toFree);
            if (errorCode) {
                errorfl(errorCode, toFree->filename, toFree->linenumber, filename, linenumber);
            }
            break;
        }else{
            preFree = toFree;
            toFree = preFree->next;
        }
    }
    
    if (!toFree) {      //未找到
        error(4, filename, linenumber);
    }
    
    /* 在链表中删除toFree结点 */
    preFree->next = toFree->next;
    free(toFree);
}
```


#### `AllocatedSize()`与`PrintAllocatedBlocks()`——获取结点信息
`AllocatedSize()`函数要求我们输出当前所有分配的内存片的`Payload`大小之和，`PrintAllocatedBlocks()`函数则要求我们打印出已分配内存片的`META`信息，因此这两个函数其实就是在**遍历**单向链表。
```c
/* returns number of bytes allocated using MyMalloc/MyFree:
	used as a debugging tool to test for memory leaks */
int AllocatedSize() {
    if (!head_block) {      //链表不存在
        return 0;
    }
    
    int sum = 0;
    struct header *temp = head_block->next;
    
    while (temp) {
        sum += temp->size;
        temp = temp->next;
    }
    
	return sum;
}

/* Prints a list of all allocated blocks with the
	filename/line number when they were MALLOC'd */
void PrintAllocatedBlocks() {
    if (!head_block) {      //链表不存在
        return;
    }
    
    struct header *temp = head_block->next;
    int sum = 0;
    
    while (temp) {
        printf("Allocated block %d: %d bytes, at line %d of the file %s.\n",
               ++sum, temp->size, temp->linenumber, temp->filename);
        temp = temp->next;
    }
    return;
}
```

#### `HeapCheck()`——进行结点的检查
在上文中我们也已经提到了，我们只有在`MyFree()`函数执行时，才会判断各内存片的`META`信息有没有被更改，因此`HeapCheck()`函数希望我们实现的功能就是：通过此函数，我们可以直接看到当前状态下，分配片链表中各结点是否健康。这当然也是一个遍历操作。

```c
int HeapCheck() {
    int status = 0;
    if (!head_block) {      //链表不存在
        return status;
    }
    
    struct header *temp = head_block->next;
    
    while (temp) {
        int errorCode = getErrorCode(temp);
        if (errorCode) {
            status = -1;
            char *msg = getMsg(errorCode);
            printf("Error: %s\n\tin block allocated at %s, line %d\n",
                   msg, temp->filename, temp->linenumber);
        }
        temp = temp->next;
    }
    
    return status;
}
```

----------
### 测试用例
```c
static void run_test_case(int n) {
    switch(n) {
        case 1: { /* no error, just a basic test */
            char *str = (char *) MALLOC(12);
            strcpy(str, "123456789");
            FREE(str);
            printf("Size: %d\n", AllocatedSize());
            PrintAllocatedBlocks();
        }
            break;
        case 2: { /* should overflow by 1 */
            char *str = (char *) MALLOC(8);
            strcpy(str, "12345678");
            FREE(str);
        }
            break;
        case 3: { /* should overflow by 1, harder to catch
                   because of alignment */
            char *str = (char *) MALLOC(2);
            strcpy(str, "12");
            FREE(str);
        }
            break;
        case 4: { /* memory leak */
            void *ptr = MALLOC(4), *ptr2 = MALLOC(6);
            FREE(ptr);
            printf("Size: %d\n", AllocatedSize());
            PrintAllocatedBlocks();
        }
            break;
        case 5: {
            void *ptr = MALLOC(4);
            FREE(ptr);
            FREE(ptr);
        }
            break;
        case 6: {
            char *ptr = (char *) MALLOC(4);
            *((int *) (ptr - 8)) = 8 + (1 << 31);
            FREE(ptr);
            HeapCheck();
        }
            break;
        case 7: {
            char ptr[5];
            FREE(ptr);
        }
            break;
        case 8: {
            int i;
            int *intptr = (int *) MALLOC(6);
            char *str = (char *) MALLOC(12);
            
            for(i = 0; i < 6; i++) {
                intptr[i] = i;
            }
            if (HeapCheck() == -1) {
                printf("\nCaught Errors\n");
            }
        }
        default:
            ;
    }
}
```
8个测试用例如上所示，均产生预期输出。

#### case 1
![1](http://img.my.csdn.net/uploads/201711/27/1511714966_1123.png)

#### case 2
![2](http://img.my.csdn.net/uploads/201711/27/1511714836_2554.png)

#### case 3
![2](http://img.my.csdn.net/uploads/201711/27/1511715002_3534.png)

#### case 4
![2](http://img.my.csdn.net/uploads/201711/27/1511715009_3301.png)

#### case 5
![2](http://img.my.csdn.net/uploads/201711/27/1511714886_1513.png)

#### case 6
![2](http://img.my.csdn.net/uploads/201711/27/1511714897_6894.png)

#### case 7
![2](http://img.my.csdn.net/uploads/201711/27/1511715048_3503.png)

#### case 8
![2](http://img.my.csdn.net/uploads/201711/27/1511714916_5488.png)

----------
### 参考资料
[1] 《C和指针》. [美] Kenneth A.reek 著.
[2]《深入理解计算机系统》（第3版）. Randal E. Bryant, David R.O’Hallaron 著.


