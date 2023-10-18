from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")

# 1st image
        img1=Image.open(r"C:\Users\stude\OneDrive\Desktop\project\Image-Processing-Project\project-images\56.jpg")#insert a image
        img1=img1.resize((455,100))#resize((530,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=455,height=100)

 # 2nd image
        img2=Image.open(r"C:\Users\stude\OneDrive\Desktop\project\Image-Processing-Project\project-images\58.jpg")#insert a image
        img2=img2.resize((455,100))#resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=455,y=0,width=455,height=100)        

 # 3rd image
        img3=Image.open(r"C:\Users\stude\OneDrive\Desktop\project\Image-Processing-Project\project-images\57.jpg")#insert a image
        img3=img3.resize((455,100))#resize((530,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=910,y=0,width=455,height=100)   

# bg image
        img4=Image.open(r"C:\Users\stude\OneDrive\Desktop\project\Image-Processing-Project\project-images\bg5.webp")#insert a image
        img4=img4.resize((1366,768))#resize((530,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=100,width=1366,height=668)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=45,width=1336,height=530)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Left_frame.place(x=10,y=10,width=650,height=500)

        img_left=Image.open(r"C:\Users\stude\OneDrive\Desktop\project\Image-Processing-Project\project-images\70.jpg")#insert a image
        img_left=img_left.resize((630,100))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=630,height=100) 

 #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information")
        current_course_frame.place(x=10,y=100,width=630,height=120)


#department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=16)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#course
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=16)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#Year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=16)
        year_combo["values"]=("Select Year","2020-21","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=16)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
#class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information")
        class_student_frame.place(x=10,y=220,width=630,height=260)

#student ID
        studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

#student name

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

#class division
        
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#roll no
        Roll_label=Label(class_student_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=1,column=2,padx=10,sticky=W)

        Roll_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        Roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
 
 #DOB
        dob_label=Label(class_student_frame,text="D.O.B:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

#phone no
        Phone_no_label=Label(class_student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        Phone_no_label.grid(row=2,column=2,padx=10,sticky=W)

        Phone_no_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        Phone_no_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

#teacher name 
        teacher_name_label=Label(class_student_frame,text="Teacher's Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_name_label.grid(row=3,column=2,padx=10,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,width=16,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

 #radio Buttonuttons
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0) 

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=5,column=1) 

#buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=625,height=37)
       
        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update=Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=1)

        delete=Button(btn_frame,text="Delete",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete.grid(row=0,column=2)

        reset=Button(btn_frame,text="Reset",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=3)

#2nd button 
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=625,height=37)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo=Button(btn_frame1,text="Update Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo.grid(row=1,column=1)


#right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Right_frame.place(x=670,y=10,width=650,height=500)


        img_right=Image.open(r"C:\Users\stude\OneDrive\Desktop\project\Image-Processing-Project\project-images\70.jpg")#insert a image
        img_right=img_right.resize((630,100))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=630,height=100) 
 
  #========Search System===============
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=10,y=105,width=630,height=65)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=14)
        search_combo["values"]=("Select","Roll_NO","Phone_NO")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=13,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(Search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)


#========table frame=====
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=180,width=630,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department",)
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSamplestatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=80)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=80)
        self.student_table.column("sem",width=80)
        self.student_table.column("id",width=80)
        self.student_table.column("name",width=80)
        self.student_table.column("div",width=80)
        self.student_table.column("roll",width=80)
        self.student_table.column("gender",width=80)
        self.student_table.column("dob",width=80)
        self.student_table.column("email",width=80)
        self.student_table.column("phone",width=80)
        self.student_table.column("address",width=80)
        self.student_table.column("teacher",width=80)
        self.student_table.column("photo",width=80)

        self.student_table.pack(fill=BOTH,expand=1)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

