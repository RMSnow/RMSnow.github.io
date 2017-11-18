### 前言

本篇博客以**“SSD6-Exercise1-Decoder Lab”**为例，分析了C／C++语言在特定编译方式下，在堆栈申请空间顺序上的特点。主要探讨的三个问题如下：

 1. **局部变量**的声明顺序，与堆栈空间分配顺序（内存地址）之间的联系.

 2. **函数形参**的顺序，与堆栈空间分配顺序（内存地址）之间的联系.
 
 3. 在汇编语言层面上，探究**函数调用／返回**时的具体过程.

----------
### 例题重现

#### Decoder Lab：Understanding a Secret Message
You have just intercepted an encoded message. The message is a sequence of bits which reads as follows in hexadecimal:

6363636363636363724646636F6D6F72

466D203A65693A7243646E206F54540A

5920453A54756F0A6F6F470A21643A6F

594E2020206F776F797275744563200A

6F786F686E6963736C206765796C656B

2C3365737420346E20216F74726F5966

7565636F202061206C61676374206C6F

20206F74747865656561727632727463

6E617920680A64746F69766120646E69

21687467630020656C6C786178742078

6578206F727478787863617800783174

You have no idea how to decode it, but you know that your grade depends on it, so you are willing to do anything to extract the message. Fortunately, one of your many agents on the field has stolen the source code for the decoder. This agent (007) has put the code and the message in the file secret.cpp, which you can download from the laboratory of your technical staff (Q).

Q has noticed that the decoder takes four integers as arguments. Executing the decoder with various arguments seems to either crash the program or produce unintelligible output. It seems that the correct four integers have to be chosen in order for the program to produce the decoded message. These four integers are the “secret keys.”

007 has been unable to find the keys, but from the desk of the encrypting personnel he was able to cunningly retrieve the first five characters of the unencoded message. These characters are: 
From:

Assignment

Your assignment is to decode the message, and find the keys.

Reminders

This exercise is not extremely difficult. However, the strategy of trying things until something works will be ineffective. Try to understand the material in the course, particularly the following:

•Memory contains nothing but bits. Bits are interpreted as integers, characters, or instructions by the compiler, but they have no intrinsic type in memory.

•The compiler can be strong-armed into interpreting integers as characters, or even as instructions, and vice versa. 
•Every group of 8 bits (a byte) has an address. 
•A pointer in C is merely a stored memory address. 
•The activation records for each function call are all together in memory, and they are organized in a stack that grows downwards and shrinks upwards on function calls and returns respectively. 
•The return address of one function as well as the addresses of all of its local variables are allocated within one activation record.

Strategy

The designers of this decoder weren’t very good. They made it possible for us to attack the keys in two independent parts. Try to break the first two keys first, and do not try to break the third and fourth keys until you have succeeded with the first two.

You can do the first part by specifying only two integer arguments when you execute the decoder. If you get the first and second keys right, a message that starts with From: will appear. This message is not the true message, but a decoy. It is useful, however, to let you know that you have indeed broken the first two keys.

In breaking the first two keys, realize that the function process_keys12 must be somehow changing the value of the dummy variable. This must be so, because the variables start and stride control the extraction of the message, and they are calculated from the value of dummy.

In breaking the third and fourth keys, try to get the code to invoke extract_message2 instead of extract_message1. This modification must somehow be controlled from within the function process_keys34.

Files

When you are done, write a brief report that includes at least the following:

1.The secret message.

2.The secret keys.

3.One paragraph describing, in your own prose, what process_keys12 does. For example, you might say that it modifies a specific program variable. 
4.The meaning of the first two keys in terms of variables and addresses in the decoder program. For example, you might describe key2 by saying that its X-Y bits contain the value to which variable start is set. Or you might describe key1 by saying, for example, that it must be set equal to the number of memory addresses separating the address of two specific variables. These are only examples.

5.One paragraph describing, in your own prose, what process_keys34 does.

6.One paragraph describing the line of source code that is executed when the first call to process_keys34 returns.

7.The meaning of the third and fourth keys in terms of variables and addresses in the decoder program.

Be precise, clear, and brief in each of the points above. Your report should not, in any case, be

longer than one page. Do not get frustrated if this takes a little longer than you expected: brief and clear text often requires more time to write than rambling prose.

Your teacher can tell you what word processors you may use to write your report. Chances are that you can write your report in a number of formats, and for simplicity’s sake, you might even want to write it using Notepad.

