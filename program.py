#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Oct 31, 2021 06:38:25 PM +03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import program_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    program_support.set_Tk_var()
    top = Toplevel1 (root)
    program_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    program_support.set_Tk_var()
    top = Toplevel1 (w)
    program_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x449+660+211")
        top.minsize(120, 1)
        top.maxsize(3364, 1063)
        top.resizable(1,  1)
        top.title("Twitch Rezilliği")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.333, rely=0.111, height=71, width=194)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Twitch yayıncısının ID'sini buraya girin''')
        self.Label1.configure(wraplength="98")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.317, rely=0.267, height=30, relwidth=0.357)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=program_support.id)

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.383, rely=0.532, height=54, width=137)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#74f471")
        self.Button1_1.configure(command=lambda :program_support.runCode())
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Çalıştır''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.133, rely=0.78, height=61, width=424)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text='''Programı all_revenues klasörü altında çalıştırmanız gerekli. İstediğiniz yayıncının ID'sini yazıp Tanımla tuşuna bastıktan sonra Çalıştır tuşuna basarak yayıncının Excel'ini alabilirsiniz.''')
        self.Label2.configure(wraplength="400")

if __name__ == '__main__':
    vp_start_gui()





