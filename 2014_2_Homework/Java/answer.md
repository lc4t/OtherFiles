##java期末习题answer

###选择部分
**1、下列叙述中正确的是()**

 - ①Java是不区分英文字母大小写的，源文件名与程序类名不允许相同
 - ②Java语言以方法为程序的基本单位
 - ③Applet是Java的一类特殊应用程序，它嵌入HTML中，随主页发布到互联网上
 - ④以//符开始的为多行注释语句


	C
	Java区分大小写,并且每个 .java 文件都包含一个public类，这个类的名字必须和这个文件名一致
	Java的基本单位是类
	正确
	/*和/**为多行注释,//是单行注释

**2、Java语言的许多特点中，下列()特点是C++语言所不具备的**

 - ①高性能 ②跨平台 ③面向对象 ④有类库



	D
	C++是函数库
	
**3、Java源文件中最多只能有一个()类，其他类的个数不限**

 - ①abstract ②public ③final ④interface


	public只能有一个且必须和文件名一致

**4、Java语言中，()是所有类的根类**

 - ①Object ②Root ③Thread ④Applet


	A
	java.lang.Object是根类,没有父类则默认从这里继承
	
**5、Java语言中，字符变量以char类型表示，它在内存中占()位bit**

 -  - ①8 ②16 ③32 ④2


	B
	char是16位 Unicode编码字符

**6、下列叙述中，()是正确的**

 - ①类是变量和方法的集合体 ②数组是无序数据的集合
 - ③抽象类可以实例化 ④类成员数据必须是公有的


	A
	数组是有序(线性)数据的集合
	抽象类不能实例化,即不能new一个新的抽象对象
	类成员数据可以是public/private/protected
	
**7、下列关于方法形参的叙述中，()是正确的**

 - ①必须有多个②至少有一个 ③可以没有 ④只能是简单变量


	C

**8、构造方法在()时候被调用**

 - ①类定义时 ②创建对象时 ③调用对象方法时 ④使用对象的变量时


	B

**9、下列关于继承的叙述中，()是正确的**

 - ①子类能继承父类的所有方法和状态 ②子类能继承父类的非私有方法和状态
 - ③子类只能继承父类的public方法和状态 ④子类只能继承父类的方法，而不继承状态


	B
	子类可继承父类的非private属性
	
**10、下列关于接口的叙述中，()是正确的**

 - ①接口与抽象类是相同的概念 ②接口之间不能有继承关系
 - ③一个类只能实现一个接口 ④接口中只含有抽象方法和常量

	
	D
	接口即(只有)方法的声明，抽象类可以含部分实现
	接口可以继承多个接口
	一个类可以实现多个接口
	接口是常量值和方法定义的集合
	
**11、下列()是异常的含义**

 - ①程序的语法错 ②程序编译或运行中所发生的异常事件
 - ③程序预先定义好的异常事件 ④程序编译错误

	
	B
	异常是程序运行所发生的异常(会打断程序执行)事件
	
**12、自定义的异常类可以从下列()类继承**

 - ①Error类 ②AWTError ③VirtualMachineError ④Exception及其子类


	D
	java.lang.Exception是异常基类
	
**13、当方法遇到异常又不知如何处理时，应该()**

 - ①捕获异常 ②抛出异常 ③用throws声明异常 ④嵌套异常

	
	B
	异常无法处理则抛出异常等待捕获(常对象沿调用栈向后传递)

**14、若要抛出异常，应该使用下列()子句**

 - ①catch ②throw ③try ④finally


	B
	捕获:catch,抛出:throw,try:进入异常处理块,finally:出异常处理快
	
**15、对于catch子句的排列，下列()是正确的**

 - ①父类在先，子类在后 ②子类在先，父类在后
 - ③有继承关系的异常不能在同一个try结构程序段内 ④排列顺序可任意


	B
	
	
**16、设有下面的两个类定义：**

```java
class A{void who(){System.out.print("A");}}
class B extends A{void who(){System.out.print("B");}}
```

**则顺序执行如下语句后输出的结果为()**

``A a=new B();B b=new B();a.who();b.who();``

 - ①AA ②AB ③BB ④BA


	C
	A a=new B();  a是B实例,A是B的基类,B是A的扩展
	
**17、()布局管理器使容器中各个构件呈网格布局，平均占据容器空间**

 - ①CardLayout ②BorderLayout ③FlowLayout ④GridLayout


	D
	CardLayout:卡片布局
	BorderLayout:边界布局
	FlowLayout:流式布局
	GridLayout:网格布局
	
**18、下面是类A的构造函数声明，其中正确的是()**

 - ①void A(int x){...}②A(int x){...}③a(int x){...}④void a(int x){...}

	
	B
	构造函数无返回值,与类同名

**19、对抽象类的描述错误的是()**

 - ①必须被继承使用 ②方法必须被重写 ③不能实例化 ④用final修饰符修饰


	D
	抽象类必须继承或匿名(特殊的继承)使用
	非抽象方法不用重写,其他必须重写
	抽象类不能实例化
	final类不能继承
	

**20、()类是所有异常类的父类**

 - ①Throwable ②Error ③Exception ④AWTError


	A
	java.lang.Object
	   ↳	java.lang.Throwable
	
**21、向容器添加新构件的方法是()**

 - ①add() ②insert() ③hill() ④set()


	A
	add:增加
	insert:插入
	
**22、下面()函数是public void example(int k){...}的重载函数**

 - ①public void example( int m){...}②public int example(int k){...}
 - ③public void example2(int k){...}
 - ④public int example( int m, float f){...}


	D
	重载要求函数名相同,参数表不同
	
**23、给出下面的代码段:**

```java
public class Base{int w, x, y ,z;
public Base(int a,int b){x=a; y=b;}
public Base(int a, int b, int c, int d)
{// assignment x=a, y=b
w=d;z=c;}
}
```

**在代码说明// assignment x=a, y=b处写入如下()代码是正确的**

 - ①Base(a,b); ②x=a, y=b; ③super(a,b); ④this(a,b);

	
	BD
	B是直接赋值,D是调用自己类的其他构造方法
	而A不满足直接调用构造函数1次的原则,会编译错误
	
**24、Java中main()函数的值是()**

 - ① String ②int ③char ④void


	D
	
**25、如下()字符串是Java中合法的用户自定义标识符**

 - ①super  ②3number  ③#number ④$number


	D
	变量:$/字母/下划线开头,后面的可以是数字/字母/下划线
	
**26、下面()语句是创建数组的正确语句**

 - ①float f[5][6] = new float[5][6]; ②float []f[] = new float[5][6];
 - ③float f[5][] = new float[][6]; ④float [5][]f = new float[5][6];

	B
	语法,前面是类型后面是空间
	
**27、已知如下的命令执行：**

``java MyTest aa bb cc``

**则下面()语句是正确的**

 - ①args[0] = "MyTest aa bb cc" ②args[0] = "MyTest"
 - ③args[0] = "aa" ④args[1]="aa"


	C
	args[0] = aa,...,为参数表
	
**28、已知如下代码：**

```java
public class Test
{static long a[] = new long[10];
public static void main ( String arg[] ) {System.out.println ( a[6] );}
}
```

**则下面()个语句是正确的**

 - ①Output is null. ②When compile, some error will occur.
 - ③Output is 0. ④When running, some error will occur.


	C
	默认以0填充

**29、以下()方法用于定义线程的执行体（线程体）**

 - ①start() ②init()  ③run()  ④synchronized()


	C
	run()用来定义启动的时候做什么,start()来启动
	
**30、以下()约束符可用于定义成员常量**

 - ①static ②final ③abstract ④No modifier can be used 

	
	B
	static是静态,不依赖类
	final类不能被继承,没有子类,final类中的方法默认是final
	final方法不能被子类的方法覆盖,但可以被继承
	final成员变量表示常量,只能被赋值一次,赋值后值不再改变
	final不能用于修饰构造方法
	
**31、监听器接口的方法返回值是()**

 - ①int ②String ③void ④Object


	C
	监听器接口:public void name(yEvent e){}
	
**32、如下()方法可以将MenuBar加入Frame中**

 - ①setMenu() ②setMenuBar() ③add() ④addMenuBar()


	B
	public void setMenuBar(JMenuBar m)
	Deprecated. As of Swing version 1.0.3 replaced by setJMenuBar(JMenuBar m).
	Sets the menuBar property for this JInternalFrame.
	所以..改成setJMenuBar()
	
**33、**

```java
class Super{public float getNum(){return 3.0f;}}
public class Sub extends Super{//overload
}
```

**which method, placed at overload, will cause a compiler error? ()**

 - ①public float getNum(){return 4.0f;}
 - ②public void getNum(){}
 - ③public void getNum(double d){}
 - ④public double getNum(float d){return 4.0d;}


	B
	A是重写父类方法,CD是重载,B试图重写父类方法但改变了返回值类型
	
**34、**

```java
public class Test
  	 {public static void main(String[] args)
       {String a=args[1];String b=args[2];String c=args[3];}
     }
```

**execute command:java Test Red Green Blue**

**what is the value of c? ()**

 - ①c has value of null ②c has value of Blue
 - ③the code does not compile ④the program throw an exception

	
	D
	数组越界

**35、**

```java
import java.awt.*;
public class X extends Frame
{public static void main(String[] args)
  {X x=new X();x.pack();x.setVisible(true);}
 public X(){setLayout(new GridLayout(2,2));
    Panel p1=new Panel();add(p1);
    Button b1=new Button("One");p1.add(b1);
    Panel p2=new Panel();add(p2);
    Button b2=new Button("Two");p2.add(b2);
    Button b3=new Button("Three");p2.add(b3);
    Button b4=new Button("Four");add(b4);
    }
 }
```

**when the frame is resized, ()**

 - ①all change height and width ②Button One change height
 - ③Button Two change height and Button Three change width
 - ④Button Four change height and width


	D
	Panel上的不会变

**36、计算机中的流是()**

 - ①流动的字节 ②流动的对象 ③流动的文件 ④流动的数据缓冲区


	C
	由C语言引入

**37、一个Java Application运行后，在系统中是作为一个()**

 - ①线程 ②进程 ③进程或线程 ④不可预知


	B
	
**38、实现下列()接口可以对TextField对象的事件进行监听和处理**

 - ①ActionListener ②FocusListener ③MouseMotionListener ④WindowListener


	A
	ActionListener：按钮按下
	FocusListener:焦点的获得和丢失
	MouseMotionListener:鼠标单击/释放/拖动/移动
	WindowListener:窗口状态
	
**39、Frame的默认布局管理器是()**

 - ①FlowLayout②BorderLayout③GridLayout④CardLayout


	B
	
**40、每个使用Swing构件的程序必须有一个()**

 - ①按钮 ②标签 ③菜单 ④容器


	D


**41、Applet运行时，被浏览器或appletviewer调用的第一个方法是()**

 - ①paint() ②init() ③start() ④destroy()


	A

**42、Applet类的直接父类是()**

 - ①Component类②Container类③Frame类④Panel类


	D
	java.lang.Object
		java.awt.Component
			java.awt.Container
				java.awt.Panel
					java.applet.Applet
**43、在Applet生命周期中，下列()方法是在装载Applet时被调用**

 - ①stop() ②init() ③start() ④destroy()

	
	B
	装载时,浏览器或appletviewer调用init()方法,通知Applet已经被加载到浏览器中,使Applet执行一些基本初始化
	
**44、在一个applet标记中，()标记属性项可以省去不写**

 - ①code ②codebase ③width ④height

**45、下列命令中，()命令是Java的编译命令**

 - ①javac ②java ③javadoc ④appletviewer

**46、下列语句的输出结果是()**

```java
public class A{public static void main(String[]args){System.out.println(2>1);}}
```
 - ①true ②false ③1  ④0

**47、下列各输出语句中，显示结果为“123”的是()**

 - ①System.out.println(1+2+3);
 - ②System.out.println(1+""+2+3);
 - ③System.out.println(1+2+3+"");
 - ④System.out.println(1+2+""+3);

**48、若在某一个类定义中定义有方法：abstract void f();则该类是()**

 - ①public类 ②final类 ③抽象类 ④不能确定

**49、main方法是Java Application程序执行的入口点，下列main方法原型是不正确的是()**

 - ①public static void main(String[]args)
 - ②public static void main(String args[])
 - ③public static void main(String[]a)
 - ④public static void main(string[]args)

**50、在Java中，用()关键字定义常量**

 - ①#define ②fixed ③const ④final

**51、在Java语言中，()包是自动导入的**

 - ①java.lang ②java.awt  ③java.applet  ④java.io

**52、如果一个Java源程序文件中定义有4个类，则使用Sun公司的SDK编译器javac.exe编译该源程序文件，将产生()个文件名与类名相同而扩展名为.class的字节码文件**

 - ①1  ②2  ③3  ④4

**53、下列()不是Java的保留字**

 - ①do ②double ③sizeof ④while

**54、在Java中，()语句作为异常处理的统一出口**

 - ①throw ②try ③finally ④catch

**55、下列语句输出结果为()**
```java
public class A{public static void main(String[]args){byte b=0xa;System.out.println(b);}}
```

 - ①0xa ②a ③1 ④10

**56、下列常见的系统定义的异常中，()是输入、输出异常**

 - ①ClassNotFoundException ②IOException
 - ③FileNotFoundException ④UnknownHostException

**57、下列叙述错误的是()**

 - ①Java是一种面向对象的网络编程语言
 - ②Java Applet程序在网络上传输不受硬软件平台的限制
 - ③Java提供了类库支持TCP/IP协议
 - ④Java语言允许使用指针访问内存

**58、下列代码的执行结果是()**

```java
public class A{ public static void main(String[]args){int a=4,b=6,c=8;String s="abc";System.out.println(a+b+s+c);}}
```
 - ①"ababcc" ②"464688" ③"46abc8" ④"10abc8"

**59、下列叙述中不正确的是()**

 - ①abstract不能与final并列修饰同一个类
 - ②abstract类中不可以有private的成员
 - ③abstract方法必须在abstract类中
 - ④static方法中能直接处理非static的属性

**60、在Applet的关键方法中，下列()方法是关闭浏览器以释放Applet占用的所有资源**

 - ①init() ②start()  ③stop() ④destroy()

**61、下列Java常见事件类中()是鼠标事件类**


 - ①InputEvent ②KeyEvent ③MouseEvent ④WindowEvent

**62、下列类定义中不正确的是()**

 - ①public class A extends B{}
 - ②public class A extends B,D{}
 - ③public class A implements B,D{}
 - ④public class A extends B implements C,D,E{}

**63、如果子类中覆盖了父类中的同名方法，则在子类中调用父类中的同名方法时应使用关键字()**

 - ①this ②super ③implements ④extends

**64、在Java中，子类重新定义一个与从父类那里继承来的域变量（成员变量）完全相同的变量，这称为域的()**

 - ①隐藏 ②覆盖 ③重载 ④Java不支持此特性

**65、为了区分同一个类中重载的各个同名方法，要求()**

 - ①采用不同的形式参数列表（形式参数的个数、类型、顺序不完全相同）
 - ②返回值的数据类型不同
 - ③调用时用类名或对象名做前缀 ④形式参数名不同

**66、Give the following java source fragement:**

```java
//point x
public class Interesting{//do something
}
```

**Which statement is correctly Java syntax at point x?()**

 - ①import java.awt.*; ②package mypackage
 - ③static int PI=3.14  ④public class MyClass{//do other thing…}

**67、A class design requires that a member variable should be accessible only by same package, which modifer word should be used? ()**

 - ①protected ②public ③no modifer ④private

**68、Which modifer should be applied to a declaration of a class member variable for the value of variable to remain constant after the creation of the object? ()**

 - ①static ②final ③const ④abstract
**69、What happens when you try to compile and run the following program? ()**

```java
class Mystery{String s;
  public static void main(String[] args)
     {Mystery m=new Mystery();m.go();}
  void Mystery(){s="constructor";}
  void go(){System.out.println(s);}
}
```

 - ①this code will not compile
 - ②this code compliles but throws an exception at runtime
 - ③this code runs and "constructor" in the standard output
 - ④this code runs and writes "null" in the standard output


**70、Give the following java class:**

```java
public class Example
{public static void main(String args[])
  {int x[] = new int[15];System.out.println(x[5]);}
}
```

**Which statement is corrected? ()**

 - ①When compile, some error will occur.
 - ②When run, some error will occur.
 - ③Output is zero. ④Output is null.


**71、在Java的基本数据类型中，int型数据占用()字节内存空间**

 - ①1   ②2   ③4    ④不能确定，取决于计算机字长

**72、在线程中，普通优先级的线程其优先级默认值为()**

 - ①1   ②2   ③5     ④10

**73、下列()布局管理器能够帮助用户处理两个或者两个以上的成员共享同一个显示空间，它把容器分成许多层，每层显示空间占据这个容器的大小**

 - ①CardLayout ②BorderLayout ③FlowLayout ④GridLayout

**74、在j2sdk1.4.2版中，解压得到的目录中，()是存放编译器、解释器和其他许多工具的目录**

 - ①jre ②lib ③demo ④bin

**75、Java Application源程序文件的扩展名为()**

 - ①.java ②.class ③.html ④.exe

**76、关键字super的作用是()**

 - ①用来访问父类被隐藏的成员变量 ②用来调用父类中被重载的方法
 - ③用来调用父类的构造方法 ④以上都是

**77、对于构造方法，下列叙述正确的是()**

 - ①构造方法的方法名必须与类名相同 ②构造方法必须用void申明返回类型
 - ③构造方法可以被程序调用 ④若编程人员没在类中定义构造方法，程序将报错

**78、Java语言是在()语言基础上衍生的**

 - ①pascal ②C ③C++  ④VF

**79、下列常见的系统定义的异常中，()是数组下标越界异常**

 - ①ArithmeticException ②IOException
 - ③ArrayIndexOutOfBoundsException ④NullPointerException
**80、设有下面两个类的定义：**

```java
class Person{long id;String name;}
class Student extends Person{int score;int getScore(){return score;}}
```

**则类Person和类Student的关系是()**

 - ①包含关系 ②继承关系 ③关联关系 ④无关系

**81、设有下面的两个类定义：**

```java
class A{void show(){System.out.print("AA");}}
class B extends A{void show(){System.out.print("BB");}}
```

**则顺序执行如下语句后输出的结果为()**

	A a=new A();B b=new B();
	a.show();b.show();
 - ①AAAA  ②AABB ③BBBB ④BBAA

**82、设有数组定义：**
``` java
int a[]={1,2,3,4};int s=0;for(int i=0;i < a.length;i++)s+=a[i];
System.out.println(s);
```

**则顺序执行上述几个语句后的输出结果为()**

 - ①0 ②1 ③10 ④1234


**83、Thread类的方法中，toString()方法的作用是()**
 - ①只返回线程的名称 ②返回当前线程所属的线程组的名称
 - ③返回当前线程对象 ④返回线程的字符串信息
**84、下列()是创建一个标识有“OK”的按钮的语句**

 - ①TextField b=new TextField("OK");②Button b=new Button("OK");
 - ③TextArea b=new TextArea("OK");④Checkbox b=new Checkbox("OK");

**85、有类定义：abstract class A{public abstract void f();}
下面关于该类的描述中正确的是()**

 - ①该类可以用new A();实例化一个对象 ②该类不能被继承
 - ③该类的方法不能被重载 ④以上说法都不对

**86、下列()关键字通常用来给对象进行加锁，该标记使得对对象的访问是排他的**

 - ①transient ②serialize ③synchronized ④static

**87、以下()可能包含菜单条**

 - ①Panel ②Applet ③Dialog ④Frame

**88、有数组定义：int a[]={0,1,2,3,4,5,6};，则a数组的数组元素个数为()**

 - ①a.length() ②a.length()+1 ③a.length ④a.length+1

**89、在使用interface声明一个接口时，只可以使用()修饰符修饰该接口**

 - ①public ②protected ③private和protected ④private

**90、创建字符串s：String s=new String("abcd");以下()将改变s**

 - ①s.append("x"); ②s.concat("y"); ③s.substring(3); ④以上语句都不会

**91、下列()是不合法的标识符**

 - ①_book ②3file ③$good ④a_$2

**92、容器Panel和Applet默认使用的布局管理器是()**

 - ①CardLayout ②BorderLayout ③FlowLayout ④GridLayout

**93、以下()不属于Java Application应用程序编写和执行步骤**

 - ①编写源代码 ②编写HTML文件 ③编译源代码 ④解释执行

**94、有如下代码：class A{private int m;public static void f(){}}
为了让f()方法能直接访问m，则应()**

 - ①将private int m;改为protected int m;②将private int m;改为public int m;
 - ③将private int m;改为static int m;④将private int m;改为int m;

**95、设有数组定义：int a[]=new int[8];，则a.length的值为()**

 - ①0 ②7 ③8 ④9

**96、下列保留字中书写正确的是()**

 - ①Case ②For ③try ④viod

**97、下列()是Java的调试器，如果编译器返回程序代码的错误，可以用它对程序进行调试**

 - ①java.exe ②javadoc.exe ③jdb.exe ④javaprof.exe

**98、下列代码的执行结果是()**
```java
public class A{public static void main(String[]args){System.out.println(5/2);}}
```

 - ①2.5 ②2.0 ③3 ④2

**99、下列Java源文件代码片段中，()是不正确的**

 - ①package t;public class A{}
 - ②import java.io.*;package t;public class A{}
 - ③import java.io.*;class A{}public class B{}
 - ④import java.io.*;import java.awt.*;public class A{}

**100、下列()修饰符可以使在一个类中定义的成员变量只能被同一包中的类访问**

 - ①private ②public ③protected ④无修饰符

**101**
```java
class A
{public String toString(){return 4+"";}}
class B extends A
{public String toString(){return super.toString()+3;}}
public class Test
{public static void main(String[]args)
   {B b=new B();System.out.println(b.toString());}
}
```
**what is the result?()**
 - ①7  ②null  ③the program throw an exception ④43

**102**
```java
class A
{public int getNumber(int a){return a+1;}}
class B extends A
{public int getNumber(int a, char c){return a+2;}
 public static void main(String[] args)
   {B b=new B();System.out.println(b.getNumber(0));}
 }
 ```

**what is the result? ()**

 - ①compilation succeeds and 1 is printed
 - ②compilation succeeds and 2 is printed
 - ③compilation succeeds and 3 is printed
 - ④An error at this program cause compilation to fail

**103、Give incompleted method:**
```java
//one
{if(unsafe()){//do something…}
else if(safe()){//do the other…}
}
```

**The method unsafe() will throw an IOException, which completes the method of declaration when added at line one?()**

 -  - ①public IOException methodName()
 - ②public void methodName()
 - ③public void methodName() throw IOException
 - ④public void methodName() throws IOException

**104、Which modifier should be applied to a method for the lock of object "this" to be obtained prior to excution any of the method body?()

 - ①synchronized ②abstract ③final ④static
**105、Which statement is correctly declare a variable a which is suitable for refering to an array of 50 string empty object? ()
 - ①String [] a; ②char a[][]; ③String a[50]; ④String [50]a;

###判断部分
**106、Java的各种数据类型占用固定长度，与具体的软硬件平台环境无关**
**107、用“+”可以实现字符串的拼接，用“-”可以从一个字符串中去除一个字符子串**
**108、A class can implement as many interfaces as needed**
**109、A subclass inherits all methods ( including the constructor ) from the superclass**
**110、Java程序里，创建新的类对象用关键字new，回收无用的类对象使用关键字free**
**111、子类要调用父类的方法，必须使用super关键字**
**112、有的类定义时可以不定义构造函数，所以构造函数不是必需的**
**113、如果p是父类Parent的对象，而c是子类Child的对象，则语句c = p是正确的**
**114、在Java语言中，系统常量null,false,true既可以大写，也可以小写**
**115、Java语言没有无符号整数类型、指针类型、结构类型、枚举类型、共用体类型**
**116、J2SDK中主要有两个相关环境变量，即path和classpath。前者指定了JDK命令搜索路径，后者指定了Java类路径**
**117、final类中的属性和方法都必须被final修饰符修饰**
**118、字符串分为两大类，一类是字符串常量，使用StringBuffer类的对象表示；另一类是字符串变量，使用String类的对象表示**
**119、Java的屏幕坐标是以像素为单位，容器的左下角被确定为坐标的起点**
**120、抽象方法必须在抽象类中，所以抽象类中的方法都必须是抽象方法**

###程序阅读部分（结果和功能）
**121**
```java
//需要预先在本源程序的相同目录下存放4张图片：1.jpg、2.jpg、3.jpg、4.jpg
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A implements ActionListener
{JFrame f=new JFrame("XXX");
 JToolBar tb=new JToolBar();
 ImageIcon m1=new ImageIcon("1.jpg");
 ImageIcon m2=new ImageIcon("2.jpg");
 ImageIcon m3=new ImageIcon("3.jpg");
 ImageIcon m4=new ImageIcon("4.jpg");
 JButton b1,b2,b3,b4;
 JPanel p=new JPanel();
 public A()
  {
   f.setSize(300,300);
   f.setContentPane(p);
   f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   f.setVisible(true);
   b1=new JButton(m1);b1.setToolTipText("红色");
   b2=new JButton(m2);b2.setToolTipText("绿色");
   b3=new JButton(m3);b3.setToolTipText("兰色");
   b4=new JButton(m4);b4.setToolTipText("粉红色");
   tb.add(b1);tb.add(b2);tb.add(b3);tb.add(b4);
   p.add(tb,BorderLayout.NORTH);
   p.add(new JLabel(),BorderLayout.CENTER);
   p.add(tb);
   b1.addActionListener(this);b2.addActionListener(this);
   b3.addActionListener(this);b4.addActionListener(this);
  }
 public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b1)p.setBackground(Color.RED);
   else if(e.getSource()==b2)p.setBackground(Color.GREEN);
   else if(e.getSource()==b3)p.setBackground(Color.BLUE);
   else if(e.getSource()==b4)p.setBackground(Color.PINK);
  }
 public static void main(String[]args)
  {new A();}
}
```language
```
**122**
```java
import java.applet.Applet;
import java.awt.* ;
import java.awt.Color;
public class A extends Applet
{int r,g,b;String s ;
public void init()
{s=getParameter("red");
if(s!=null)r=Integer.parseInt(s);
s=getParameter("green");
if(s!=null)g=Integer.parseInt(s);
s=getParameter("blue");
if(s!=null)b=Integer.parseInt(s);
Color c=new Color(r,g,b);
setBackground(c);
setForeground(Color.white);
}
public void paint(Graphics g)
{g.fillOval(50,25,300,100);
g.setColor(Color.blue);
g.setFont(new Font("宋体",Font.ITALIC,18));
g.drawString("设定颜色",40,80);
}
}
<html>
<applet code=A.java width=400 height=160>
<param name=red value=128>
<param name=green value=255>
<param name=blue value=128>
</applet>
</html>
```

**123**
```java
import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;
public class A extends Applet implements ActionListener
{Panel p;
 Button[]b=new Button[10];
 TextField t;
 Button b1,b2,b3,b4,b5,b6;
 int x=0;
 public void init()
  {p=new Panel();
   t=new TextField("",100);
   b1=new Button("^2");b2=new Button("/2");b3=new Button("*2");
   b4=new Button("v2");b5=new Button("<-");b6=new Button("C");
   setLayout(new BorderLayout());
   setFont(new Font("黑体",Font.BOLD,20));
   add(t,"North");add(p,"Center");
   p.setLayout(new GridLayout(4,4,5,5));
   for(int i=0;i<b.length;i++)
      {b[i]=new Button(""+i);
       p.add(b[i]);
       b[i].addActionListener(this);
      }
   p.add(b1);p.add(b2);p.add(b3);p.add(b4);p.add(b5);p.add(b6);
   b1.addActionListener(this);b2.addActionListener(this);
   b3.addActionListener(this);b4.addActionListener(this);
   b5.addActionListener(this);b6.addActionListener(this);
   }
 public void actionPerformed(ActionEvent e)
  {
   if(e.getSource()==b[0])t.setText(""+t.getText()+0);
   else if(e.getSource()==b[1])t.setText(""+t.getText()+1);
   else if(e.getSource()==b[2])t.setText(""+t.getText()+2);
   else if(e.getSource()==b[3])t.setText(""+t.getText()+3);
   else if(e.getSource()==b[4])t.setText(""+t.getText()+4);
   else if(e.getSource()==b[5])t.setText(""+t.getText()+5);
   else if(e.getSource()==b[6])t.setText(""+t.getText()+6);
   else if(e.getSource()==b[7])t.setText(""+t.getText()+7);
   else if(e.getSource()==b[8])t.setText(""+t.getText()+8);
   else if(e.getSource()==b[9])t.setText(""+t.getText()+9);
   else if(e.getSource()==b6)t.setText("");
   else if(!(t.getText().equals("")))
      {x=Integer.parseInt(t.getText());
        if(e.getSource()==b1)t.setText(""+(x*x));
        else if(e.getSource()==b2)t.setText(""+(x/2));
        else if(e.getSource()==b3)t.setText(""+(x*2));
        else if(e.getSource()==b4)t.setText(""+((int)(Math.sqrt(x))));
        else if(e.getSource()==b5)t.setText(""+(x/10));
       }
  else t.setText("请输入数据！");
  }
}
```

**124**
```java
import java.awt.*;
import java.awt.event.*;
public class D extends WindowAdapter implements ActionListener
{Frame f=new Frame("GUI");
Button b1=new Button("Dialog");
Button b2=new Button("Exit");
Dialog d=new Dialog(f,"Dialog",true);
public D()
  {f.add(b1,"West");
   f.add(b2,"Center");
   b1.addActionListener(this);
b2.addActionListener(this);
   d.add("Center",new Label("I'm a Dialog"));
   d.pack();
   d.addWindowListener(this);
   f.addWindowListener(this);
   f.pack();
   f.setVisible(true);
  }
public static void main(String args[])
{new D();}
public void actionPerformed(ActionEvent e)
{String s=e.getActionCommand();
 if(s.equals("Dialog"))d.setVisible(true);
 else if(s.equals("Exit")){System.exit(1);}
}
public void windowClosing(WindowEvent e)
{System.exit(1);}
}
**125**
```java
//请在源程序文件夹中预先存放一张图片：1.jpg
import java.applet.Applet;
import java.awt.*;
public class A extends Applet
{Image m;
public void init()
{m=getImage(getCodeBase(),"1.jpg");}
public void paint(Graphics g)
{g.drawImage(m,30,10,this);}
}
<html>
<body bgcolor=yellow>
<applet code=A.class width=300 height=400>
</applet>
</body>
</html>
```
**126**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A implements ActionListener
{JFrame f=new JFrame("XXX");
 JPanel p=new JPanel();
 JButton b=new JButton("0");
 static int count=0;
 public A()
  {
   f.setSize(300,300);
   f.setContentPane(p);
   p.setLayout(new FlowLayout());
   p.add(b);
   b.setFont(new Font("黑体",Font.BOLD,30));
   b.addActionListener(this);
   f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   f.setVisible(true);
  }
 public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b)count++;
   b.setText(""+count);
  }
 public static void main(String[]args)
  {A a=new A();}
}
```
**127**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JApplet implements ItemListener
{JRadioButton r1,r2,r3;
 ButtonGroup bg;
 Container c;
 public void init()
 {c=getContentPane();
  c.setLayout(new FlowLayout());
  c.setBackground(Color.YELLOW);
  r1=new JRadioButton("红色");
  r2=new JRadioButton("绿色");
  r3=new JRadioButton("兰色");
  bg=new ButtonGroup();
  bg.add(r1);bg.add(r2);bg.add(r3);
  c.add(r1);c.add(r2);c.add(r3);
  r1.addItemListener(this);
  r2.addItemListener(this);
  r3.addItemListener(this);
 }
 public void itemStateChanged(ItemEvent e)
 {if(e.getSource()==r1)c.setBackground(Color.RED);
  else if(e.getSource()==r2)c.setBackground(Color.GREEN);
  else if(e.getSource()==r3)c.setBackground(Color.BLUE);
 }
}
```
**128**
```java
import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;
public class A extends Applet implements KeyListener
{Button b;
 Font f1,f2;
 public void init()
  {f1=new Font("黑体",Font.PLAIN,30);
   f2=new Font("黑体",Font.BOLD+Font.ITALIC,30);
   b=new Button("电子科技大学");
   add(b);
   b.setFont(f1);
   b.addKeyListener(this);
   }
 public void keyPressed(KeyEvent e)
   {if(e.getKeyCode()==KeyEvent.VK_R)b.setForeground(Color.RED);
    else if(e.getKeyCode()==KeyEvent.VK_G)b.setForeground(Color.GREEN);
    else if(e.getKeyCode()==KeyEvent.VK_B)b.setForeground(Color.BLUE);
    else if(e.getKeyCode()==KeyEvent.VK_F)b.setFont(f2);
    else if(e.getModifiers()==InputEvent.CTRL_MASK && e.getKeyCode()==KeyEvent.VK_Z)
      {b.setFont(f1);b.setForeground(Color.BLACK);}
    }
 public void keyTyped(KeyEvent e){}
 public void keyReleased(KeyEvent e){}
}
```
**129**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JApplet implements ActionListener
{Container c;
 JButton bnext,bprev;
 JPanel p1,p2,p11,p12,p13,p14,p15;
 CardLayout cd;
 public void init()
 {c=getContentPane();
  cd=new CardLayout();
  p1=new JPanel();p1.setLayout(cd);
  p2=new JPanel();p2.setLayout(new GridLayout(1,2,5,5));
  p11=new JPanel();p11.setBackground(Color.RED);
  p12=new JPanel();p12.setBackground(Color.ORANGE);
  p13=new JPanel();p13.setBackground(Color.YELLOW);
  p14=new JPanel();p14.setBackground(Color.GREEN);
  p15=new JPanel();p15.setBackground(Color.BLUE);
  bnext=new JButton("下一张");
  bprev=new JButton("上一张");
  c.add(p1,BorderLayout.CENTER);
  c.add(p2,BorderLayout.SOUTH);
  p1.add("1",p11);p1.add("2",p12);
  p1.add("3",p13);p1.add("4",p14);
  p1.add("5",p15);
  p2.add(bprev);p2.add(bnext);
  bprev.addActionListener(this);
  bnext.addActionListener(this);
 }
 public void actionPerformed(ActionEvent e)
 {if(e.getSource()==bprev)cd.previous(p1);
  else if(e.getSource()==bnext)cd.next(p1);
 }
}
```
**130**
```java
import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;
public class A extends Applet implements Runnable
{int x=1,y=0;
 boolean b=true;
 Thread t;
 public void init()
   {t=new Thread(this);t.start();}
 public void run()
   {while(true)
      {repaint();
       try{t.sleep(10);}
       catch(InterruptedException e){}      
      }
   }
  public void paint(Graphics g)
    {if(x%300==0)b=!b;
     if(b)x++;
     else x--;
     g.drawOval(x,y,100,100);
    }
}
```
**131（1）**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A implements MouseMotionListener
{JFrame f=new JFrame("XXX");
 JPanel p=new JPanel();
 JLabel s=new JLabel("");
 public A()
 {f.setContentPane(p);
  p.setBackground(Color.YELLOW);
  p.add(s,BorderLayout.NORTH);
  p.addMouseMotionListener(this);
  f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  f.setSize(300,320);
  f.setVisible(true);
 }
 public void mouseDragged(MouseEvent e){}
 public void mouseMoved(MouseEvent e)
 {if(e.getSource()==p)
      s.setText("鼠标当前的位置坐标为：("+e.getX()+","+e.getY()+")");
 }
 public static void main(String[]args)
 {A a=new A();}
}
```
**131（2）**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JApplet implements MouseMotionListener
{Container c;
 JLabel s;
 public void init()
 {c=getContentPane();
  c.setBackground(Color.YELLOW);
  s=new JLabel("",JLabel.CENTER);
  c.add(s,BorderLayout.NORTH);
  c.addMouseMotionListener(this);
 }
 public void mouseDragged(MouseEvent e){}
 public void mouseMoved(MouseEvent e)
 {if(e.getSource()==c)
      s.setText("鼠标当前的坐标点为：("+e.getX()+","+e.getY()+")");
 }
}
```
**132**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JApplet implements MouseListener
{Container c;
 JLabel s;
 public void init()
 {c=getContentPane();
  c.setBackground(Color.YELLOW);
  s=new JLabel("",JLabel.CENTER);
  c.add(s,BorderLayout.NORTH);
  c.addMouseListener(this);
 }
 public void mousePressed(MouseEvent e){}
 public void mouseReleased(MouseEvent e){}
 public void mouseEntered(MouseEvent e){}
 public void mouseExited(MouseEvent e){}
 public void mouseClicked(MouseEvent e)
 {if(e.getSource()==c)
      s.setText("鼠标单击点的坐标为：("+e.getX()+","+e.getY()+")");
 }
}
```
**133**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JApplet implements ActionListener{
 JPanel p;
 JButton b1,b2,b3;
 JLabel s;
 Font f;
 static int count=0;
 public void init(){
    p=new JPanel();
    setContentPane(p);
    p.setLayout(new GridLayout(2,2,5,5));
    f=new Font("黑体",Font.BOLD,30);
    b1=new JButton("+");b1.setFont(f);
    b2=new JButton("-");b2.setFont(f);
    b3=new JButton("清零");b3.setFont(f);
    s=new JLabel(" "+count,JLabel.CENTER);
    s.setFont(f);
    p.add(b1);p.add(b2);
    p.add(s);p.add(b3);
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    }
 public void actionPerformed(ActionEvent e){
     if(e.getSource()==b1)count++;
     else if(e.getSource()==b2)count--;
     else if(e.getSource()==b3)count=0;
     s.setText(""+count);
    }
}
```
**134**
```java
import java.io.*;import java.awt.*;import java.awt.event.*;
public class A extends Frame implements ActionListener
{FileDialog fileDlg;
String str, fileName;
byte byteBuf[]=new byte[10000];
TextArea ta=new TextArea();
MenuBar mb=new MenuBar();
Menu m1=new Menu("文件");
MenuItem open=new MenuItem("打开");
MenuItem close=new MenuItem("关闭");
MenuItem save=new MenuItem("保存");
MenuItem exit=new MenuItem("退出");
A(){setTitle("简易文本编辑器");
setSize(400,280); add("Center",ta);
addWindowListener(new WindowAdapter(){
public void windowClosing(WindowEvent e)
{System.exit(0);}
});
m1.add(open);m1.add(close);m1.add(save);
m1.addSeparator();m1.add(exit);
open.addActionListener(this);close.addActionListener(this);
save.addActionListener(this);exit.addActionListener(this);
mb.add(m1);
setMenuBar(mb);
show();
}
public void actionPerformed(ActionEvent e)
{if(e.getSource()==exit)System.exit(0);
else if(e.getSource()==close)//关闭文件
ta.setText(null);//设置文本区为空
else if(e.getSource()==open)//打开文件
{fileDlg=new FileDialog(this,"打开文件");//生成文件对话框
fileDlg.show();//显示文件对话框
fileName=fileDlg.getFile();//获取文件名
try{
FileInputStream in=new FileInputStream(fileName);//建立文件输入流
in.read(byteBuf);//将文件内容读到字节数组
in.close();//关闭文件输入流
str=new String(byteBuf);//将字节数组转换成字符串
ta.setText(str);//将字符串显示在文字区
setTitle("简易文本编辑器一"+fileName);
}
catch(IOException ioe){}
}
else if(e.getSource()==save)//保存文件
{fileDlg=new FileDialog(this,"保存文件",FileDialog.SAVE);//生成文件对话框
fileDlg.show();
fileName=fileDlg.getFile();
str=ta.getText();//将文本区内容读至字符串
byteBuf=str.getBytes();//将字符串转换成字节数组
try{
FileOutputStream out=new FileOutputStream(fileName);//建立文件输出流
out.write(byteBuf);//将字节数组写入文件输出流
out.close();//关闭文件输出流
}
catch(IOException ioe){}
}
}
public static void main(String args[])
{new A();}
}
```
**135**
```java
import java.applet.Applet; import java.awt.*; import java.awt.event.*;
import java.util.Vector; import java.awt.Rectangle;
public class A extends Applet implements ActionListener
{Button a,b,c;
M m;
public void init()
{m=new M();
m.setSize(350,200); m.setBackground(Color.green);
a=new Button("画线"); b=new Button("画点"); c=new Button("清除");
add(a); add(b); add(c); add(m);
a.addActionListener(this);
b.addActionListener(this);
c.addActionListener(this);
}
public void actionPerformed(ActionEvent e)
{if(e.getSource()==a) m.mode=0;//设为画直线模式
else if(e.getSource()==b) m.mode=1;//设为画连续点模式
else if(e.getSource()==c)//清除画面
{m.p=new Vector();
m.x1=-1;
m.repaint();
}
}
}
class M extends Canvas implements MouseListener,MouseMotionListener
{int x1,y1,x2,y2,mode;
Vector p=new Vector();
M(){addMouseListener(this);
addMouseMotionListener(this);
}
public void paint(Graphics g)
{for(int i=0;i<p.size();i++)//所有操作结果被重新画出
{Rectangle r=(Rectangle)p.elementAt(i);
g.drawLine(r.x,r.y,r.width,r.height);}
if(x1!=-1&&mode==0)//画当前直线
g.drawLine(x1,y1,x2,y2);
}
public void mousePressed(MouseEvent e)//记录起点坐标
{x1=e.getX(); y1=e.getY();}
public void mouseDragged(MouseEvent e)
{if(mode==0)//记录当前坐标
{x2=e.getX();y2=e.getY();}
else//画连续点时保存每一个笔画的起点和当前坐标
{p.addElement(new Rectangle(x1,y1,e.getX(),e.getY()));
x1=e.getX();y1=e.getY();}
repaint();
}
public void mouseReleased(MouseEvent e)
{if(mode==0)//保存当前直线的起点和终点坐标
p.addElement(new Rectangle(x1,y1,e.getX(),e.getY()));
}
public void mouseClicked(MouseEvent e){}
public void mouseEntered(MouseEvent e){}
public void mouseExited(MouseEvent e){}
public void mouseMoved(MouseEvent e){}
}
```
**136**
```java
import java.awt.*;
import java.awt.event.*;
public class A extends Frame implements ActionListener,MouseListener
{TextArea s=new TextArea();
PopupMenu pm=new PopupMenu();
MenuItem t1=new MenuItem("复制");
MenuItem t2=new MenuItem("剪切");
MenuItem t3=new MenuItem("粘贴");
A(){setTitle("弹出式菜单");
setSize(200,150);
addWindowListener(new WindowAdapter(){//注册窗口的事件监听器
public void windowClosing(WindowEvent e)
{System.exit(0);}
});
add(s);
s.add(pm);//将弹出式菜单加入到文本区中
pm.add(t1);
pm.add(t2);
pm.add(t3);
t1.addActionListener(this);
t2.addActionListener(this);
t3.addActionListener(this);
s.addMouseListener(this);//注册文本区的鼠标事件监听器
show();   
}
public void actionPerformed(ActionEvent e)
{s.append("你选择了"+e.getActionCommand()+"\n");}
public void mouseReleased(MouseEvent e)
{if(e.isPopupTrigger())//判断是否单击鼠标右键
pm.show(this,e.getX(),e.getY());//显示弹出式菜单
}
public void mouseClicked(MouseEvent e){}
public void mouseEntered(MouseEvent e){}
public void mouseExited(MouseEvent e){}
public void mousePressed(MouseEvent e){}
public static void main(String arg[]){new A();}
}
```
**137**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JApplet implements ActionListener{
 JPanel p,p1;
 JButton b1,b2;
 JLabel s;
 Font f;
 static int count=25;
 public void init(){
    p=new JPanel();
    setContentPane(p);
    p.setLayout(new BorderLayout());
    p1=new JPanel();
    b1=new JButton("+");
    b2=new JButton("-");
    p1.add(b1);p1.add(b2);
    s=new JLabel("电子科技大学",JLabel.CENTER);
    s.setFont(new Font("宋体",Font.BOLD,count));
    p.add(p1,BorderLayout.NORTH);
    p.add(s,BorderLayout.CENTER);
    b1.addActionListener(this);
    b2.addActionListener(this);
    }
 public void actionPerformed(ActionEvent e){
     if(e.getSource()==b1)count++;
     else if(e.getSource()==b2)count--;
     if(count>=50)count=50;
     else if(count<=0)count=0;
     s.setFont(new Font("宋体",Font.BOLD,count));
    }
}
```
**138**
```java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
public class A extends Applet implements AdjustmentListener
{ Scrollbar r;
  static int size=15;
  Label s,t;
  Panel p;
  public void init(){setLayout(new BorderLayout());
     p=new Panel();p.setLayout(new GridLayout(2,1));
     r=new Scrollbar(Scrollbar.HORIZONTAL,size,1,0,255);
     s=new Label("fontsize="+size,Label.CENTER);
     t=new Label("电子科技大学",Label.CENTER);
     t.setFont(new Font("宋体",Font.BOLD,size));
     p.setForeground(Color.BLUE);
     add(p,BorderLayout.NORTH);p.add(r);p.add(s);
     add(t,BorderLayout.CENTER);
     r.addAdjustmentListener(this);
}
public void adjustmentValueChanged(AdjustmentEvent e)
{size=r.getValue();
 s.setText("fontsize="+size);
 t.setFont(new Font("宋体",Font.BOLD,size));
}
}
```
**139**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A implements ActionListener
{JFrame f;;
 JPanel p;
 JMenuBar mb;
 JMenu m1;
 JMenuItem m11,m12,m13,m14;
 static String fontType="华文行楷"; 
 JLabel s;
 public void init()
 {f=new JFrame("XXX");
  p=new JPanel();
  f.setContentPane(p);
  p.setBackground(Color.YELLOW);
  p.setForeground(Color.BLUE);
  mb=new JMenuBar();
  m1=new JMenu("设置字体");
  m11=new JMenuItem("黑体");
  m12=new JMenuItem("隶书");
  m13=new JMenuItem("方正姚体");
  m14=new JMenuItem("还原");
  f.setJMenuBar(mb);
  mb.add(m1);
  m1.add(m11);m1.add(m12);m1.add(m13);
  m1.addSeparator();m1.add(m14);
  m11.addActionListener(this);
  m12.addActionListener(this);
  m13.addActionListener(this);
  m14.addActionListener(this);
  s=new JLabel("电子科技大学",JLabel.CENTER);
  s.setFont(new Font(fontType,Font.BOLD,30));
  p.add(s);
  f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  f.setBounds(200,200,300,150);
  f.setVisible(true);
 }
 public void actionPerformed(ActionEvent e)
 {
  if(e.getSource()==m11)fontType="黑体";
  else if(e.getSource()==m12)fontType="隶书";
  else if(e.getSource()==m13)fontType="方正姚体";
  else if(e.getSource()==m14)fontType="华文行楷";
  s.setFont(new Font(fontType,Font.BOLD,30));
 }
 public static void main(String[]args)
 {A a=new A();a.init();}
}
```
**140**
```java
public class A
{public static void main(String args[])
{String s=new String("");
System.out.println("本类名="+s.getClass().getName());
System.out.println("超类名="+s.getClass().getSuperclass().getName());
System.out.println("包名="+s.getClass().getPackage().getName());
System.out.println("操作系统="+System.getProperty("os.name"));
System.out.println("Java版本="+System.getProperty("java.vm.version"));
System.out.println("内存总量="+Runtime.getRuntime().totalMemory());
System.out.println("剩余空间="+Runtime.getRuntime().freeMemory());
}
}
```
**141**
```java
import java.awt.*;
public class M extends java.applet.Applet
{int a,b;String s="";
Label s1=new Label("鼠标指针当前的坐标是：");
Label s2=new Label("鼠标指针单击点坐标是：");
TextField tf1=new TextField(10);
TextField tf2=new TextField(10);
public void init()
{add(s1);add(tf1);add(s2);add(tf2);}
public boolean mouseMove(Event e,int x,int y)
{a=x;b=y;s="("+a+","+b+")";
tf1.setText(s);
repaint();
return true;
}
public boolean mouseDown(Event e,int x,int y)
{a=x;b=y;s="("+a+","+b+")";
tf2.setText(s);
repaint();
return true;
}
}
```
**142**
```java
import java.awt.*;
import java.applet.*;
import java.awt.event.*;
 public class A extends Applet
{R[]s;
public void init()
{setLayout(null);
setSize(426,266);
s=new R[10];
for(int i=0;i<s.length;i++)
s[i]=new R(this);
}
public void start()
{for(int i=0;i<s.length;i++);
//s[i].start();//it started when it's constructed
super.start();
}
public void stop()
{for(int i=0;i<s.length;i++)s[i].suspend();
super.stop();
}
public void destroy()
{for(int i=0;i<s.length;i++)s[i].stop();
super.destroy();
}
public static void main(String[]args)//Applet和Application相统一 
{Frame f=new Frame();
f.setSize(450,300);
A p=new A();
f.add(p);
f.setVisible(true);
p.init();
p.start();
f.addWindowListener(new WindowAdapter(){
public void windowClosing(WindowEvent e)
{System.exit(0);}
});
}
}
class R extends Thread
{boolean b=false;
private int size=100,speed=10,type,x,y,w,h,dx,dy;
private Color c;
protected java.awt.Component a;
R(java.awt.Component d)
{a=d;
x=(int)(Math.random()*d.getSize().width);
y=(int)(Math.random()*d.getSize().height);
w=(int)(Math.random()*size);
h=(int)(Math.random()*size);
dx=(int)(Math.random()*speed);
dy=(int)(Math.random()*speed);
c=new Color((int)(Math.random()*128+128),
(int)(Math.random()*128+128),(int)(Math.random()*128+128));
type=(int)(Math.random()*3);
b=true;this.start();
}
public void run()
{while(true){x+=dx;y+=dy;
if(x<0||x+w>a.getSize().width )dx=-dx;
if(y<0||y+h>a.getSize().height)dy=-dy;
Graphics g=a.getGraphics();
switch(type){
case 0:g.setColor(c);
       g.fillRect(x,y,w,h);
       g.setColor(Color.black);
       g.drawRect(x,y,w,h);
       break;
case 1:g.setColor(c);
       g.fillOval(x,y,w,h);
       g.setColor(Color.black);
       g.drawOval(x,y,w,h);
       break;
case 2:g.setColor(c);
       g.fillRoundRect(x,y,w,h,w/5,h/5);
       g.setColor(Color.black);
       g.drawRoundRect(x,y,w,h,w/5,h/5);
       break;
}
//System.out.printin(x+","+y+","+w+","+h+":"+type+","+dx+","+dy);
try{Thread.sleep(130);}catch(InterruptedException e){}
}
}
}
```
**143（1）**
```java
import java.awt.*;
import java.awt.event.*;
public class A implements ActionListener
 {Frame f=new Frame("计算器");
  Button b1,b2,b3;TextField t1,t2,t3;
  public static void main(String[]args){new A().g();}
  public void g()
   {b1=new Button("+");b2=new Button("-");b3=new Button("清除");
    t1=new TextField(5);t2=new TextField(5);t3=new TextField(5);
    f.setLayout(new GridLayout(3,3,5,5));
    f.add(new Label("运算量1",Label.CENTER));
    f.add(new Label("运算量2",Label.CENTER));
    f.add(new Label("运算结果",Label.CENTER));
    f.add(t1);f.add(t2);f.add(t3);
    f.add(b1);f.add(b2);f.add(b3);
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    f.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent e){System.exit(0);}});
    f.pack();
    f.setVisible(true);
 }
 public void actionPerformed(ActionEvent e)
 {int x=Integer.parseInt(t1.getText());
  int y=Integer.parseInt(t2.getText());
  if(e.getSource()==b1)t3.setText(x+y+"");
  if(e.getSource()==b2)t3.setText(x-y+"");
  if(e.getSource()==b3){t1.setText("");t2.setText("");t3.setText("");}
 }
}
```
**143（2）**
```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class A implements ActionListener
 {JFrame f=new JFrame("计算器");
  JButton b1,b2,b3;
  JTextField t1,t2,t3;
  public static void main(String[]args)
   {new A().g();}
  public void g()
   {b1=new JButton("+");
    b2=new JButton("-");
    b3=new JButton("清除");
    t1=new JTextField(5);
    t2=new JTextField(5);
    t3=new JTextField(5);
    Container c=f.getContentPane();
    c.setLayout(new GridLayout(3,3,5,5));
    c.add(new JLabel("运算量1",JLabel.CENTER));
    c.add(new JLabel("运算量2",JLabel.CENTER));
    c.add(new JLabel("运算结果",JLabel.CENTER));
    c.add(t1);c.add(t2);c.add(t3);
    c.add(b1);c.add(b2);c.add(b3);
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.pack();
    f.setVisible(true);
 }
 public void actionPerformed(ActionEvent e)
 {int x=Integer.parseInt(t1.getText());
  int y=Integer.parseInt(t2.getText());
  if(e.getSource()==b1)t3.setText(x+y+"");
  if(e.getSource()==b2)t3.setText(x-y+"");
  if(e.getSource()==b3){t1.setText("");t2.setText("");t3.setText("");}
 }
}
```
**143（3）**
```java
import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;
public class A extends Applet implements ActionListener
 {Button b1,b2,b3;TextField t1,t2,t3;
  public void init()
   {b1=new Button("+");b2=new Button("-");b3=new Button("清除");
    t1=new TextField(5);t2=new TextField(5);t3=new TextField(5);
    setLayout(new GridLayout(3,3,5,5));
    add(new Label("运算量1",Label.CENTER));
    add(new Label("运算量2",Label.CENTER));
    add(new Label("运算结果",Label.CENTER));
    add(t1);add(t2);add(t3);
    add(b1);add(b2);add(b3);
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
   }
 public void actionPerformed(ActionEvent e)
 {int x=Integer.parseInt(t1.getText());
  int y=Integer.parseInt(t2.getText());
  if(e.getSource()==b1)t3.setText(x+y+"");
  if(e.getSource()==b2)t3.setText(x-y+"");
  if(e.getSource()==b3){t1.setText("");t2.setText("");t3.setText("");}
 }
}
<html>
<applet code=A.java width=200 height=100>
</applet>
</html>
```
**143（4）**
```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class A extends JApplet implements ActionListener
 {JButton b1,b2,b3;
  JTextField t1,t2,t3;
  public void init()
   {b1=new JButton("+");
    b2=new JButton("-");
    b3=new JButton("清除");
    t1=new JTextField(5);
    t2=new JTextField(5);
    t3=new JTextField(5);
    Container c=getContentPane();
    c.setLayout(new GridLayout(3,3,5,5));
    c.add(new JLabel("运算量1",JLabel.CENTER));
    c.add(new JLabel("运算量2",JLabel.CENTER));
    c.add(new JLabel("运算结果",JLabel.CENTER));
    c.add(t1);c.add(t2);c.add(t3);
    c.add(b1);c.add(b2);c.add(b3);
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
   }
 public void actionPerformed(ActionEvent e)
 {int x=Integer.parseInt(t1.getText());
  int y=Integer.parseInt(t2.getText());
  if(e.getSource()==b1)t3.setText(x+y+"");
  if(e.getSource()==b2)t3.setText(x-y+"");
  if(e.getSource()==b3){t1.setText("");t2.setText("");t3.setText("");}
 }
}
<html>
<applet code=A.java width=200 height=100>
</applet>
</html>
```
**144（1）**
```
import java.awt.*;
import java.awt.event.*;
public class A implements ActionListener
 {Frame f,f1,f2;static int n=1,x=0,y=0,z=1;Panel p1,p2,p3;
  Button b1,b2;TextField t1,t2;Label s=new Label("",Label.CENTER);
  public static void main(String[]args){new A().g();}
  public void g()
   {f=new Frame("系统登录");b1=new Button("提交");b2=new Button("重填");
    p1=new Panel();p2=new Panel();p3=new Panel();
    t1=new TextField(10);t2=new TextField(10);t2.setEchoChar('*');
    f.setLayout(new GridLayout(4,1,5,5));
    f.add(p1);p1.add(new Label("姓名：",Label.CENTER));p1.add(t1);
    f.add(p2);p2.add(new Label("口令：",Label.CENTER));p2.add(t2);
    f.add(p3);p3.add(b1);p3.add(b2);f.add(s);
    b1.addActionListener(this);
    b2.addActionListener(this);
    f.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent  
e){z--;if(z==0)System.exit(0);else f.setVisible(false);}});
    f.setSize(200,150);f.setVisible(true);
 }
 public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b2){n++;if(n>3){z--;if(z==0)System.exit(0);else f.setVisible(false);}
      else {t1.setText("");t2.setText("");s.setText("");}}
   if(e.getSource()==b1)
    {if(t1.getText().equals("abc")&&t2.getText().equals("123"))
       {n=0;x++;z++;if(x==1){f1=new Frame("欢迎"+t1.getText());f1.setSize(120,50);
        f1.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent  
e){z--;if(z==0)System.exit(0);else f1.setVisible(false);}});}f1.setVisible(true);
       }
     else if(t1.getText().equals("efg")&&t2.getText().equals("456"))   
       {n=0;y++;z++;if(y==1){f2=new Frame("欢迎"+t1.getText());f2.setSize(120,50);
        f2.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent  
e){z--;if(z==0)System.exit(0);else f2.setVisible(false);}});}f2.setVisible(true);
       }
     else s.setText("这是你第"+n+"次登录失败！");
    }
  }
}
```
**144（2）**
```
import java.awt.*;
import java.awt.event.*;
public class A implements ActionListener
 {Frame f,f1;static int n=1;Panel p1,p2,p3;
  Button b1,b2;TextField t1,t2;Label s=new Label("",Label.CENTER);
  public static void main(String[]args){new A().g();}
  public void g()
   {f=new Frame("系统登录");b1=new Button("提交");b2=new Button("重填");
    p1=new Panel();p2=new Panel();p3=new Panel();
    t1=new TextField(10);t2=new TextField(10);t2.setEchoChar('*');
    f.setLayout(new GridLayout(4,1,5,5));
    f.add(p1);p1.add(new Label("姓名：",Label.CENTER));p1.add(t1);
    f.add(p2);p2.add(new Label("口令：",Label.CENTER));p2.add(t2);
    f.add(p3);p3.add(b1);p3.add(b2);f.add(s);
    b1.addActionListener(this);
    b2.addActionListener(this);
    f.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent  
e){System.exit(0);}});
    f.setSize(200,150);f.setVisible(true);
 }
 public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b2){n++;if(n>3)System.exit(0);
      else {t1.setText("");t2.setText("");s.setText("");}}
   if(e.getSource()==b1) 
{if((t1.getText().equals("abc")&&t2.getText().equals("123"))||(t1.getText().equals("efg")&&t2.getText().equals("456")))
       {n=0;f1=new Frame("欢迎"+t1.getText());f1.setSize(150,50);f1.setVisible(true);
        f1.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent  
e){f1.setVisible(false);}});}
     else s.setText("这是你第"+n+"次登录失败！");
    }
  }
}
```
**145（1）**
```java
import java.awt.*;
import java.awt.event.*;
public class A extends WindowAdapter implements ActionListener
{ Frame  f=new Frame("猜数字游戏");
   Label s1=new Label();
   Label s2=new Label();
   Label s3=new Label();
   Button b1=new Button("提交");
   Button b2=new Button("重新开始");
   TextField t=new TextField();
   int x,y,n=1;
   boolean b=true;
   public A()
   {  f.setLayout(new GridLayout(3,2,10,10));
       f.add(s1);
       f.add(t);
       f.add(b1);
       f.add(s2);
       f.add(b2);
       f.add(s3);
       f.pack();
       f.setVisible(true);
       b1.addActionListener(this);
       b2.addActionListener(this);
       f.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent e){System.exit(0);}});
       show(n);
       s();
   }
  public void s(){x=(int)(Math.random()*100);}
  public void show(int m){s1.setText("第"+m+"次输入：");}
  public static void main(String[]args){new A();}
  public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b1)
     { n++;
        if(n<=10&&b)
            { y=Integer.parseInt(t.getText());
               if(x==y)
                    { s2.setText("x="+x);
                       s3.setText("ok!");
                       b=false;
                    }
               else if(x>y)
                    { s2.setText(y+"小了!");
                       show(n);
                    }
               else
                    { s2.setText(y+"大了!");
                       show(n);
                    }
             }
        else begin();
      }
   if(e.getSource()==b2)
        begin();
 }
 public void begin()
    { n=1;
       b=true;
       s();
       show(n);
       s2.setText("");
       s3.setText("");
       t.setText("");
    }
}
```
**145（2）**
```java
import java.awt.*;
import java.awt.event.*;
public class A extends WindowAdapter implements ActionListener
{  Frame  f=new Frame("猜数字游戏");
   Label s1=new Label("被猜数据的最大值=");
   Label s2=new Label("被猜数据的最小值=");
   Label s3=new Label("允许的猜数次数=");
   Label s4=new Label("",Label.CENTER);
   Label s5=new Label("",Label.CENTER);
   Button b1=new Button("重新开局");
   Button b2=new Button("退  出");
   Button b3=new Button("提  交");
   Button b4=new Button("重  填");
   TextField t1=new TextField("100");
   TextField t2=new TextField("0");
   TextField t3=new TextField("10");
   TextField t4=new TextField();
   Panel p=new Panel();
   int max,min,x,y,n,count;
   boolean b=true;
   public A()
   {   f.add(p,"Center");
       p.setLayout(new GridLayout(6,2,10,10));
       p.add(s1);p.add(t1);
       p.add(s2);p.add(t2);
       p.add(s3);p.add(t3);
       p.add(b1);p.add(b2);
       p.add(s4);p.add(t4);
       p.add(b3);p.add(b4);
       f.add(s5,"South");
       f.pack();
       f.setVisible(true);
       b1.addActionListener(this);
       b2.addActionListener(this);
       b3.addActionListener(this);
       b4.addActionListener(this);
       f.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent e){System.exit(0);}});
       init();
   }
  public void init()
     {  max=Integer.parseInt(t1.getText());
        min=Integer.parseInt(t2.getText());
        n=Integer.parseInt(t3.getText());
        x=(int)(Math.random()*(max-min))+min;
        count=0;
        display(count+1);
        b=true;
        t4.setEditable(true);
        t4.setText("");
        s5.setText("");
     }
  public void display(int m){s4.setText("请提交第"+m+"个数据！");}
  public void show(int m){s4.setText("第"+m+"次输入的数据是：");}
  public void go()
     {  if(count>10 && b)
             { s4.setText("请重新开局！");
               s5.setText("x="+x+"     timesout！    本局未猜中！");
               t4.setEditable(false);
             }
        else if(count<=10 && !b)
             { 
               s5.setText("你已经猜中了，请重新开局！");
             }
      }
  public static void main(String[]args){new A();}
  public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b1)init();
   else if(e.getSource()==b2)System.exit(0); 
   else if(e.getSource()==b3)
       { count++;
         if(count<=10 && b)
            {  y=Integer.parseInt(t4.getText());
               if(x==y)
                    {  t4.setEditable(false);
                       s5.setText("x="+x+"   ok！   你用了"+count+"次猜中该数据！");
                       b=false;
                    }
               else  if(x>y)s5.setText(y+"小了！");
               else  s5.setText(y+"大了！");
               show(count);
            }
        else go();
       }
   else if(e.getSource()==b4)
        {if(count<=10 && b){t4.setText("");display(count+1);}
         else go();
        }
 }
}
```
**146**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
public class A extends JApplet
{int r=0,g=0,b=0;
 Container ctp=getContentPane();
 JLabel s1,s2,s3;JSlider sd1,sd2,sd3;
 JTextField tf;
 public void init()
  {tf=new JTextField(20);
   s1=new JLabel("红");
   s2=new JLabel("绿");
   s3=new JLabel("蓝");
   sd1=new JSlider(JSlider.HORIZONTAL,0,255,0);
   sd2=new JSlider(JSlider.HORIZONTAL,0,255,0);
   sd3=new JSlider(JSlider.HORIZONTAL,0,255,0);
   ctp.setLayout(new FlowLayout());
   ctp.add(s1);
   ctp.add(sd1);
   sd1.setPaintTicks(true);
   sd1.setMajorTickSpacing(5);
   sd1.addChangeListener(new K1());
   ctp.add(s2);
   ctp.add(sd2);
   sd2.setPaintTicks(true);
   sd2.setMajorTickSpacing(5);
   sd2.addChangeListener(new K2());
   ctp.add(s3);
   ctp.add(sd3);
   sd3.setPaintTicks(true);
   sd3.setMajorTickSpacing(5);
   sd3.addChangeListener(new K3());
   ctp.add(tf);
  }
  class K1 implements ChangeListener
  {  public void stateChanged(ChangeEvent e)
       {r=sd1.getValue();
        tf.setBackground(new Color(r,g,b));
       }
   }
  class K2 implements ChangeListener
  {public void stateChanged(ChangeEvent e)
     {g=sd2.getValue();
      tf.setBackground(new Color(r,g,b));
     }
  }
  class K3 implements ChangeListener
  {public void stateChanged(ChangeEvent e)
      {b=sd3.getValue();
       tf.setBackground(new Color(r,g,b));
      }
  }
}
```
**147**
```
import java.awt.*;
import java.awt.event.*;
public class A extends WindowAdapter implements ActionListener
{ Frame  f=new Frame("XXX");
   Label s=new Label("",Label.CENTER);
   Button b1=new Button("显示");
   Button b2=new Button("隐藏");
   MenuBar mb=new MenuBar();
   Menu m=new Menu("AA");
   MenuItem m1=new MenuItem("11");
   MenuItem m2=new MenuItem("22");
   MenuItem m3=new MenuItem("退出");
   Panel p=new Panel();
   public A()
   {  f.setMenuBar(mb);
       f.add(p,"Center");
       p.add(b1);p.add(b2);
       f.add(s,"South");
       mb.add(m);
       m.add(m1);
       m.add(m2);
       m.addSeparator();
       m.add(m3);
       f.pack();
       f.setVisible(true);
       b1.addActionListener(this);
       b2.addActionListener(this);
       m3.addActionListener(this);
       f.addWindowListener(new WindowAdapter(){public void windowClosing(WindowEvent e){System.exit(0);}});
   }
  public static void main(String[]args){new A();}
  public void actionPerformed(ActionEvent e)
  {if(e.getSource()==b1)s.setText("电子科技大学");
   else if(e.getSource()==b2)s.setText(""); 
   else if(e.getSource()==m3)System.exit(0);
  }
}
```
**148**
```java
//本程序需要预先用Windows的画图等软件制作准备3张图片：jia.ico、jian.ico、zero.ico
//并将它们存放于本源程序同一个目录下。
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A extends JFrame implements ActionListener
{JButton b1,b2,b3;
  JLabel s;
  static int count=0;
  JToolBar tb;
  JPanel p;
  JMenuBar mb;
  JMenu m1;
  JMenuItem m11,m12,m13;
  public A()
    {  super("工具栏演示程序");
       setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       p=new JPanel();p.setLayout(new BorderLayout());
       setContentPane(p);
       tb=new JToolBar();
       b1=new JButton(new ImageIcon("jia.ico"));b1.setToolTipText("加");
       b2=new JButton(new ImageIcon("jian.ico"));b2.setToolTipText("减");
       b3=new JButton(new ImageIcon("zero.ico"));b3.setToolTipText("清零");
       s=new JLabel(""+count,JLabel.CENTER);
       mb=new JMenuBar();
       m1=new JMenu("计数",false);
       m11=new JMenuItem("加",new ImageIcon("jia.ico"));
       m12=new JMenuItem("减",new ImageIcon("jian.ico"));
       m13=new JMenuItem("清零",new ImageIcon("zero.ico"));
       setJMenuBar(mb);
       mb.add(m1);
       m1.add(m11);m1.add(m12);m1.add(m13);
       tb.add(b1);tb.add(b2);tb.add(b3);
       p.add(tb,BorderLayout.NORTH);p.add(s,BorderLayout.CENTER);
       setSize(200,200);setVisible(true);
       b1.addActionListener(this);b2.addActionListener(this);
       b3.addActionListener(this);m11.addActionListener(this);
       m12.addActionListener(this);m13.addActionListener(this);
     }
   public static void main(String[]args)
      {A a=new A();}
   public void actionPerformed(ActionEvent e)
      {if(e.getSource()==b1||e.getSource()==m11)count++;
        else if(e.getSource()==b2 || e.getSource()==m12)count--;
        else if(e.getSource()==b3 || e.getSource()==m13)count=0;
        s.setText(""+count);
       }
}
```
**149**
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class A implements ActionListener
{JFrame f;;
 JPanel p;
 JMenuBar mb;
 JMenu m1;
 JMenuItem m11,m12,m13,m14;
 Color defaultColor=Color.YELLOW;
 public void init()
 {f=new JFrame("XXX");
  p=new JPanel();
  f.setContentPane(p);
  p.setBackground(Color.YELLOW);
  mb=new JMenuBar();
  m1=new JMenu("设置背景颜色");
  m11=new JMenuItem("红色");
  m12=new JMenuItem("绿色");
  m13=new JMenuItem("兰色");
  m14=new JMenuItem("还原");
  f.setJMenuBar(mb);
  mb.add(m1);
  m1.add(m11);m1.add(m12);m1.add(m13);
  m1.addSeparator();m1.add(m14);
  m11.addActionListener(this);
  m12.addActionListener(this);
  m13.addActionListener(this);
  m14.addActionListener(this);
  f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  p.setBackground(defaultColor);
  f.setBounds(200,200,200,200);
  f.setVisible(true);
 }
 public void actionPerformed(ActionEvent e)
 {if(e.getSource()==m11)p.setBackground(Color.RED);
  else if(e.getSource()==m12)p.setBackground(Color.GREEN);
  else if(e.getSource()==m13)p.setBackground(Color.BLUE);
  else if(e.getSource()==m14)p.setBackground(defaultColor);
 }
 public static void main(String[]args)
 {A a=new A();a.init();}
}
```
**150**
```java
import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;
public class A extends Applet implements ActionListener
{Label s1=new Label("输人十进制数");
TextField t1=new TextField(6);
Label s2=new Label("二进制数为");
TextField t2=new TextField(6);
Label s3=new Label("八进制数为");
TextField t3=new TextField(6);
Label s4=new Label("十六进制数为");
TextField t4=new TextField(6);
Button b=new Button("变换");
public void init()//初始化
 {setLayout(new GridLayout(5,2));
  add(s1);add(t1);
  add(s2);add(t2);
  add(s3);add(t3);
  add(s4);add(t4);
  add(b);
  b.addActionListener(this);
}
public void actionPerformed(ActionEvent e)//处理按钮事件
 {int x=Integer.parseInt(t1.getText());
  t2.setText(Integer.toBinaryString(x)); //数值转换为字符串
  t3.setText(Integer.toOctalString(x));
  t4.setText(Integer.toHexString(x));
}
}
```