Enjoy!


----------
### 解题思路
题目作了如下提示：

 - 先解出`key1`和`key2`，再去解`key3`和`key4`
 
 - `key1`和`key2`正解以后会有`From：`开头的输出
 
 - 函数`process_keys12`会改变变量`dummy`的值
 
 - 解`key3`和`key4`时，尝试让代码调用`extract_message2`而不调用`extract_message1`
 


----------
### 题目本质

####key1 & key2

下面我们来分析`secret.cpp`文件，首先查看主函数：

```C++
int main (int argc, char *argv[])
{
    int dummy = 1;
    int start, stride;
    int key1, key2, key3, key4;
    char * msg1, * msg2;

    key3 = key4 = 0;
    if (argc < 3) {
        usage_and_exit(argv[0]);
    }
    
    key1 = strtol(argv[1], NULL, 0);
    key2 = strtol(argv[2], NULL, 0);
    if (argc > 3) key3 = strtol(argv[3], NULL, 0);
    if (argc > 4) key4 = strtol(argv[4], NULL, 0);

    process_keys12(&key1, &key2);

    start = (int)(*(((char *) &dummy)));
    stride = (int)(*(((char *) &dummy) + 1));

    if (key3 != 0 && key4 != 0) {
        process_keys34(&key3, &key4);
    }

    msg1 = extract_message1(start, stride);

    if (*msg1 == '\0') {
        process_keys34(&key3, &key4);
        msg2 = extract_message2(start, stride);
        printf("%s\n", msg2);
    }
    else {
        printf("%s\n", msg1);
    }
    return 0;
}
```

在不输入key3和key4时，程序是只会执行`extract_message1()`并输出其内容的，而且由提示还可以知道，输出的内容以`From:`开头。

那么，影响`extract_message1()`输出的代码都有哪些呢？

```c++
//start为dummy地址最低位的值
start = (int)(*(((char *) &dummy)));
//stride为dummy地址最低位+1的值
stride = (int)(*(((char *) &dummy) + 1));

//extract_message1
//从data的(start+1)位开始读，每读(stride-1)个字符，跳过一个字符
char * extract_message1(int start, int stride) {
    int i, j, k;
    int done = 0;
    
    for (i = 0, j = start + 1; ! done; j++) {
        for (k = 1; k < stride; k++, j++, i++) {
            if (*(((char *) data) + j) == '\0') {
                done = 1;
                break;
            }
            
            message[i] = *(((char *) data) + j);
        }
    }
    message[i] = '\0';
    return message;
}
```

由此我们可知：要修改`extract_message1()`的输出 ==> 要给`start`和`stride`赋合适的值 ==> 要修改`dummy`变量的值 ==> 通过给`key1`和`key2`赋值来实现。

再来看`key1`和`key2`是如何改变`dummy`变量的值。
```c++
void process_keys12 (int * key1, int * key2) {
    *((int *) (key1 + *key1)) = *key2;
}
```
`process_keys12()`的意思是说：首先，（`main`函数里局部变量`key1`的地址 + `key1`的值），这得到了一个新地址。然后再把这个新地址里的值，赋值成为`key2`的值。

再联系到刚才的解题逻辑，很自然地想到：这个“新地址”，也就是`dummy`变量的地址，`key2`的值，也就会变成`dummy`变量的值。

由此，我们进入了本篇博客中讨论的第一个问题。

也就是说，我们现在需要知道，`dummy`变量和`key1`变量在内存地址中的关系，也就是说，解`key1`和`key2`的过程，从本质上来讲，其实就是让我们找到***“局部变量的声明顺序，与堆栈空间分配顺序（内存地址）之间的联系”***。

到此，我们暂时不去解`key1`和`key2`的具体值，我们直接进入`key3`和`key4`的环节，看看解`key3`和`key4`的过程，要我们做的实际上是什么事情。

####key3 & key4

由提示我们知道：解`key3`和`key4`时，尝试让代码调用`extract_message2`，而不调用`extract_message1`。

我们依然先来看主函数：
```c++
if (key3 != 0 && key4 != 0) {
        process_keys34(&key3, &key4);
        //位置1
    }

    //位置2
    msg1 = extract_message1(start, stride);

    if (*msg1 == '\0') {
        process_keys34(&key3, &key4);
        //位置3
        msg2 = extract_message2(start, stride);
        printf("%s\n", msg2);
    }
    else {
        printf("%s\n", msg1);
    }
```

