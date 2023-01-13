def signup():
    def on_enter(e):
        name = username.delete(0,'end')
    def on_exit(e):
        name = username.get()
        if name == "":
            username.insert(0,"username")
    def on_penter(e):
        name = password.delete(0,'end')
    def on_pexit(e):
        name = password.get()
        if name == "":
            password.insert(0,'Password')
    def on_center(e):
        name = password_confirm.delete(0,'end')
    def on_cexit(e):
        name = password_confirm.get()
        if name == "":
            password_confirm.insert(0,"confirm")
    def save_data():
        userrname = username.get()
        passsword = password.get()
        passsword_confirm = password_confirm.get()
        if userrname == "" or password == "":
            messagebox.showerror(title = "error",message = "username and password cannot be blank ")
        elif passsword != passsword_confirm:
            messagebox.showerror(message = "password mismatch")
        elif passsword == passsword_confirm:
            
            
            try:
                file = open('datasheet.txt','r+')
                d = file.read()
                r = ast.literal_eval(d)
                
                dict2 = {userrname:passsword}
                r.update(dict2)
                file.truncate(0)
                file.close()
                
                file=open('datasheet.txt','w')
                w = file.write(str(r))
                
                messagebox.showinfo(message = " signed up succesfully")
            except:
                file=open('datasheet.txt','w')
                pp = str({'username':'password'})
                file.write(pp)
                file.close()
