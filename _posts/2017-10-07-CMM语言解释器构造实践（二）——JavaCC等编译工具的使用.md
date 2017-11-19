---
layout:     post
title:      "CMM语言解释器构造实践（二）——JavaCC等编译工具的使用"
subtitle:   " "
date:      2017-10-07 00:25:00
author:     "Snow"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
- CMM
---

### 前言
上篇博文中我们已经简要介绍了CMM语言的基础特点，以及整个编译器项目的基本开发流程。下面就对开发的第一个阶段**“编译工具的使用”**详细说明。

----------


### 编译工具的发展

>  
- lex/yacc (flex/bison)
generate bottom-up parsers which are often hard to understand, hard to debug and give weird error messages
- antlr4 (Java) and antlr3 
produces a recursive descent top-down parser which is much easier to understand, you can actually debug it easily, you can only use subrules for a parse operation (e.g. just parse expressions instead of the full language)
- SableCC (Java)
- and SimpleParse (Python)
- JavaCC
……

在编译原理的课堂上，我们粗略接触了lex/yacc等最初的编译工具。这类编译器最大的特点，是**自底向上分析**，通常很难理解，也难以在开发过程中进行调试与错误处理。

Antlr (ANother Tool for Language Recognition)、JavaCC等编译工具，是如今更为常用的编译器生成工具，此类编译器由于具有**自顶向下分析**的特点，更易被人接受，也更易使用，极大的提高了开发效率。这样的编译工具所生成的解析器叫做递归下降解析器（recursive-descent parser），属于自顶向下解析器（top-down parser）的一种。

除此之外，还存在着SableCC，以及针对解释型语言Python的SimpleParse等编译工具。

在本项目中，笔者主要采用了JavaCC编译工具，下面来对其进行更进一步的了解。

----------

### JavaCC简介

JavaCC是一个词法分析生成器和语法分析生成器。

> 词法分析和语法分析是处理输入字符序列的软件构件，编译器和解释器协同词法分析和语法分析来“解密”程序文件，不仅如此，词法分析和语法分析有更广泛的用途。

> JavaCC并不是一个词法分析器或者语法分析器，它只是一个生成器。就是说，它读取文本后，基于一定的规则产生词法分析器和语法分析器的Java代码。

> 词法分析和语法分析变的越来越复杂，软件工程师直接用Java进行词法分析和语法分析时必须要充分考虑各规则间的相互作用。

> 例如，在对 C语言的词法分析中，处理整型常量和浮点常量的代码是不能分开的，因为浮点数和整数的前面部分是一样的。使用诸如JavaCC语法分析产生器，对整型常量 和浮点常量是可以区分的，它们的共同点可在代码生成过程中提取出来。这种模块性意味着JavaCC文件比直接的Java程序更容易写，更容易读，也更容易 修改。通过JavaCC语法分析生成器的使用，软件工程师可以节省大量的时间，并且软件的质量也更高。
 
总之，如何使用JavaCC呢？一句话来讲：你只需要叙述“待编译语言”的**语法规则**，而JavaCC自动替你生成词法、语法分析器。
也就是说，JavaCC并不是编译器，而是**生成编译器的工具**，而且它所生成的编译器只包括了词法分析、语法分析过程，后续的语义分析等过程，还是需要你来完成。
而为什么这个工具叫“Java”CC呢？这是因为JavaCC生成这个编译器，是由Java语言编写的。

那么，我们的工作就演化成了三步：首先，配置JavaCC环境。其次，叙述语法规则，也就是编写`.jj`文件。最后，使JavaCC处理`.jj`文件，以生成若干个类文件（也就是我们的编译器）。

上述过程工作完成后，JavaCC为我们生成了相应的编译器。那么这个编译器又是如何工作的呢？
我们先不考虑代码怎么写，只思考开发过程。假如我们现在已经得到了这个编译器，并假设我们需要从命令行中输入源码，我们输入一个简单的赋值语句：`sp = 100;`，那么编译器会做什么事情呢？

毫无疑问，编译器会对我们所输入的源码进行解析，该解析过程包括两个阶段：

