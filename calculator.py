import math
import time
import tkinter
import tkinter.messagebox

class Calculator:
    def __init__(self):
        #setting main window
        self.root = tkinter.Tk()
        #setting the min-size and max-size of main window
        self.root.minsize(300, 450)
        self.root.maxsize(360, 540)
        self.root.title('简易计算器Version 1.0')
        #settring output result box
        self.result = tkinter.StringVar()
        self.result.set(0)
        #setting a global variable to store the different numbers and signals
        self.lists = []
        self.resetting_flag = False
        #layout of main window
        self.menus()
        self.layout()
        self.root.mainloop()

    #setting the layout of menus
    def menus(self):
        #root menu
        allmenu = tkinter.Menu(self.root)
        #define file sub-menu
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        #add other options
        filemenu.add_command(label='标准型(T)            Alt+1', command=self.fortesting)
        filemenu.add_command(label='科学型(S)            Alt+2', command=self.fortesting)
        #add separator-line
        filemenu.add_separator()
        filemenu.add_command(label='历史记录(Y)      Ctrl+H', command=self.fortesting)
        filemenu.add_separator()
        filemenu.add_command(label='显示日期(D)      Ctrl+D', command=self.showtime)
        filemenu.add_separator()

        #define sub-sub-menu in file sub-menu
        sub_fm = tkinter.Menu(filemenu, tearoff=0)
        sub_fm.add_command(label='示例1', command=self.fortesting)
        sub_fm.add_command(label='示例2', command=self.fortesting)

        #add sub-sub-menu to file sub-menu
        filemenu.add_cascade(label='测试', menu=sub_fm)
        #add file sub-menu to main menu
        allmenu.add_cascade(label='查看', menu=filemenu)

        #define edit sub-menu
        editmenu = tkinter.Menu(allmenu, tearoff=0)
        editmenu.add_command(label='复制(C)         Ctrl+C', command=self.fortesting)
        editmenu.add_command(label='粘贴(V)         Ctrl+V', command=self.fortesting)
        allmenu.add_cascade(label='编辑', menu=editmenu)

        #define help sub-menu
        helpmenu = tkinter.Menu(allmenu, tearoff=0)
        helpmenu.add_command(label='关于计算器', command=self.helpfunc)
        allmenu.add_cascade(label='帮助', menu=helpmenu)
        self.root.config(menu=allmenu)

    #setting the layout of Calculator
    def layout(self):
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 45), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=135)
        # ←
        button_zuo = tkinter.Button(self.root, text='←', command=self.dele_one)
        button_zuo.place(x=5, y=150, width=50, height=50)
        #CE: clear 0
        button_ce = tkinter.Button(self.root, text='CE', command=lambda: self.result.set(0))
        button_ce.place(x=60, y=150, width=50, height=50)
        #C
        button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
        button_c.place(x=115, y=150, width=50, height=50)
        #sqrt
        button_c = tkinter.Button(self.root, text='Sqrt', command=self.sqrt)
        button_c.place(x=170, y=150, width=50, height=50)
        #power
        button_c = tkinter.Button(self.root, text='Power', command=self.power)
        button_c.place(x=225, y=150, width=50, height=50)
        #7
        button_7 = tkinter.Button(self.root, text='7', command=lambda: self.pressnum('7'))
        button_7.place(x=5, y=205, width=50, height=50)
        #8
        button_8 = tkinter.Button(self.root, text='8', command=lambda: self.pressnum('8'))
        button_8.place(x=60, y=205, width=50, height=50)
        #9
        button_9 = tkinter.Button(self.root, text='9', command=lambda: self.pressnum('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        #/
        button_division = tkinter.Button(self.root, text='/', command=lambda: self.presscalculate('/'))
        button_division.place(x=170, y=205, width=50, height=50)
        #%
        button_remainder = tkinter.Button(self.root, text='//', command=lambda: self.presscalculate('//'))
        button_remainder.place(x=225, y=205, width=50, height=50)
        #4
        button_4 = tkinter.Button(self.root, text='4', command=lambda: self.pressnum('4'))
        button_4.place(x=5, y=260, width=50, height=50)
        #5
        button_5 = tkinter.Button(self.root, text='5', command=lambda: self.pressnum('5'))
        button_5.place(x=60, y=260, width=50, height=50)
        #6
        button_6 = tkinter.Button(self.root, text='6', command=lambda: self.pressnum('6'))
        button_6.place(x=115, y=260, width=50, height=50)
        #*
        button_multiplication = tkinter.Button(self.root, text='*', command=lambda: self.presscalculate('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)
        #1/x
        button_reciprocal = tkinter.Button(self.root, text='1/x', command=self.ds)
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        #1
        button_1 = tkinter.Button(self.root, text='1', command=lambda: self.pressnum('1'))
        button_1.place(x=5, y=315, width=50, height=50)
        #2
        button_2 = tkinter.Button(self.root, text='2', command=lambda: self.pressnum('2'))
        button_2.place(x=60, y=315, width=50, height=50)
        #3
        button_3 = tkinter.Button(self.root, text='3', command=lambda: self.pressnum('3'))
        button_3.place(x=115, y=315, width=50, height=50)
        #-
        button_subtraction = tkinter.Button(self.root, text='-', command=lambda: self.presscalculate('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)
        #=
        button_equal = tkinter.Button(self.root, text='=', command=lambda: self.pressequal())
        button_equal.place(x=225, y=315, width=50, height=105)
        #0
        button_0 = tkinter.Button(self.root, text='0', command=lambda: self.pressnum('0'))
        button_0.place(x=5, y=370, width=105, height=50)
        #.
        button_point = tkinter.Button(self.root, text='.', command=lambda: self.pressnum('.'))
        button_point.place(x=115, y=370, width=50, height=50)
        #+
        button_plus = tkinter.Button(self.root, text='+', command=lambda: self.presscalculate('+'))
        button_plus.place(x=170, y=370, width=50, height=50)

    #计算器菜单功能
    def fortesting(self):
        tkinter.messagebox.showinfo('', 'For Testing')

    def helpfunc(self):
        tkinter.messagebox.showinfo('', 'Version 1.0 by Renjie Lu')

    def showtime(self):
        tkinter.messagebox.showinfo('', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    #function: ←
    def dele_one(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:#num = 1
                self.result.set('0')
            return

    #clear the context of input box and lists
    def sweeppress(self):
        self.lists.clear()
        self.result.set(0)

    #1/x
    def ds(self):
        value = 1 / int(self.result.get())
        self.result.set(str(value)[:8])
        self.lists.clear()
        self.resetting_flag = True

    def sqrt(self):
        value = math.sqrt(int(self.result.get()))
        self.result.set(str(value)[:8])
        self.lists.clear()
        self.resetting_flag = True

    def power(self):
        value = math.pow(int(self.result.get()), 2)
        self.result.set(str(value)[:8])
        self.lists.clear()
        self.resetting_flag = True

    def pressnum(self, num):
        if self.resetting_flag == False:
            pass
        else:
            self.result.set(0)
            self.resetting_flag = False
        pre_num = self.result.get()
        if pre_num == '0':
            if num == '.':
                num = '0.'
            self.result.set(num)
        else:
            num = pre_num + num
            self.result.set(num)

    def presscalculate(self, sign):
        #保存已经按下的数字和运算符号
        num = self.result.get()
        self.lists.append(num)
        self.lists.append(sign)
        self.resetting_flag = True

    #calculate the value
    def pressequal(self):
        num = self.result.get()
        # 将当前界面的数字存入列表
        self.lists.append(num)
        operation = ''.join(self.lists)
        #使用eval直接计算该字符对应的表达式的值
        value = eval(operation)
        self.result.set(str(value)[:8])
        self.lists.clear()
        self.resetting_flag = True

#create a instance
myCalculator = Calculator()