我们能够看到，要想达到提示所说的要求：即，不执行`extract_message1()`而直接执行`extract_message2()`，我们就需要在`位置1`处直接跳到`位置3`处，而不执行`位置2`处。因为如果执行了`位置2`，那么`msg1`就不会为空值，也就是说`位置3`是无法运行到的。

这其实就是在讲：我们需要对位置1处，也就是第一次调用函数`process_key34()`的返回地址进行修改，让这个返回地址直接跳到位置2处。

那么我们再来看process_key34()是如何完成这个工作的：
```c++
void process_keys34 (int * key3, int * key4) {
    *(((int *)&key3) + *key3) += *key4;
}
```
`process_key34()`的意思是：（**形参**`key3`的地址 + `key3`的值），这构成了一个新的地址，而这个地址的值，被`key4`的值赋予（注意：此处的`&key3`是形参`key3`，而不是主函数里的局部变量`key3`）。而且，这个新的地址，就是函数`process_key34()`的返回地址。

那么，要完成这个工作，就进入了本篇博客探讨的第二个和第三个问题：
（1）首先，我们需要知道，在函数调用与返回工作，具体到内存地址上是如何操作的。这就需要我们去汇编代码层面上寻找答案。
（2）其次，因为`process_key34()`让我们去寻找形参`key3`的地址与函数返回地址之间的关系，这也自然带着一个附加要求：我们也需要知道形参`key3`和形参`key4`之间的地址关系，否则我们就无法给`key3`赋值。

#### 结论

至此，我们也能够明白这个“Decoder Lab”的本质了。尽管它的情景设置非常隐晦，但这个练习想让我们掌握的基础知识，其实就是文章开头提到的那三个：

1. **局部变量**的声明顺序，与堆栈空间分配顺序（内存地址）之间的联系.

2. **函数形参**的顺序，与堆栈空间分配顺序（内存地址）之间的联系.

3. 在汇编语言层面上，探究**函数调用／返回**时的具体过程.


----------
### 解题过程

首先我们需要明白的一点是：在不同的编译方式下（如gcc -m32、gcc -m64、clang等），或在编译器所做不同的优化方式时（如是否增加栈溢出保护机制），上面三个问题的答案可能不同。

因此我们所最终得到的`key1`至`key4`的值，是在某种特定的编译方式下所计算出的结果，所以当改变编译方式时，这些结果可能出现改变。

笔者在几种编译方式下做了一定的尝试。

#### Xcode编译与调试（LLVM + LLDB）

如今的Xcode所用编译器均为LLVM，调试工具则是LLDB。下面我们探究堆栈申请空间的过程。

