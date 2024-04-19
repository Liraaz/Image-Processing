from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk         # pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_chek = IntVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(r"project-images\7.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        self.bg1 = ImageTk.PhotoImage(r"project-images\7.png")
        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkblue", bg="white")
        register_lbl.place(x=20, y=20)  # x=285,y=20 is middle

        # Label & Entry
        # Row 1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # Row 2
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # Row 3
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Bestfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # Row 4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, show="*", textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, show="*", textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # Check Button
        checkbutton = Checkbutton(frame, variable=self.var_chek, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"),activeforeground="white", activebackground="grey", onvalue=1, offvalue=0)
        checkbutton.place(x=50, y=390)  # x=285,y=20 is middle

        # Register Now Button
        register_btn = Button(frame, command=self.register_data, text="Register Now", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="darkblue", activeforeground="white", activebackground="blue")
        register_btn.place(x=50, y=430, width=200)

        # Login Button
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="darkblue", activeforeground="white", activebackground="blue")
        login_btn.place(x=370, y=430, width=200)

    # Function Declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same")
        elif self.var_chek.get() == 0:
            messagebox.showerror("Error", "Please agree  our terms & conditions")
        else:
           try:
            conn = mysql.connector.connect(host="localhost", user="root",password="Himadri@124",database="face_recognizer")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row>0:
                messagebox.showerror("Error", "This email already exists. Please try another email")
            else:
                my_cursor.execute("Insert Into Register Values (%s, %s, %s, %s, %s, %s, %s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                            self.var_pass.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Successful", "Registration successful")
           except Exception as es:
                messagebox.showerror("Error", f"Error during registration: {str(es)}")
            

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
