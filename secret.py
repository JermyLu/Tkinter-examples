from tkinter import *
from tkinter import ttk
import time
import hashlib

log_num = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本加密工具Version 1.0")
        self.init_window_name.geometry('720x360+10+10')#290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.init_window_name["bg"] = "white"
        #Label
        self.init_data_label = Label(self.init_window_name, text="原始文本")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="加密结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="运行日志")
        self.log_label.grid(row=12, column=0)

        #Text
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)

        #加密
        self.algorithm_label = Label(self.init_window_name, text="请选择一种加密算法")
        self.algorithm_label.grid(row=0, column=11)
        self.algorithm_chosen = ttk.Combobox(self.init_window_name, width=12, textvariable=StringVar(), state='readonly')
        self.algorithm_chosen['values'] = ['md5', 'sha1']
        self.algorithm_chosen.grid(row=1, column=11)
        self.algorithm_chosen.current()
        self.secret_button = Button(self.init_window_name, text='点击加密', bg="lightblue", width=10,
                                    command=self.str_secret)
        self.secret_button.grid(row=2, column=11)

    #加密函数
    def str_secret(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        # print("src =%s" % src)
        if src:
            try:
                if self.algorithm_chosen.get() == 'md5':
                    secret = hashlib.md5()
                elif self.algorithm_chosen.get() == 'sha1':
                    secret = hashlib.sha1()
                secret.update(src)
                secret_digest = secret.hexdigest()
                # print(secret_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, END)  # 删除上次加密结果
                self.result_data_Text.insert(1.0, secret_digest)
                self.write_log_to_Text("INFO: str_secret_by_%s success" % self.algorithm_chosen.get())
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "使用%s加密算法，对字符串加密失败" % self.algorithm_chosen.get())
        else:
            self.write_log_to_Text("ERROR: str_secret_by_%s failed" % self.algorithm_chosen.get())

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    #日志动态打印
    def write_log_to_Text(self, logmsg):
        global log_num
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"      #换行
        if log_num < 6:#最多显示6行日志
            self.log_data_Text.insert(END, logmsg_in)
            log_num += 1
        else:
            self.log_data_Text.delete(1.0, END)
            log_num = 0#重新置为0
            self.log_data_Text.insert(END, logmsg_in)
            log_num += 1

def gui_start():
    init_window = Tk()#实例化出一个父窗口
    Test = MY_GUI(init_window)
    # 设置根窗口默认属性
    Test.set_init_window()
    init_window.mainloop()#父窗口进入事件循环，窗口运行，否则界面不展示

gui_start()