![recog](http://img.my.csdn.net/uploads/201710/06/1507304907_2663.png)

在第一阶段，使用词法分析器将输入解析成一个个单词（token），即词法分析（lexical analysis），对应的分析程序叫做lexer，负责将符号（token）分组成符号类（token class or token type）
在第二阶段，对第一阶段的tokens进行分析，解析出句子的结构，对应的分析程序为parser。默认JavaCC会构建出一棵分析树（parse tree）或叫语法树（syntax tree）。

这里简要的介绍一下语法树 (Syntax Tree)。
> 语法树的叶节点token，而父结点是包含其子结点的词组名（phase），线性的句子也就是对语法树的序列化。
生成语法树的好处有：
1） 树形结构易于遍历和处理，易于理解，方便应用代码做进一步处理。
2） 多种解释或翻译的应用代码都可以重用一个解析器。JavaCC还支持将应用处理代码嵌入到语法中。
3） 对于因为计算依赖而需要多趟处理的翻译器来说，语法树使得可以被高效地多次遍历，而无需每次解析。

到这里，JavaCC的基本工作原理就介绍完成了。

----------

### JavaCC环境配置
关于JavaCC的环境配置，已经有各式各样的使用教程了，这里就不再赘述。总的来说，可采用如下两种方式：

 1. 通过命令行：先在官网下载对应的配置包，再配置环境变量，最后通过`javacc *.jj`命令，生成若干个类文件。
 2. 通过IDE插件：在eclipse或idea等IDE的插件库中，都含有JavaCC插件，只需搜索后安装即可。

----------

### 编写语法规则

配置好环境之后，我们就进入了第二步，也是核心的一步：叙述语法规则，即编写`.jj`文件。

`.jj`文件不属于某种高级语言，其编写有自己的语法规则，但非常简单，极易上手。文件中主要包含以下四个部分：参数配置、程序入口、词法叙述、语法叙述，我们下面就把一个`.jj`文件拆解开来看，分别进行这四个部分的编写。

在正式开始之前，我们先通过官方文档上的一个简单的例子，来整体了解一下`.jj`文件是如何叙述语法的。
```java
/*
* javacc-5.0/examples/SimpleExamples/Simple1.jj
*/

options {
  LOOKAHEAD = 1;
  CHOICE_AMBIGUITY_CHECK = 2;
  OTHER_AMBIGUITY_CHECK = 1;
  STATIC = true;
  DEBUG_PARSER = false;
  DEBUG_LOOKAHEAD = false;
  DEBUG_TOKEN_MANAGER = false;
  ERROR_REPORTING = true;
  JAVA_UNICODE_ESCAPE = false;
  UNICODE_INPUT = false;
  IGNORE_CASE = false;
  USER_TOKEN_MANAGER = false;
  USER_CHAR_STREAM = false;
  BUILD_PARSER = true;
  BUILD_TOKEN_MANAGER = true;
  SANITY_CHECK = true;
  FORCE_LA_CHECK = false;
}

PARSER_BEGIN(Simple1)

/** Simple brace matcher. */
public class Simple1 {

  /** Main entry point. */
  public static void main(String args[]) throws ParseException {
    Simple1 parser = new Simple1(System.in);
    parser.Input();
  }

}

PARSER_END(Simple1)

/** Root production. */
void Input() :
{}
{
  MatchedBraces() ("\n"|"\r")* <EOF>
}

/** Brace matching production. */
void MatchedBraces() :
{}
{
  "{" [ MatchedBraces() ] "}"
}
```

> 这是一个简单的JavaCC语法来识别一系列的“{”和后面的相同数量的“}”，之后跟着0个或多个行终结符，最后是文件的结尾。

> 
这个语法文件以一些JavaCC所提供的Options的参数设置开始。在这个例子中，Options的参数都是它们的默认值。因此，这些参数实际上是不需要的。程序员甚至可以完全忽略Options这一部分，或者省略其中的一个或多个Options的参数，详细的关于Options的参数设置的问题请参考JavaCC的文档。


> 
接下来的是一个处在”PARSER_BEGIN(name)”和”PARSER_END(name)”中间的编译单元。这个编译单元可以是任意的复杂。在这个编译单元中唯一的限制就是它必须定一个一个叫”name”的类——与PARSER_BEGIN和PARSER_END的参数的相同。这个”name”被用作语法分析产生器生成的java文件的前缀。


> 
在上面的例子中，语法分析器产生的类包括一个主程序。这个主程序通过调用使用一个类型为java.io.InputStream的参数的构造函数创建了一个Simple1的对象。


> 
这个主程序调用文法的非终结符。所有的非终结符在JavaCC的语法分析器中的地位是平等的，因此，一个非终结符可以分析有关的任何一个该文法的非终结符。

 


> 
下面是一系列的产生式。在这个例子中，有两个被分别定义为非终结符Input和MatchedBraces的产生式。**在JavaCC的语法中，非终结符的编写和实现与Java中的方法是一致的。当一个非终结符位于一个产生式的左边的时候，它被认为将要被声明，它的句法和Java的相一致。当它在产生式的右边的时候，它的用途与Java中的方法调用相似。**


> 
每一个产生式定义它的左边的非终结符以一个冒号（：）结尾。之后紧跟着的是一些在花括号（{}）里面的声明和语句，它们将作为产生方法的普通声明和语句。（在上面的例子中，因为没有声明，所以是空的{}）这之后是一系列的在闭合的花括号里的拓展语句。


> 
JavaCC中的词法的Tokens是简单的字符串如"{", "}", ""n", ""r"，或者是复杂的正则表达式。在上面的例子中，有一个正则表达式<EOF>,当它被匹配的时候意味着文件的结束。所有的正则表达式都在封闭的尖括号（<>）内。


> 
上面列子的第一个产生式的非终结符”Input”拓展到非终结符”MethodBraces”，之后跟着0个或多个行终结符(""n" 或 ""r")，然后这文件的结束符。


> 
上面列子的第二个产生式的非终结符” MethodBraces”拓展到token”{”，之后跟着可选择嵌套的MethodBraces，之后跟着一个token”}”。在JavaCC输入文件中，方括号[…]表示…是可选的。


> 
[…]同样可以写成(…)?。这两种形式是相等的。其他可能会在拓展式中出现的结构是：


> 
   e1 | e2 | e3 | ...    : 选择 e1, e2, e3, etc.其中之一


> 
   ( e )+             : e出现一次或多次


> 
   ( e )*             : e出现零次或多次


> 
上面的结构可以相互嵌套，如：(( e1 | e2 )* [ e3 ] ) | e4


#### 参数配置

```java
options{
    //待编写
}
```

#### 程序入口

```java
PARSER_BEGIN(CMMParser)

import java.util.*;

public class CMMParser{

    public static void main(String[] args) throws ParseException{
        CMMParser parser = new CMMParser(System.in);
        parser.Start();
    }
}

PARSER_END(CMMParser)

SKIP : {
    " "
    |  "\t"
    |  "\n"
    |  "\r"
    |  <"//" (~["\n","\r"])* ("\n" | "\r" | "\r\n")>
    |  <"/*" (~["*"])* "*" ("*" | ~["*","/"] (~["*"])* "*")* "/">
}

//--------------------开始进行词法分析--------------------
//定义关键字
TOKEN : {
	<IF: "if">
	| <ELSE: "else">
	| <WHILE: "while">
	| <READ: "read">
	| <WRITE: "write">
	| <INT: "int">
	| <REAL: "real">
}
    ...
```
其中，所要生成的编译器入口，就涵盖在`PARSER_BEGIN()`和`PARSER_END()`中，这个主体部分由一个类组成，这个类的[类名]（即`CMMParser`）由我们自由编写，最终生成的若干个类文件中，存在一个“[类名].java”类。在此例中，即会生成`CMMParser.java`。
!(IDE)[]

我们再来看所编写的CMMParser类。CMMParser类中采用了最简单的编写方式，只包含了一个主函数。程序的第8行说明：通过`System.in`参数，这个编译器能够在控制台输入代码。第9行的`Start()`函数则标志着，整个语法分析的过程，是从`Start()`函数开始的。也毫无疑问，在程序下面语法叙述的部分，一定包含着一个`Start()`函数。

其实程序入口的代码到13行就已经结束了。那么接下来的`SKIP`块又有什么功能呢？
`SKIP`块的代码就是在说，编译器在读取源码的时候，如果碰上了下面所列出的内容，则会自动跳过，也就是忽略这些内容对其解析的影响。
在此文件中我们可以知道，编译器会跳过tab符、空格、回车，以及单行注释"//"与多行注释"/* */"。

#### 词法叙述

```java
//定义关键字
TOKEN : {
	<IF: "if">
	| <ELSE: "else">
	| <WHILE: "while">
	| <READ: "read">
	| <WRITE: "write">
	| <INT: "int">
	| <REAL: "real">
}

//定义自然数
TOKEN : {
	<INTEGER_LITERAL: ["1"-"9"](<DIGIT>)* | "0">
}

//定义实数
TOKEN : {
	<REAL_LITERAL: (<DIGIT>)+
	| (<DIGIT>)+"."
	| (<DIGIT>)+"."(<DIGIT>)+
	| "."(<DIGIT>)+>
}

//定义标识符
TOKEN : {
	<IDENTIFIER: <LETTER>
	| <LETTER>(<LETTER> | <DIGIT> | "_")*(<LETTER> | <DIGIT>)+>
	| <#LETTER: ["a"-"z", "A"-"Z"]>
	| <#DIGIT: ["0"-"9"]>
}
```

下面进入了词法分析部分，我们通过正则表达式，定义了关键字、自然数、实数以及标识符。

#### 语法叙述

接下来则是最为困难的语法分析部分。在上方我们提到了`Start()`函数，它是整个语法分析过程的开始。
```java
void Start() : {}
{
    Procedure() "#"
}

void Procedure() : {}
{
    //...
}
    ...
```
从上面的代码我们就可以清晰地体会到**自顶向下分析**的特点了，语法分析从`Start()`函数开始，然后再到`Procedure()`函数，再到……
同时我们也看到，第3行的代码说明了程序的输入结束符`#`。

在进行后续代码的编写之前，我们首先要**“理解CMM是怎样一种语言”**，即对CMM的语法有整体的了解。由于我们不可能一下子就开发一个像C语言那样庞大的编译器，涵盖函数、指针等各种复杂的功能。即便我们拥有那样伟大的理想，从**迭代开发**的角度来看，我们也要先实现一个“初级版本”的编译器，因此就需要明确这个“初级版本”的CMM语言有哪些语法要求。

我们先回顾一下一个`.c`文件的常见格式。
```c
 //头文件
 #include<stdio.h>
 ...

 //全局变量
 int a,b;
 ...

 //函数声明
 void func();
 ...

 //主函数
 int main(int argc, char* argv[]){
    ...
    return 0;
 }

 //函数实现
 void func(){
    ...
 }
```
在这个初级版本中，我们先忽略函数、头文件这样的复杂语法，只考虑基础的语法语句。通过进一步分析语法，我们也做了如下简化,以降低难度。（这样简化的原因，可参见最下方的附录）
> 
1. 声明语句与赋值语句：必须先声明，后赋值。
  如：`int a; a = 1;`为正确语法，而不能使用`int a = 1;`
2. 数组的赋值：由于没有只有词法与语法分析，因此数组的赋值只能先统一声明，再对单个元素赋值的方法。
  如：`real[] r; r[0] = 0; r[1] = 1;`
3. if-else语句：选择语句包含两种，含else的语句，与不含else的语句。
  如：`if(){}`、`if(){}else{}`、`if(){}else if(){}else{}`均为正确语句，但`if(){}else if(){}`则无法识别。
4. 算数运算符不含`++`、`--`等运算符。
5. 需在控制台输入文本。`#`为输入结束符。

对于简化后的CMM语言，我们可以将CMM语言的语法通过语法描述图 (Syntax Diagram) 描绘出来。

![d1](http://img.my.csdn.net/uploads/201710/07/1507306512_2760.jpg)

![d2](http://img.my.csdn.net/uploads/201710/07/1507306519_4188.jpg)

![d3](http://img.my.csdn.net/uploads/201710/07/1507306525_1307.jpg)

通过查阅语法描述图，再通过正则表达式将各**产生式**描述出来，语法分析的过程就完成了。
```java
void Start() : {}
{
    Procedure() "#"
}

void Procedure() : {}
{
    Block() | (Statement())+
}

void Block() : {}
{
    "{" (Block() | (Statement())+)+ "}"
}

void Statement() : {}
{
    Declaration()
    | Assignment()
    | <WHILE> "(" Condition() ")" Block()
    | <READ> "(" <IDENTIFIER> ("," <IDENTIFIER>)* ")" ";"
    | <WRITE> "(" Expression() ("," Expression())* ")" ";"
    | Choice()
}

void Declaration() : {}
{
    //...
}

...
```

----------

### 调试与出错处理

通过对CMM语法的分析，笔者编写了如下的测试用例，经多次调试后可成功编译。
```c
//测试用例

int a, b;
real[] r;
a = 1;
read(b);
r[0] = 0;

while(a < b){
    if(a == 3){
        r[3] = 3;
    }else if(a == 5){
        r[5] = 5;
    }else{
        r[7] = (a * 3) - (b / 3);
    }
    a = a + 1;
}

write(a, b, r);

#
```

至此，我们通过JavaCC编译工具，就得到了一个具有词法、语法分析功能的编译器。

----------

### 附录
#### 关于JavaCC
JavaCC是一个用Java语言写的一个Java语法分析生成器，它所产生的文件都是纯Java代码文件，JavaCC和它所自动生成的语法分析器可以在多个平台上运行。

下面是JavaCC的一些具体特点：

 1. TOP-DOWN：JavaCC产生自顶向下的语法分析器，而YACC等工具则产生的是自底向上的语法分析器。采用自顶向下的分析方法允许更通用的语法（但是包含左递归的语法除外）。自顶向下的语法分析器还有其他的一些优点，比如：易于调试，可以分析语法中的任何非终结符，可以在语法分析的过程中在语法分析树中上下传值等。
 
 2.  LARGEUSER COMMUNTIY：是一个用JAVA开发的最受欢迎的语法分析生成器。拥有成百上千的下载量和不计其数是使用者。我们的邮件列表(https://JavaCC.dev.java.net/doc/mailinglist.html )和新闻组(comp.compilers.tools.JavaCC)里的参与者有1000多人。
 
 3.  LEXICALAND GRAMMAR SPECIFICATIONS IN ONE FILE：词法规范（如正则表达式、字符串等）和语法规范（BNF范式）书写在同一个文件里。这使得语法易读和易维护。
 
 4.  TREEBUILDING PREPROCESSOR： JavaCC提供的JJTree工具，是一个强有力的语法树构造的预处理程序。
 
 5. EXTREMELYCUSTOMIZABLE：JavaCC提供了多种不同的选项供用户自定义JavaCC的行为和它所产生的语法分析器的行为。
 
 6. CERTIFIEDTO BE 100% PURE JAVA：JavaCC可以在任何java平台V1.1以后的版本上运行。它可以不需要特别的移植工作便可在多种机器上运行。是Java语言”Write Once, Run Everywhere”特性的证明。
 
 7. DOCUMENTGENERATION：JavaCC包括一个叫JJDoc的工具，它可以把文法文件转换成文本本件(Html).

 8. MANYMANY EXAMPLES：JavaCC的发行版包括一系列的包括Java和HTML文法的例子。这些例子和相应的文档是学习JavaCC的捷径。
 
 9.  INTERNATIONALIZED：JavaCC的词法分析器可以处理全部的Unicode输入，并且词法规范何以包括任意的Unicode字符。这使得语言元素的描述，例如Java标识符变得容易。
 
 10. SYNTACTIC AND SEMANTICLOOKAHEAD SPECIFICATIONS：默认的，JavaCC产生的是LL(1)的语法分析器，然而有许多语法不是LL(1)的。JavaCC提供了根据语法和语义向前看的能力来解决在一些局部的移进-归约的二义性。例如，一个LL(k)的语法分析器只在这些有移进-归约冲突的地方保持LL(k)，而在其他地方为了更好的效率而保持LL(1)。移进-归约和归约-归约冲突不是自顶向下语法分析器的问题。
 
 11. PERMITS EXTENDED BNFSPECIFICATIONS：JavaCC允许拓展的BNF范式——例如(A)*,(A)+等。拓展的BNF范式在某种程度上解决了左递归。事实上，拓展的BNF范式写成A ::= y(x)* 或 A ::= Ax|y更容易阅读。
 
 12. LEXICAL STATES ANDLEXICAL ACTIONS：JavaCC提供了像lex的词法状态和词法动作的能力。
 
 13.  CASE-INSENSITIVELEXICAL ANALYSIS：词法描述可以在整个词法描述的全局域或者独立的词法描述中定义大小写不敏感的Tokens。
 
 14.  EXTENSIVE DEBUGGINGCAPABILITIES：使用选项DEBUG_PARSER, DEBUG_LOOKAHEAD, 和 DEBUG_TOKEN_MANAGER，使用者可以在语法分析和Token处理中使用深层次的分析。
 
 15. SPECIAL TOKENS：Tokens可以在词法说明中被定义成特殊的Tokens从而在语法分析的过程中被忽略，但这些Tokens可以通过工具进行处理。
 
 16. VERY GOOD ERRORREPORTING：JavaCC的错误提示在众多语法分析生成器中是最好的。JavaCC产生的语法分析器可以清楚的指出语法分析的错误并提供完整的诊断信息。

总体来说，JavaCC主要有以下功能：

 1. JavaCC用来处理语法文件（jj）生成解析代码
 2. JJTree 用来处理jjt文件，生成树节点代码和jj文件
 3. JJDoc 根据jj文件，生成文本本件(Html)

#### 关于语义分析
我们开始时就提到，JavaCC能够帮我们做的，只有词法分析和语法分析过程，而语义分析是无法自动完成的。因此也就不存在**“语境”**，或者**“上下文”**的概念，对于类似于“类型兼容”、“数组越界”等问题，是无法处理的。
```c
int a;
real[] r;

a = 0;
r[a] = 1;   //该语句无法识别，因为“[]”中只能识别自然数，而不能识别标识符。
```

#### 关于LOOKAHEAD
我们经常使用的if-else语句，其实属于非常复杂的文法，也不能通过常规的LL(k)文法识别。其文法的复杂型体现在两点：
1. 大括号`{` `}`的使用：如，当if、else后面只有一行语句时，可以不使用大括号，而当语句多于一行时，则必须使用。
2. else的使用：如，可以不使用else，可以使用if-else if-else，也可以使用if-else if。

以else的使用为例，若用正则表达式列举出其所有的使用方法，则如下方所示
```java
...

<IF> "(" Condition() ")" Block() 
    (<ELSE> <IF> "(" Condition() ")" Block())*      //可重复0次至无穷次
        [<ELSE> Block()]        //可选

...

//若输入如下代码：
if(a == 0){
    b = 1;
}else {     //此行无法识别
    b = 0;
}

```

但若如此书写`.jj`文件，编译器在碰到`if-else`语句时，即：当解析至`<ELSE>`时，编译器不知道是该选择第4行所示的分支，还是第5行所示的分支，因此便无法识别。

因此我们在上面才做了适当的简化操作，对于if-else语句：选择语句包含两种，含else的语句，与不含else的语句。若语句中包含else，则必须有`else{}`,而不能只包括`if(){}else if(){}`。

通过简化后的语法叙述如下：
```java
(<IF> "(" Condition() ")" Block() <ELSE>)+ Block()
    | <IF> "(" Condition() ")" Block()
```
但这样的语法仍存在相同的问题。类似于上方的情况，当编译器在解析`<IF> "(" Condition() ")" Block()`的时候，依然不知道是该选择哪个分支。
但如果再往下扫描，通过判断下面的代码中存不存在`<ELSE>`，就可进行准确的识别。即：若存在`<ELSE>`，则进入第一行的分支，否则则进入第二行的分支。
其实这样的判断，就是LOOKAHEAD文法的思想，当不同产生式的右侧，存在相同的左部时，通过**“先向前扫描”**，来判断出到底采用哪个产生式来进行归约。
```java
LOOKAHEAD(<IF> "(" Condition() ")" Block())
    (<IF> "(" Condition() ")" Block() <ELSE>)+ Block()
    | <IF> "(" Condition() ")" Block()
```
我们通过LOOKAHEAD语句即可解决这一问题，参数`<IF> "(" Condition() ")" Block()`的意思就是：在遇见`<IF> "(" Condition() ")" Block()`之前（而且要求后面不再存在其他字符，即：只存在这个参数），就一直进行移进而不进行归约，当能够判断出“是否只存在`<IF> "(" Condition() ")" Block()`”时，才进行规约。

那么我们也许会产生疑问，这样的LOOKAHEAD语句，为何无法应用于最初定义的那个文法？
```java
<IF> "(" Condition() ")" Block() 
    LOOKAHEAD（[<ELSE> Block()]）       //向前识别[<ELSE> Block()]
    (<ELSE> <IF> "(" Condition() ")" Block())*      
        [<ELSE> Block()]
```
笔者尝试用这样的方法解决该文法存在的归约冲突，但结果却不如人意。我们来分析这种情况：当我们只使用最简单的if语句，没有else-if，也没有else时，编译器无法识别。因为`(<ELSE> <IF> "(" Condition() ")" Block())*`分支可能为空，`[<ELSE> Block()]`分支也可能为空，归约冲突便依然没有得到解决。
这也说明了这个文法的复杂程度已经超出了LL(k)文法，需要更强大的文法来识别。

关于LOOKAHEAD语句的更详细用法，参见http://blog.csdn.net/chaofanwei/article/details/25559029.
