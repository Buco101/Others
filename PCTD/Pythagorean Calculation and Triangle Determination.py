# ===============================================================
# 勾股计算与三角形判定
# Pythagorean Calculation and Triangle Determination
# 作者：JBY（拼音缩写） - Buco
# Author: JBY (Pinyin Abbreviation) - Buco
# See: https://github.com/Buco101/Others
# ===============================================================

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math
import os
import sys
import gettext

# ---------------------------------------------------------------
# 计算与判断功能部分
# Calculation And Judgment Function Part
# ---------------------------------------------------------------

# 计算勾股定理
def calculate_pythagoras():
    try:
        # 从 entry 组件内获得输入的值
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = math.sqrt(a**2 + b**2)
        entry_c.delete(0, tk.END)
        entry_c.insert(0, f"{c:.2f}")
    
    # 若输入的值无效，提示错误
    except ValueError:
        messagebox.showerror("错误", "你输入的数字似乎无效。")

# 判断是否能构成三角形
def check_triangle():
    try:
        # 从 entry 组件内获得输入的值
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        # 进行判断
        if a + b > c and a + c > b and b + c > a:
            messagebox.showinfo("判断结果", [f"{a:g}", f"{b:g}", f"{c:g}", "可以构成三角形"])  # f"{value:g}" 可以让值自动去除整数后的小数点部分
        else:
            messagebox.showinfo("判断结果", [f"{a:g}", f"{b:g}", f"{c:g}", "不可以构成三角形"])
    
    # 若输入的值无效，提示错误
    except ValueError:
        messagebox.showerror("错误", "你输入的数字似乎无效。")

# ---------------------------------------------------------------
# 界面自动调整部分
# Automatic Adjustment of the Interface
# ---------------------------------------------------------------

# 更新字体大小
def update_font_size():
    # 使用窗口的当前宽度来调整字体大小
    width = root.winfo_width()
    font_size = int(width / 30)  # 根据窗口宽度来调整字体大小
    style.configure("RoundedButton.TButton",
                    font=("PingFang SC", font_size-3, "bold"))
    label_a.config(font=("PingFang SC", font_size), background="#F5F5F7")
    label_b.config(font=("PingFang SC", font_size), background="#F5F5F7")
    label_c.config(font=("PingFang SC", font_size), background="#F5F5F7")
    entry_a.config(font=("SF Pro Text", font_size))
    entry_b.config(font=("SF Pro Text", font_size))
    entry_c.config(font=("SF Pro Text", font_size))

# 延迟执行字体更新，确保只有窗口调整完时才执行
def delayed_update_font_size():
    global resizing
    if resizing:
        resizing = False  # 标记已经完成调整
        update_font_size()

# 窗口大小调整事件
def resize(event):
    global resizing
    if not resizing:
        resizing = True  # 标记正在调整
        root.after(100, delayed_update_font_size)  # 延迟100毫秒执行更新

# 初始化变量
resizing = False  # 用于标记是否正在调整窗口

# 创建 GUI 窗口
root = tk.Tk()
root.title("勾股计算与三角形判定")

width = 400  # 设置窗口宽度
height = 400  # 设置窗口长度
root.config(bg='#F5F5F7')  # 设置窗口背景色
root.minsize(width, height)  # 设置窗口最小尺寸

# 设置窗口位置
g_screenwidth = root.winfo_screenwidth()
g_screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (g_screenwidth-width)/2, (g_screenheight-height)/2)
root.geometry(alignstr)

# 绑定窗口大小改变事件
root.bind("<Configure>", resize)

# ---------------------------------------------------------------
# 菜单部分
# Menu Part
# ---------------------------------------------------------------

# 重新启动应用
def restart_app():
    # 获取当前脚本路径，使用 os.execv 来重新启动该脚本
    python = sys.executable  # 获取当前 Python 解释器路径
    os.execv(python, ['python'] + sys.argv)  # 重启当前程序

# 显示关于信息
def show_about():
    messagebox.showinfo("关于", "勾股计算与三角形判定 App\nVersion 1.1\n可能需要 Python 3.13 或更高版本\nCopyright © 2025 不可 Buco 保留所有权利。")

# 显示入门信息 1
def show_usePythagorean():
    messagebox.showinfo("勾股一下 - 入门", "“勾股一下”， 意思很简单，就是在直角三角形内，根据你输入的第一条边、第二条边来算出第三条边。\n注意：当你使用该功能时，你输入的第一边和第二边将作为直角边，第三边将为作为斜边计算！")

# 显示入门信息 2
def show_useJudgment():
    messagebox.showinfo("判断三角形 - 入门", "判断三角形，就是将你输入的三条边的长度进行判断是否能组成三角形")

# 创建菜单栏
menu_bar = tk.Menu(root)

# 创建文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件(F)", menu=file_menu, underline=3)
file_menu.add_command(label="重新启动(R)", command=restart_app, underline=5)
file_menu.add_separator()
file_menu.add_command(label="退出(E)", command=root.quit, underline=3)

# 创建帮助菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
getStarted_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_cascade(label="入门(G)", menu=getStarted_menu, underline=3)
getStarted_menu.add_command(label="勾股一下", command=show_usePythagorean)
getStarted_menu.add_command(label="判断三角形", command=show_useJudgment)
help_menu.add_command(label="关于(A)", command=show_about, underline=3)
menu_bar.add_cascade(label="帮助(H)", menu=help_menu, underline=3)


# 配置窗口的菜单
root.config(menu=menu_bar)

# ---------------------------------------------------------------
# 内容样式部分
# Content Style Part
# ---------------------------------------------------------------

# 输入框标签
label_a = tk.Label(root, text="第一边:")
label_a.grid(row=0, column=0, padx=10, pady=5, sticky="w")

label_b = tk.Label(root, text="第二边:")
label_b.grid(row=1, column=0, padx=10, pady=5, sticky="w")

label_c = tk.Label(root, text="第三边:")
label_c.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# 输入框
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# 创建样式并设置圆角按钮
style = ttk.Style()
style.configure("RoundedButton.TButton",
                relief="flat",
                padding=10,
                foreground="#1D1D1F",
                # font=("PingFang SC", 10, "bold"),  # 字体在第 64 行设置
                borderwidth=1,
                focusthickness=3,
                focuscolor="#0071E3")

# 计算勾股定理按钮
button_calculate = ttk.Button(root, text="勾股一下第三边", command=calculate_pythagoras, style="RoundedButton.TButton")
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# 判断是否为三角形按钮
button_check = ttk.Button(root, text="判断三角形", command=check_triangle, style="RoundedButton.TButton")
button_check.grid(row=4, column=0, columnspan=2, pady=10)

# 配置行和列的权重，让控件自适应窗口大小
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

# ---------------------------------------------------------------
# 其他内容
# Other Content
# ---------------------------------------------------------------

# 运行GUI
root.mainloop()
