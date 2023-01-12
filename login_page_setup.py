root = Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg = '#fff')
root.resizable(False,False)
img = PhotoImage(file = 'C:\Anaconda3\login.png')
Label(root,image=img,bg='#57a1f8').place(x = 20,y = 20)

frame = Frame(root,width = 600,height = 60050,bg = 'black')
frame.place(x = 450,y = 70)

heading = Label(frame,text='Sign In',fg = '#57a1f8',bg = 'black',font=('Microsoft YaHei VI Light',23,'bold'))
heading.place(x = 100,y = 5)





user  =Entry(frame,width = 25,fg = 'white',border = 5,bg = 'black',font = ('Microsoft YaHei VI Light',14))
user.place(x = 30,y = 80)
user.insert(0,'UserName')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_exit)


Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 107)






code = Entry(frame,width = 25,fg = 'white',border = 5,bg = 'black',font = ('Microsoft YaHei VI Light',14),show = '.')
code.place(x = 30,y = 150)
code.insert(0,'Password')
code.bind('<FocusIn>',pass_enter)
code.bind('<FocusOut>',pass_exit)



Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 177)





Button(frame,width = 39,pady = 7,text = 'Login',bg ='#57a1f8',fg = 'white',border = 0,cursor = 'hand2',command = signin ).place(x = 35,y = 204)
label = Label(frame,text = "Dont have an account?",fg = 'white',bg ='black',font = ('Microsoft YaHei VI Light',9) ).place(x = 75,y = 270)








root.mainloop()
