---
layout:     single
title:      "的大学"
excerpt:   "迎接总大张旗鼓，告别都悄无声息。"
date:       2018-8-4 15:10:00
toc: true
categories:
- Essay
---

## 前言

最近，保研之事终于告一段落，最终拿到的offer是：中国科学院计算技术研究所-前瞻研究实验室-跨媒体计算组-学硕，导师为曹娟老师，研究方向为大规模社会媒体数据挖掘。

从结果来看，研究方向非常适合自己，“学术型硕士”也为之后的 工作/读博 提供了缓冲的空间，应该算给自己三年的大学生活交了一份不错的答卷。

<img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-0.jpg" width="60%">

以我的所见所闻，从“硬件”的角度讲：若论“什么是对offer最重要”，那一定是课业成绩（GPA）与排名，这决定了最终可以拿到**哪一档**的offer，或者说，它决定了我们的**最低水平**。在成绩因素之外，第二重要的即是 科研/项目/比赛经历，这决定了最终可以拿到**哪一个**offer。其实这也是显而易见的——研究生，重在“研究”二字，只有学生的经历和导师实验室的生活越相关，竞争力才越强：对于理论研究氛围浓重的实验室，最关键的一定是科研经历；对于开发项目多的实验室，最关键的一定是项目/比赛经历（工程能力）。

有很多老师在招生时都会宣称：非常看重学生的“软性”指标，比如性格是否踏实稳重，是否有“self-motivation”，是否具有良好的沟通能力与团队精神，但此类标准常常难以捉摸、飘忽不定、无从发力。

回顾过去的三年生活，自己在 科研/项目/比赛经历 上面，经历了非常困难的探索之路，也遇到过数不清的烦恼：

- 什么是科研？
- 究竟是做科研还是搞开发（或，究竟做科学家还是工程师）？
- 人工智能（或数据挖掘、机器学习、深度学习等）如此热门，就偏偏选择它吗？
- 确定了科研，也确定了人工智能，之后呢？该选择什么研究领域（如计算机视觉、自然语言处理、生物信息、脑科学、机器学习理论等）？

当然，找寻答案的过程均非一蹴而就。有的问题，确实需要通过大量的实践，甚至需要花好多年去不断认识、理解、修正。

此文记录了我的若干探索经历。

## 实验室经历

### 大二下（2017年3月-8月）

我是在大二下学期加入实验室的，绝不算早，但也不算太晚。当时有幸结识了一位大神级别的学长，于是就加入了他所在的实验室。这位学长决心出国申博，在多次交谈中，他也给我讲述了许多出国念书的好处。在此之前我并没有出国的打算，但学长的观点对我的冲击还是很大的，我决定从那个学期开始准备托福，开始进行出国的准备。于是便顺理成章地，在加入实验室后开始从事科研，也树立了发表paper的目标。

可科研生活并不像我想象的那么简单。

老师给我安排的研究方向是**生物信息数据挖掘**，再具体点说，是**单细胞基因表达数据的数据集成方法**。那时我对数据挖掘、机器学习、深度学习等一无所知，也不太知道这个研究方向跟计算机之间有什么联系，只是听老师讲这个方向很火，容易发论文。当时这个课题是两位学长在做，但只做了一半。老师首先给我的具体任务就是：弄清楚学长们在做什么，之后再把代码跑通。

#### “危险”的学习方法

机器学习、深度学习、python，我都不会。我询问学长应该怎样自学相关的理论，学长说“先学机器学习，之后学的差不多了再过渡到深度学习”；又问了大神室友，他介绍了一些西瓜书、CS229、CS231、廖雪峰python教程等学习资料。很迷茫，资料太多，该学的东西太多，也不知该如何下手。又看了看知乎上的一票小软文，大家都说“要慢慢学，不能急”，于是就劝自己静下心来，打算用一个学期的时间学习斯坦福的CS229课程。

大家都说这门课是“神课”，我一开始学习的时候，也是激情澎湃、热情似火，又是记笔记，又是学习英文教案，有时还故意把中文的字幕关掉，想着能够练一练自己的英语听力。

在看似按部就班、扎扎实实的学习中，我至少犯了如下的错误：

