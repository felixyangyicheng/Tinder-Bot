import tkinter as tk
import TinderBot




root=tk.Tk()

HEIGHT=700
WIDTH=800

def start_function(Login_entry, Password_entry):
    #usernameTinder=Login_entry
    #password=Password_entry
    with open('secrets.py', 'w+') as f:
        f_contents=f.write("usernameTinder="+"'"+Login_entry+"'" "\npassword=" "'"+Password_entry+"'")
    print(f_contents)
    TinderBot.main()

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

Login_frame=tk.Frame(root,bg='#F6445C',bd=5)
Login_frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.2, anchor='n')

Login_frame_label=tk.Label(Login_frame, text="Login") #no effect
Login_frame_label.place(relx=0.1, rely=0.1) #no effect

Login_entry=tk.Entry(Login_frame, font=40)
Login_entry.place(relwidth=0.65, relheight=0.5)


button=tk.Button(Login_frame, text="Login", font=40)  
button.place(relx=0.7, relheight=0.5, relwidth=0.3)  

Password_frame =tk.Frame(root, bg="#F6445C", bd=5)
Password_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.2, anchor='n')

Password_entry=tk.Entry(Password_frame, font=40)
Password_entry.place(relwidth=0.65, relheight=0.5)

Start_button_frame = tk.Frame(root, bg="#F6445C", bd=5)
Start_button_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.1, anchor='n')
Start_button=tk.Button(Start_button_frame, text="Start auto Sweap", font=40, command=lambda: start_function(Login_entry.get(), Password_entry.get()))
Start_button.place(relwidth=0.65, relheight=1)
#button.pack()
root.mainloop()


