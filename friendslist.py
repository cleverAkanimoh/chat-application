import tkinter as tk
import tkinter.ttk as ttk

class FriendsList(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Crush Chat")
        self.geometry('700x500')

        self.canvas=tk.Canvas(self,bg="white")
        self.canvas_frame=tk.Frame(self,canvas)

        self.scrollbar=ttk.scrollbar(self,orient="vertical",
                                     command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.LEFT,fill=tk.Y)
        self.canvas.pack(side=tk.LEFT,expand=1,fill=tk.BOTH)

        self.friends_area=self.canvas.create_window((0,0),
                            window=self.canvas_frame,anchor="nw")

        self.bind_events()

        self.load_friends()

def bind_events(self):
    self.bind('<Configure>',self.on_frame_resized)

def on_frame_resized(self,event=None):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

def load_friends(self):
    friend_frame=ttk.Frame(self.canvas_frame)

    profile_photo=tk.PhotoImage(file="images/avatar.png")
    profile_photo_label=ttk.Label(friend_frame,image=profile_photo)
    profile_photo_label.image=profile_photo

    friend_name=ttk.Label(friend_frame,text="Adonis Abia",
                          anchor=tk.W)

    message_button=ttk.Button(friend_frame,text="Chat",
                              command=self.open_chat_window)

    profile_photo_label.pack(side=tk.LEFT)
    friend_name.pack(side=tk.LEFT)
    message_button.pack(side=tk.RIGHT)

    friend_frame.pack(fill=tk.X,expand=1)

def bind_events(self):
    ...
    self.canvas.bind('<Configure>',self.friends_width)

def friends_width(self,event):
    canvas_width=event.width
    self.canvas.itemconfig(self.friend_area,width=canvas_width)

def __init__(self,**kwargs):
    ...
    self.menu=tk.Menu(self, bg="lightgrey",fg='black',tearoff=0)
    self.friends_menu=tk.Menu(self.menu,fg='black',bg='lightgrey',
                              tearoff=0)
    self.friends_menu.add_command(label="Add Friend",
                                  command=self.add_friend)
    self.menu.add_cascade(label="Friends", menu=self.friends_menu)

    self.configure(menu=self.menu)

def add_friends(self):
    self.load_friends()

from chatwindow import ChatWindow

...

def open_chat_window(self):
    cw=ChatWindow(self, 'Adonis Abia', 'images/avatar.png')