- 高估了自己的英文学术能力。对英文课程、英文教案的学习效率很低，总是如浮光掠影，看了就忘。
- 一味追求理论输入，严重缺乏实践。在学习方法上，还是像高中学习时那样，以为听讲、看书、记笔记就能解决一切问题，没有代码或项目的辅助练习。
- “单线程”的学习方法。认为学习路线图就应该是“先学A，再学B，后学C”，但花了两三个月的时间，只学了A，而且学的似懂非懂，对B、C，更是完全陌生。

除此之外，我还发现了一些人们称之为“天赋”的东西。在大学之前，我一直觉得自己“有天赋”，觉得对于多个知识点，可以很快地理清脉络，并发现其中的关联性。但对于计算机科学的学习，并没有丝毫的敏感性，学A时，觉得A就是A，跟B并无关系。在观察了一些同学之后，我才知道什么叫天赋，比如室友就经常说“我觉得A、B一起学，会有奇效”。此种境界，大抵就是“蓦然回首，那人却在灯火阑珊处”吧。

#### “痛苦”的研究方向

在基础知识的补充之外，我的科研轨迹似乎始终停滞不前。

在我认为自己已经“搞清楚学长们做的工作”之后，便去向老师汇报。那段时间，老师似乎有很多别的事情，经常整个月的出差，整个实验室里也人员繁杂，管理松懈，“混水摸鱼”的现象非常多。老师让我“读论文，找idea，如果找到idea了就去和他讨论”。

读论文真的是一件痛苦的事情，尤其是读这种“生物信息”相关的论文，学科背景太过浓重，有太多太多生物学科的单词。我跟老师反映“没有idea”，老师说“这很正常，论文读多了就有了，说明你读的还不够多”。

我承认自己读的论文确实还不算多，但这种太过放养的培养方式，确实让我很无力。我问过其他实验室的情况，可得到的反馈大多是“差不多，大家都这样，整个国软都非常水，没几个老师搞科研”，而且很多同学跟我说，我的老板已经算是整个院里做科研做得非常好的了。

因为自己也不明白科研究竟是怎么一回事，所以也就稀里糊涂的，认为大家都是这样。但确实很多时候都想吐槽，想说自己作为一个本科生，难道不应该是老师提出一些idea，然后我去实现，或者是在学长的手下打打杂什么吗。自己找idea，再做实验，这好像是博士才要干的事吧……

最关键的是，这个研究方向真的让我“欲罢不能”，我根本提不起任何兴趣去寻找“单细胞基因表达”中振奋人心的研究之处。

直到现在，我都对人工智能生物方向的研究存有阴影，毕竟是被狠狠安排过的人……

#### 不出国了，“真香！”

在迷茫且痛苦的五个月过后，我决定不出国了。

逻辑线条：

- 首先，出国申master太贵。（那读博？
- 我都被研究生活制裁成这样了，还读博？？
- 好，不出了。真香。

导火索：

- 英语不好。
- 真香。

我也尝试分析了与出国有关的很多选择，仅以北美为例：

| 选择       | 特点                                         | 阐述                                                         |
| :--------- | :------------------------------------------- | :----------------------------------------------------------- |
| 授课型硕士 | 巨额学费，申请难度最小                       | 由于读书时花销巨大，因此最好需要留在当地工作，3-5年之后赚回成本、利润 |
| 博士       | 全额奖学金，但申请难度很大，要决心致力于科研 | 如果本科期间没有较好的科研训练、没有形成良好的研究视野、对研究方向的敏感度不够，则很容易“踩坑” |
| 研究型硕士 | 申请难度大                                   | 给自己留了很好的 工作/科研 缓冲空间，在研究生期间将得到很好的科研训练 |

当然还有各种曲线救国的方式：不去北美，而选择香港、澳洲、欧洲等；不申CS方向，而改换相近的专业等。对我而言：一来，自己缺少直博的勇气。二来，如果不致力于科研，仅论在国外工作、生活，这其中的吸引力对我并不算特别巨大，觉得没有“铁了心出国”的必要。加之，申请本身就是一件昂贵、复杂，且充满运气与玄学的事情，因此就放弃了出国的打算。

