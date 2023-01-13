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
