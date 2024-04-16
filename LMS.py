from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")



        # =============================Variable============================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1430,height=350)


        # ==========================DataFrameLeft==============================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type :",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")  
        comMember["value"]=("Admin staf","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO :",font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID NO :",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName :",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName :",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1 :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2 :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code :",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile :",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id :",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title :",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",13,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine :",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",13,"bold"),width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price :",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

        # =================================DataFrameRight==================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,
                                                                                font=("times new roman",12,"bold"))
        DataFrameRight.place(x=810,y=5,width=500,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBoooks=['Head First Book','Learn Python The Hard Way','Python Programming','Secrete Rahshu','Python CookBook','Intro to Machine Learning','Java Programming','Aptitude Reasoning'
        'Machine Techno','My Python','Joss Ellif Guru','Elite Jungle Python','Advance Python','Intro to Programming','Intro to Sql','DBMS','MySql','Advance Java','Artificial Intelligence']

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Mohan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.799")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID1235")
                self.booktitle_var.set("basic of python")
                self.author_var.set("Sravan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.999")

            elif (x=="Python Programming"):
                self.bookid_var.set("BKID1236")
                self.booktitle_var.set("Intro to python")
                self.author_var.set("Venkat")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.899")

            elif (x=="Secrete Rahshu"):
                self.bookid_var.set("BKID1237")
                self.booktitle_var.set("python")
                self.author_var.set("Chetan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.599")

            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID1238")
                self.booktitle_var.set("python cookbook")
                self.author_var.set("sujan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.799")

            elif (x=="Intro to Machine Learning"):
                self.bookid_var.set("BKID1239")
                self.booktitle_var.set("Basic of ML")
                self.author_var.set("Ashok")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.759")

            elif (x=="Java Programming"):
                self.bookid_var.set("BKID1240")
                self.booktitle_var.set("Java")
                self.author_var.set("Ramesh Babu")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1099")

            elif (x=="Aptitude Reasoning"):
                self.bookid_var.set("BKID1241")
                self.booktitle_var.set("Aptitude")
                self.author_var.set("Naik")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.999")

            elif (x=="Machine Techno"):
                self.bookid_var.set("BKID1242")
                self.booktitle_var.set("Machine")
                self.author_var.set("Shivanand")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.789")

            elif (x=="My Python"):
                self.bookid_var.set("BKID1243")
                self.booktitle_var.set("Python")
                self.author_var.set("Rakesh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.659")

            elif (x=="Joss Ellif Guru"):
                self.bookid_var.set("BKID1244")
                self.booktitle_var.set("Guru")
                self.author_var.set("Zoe")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.559")

            elif (x=="Elite Jungle Python"):
                self.bookid_var.set("BKID1245")
                self.booktitle_var.set("Jungle")
                self.author_var.set("Suresh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.679")

            elif (x=="Advance Python"):
                self.bookid_var.set("BKID1246")
                self.booktitle_var.set("Advance")
                self.author_var.set("Veeresh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.779")

            elif (x=="Intro to Programming"):
                self.bookid_var.set("BKID1247")
                self.booktitle_var.set("Programming")
                self.author_var.set("Naresh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.879")

            elif (x=="Intro to Sql"):
                self.bookid_var.set("BKID1248")
                self.booktitle_var.set("sql")
                self.author_var.set("Shashidhar")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.777")

            elif (x=="DBMS"):
                self.bookid_var.set("BKID1249")
                self.booktitle_var.set("dbms")
                self.author_var.set("Abdulla")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.799")

            elif (x=="MySql"):
                self.bookid_var.set("BKID1250")
                self.booktitle_var.set("mysql")
                self.author_var.set("Shiva")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.877")

            elif (x=="Advance Java"):
                self.bookid_var.set("BKID1251")
                self.booktitle_var.set("java")
                self.author_var.set("Prabhakar")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.987")

            elif (x=="Artificial Intelligence"):
                self.bookid_var.set("BKID1252")
                self.booktitle_var.set("AI")
                self.author_var.set("Ganesh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.897")




        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=18,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END,item)
      
        # ====================================Buttons Frame=====================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=490,width=1530,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text='Add Data',font=("arial",12,"bold"),width=20,bg="white",fg="Black")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text='Show Data',font=("arial",12,"bold"),width=20,bg="white",fg="Black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text='Update',font=("arial",12,"bold"),width=20,bg="white",fg="Black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text='Delete',font=("arial",12,"bold"),width=20,bg="white",fg="Black")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text='Reset',font=("arial",12,"bold"),width=20,bg="white",fg="Black")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text='Exit',font=("arial",12,"bold"),width=20,bg="white",fg="Black")
        btnAddData.grid(row=0,column=5)

        # ====================================Information Frame=====================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=540,width=1350,height=150)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1400,height=140)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=80)
        self.library_table.column("prnno",width=80)
        self.library_table.column("title",width=80)
        self.library_table.column("firstname",width=80)
        self.library_table.column("lastname",width=80)
        self.library_table.column("address1",width=80)
        self.library_table.column("address2",width=80)
        self.library_table.column("postid",width=80)
        self.library_table.column("mobile",width=80)
        self.library_table.column("bookid",width=80)
        self.library_table.column("booktitle",width=80)
        self.library_table.column("author",width=80)
        self.library_table.column("dateborrowed",width=80)
        self.library_table.column("datedue",width=80)
        self.library_table.column("days",width=80)
        self.library_table.column("latereturnfine",width=80)
        self.library_table.column("dateoverdue",width=80)
        self.library_table.column("finalprice",width=80)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mohan@123",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.member_var.get(),
                                                                                                    self.prn_var.get(),
                                                                                                    self.id_var.get(),
                                                                                                    self.firstname_var.get(),
                                                                                                    self.lastname_var.get(),
                                                                                                    self.address1_var.get(),
                                                                                                    self.address2_var.get(),
                                                                                                    self.postcode_var.get(),
                                                                                                    self.mobile_var.get(),
                                                                                                    self.bookid_var.get(),
                                                                                                    self.booktitle_var.get(),
                                                                                                    self.author_var.get(),
                                                                                                    self.dateborrowed_var.get(),
                                                                                                    self.datedue_var.get(),
                                                                                                    self.daysonbook_var.get(),
                                                                                                    self.latereturnfine_var.get(),
                                                                                                    self.dateoverdue_var.get(),
                                                                                                    self.finalprice_var.get(),
                                                                                                    ))
        conn.commit()
        self.fatch_data()
        conn.close()      

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mohan@123",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,BookTitle=%s,Author=%s,Dateborrowed=%s,Datedue=%s,DaysonBook=%s,latereturnfine=%s,Dateoverdue=%s,Finalprice=%s where PRN_No=%s",(
                                                                                                    self.member_var.get(),
                                                                                                    self.id_var.get(),
                                                                                                    self.firstname_var.get(),
                                                                                                    self.lastname_var.get(),
                                                                                                    self.address1_var.get(),
                                                                                                    self.address2_var.get(),
                                                                                                    self.postcode_var.get(),
                                                                                                    self.mobile_var.get(),
                                                                                                    self.bookid_var.get(),
                                                                                                    self.booktitle_var.get(),
                                                                                                    self.author_var.get(),
                                                                                                    self.dateborrowed_var.get(),
                                                                                                    self.datedue_var.get(),
                                                                                                    self.daysonbook_var.get(),
                                                                                                    self.latereturnfine_var.get(),
                                                                                                    self.dateoverdue_var.get(),
                                                                                                    self.finalprice_var.get(),
                                                                                                    self.prn_var.get(),
                                                                                ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mohan@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do You Want to Exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mohan@123",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")

    

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()                