### 大三上（2017年10月-2018年1月）

#### 不做科研了

大二下学期+暑假，差不多半年的时间过去了，我并没有感觉自己有任何提高：

- 科研上：对“生物信息”的研究，不仅没带来实质上科研能力的提高，而且还让我丧失了对研究的兴趣。
- 技术上：没有做过开发项目，代码熟练度没有提升；对专业主干课程，也仅停留于课堂所学的理论知识，技术能力也没有长进。

为了让自己迅速的成长起来，或者说，希望能够在最短的时间内做出“肉眼可见”的成果，我选择了退出实验室的科研组，而加入开发组，成为一个跨平台应用开发团队的一员。

整个团队大约有30人，并有一位代码能力极强的学长作为leader。项目采用微服务的架构，我作为其中一名Java后台开发者，独立维护一个服务模块。由于应用需要在短时间内上线，因此项目的功能需求、开发流程还算符合现实场景，而不是“小打小闹”的玩具性实验工程。

项目大约持续了2-3个月，我最终的代码量应该在3500行左右，感觉自己的能力确实得到了较大提升。

#### “你渴望力量吗？”
<img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-2.JPG" width="70%">
除此之外，这个学期还沉浸于“技能树养成”，希望自己能够在编程语言、算法、操作系统、编译原理、计算机系统等多个专业主干课程方面，都能得到全面的提高。

这里暂不评判这种学习方法（下文会详细分析），只列举一些它为我带来的影响：

- 首先，我更清楚地认识到了各门课程之间的关联。
- 其次，在“养成”的过程中，我选读了《Head First Java》、《算法》、《利用python进行数据分析》、《编译原理》等书中的部分章节，并培养起快速阅读、重点阅读的习惯。
- 最关键的是，这个积累的过程会令人安宁、充实，不再急功近利，而注重于积累本身。

<img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-1.png" width="100%">

### 大三下（2018年3月-2018年6月）

#### 重新认识科研

今年3月份——最后一个可以给保研加分的学期，开始了。

我退出了原来的实验室，并物色了一个新的导师和实验室，打算重新做科研，其中有几个原因：

- 原来的开发项目已经入尾声，团队中的大多数人已经开始准备春招（公司实习）。
- 经过一个项目的锻炼，已经大致明白了实际应用开发的流程。如果继续留在原来的实验室，做新的开发项目，很大可能会写大量的业务代码，能力提升的速度将不再像之前那样快。
- 从技能树的角度，“开发技能”已掌握了一部分，但“科研能力”的分支仍存在大片的空白。
- 之前虽然被“生物信息”的研究折磨了很久，但若由此便永久放弃科研，未免显得武断。如今自己有了一定的代码能力，对学科也有了更深的认识，此时再去接触科研，或许是个好时机。
- 从功利的角度：研究生，或多或少都要搞一些研究。只有提前认识了研究，并拥有相关经历，才能让自己更有竞争力。

新加入的实验室科研氛围很浓厚，组里完全不做工程，导师对学生很负责，且对服务器等硬件的投资绝不含糊。导师之前主攻网络方向，但鉴于人工智能实在太火，学生们也都想做机器学习相关的研究，因此组里便也刚增添了一些类似的课题。

初入实验室，尽管老师很热情，但依然说“以学生为主，并让我们找自己感兴趣的研究方向”。由于之前的科研就死在了“自己找idea”上面，这次确实是有点怕了。

我觉得不能再这样漫无目的了，于是和另一个同学在 Kaggle 上找了一个数据挖掘竞赛，主题是广告欺骗检测（Ad Fraud Detection），打算“以赛带学”，从比赛中学习，也想从比赛过渡到科研，以找到感兴趣的研究方向。

重新着手科研，三个月的时间内，几乎没有做无谓的工作：

- 开始时，学习打Kaggle比赛，学习其他参赛选手的解决思路，并亲自动手实践。比赛的过程大约持续了40天，最终的结果是Top 30%，排名不算好，但对于“入手科研”的目标算是基本达到了。
- 在比赛行至中程，也同时开始阅读相关领域论文。在浏览相关博客的过程中，发现了一个新的研究领域：用户点击率预测（Click-Through Rate, CTR），并在这个领域下发现了工业界的海量探索。
- 比赛结束后，把CTR作为了新的研究方向，并开始学习深度学习、神经网络等模型在其中的应用。阅读了2016年至今的大量的优质论文，并有了一些小的idea。
- 在此期间，也同时学习吴恩达在Coursera上的网课：Deep Learning Specialization，保持理论知识的同步摄入。