（图1）
![1](http://img.my.csdn.net/uploads/201710/25/1508917880_7524.png)

由上图可知，先声明的变量，拥有较高的内存地址。因此`dummy`变量与`key1`变量的地址相差12，由于`process_key12()`中指针类型为整型指针，因此`key1 = 12 ／ 4  = 3`。

在计算`key2`时，我们需要探究当`dummy`的值为多少时，才能时`extract_message1()`开头的信息为`From:`。此处我们可以分析全局变量`data`中的字符，最终算出`key2`的值，解题过程略。需要注意的是，`key2`的值与编译器是无关的。

（图2）
![2](http://img.my.csdn.net/uploads/201710/25/1508918410_3833.png)

由上图可知，形参`key3`的地址高于形参`key4`的地址，也就是说，在LLVM的64位编译方式下，函数形参申请堆栈空间时，是按照函数参数列表的从左到右的顺序。

接下来，我们需要探究第三个，也是最复杂的一个问题：即在汇编语言的层面上，分析函数调用／返回的具体过程。

对于这个问题，博客：[深入理解C语言的调用过程](http://blog.chinaunix.net/uid-23069658-id-3981406.html) 作了较为详细的解释。

>汇编语言里的函数大部分情况下都符合以下的函数模板：
```c++
  .globl fun_name
.type fun_name, @function
fun_name:
        pushl %ebp
        movl %esp, %ebp
        <函数主体代码> 
        leave
        ret
```
> 如果我们有个函数原型：int funtest(int x,int y int z char* ptr)，在汇编层面，当调用它时栈的布局结构一般是下面这个样子：
> ![t](http://blog.chinaunix.net/attachment/201311/7/23069658_1383830002vsoC.jpg)

需要注意：该篇博客中，作者使用的是gcc在32位下的编译方式，因此函数堆栈对于局部变量、函数形参的调用顺序，和我们所使用的LLVM是不一样的。但我们依然能够了解到函数调用时的压栈过程，尤其是寄存器%ebp与%esp（在64位操作系统下对应的是%rbp与%rsp）的详细操作过程。

（图3）
![3](http://img.my.csdn.net/uploads/201710/25/1508919176_7920.png)

我们先在第115行加断点，我们要做的事情是：把第一次调用的返回地址，直接修改为第二次调用的返回地址。

（图4）
![4](http://img.my.csdn.net/uploads/201710/25/1508919068_2890.png)

在图4中我们可以看到，在汇编语言上，如果我们想把第一次调用的返回地址，改为第二次调用的返回地址，则`key4 = 287 - 243 = 44`

（图5）
![5](http://img.my.csdn.net/uploads/201710/25/1508919199_3024.png)

在图5中我们能够看到，在LLVM的编译方式下，形参申请堆栈空间的过程，是由**被调用者**完成的，而不是像博客“[深入理解C语言的调用过程](http://blog.chinaunix.net/uid-23069658-id-3981406.html)”中提到的那样，由**调用者**完成。

也就是说，在gcc的32位编译方式下：形参的内存地址，高于存储值为“返回地址”的那个地址。而在LLVM编译方式下，形参的内存地址，低于存储值为“返回地址”的那个地址。

因此，在LLVM编译方式下，我们可以大致地画出`process_key34()`被调用时的内存地址分配方式：

|  |
| :-: |
|**返回地址**|
|**old rbp**|
|*rbp|
|*(rbp-4)|
|**形参key3**|
|**形参key4**|
|...|


故`形参key3的地址 + 16 = 存储值为函数返回地址的那个地址`。即：`key3 = 16 / 4 = 4`.

#### 其他编译方式

由于篇幅的原因，在此不再叙述其他编译方式的实操过程，在此单列出结论。

```c++
void func(int key1, int key2){
	//...
	return;
}

int main(int argc, char **argv){
	int key1, key2;
	func(key1, key2);
}
```
在上述代码的调用过程中，不同编译方式下的堆栈申请空间特点如下：

|||clang 32位／64位|gcc-32位|gcc-64位|
|:-|:-|:-|:-|
|局部变量的地址|key1 > key2|key2 > key1|key1 > key2|
|形参的地址|key1 > key2|key2 > key1|key1 > key2|
|形参申请空间的过程|被调用者申请|调用者申请|调用者申请|
*注：上述编译方式均在栈溢出保护机制下.

----------
### Decoder总结

 1. The Secret Message
 > [messge1]
 From: Friend
 To: You
 Good! Now try choosing keys3,4 to force a call to extract2 and
 avoid the call to extract1
 
 > [message2]
 From: CTE
 To: You
 Excellent!You got everything!
 
 2. The Secret Keys
 > 在LLVM编译方式下：
 > key1 = 3
 > key2 = 777
 > key3 = 4
 > key4 = 44 
 
 3. What `process_keys12` Does
 > 在了解局部变量申请堆栈空间的顺序之后，通过`process_key12`可改变局部变量`dummy`的值.
 
 4. The meaning of the first two keys in terms of variables and addresses in the decoder program
> 要修改`extract_message1()`的输出 ==> 要给`start`和`stride`赋合适的值 ==> 要修改`dummy`变量的值 ==> 通过给`key1`和`key2`赋值来实现
 
 5. What `process_keys34` Does
 > 在了解函数形参申请堆栈空间的顺序、以及函数调用过程中返回地址的存储过程之后，通过`process_key34`可以改变程序的执行顺序。
 
 6. The line of source code that is executed when the first call to `process_keys34` returns.
 > 在`key3`与`key4`被赋予正确值的情况下，第一次调用`process_key34`的返回地址，被修改为第二次调用`process_key34`的返回地址。故：在第一次调用`process_key34`后，程序直接执行`extract_message2`函数。
 
 7. The meaning of the third and fourth keys in terms of variables and addresses in the
decoder program.
> 要强制执行`extract_message2` ==> 要修改`process_key34`的返回地址 ==> 通过给`key3`和`key4`赋值来实现


----------
### 参考资料

博客：[深入理解C语言的调用过程](http://blog.chinaunix.net/uid-23069658-id-3981406.html) .