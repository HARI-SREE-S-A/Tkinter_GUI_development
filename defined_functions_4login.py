def on_enter(e):
    name = user.delete(0,'end')
def on_exit(e):
    name = user.get()
    if name == "":
        user.insert(0,'Username')
def pass_enter(e):
    code.delete(0,'end')
def pass_exit(e):
    name = code.get()
    if name == "":
        code.insert(0,'Password')
def signin():
    username = user.get()
    password = code.get()
    if username == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("successful Login")
        screen.geometry('925x500+300+200')
        screen.config(bg = 'green')
        Label(screen,text = "Logged in Successfully",bg = 'blue',font = ('Calibri(Body)',50,'bold')).pack(expand = True)
        screen.mainloop()
    elif username != 'admin' and password != '1234':
        messagebox.showerror("invalid username and password")
    elif username != 'admin':
        messagebox.showerror("invalid username")
    elif password != '1234':
        messagebox.showerror("invalid password")