由于导师之前亦没接触过人工智能的相关课题，说实话，对我们的指导并不如预期。科研过程的几乎所有决策，都是在我和partner的反复商讨后确定的。很幸运，作为初学者能够在三个月内有这样的进展，已经很令人满意了。

#### 就一定是人工智能吗？

在这个过程中，也看了很多知乎上的“人工智能劝退文”。在科研之初，也确实很惆怅，觉得计算机科学、软件工程可以研究的领域那么多，就偏偏要选择人工智能吗？就偏偏要凑这个热闹，争做风口的一头猪吗？万一将来人工智能不火了，岂不是凉透了？

当时的思路斗争大致如下吧：

- 不做人工智能，还能做什么？
- 体系结构，操作系统，数据库，编译原理，分布式计算，高性能计算，网络，软件理论……好像有很多领域，可能略微拥有兴趣的，也只有分布式计算、网络。
- 对于分布式，本科期间确实太难接触到；对于计算机网络，由于大三下学期才刚开始学这门课，可能也来不及对它进行深入研究了。
- 再来看人工智能：首先，由于它是近几年最火的领域，社区活跃、学习资料齐全、练手项目多、门槛低，因此或许是最便于上手的领域了；其次，若想要将来在人工智能领域学有所成，一定要拥有良好的数学素养，对我个人而言，这是我或许还依稀具备的“天赋”（当然，很大程度上应该是一种错觉。但比起计算机的传统领域，也许还是在数学上的天赋更大吧……）；最后，从功利的角度讲，由于人工智能很火，众多高校、众多老师都在着手相关研究，因此如果能够具备这样的项目经历，至少对于保研来说是不会吃亏的。

其实很多迷茫都是在“无所事事”时才会产生，在科研进入到中期以后，真正上路以后，我就不再有这样的疑问了。

## 学习方法的体会

在这一路走来的探索的过程中，也体会到了学习高等知识，和高中学习方式的大相径庭。我个人认为，由于高中的知识太少，且有限，因此不同的学习方法在当时而言，区别并不明显，只要时间充足、训练充足，最后结果可能都大体相近。但对于大学学习，由于高等知识是无穷无尽的，大家的学习时间相同，因此谁能走的远，方法的效用就十分明显了。更不用提，大学还要面临着诸如社团、学生工作之类的事情，不同的选择也带来了更为多元化的挑战。

### “宽-深”大战

<img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-3.png" width="50%">

走的“宽”还是走的“深”，这是一个永恒的trade-off问题。从最宏观的角度来看，这个问题可以翻译为：综合素质和一技之长哪一个更重要，或者说，对于木桶理论来说，究竟是最长板重要还是最短板重要。

<img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-1.png" width="100%">

重新回到这个“技能树养成”的问题。从求职的角度而言，只要任何一个树干足够发达，都可飞黄腾达，北大青鸟等技校，仅培养学生“编程语言”、“开发技能”的树干，也一样可以找到工作；从科研的角度而言，对于“科研能力”的树干，只要任何一个分支足够发达，都可功成名就。

但若只注重某个树干，把其余全部剪枝：首先，风险极大。就像人工智能如今的泡沫，一旦某天浪潮退去，只懂得调库的人，一定会被发现是在裸泳；其次，上限很低。只注重某个树干的发展，之后的天花板一定非常低。这其实也是重点高校与专科学校的最重要区别，即高校所称的培养“宽口径人才”，扎实的基础是规避风险的最好方式，就像某天出现了一种吊打所有编程语言的终极语言，大不了再重新学就是了（当然这几乎不可能）。

做“宽”的意识大部分人都有，但这之后便很容易进入一个误区，就是**太想做宽了**。就像年轻的时候大家都“渴望力量”，渴望把机械工业出版社的那些黑皮书全部看完，之后就可以尽情地放大招。但最关键的是，时间非常有限，而且也不要太高估自己的智力，认为自己可以鲸吞所有领域，而最后的结果只能是什么都会一点，但什么都不精。

