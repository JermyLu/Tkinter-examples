import os
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import tkinter.filedialog as dir
from queue import Queue

def dfs(result, key_words, root_path):
    name_list = os.listdir(root_path)
    for name in name_list:
        sub_path = os.path.join(root_path, name)
        if os.path.isfile(sub_path):
            for key_word in key_words:
                if key_word in name:
                    result.append(sub_path)
        else:
            dfs(result, key_words, sub_path)

def bfs(key_words, root_path):
    result = []
    file_queue = Queue()
    for ele in os.listdir(root_path):
        file_queue.put(os.path.join(root_path, ele))

    while not file_queue.empty():#true: empty; false: not empty
        pop_path = file_queue.get()
        if os.path.isfile(pop_path):
            for key_word in key_words:
                if key_word in os.path.basename(pop_path):
                    #print(os.path.basename(pop_path))
                    result.append(pop_path)
        elif os.path.isdir(pop_path):
            for ele in os.listdir(pop_path):
                file_queue.put(os.path.join(pop_path, ele))
    return result


class searchUI():
    def __init__(self):
        self.path = "C:/"
        root = Tk()
        root.title("简易磁盘文件搜索工具")

        curWidth = root.winfo_width()  # get current width
        curHeight = root.winfo_height()  # get current height
        scnWidth, scnHeight = root.maxsize()  # get screen width and height
        position = '+%d+%d' % ((scnWidth - curWidth)/4, (scnHeight - curHeight)/4)
        root.geometry(position)

        self.key_words = StringVar()
        self.output_results = scrolledtext.ScrolledText(root, width=80)
        self.clear_chosen = ttk.Combobox(root, width=12, textvariable=StringVar(), state='readonly')
        #self.output_results = Text(root)

        self.create_menu(root)
        self.create_content(root)
        root.mainloop()

    def create_menu(self, root):
        menu = Menu(root)

        #two-level menu
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="设置路径", command=self.open_dir)

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="Version:1.0")

        #one-level menu
        menu.add_cascade(label="文件", menu=file_menu)
        menu.add_cascade(label="关于", menu=about_menu)
        root['menu'] = menu

    def create_content(self, root):
        ttk.Label(root, text="请输入关键词，关键词之间以;分割").grid(row=0, column=0)

        key_words_entered = ttk.Entry(root, width=60, textvariable=self.key_words)
        key_words_entered.grid(row=1, column=0)

        action = ttk.Button(root, text="搜索", command=self.search_file)
        action.grid(row=2, column=0)

        clear = ttk.Button(root, text="清空", command=self.clear_keys)
        clear.grid(row=3, column=0)

        self.clear_chosen['values'] = ['关键字', '搜索结果', 'ALL']
        self.clear_chosen.grid(row=4, column=0)
        self.clear_chosen.current()

        ttk.Label(root, text="搜索结果以绝对路径的方式呈现，每行为一个搜索结果").grid(row=5, column=0)
        self.output_results.grid(row=6, column=0)

    def open_dir(self):
        d = dir.Directory()
        self.path = d.show(initialdir=self.path)

    def clear_keys(self):
        if self.clear_chosen.get() == "关键字":
            self.key_words.set('')
        elif self.clear_chosen.get() == "搜索结果":
            self.output_results.delete(1.0, END)
        else:
            self.key_words.set('')
            self.output_results.delete(1.0, END)

    def search_file(self):
        root_path = self.path
        print(root_path)
        key_words = self.key_words.get()
        if key_words == '':
            self.output_results.delete(1.0, END)
            self.output_results.insert(END, "请输入搜索关键词\n")
            self.output_results.update()
        else:
            #print(key_words)
            key_words = key_words.split(';')
            result = bfs(key_words, root_path)
            self.output_results.delete(1.0, END)
            if len(result) == 0:
                self.output_results.insert(END, "结果为空\n")
                self.output_results.update()
            else:
                for ele in result:
                    self.output_results.insert(END, str(ele) + "\n")
                    self.output_results.see(END)
                    self.output_results.update()

if __name__ == "__main__":
    searchUI()