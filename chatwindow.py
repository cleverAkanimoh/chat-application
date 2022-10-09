import tkinter as tk
import tkinter.ttk as ttk

class ChatWindow(tk.Toplevel):
    def __init__(self, master, friend_name, friend_avatar, **kwargs):
        super().__init__(**kwargs)
        
        self.master = master
        self.title(friend_name)
        self.geometry('540x640')
        
        self.minsize(540, 640)
        self.right_frame = tk.Frame(self)
        self.left_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self.left_frame) 