举个现实的例子，拿我自身来说：在大三上学期，养成自己的技能树时，时常会学学这个，学学那个，而且很容易陷入自我麻痹的状态，虽然很努力、很勤奋，但也**很贪心**。就像在保研考核时，我做过项目开发，也学过很多树干包含的技术，也做过科研，但导师最终决定发不发offer时，一定需要衡量我在某个具体领域是否做深了，是否有自己的理解，如果不能很好地体现出这一点，还有很大可能会被导师认为那些杂七杂八的项目都是在“混水摸鱼”。

### “压栈式”的苦恼

在很长一段时间内，我还苦恼于一种“压栈式”的学习过程。

比如，在刚刚接触科研时，我需要阅读一篇科研论文：

- 首先，有很多学术单词是很陌生的——需要查单词。
- 嗯，论文主要提出了一种改良的GBDT模型——这……我至少得先搞清楚什么是GBDT模型吧，赶快Google一下。
- 噢，这篇博客里提到GBDT模型是一种集成模型，博客中说“模型每一轮迭代会产生一个基分类器，即产生一个CART TREE”——“基分类器”，这是什么概念啊，不过好像不太重要，先不管。“CART TREE”，这个不能不管吧，看起来是一个什么厉害的模型，赶快Google一下。
- 诶，这个文章里说“CART TREE”是决策树的一种——“决策树”？貌似听说过，隐约记得周志华的西瓜书里有讲，赶紧翻开书看看。
- 好决策树弄懂了，现在来看CART TREE。“一般的决策树解决分类问题，CART TREE解决的是回归问题”——分类与回归？好像是个挺基础的概念，但是有点记不清楚了，百度一下区别。
- 好，终于弄清楚CART TREE了。回到刚才的进度，“模型每一轮迭代会产生一个基分类器，即产生一个CART TREE”这句话弄懂了，接下来，“在训练GBDT时，即让损失函数沿着梯度方向的下降”——“损失函数”？好像是个机器学习上的概念。“梯度方向”？高数上学过，但是有点忘了，还是查一下吧。
- ……

这一趟流程下来，大概半天就过去了。学的太慢了，我要反思一下是哪里出了问题：

- 好像还是因为我的机器学习基础不够，先去知乎上搜一下“机器学习应该如何学”吧。
- 这个回答应该是最高赞了吧，答主说“要有一定的高等数学、线性代数、概率论与数理统计知识”，还列了一大堆网课、电子书资料，干货满满啊。
- 但接下来呢？……
- 学高数、线代、概率论？……
- 学网课？……

<img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-4.png" width="50%">

我觉得自己的脑子就像一个栈，本来只想学一下A，结果A中提到了B，B中又提到了C，C说我要先学一下D、E、F，我把A、B、C、D、E、F依次压栈，但都是只进不出，且越进越多。最后，栈爆了……

### “快速原型”与“螺旋模型”

也许人们都津津乐道于，中国学生与其他国家学生的思维方式的不同。

曾看到这样一个比较中美高中数学教学的[文章](https://www.zhihu.com/question/20953633/answer/377431723)：

> <img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-6.png" width="100%">
>
> 中国高中课本侧重于高中知识往“深”和“复杂变化”，与大学知识结合不多。结果是：很多中国的学生高中数学不错，但到大学就听不懂、跟不上了。不信你看看全国多少大学每到考高数时，中国学生处于不理解，硬背公式的状态，继而有人去作弊，或者挂科一大片。
>
> 美国高中及国际学校高中数学主要路线是：高一学习 Pre-calculus ，这部分内容和中国的函数部分类似，快速进入和大学衔接的 Calculus 的学习。
>
> <img src="https://raw.githubusercontent.com/RMSnow/RMSnow.github.io/master/assets/images/posts/2018-08-01-7.png" width="100%">
>
> 虽然有些板块的知识确实不如中国学生学的那么深、刷那么多题，但把有限的时间分配在更”远“的知识上，大家对于一些大学的数学知识，在高中已经有了直观的了解。这对于很多学生在大学的发展，是非常有利的。

暂且不论两种教学方式的优劣，但就对学生的思维习惯的培养而言，我觉得后一种学习方式，更为适合工科类（至少是计算机科学）的初期发展。所谓“初期”，指的应是大学本科阶段。因为研究生之后，当必须在某一个，或某几个领域作出更深的研究时，可能又需要回到前一种学习方式。

我相信大多数中国学生应该是更习惯于第一种学习方式的，这体现在：假设，一本教材有10章，那首先我们一定会选择从前向后的顺序；如果学完了前2章，可能大部分人也依然选择按部就班，继续学第3章、第4章，而不会直接跳到第8章，去瞧瞧后面在讲什么；除此之外，拿我自己来说，如果第5章有几节学的不是很明白，那一定硬要把这几节弄懂，再去看第6章，否则会“别扭”、“不爽”。

这种传统思维的优势就是所谓的“扎实”，在此就不再赘述，而主要说说它的缺点。

一个最直观的问题就是：这种思维定式越明显的同学，就越不能翘课。比如开学前几周，听讲还算认真，前3章基本上都学的不错。之后偷懒了两周，没去上课，当再回来听讲的时候，发现老师已经讲到第5章的某一节了。这时候怎么办？如果思维里只有这种定式，那么就只能“课下拼命补，赶上进度”，但事实上由于一些大家都懂的原因，到最后一定会演化成“以后的课堂，老师在上面讲，自己在下面学”，或者“把一切都推到期末考试前再学”。

在理论课程的学习之外，假设我们现在开始学C语言：

```c

#include <stdio.h>
 
int main()
{
    /* 我的第一个 C 程序 */
    printf("Hello, World! \n");
 
    return 0;
}
```

当对于一个完全陌生的领域，最快的学习一定是先领会“主要矛盾”，再模仿，最后在反复的实践中慢慢学深。比如这个C语言的入门级程序输出了`Hello World!`，因此“主要矛盾”一定是`printf("Hello, World! \n")`，如果现在题目要求输出`Byebye World!`，那么一定是修改`printf()`中的内容，至于`#include`、`int`、`main(){}`、`return`的含义，就可先抛在脑后。在学习初期，一定是先“完成功能”，再“思考原因”，最后“追求性能”。

再举个更深点的例子，假设我们拥有Java，或者C/C++等一门编程语言的基础（但是从未接触过python），现在想要学习用python实现一个数据科学的项目。那么最节省时间的方法，一定是先搜索大量的项目，观察别人的代码是怎么写的。在找到了一些蛛丝马迹之后，再有目的地去重点学一学`numpy`、`pandas`、`matplotlib`等数据处理库，之后就可以开始实践了。而无需按部就班地，先买书，再学语法，最后再大张旗鼓地动手。太追求“高屋建瓴”，有时不见得是好事。

这好像类似于软件开发过程中的两个模型：快速模型以及螺旋模型。“快速”，其哲学在于把握主要矛盾，能够在最短的时间内完成各项基本要求；“螺旋”，其核心在于“螺旋上升”，把一件事情分为很多次螺旋迭代的阶段，而在每个阶段都是一次快速原型。利用快速原型来追求效率，利用螺旋模型以满足学习的深度。

## 后记

回想本科期间这曲曲折折的一路，曾热忱于一年半的学生工作，直到大二下学期，才意识到与大牛的差距已经太过悬殊；曾受到科研的折磨，在了解学院特点后尝试转型为功利的“老油子”；曾做过开发，却在大三下学期重新认识科研，努力变得客观；想过出国，想过读专硕工作，想过读个土博今后混日子，最终还是回到了现在看来可能更适合自己的学硕。

细细想来，百转千回，好像处处都在走弯路。但应该又无法定义，之前的那些选择到底是不是弯路。由于信息不对称，所有的选择都是根据当下某个时刻的所知做出的决断，都是那个时刻所认为的最佳。人永远会质疑着之前的选择，在走完一段路之后说上一句“要是当初那么走就更快了”，有时可以称之为成长，更多时候应该只是思维的变化，或许不存在什么自由，所有的选择只不过是一种表层的假象。