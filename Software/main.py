from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import random,os
from tkinter import messagebox
import tempfile 
from time import strftime


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Billing software")

        # ===============Variables============================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Product Categories list
        self.Category=["Select Option","Clothing","Lifestyle","Mobiles"]
        
        # SubCatClothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","HRX","Clavin","Spykar","Roadster"]
        self.price_levis=5000
        self.price_hrx=3000
        self.price_clavin=1000
        self.price_spykar=4000
        self.price_roadster=1500

        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_Polo=1800
        self.price_Roadster=2100
        self.price_JackJones=1700

        self.Shirt=['Peter England','Louis Phillips','Park Avenue']
        self.price_Peter=2500
        self.price_Louis=2700
        self.price_Park=1740

        # SubCatLifstyle
        self.SubCatLifstyle=["Bath Soap","Face Creame","Hair Oil"]
        self.Bath_soap=['LifeBuy','Lux','Santoor','Pearl']
        self.price_life=25
        self.price_lux=20
        self.price_santoor=28
        self.price_pearl=30

        self.Face_creame=['Fair&Lovely','Ponds','Olay','Garnier']
        self.price_fair=25
        self.price_ponds=40
        self.price_olay=20
        self.price_garnier=35

        self.Hair_oil=['Paractute','Jashmin','Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30

        # SubCatMobiles
        self.SubCatMobiles=['Iphone','Samsung','Xiome','RealMe','Oneplus+']
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_ix=70000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_Sm16=16000
        self.price_Sm12=12000
        self.price_Sm21=18000

        self.Xiome=['Red11','Redme-12','RedmePro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=19000

        self.RealMe=['RealMe 12','RealMe 13','RealMe Pro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.Oneplus=['Oneplus1','Oneplus2','Oneplus3']
        self.price_one1=45000
        self.price_one2=48500
        self.price_one3=65000


        #Image1
        img=Image.open("image/b1.jpg")
        img=img.resize((200,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=200,height=130)

        #Image2
        img_1=Image.open("image/girls.jpg")
        img_1=img_1.resize((600,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=200,y=0,width=600,height=130)

        #Image3
        img_2=Image.open("image/girl1.jpg")
        img_2=img_2.resize((600,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=800,y=0,width=600,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="black",fg="white")
        lbl_title.place(x=0,y=130,width=1366,height=45)

        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font = ('times new roman',20,'bold'),background = 'black',foreground = 'red')
        lbl.place(x=0,y=0,width=180,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1366,height=620)

        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=0,width=300,height=125)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('times new roman',12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.textCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('times new roman',10,'bold'),width=20)
        self.textCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('times new roman',12,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.textEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('times new roman',10,'bold'),width=20)
        self.textEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=320,y=0,width=620,height=125)

        # Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state='readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        # SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,stick=W,padx=5,pady=2)

        # Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)

        # Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=9,y=130,width=930,height=280)

        #Image4
        img_12=Image.open("image/good.jpg")
        img_12=img_12.resize((930,300),Image.ANTIALIAS)
        self.photoimg_12=ImageTk.PhotoImage(img_12)

        lbl_img_12=Label(MiddleFrame,image=self.photoimg_12)
        lbl_img_12.place(x=0,y=0,width=910,height=265)

        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=950,y=1,width=2000,height=40)


        self.lblBill=Label(Search_Frame,font=('arial',11,'bold'),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=18)
        self.txt_Entry_Search.grid(row=0,column=1,stick=W,padx=2)


        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)



        # RigthFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=950,y=32,width=400,height=379)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="black",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=410,width=1366,height=120)

        self.lblSubTotal=Label(Bottom_Frame,font=('times new roman',11,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('times new roman',11,'bold'),width=22)
        self.EntrySubTotal.grid(row=0,column=1,stick=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,font=('times new roman',11,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('times new roman',11,'bold'),width=22)
        self.txt_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=('times new roman',11,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('times new roman',11,'bold'),width=22)
        self.txtAmountTotal.grid(row=2,column=1,stick=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        
        self.l=[]
    #=====================Function Declartion=========================     
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome To Super Market")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Number:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n=========================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n=========================================\n")

       
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=========================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=========================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to Save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()
 
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f'bills/{i}','r')
                    self.textarea.delete(1.0,END)
                    for d in f1:
                        self.textarea.insert(END,d)
                    f1.close()
                    found="yes"
        if found=='no':
                messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()

    def Categories(self,event=""):
            if self.Combo_Category.get()=="Clothing":
                self.ComboSubCategory.config(value=self.SubCatClothing)
                self.ComboSubCategory.current(0)
            
            if self.Combo_Category.get()=="Lifestyle":
                self.ComboSubCategory.config(value=self.SubCatLifstyle)
                self.ComboSubCategory.current(0)
            
            if self.Combo_Category.get()=="Mobiles":
                self.ComboSubCategory.config(value=self.SubCatMobiles)
                self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
            if self.ComboSubCategory.get()=="Pant":
                self.ComboProduct.config(value=self.pant)
                self.ComboProduct.current(0)
            
            if self.ComboSubCategory.get()=="T-Shirt":
                self.ComboProduct.config(value=self.T_shirt)
                self.ComboProduct.current(0)
            
            if self.ComboSubCategory.get()=="Shirt":
                self.ComboProduct.config(value=self.Shirt)
                self.ComboProduct.current(0)

            # LifeStyle
            if self.ComboSubCategory.get()=="Bath Soap":
                self.ComboProduct.config(value=self.Bath_soap)
                self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Face Creame":
                self.ComboProduct.config(value=self.Face_creame)
                self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Hair Oil":
                self.ComboProduct.config(value=self.Hair_oil)
                self.ComboProduct.current(0)

            # Mobile
            if self.ComboSubCategory.get()=="Iphone":
                self.ComboProduct.config(value=self.Iphone)
                self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Samsung":
                self.ComboProduct.config(value=self.Samsung)
                self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Xiome":
                self.ComboProduct.config(value=self.Xiome)
                self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="RealMe":
                self.ComboProduct.config(value=self.RealMe)
                self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Oneplus+":
                self.ComboProduct.config(value=self.Oneplus)
                self.ComboProduct.current(0)

    def price(self,event=""):
            # Pant
            if self.ComboProduct.get()=="Levis":
                self.ComboPrice.config(value=self.price_levis)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="HRX":
                self.ComboPrice.config(value=self.price_hrx)
                self.ComboPrice.current(0)
                self.qty.set(1) 

            if self.ComboProduct.get()=="Clavin":
                self.ComboPrice.config(value=self.price_clavin)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Spykar":
                self.ComboPrice.config(value=self.price_spykar)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Roadster":
                self.ComboPrice.config(value=self.price_roadster)
                self.ComboPrice.current(0)
                self.qty.set(1)

            # T-Shirt
            if self.ComboProduct.get()=="Polo":
                self.ComboPrice.config(value=self.price_Polo)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Roadster":
                self.ComboPrice.config(value=self.price_Roadster)
                self.ComboPrice.current(0)
                self.qty.set(1) 

            if self.ComboProduct.get()=="Jack&Jones":
                self.ComboPrice.config(value=self.price_JackJones)
                self.ComboPrice.current(0)
                self.qty.set(1)

            # Shirt
            if self.ComboProduct.get()=="Peter England":
                self.ComboPrice.config(value=self.price_Peter)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Louis Phillips":
                self.ComboPrice.config(value=self.price_Louis)
                self.ComboPrice.current(0)
                self.qty.set(1) 

            if self.ComboProduct.get()=="Park Avenue":
                self.ComboPrice.config(value=self.price_Park)
                self.ComboPrice.current(0)
                self.qty.set(1)

            # Bath Soap
            if self.ComboProduct.get()=="LifeBuy":
                self.ComboPrice.config(value=self.price_life)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Lux":
                self.ComboPrice.config(value=self.price_lux)
                self.ComboPrice.current(0)
                self.qty.set(1) 

            if self.ComboProduct.get()=="Santoor":
                self.ComboPrice.config(value=self.price_santoor)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Pearl":
                self.ComboPrice.config(value=self.price_pearl)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Fair&Lovely":
                self.ComboPrice.config(value=self.price_fair)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Ponds":
                self.ComboPrice.config(value=self.price_ponds)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Olay":
                self.ComboPrice.config(value=self.price_olay)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Garnier":
                self.ComboPrice.config(value=self.price_garnier)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Parachute":
                self.ComboPrice.config(value=self.price_para)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Jashmin":
                self.ComboPrice.config(value=self.price_jashmin)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Bajaj":
                self.ComboPrice.config(value=self.price_bajaj)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Iphone_X":
                self.ComboPrice.config(value=self.price_ix)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Iphone_11":
                self.ComboPrice.config(value=self.price_i11)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Iphone_12":
                self.ComboPrice.config(value=self.price_i12)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Samsung M16":
                self.ComboPrice.config(value=self.price_Sm16)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Samsung M12":
                self.ComboPrice.config(value=self.price_Sm12)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Samsung M21":
                self.ComboPrice.config(value=self.price_Sm21)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Red11":
                self.ComboPrice.config(value=self.price_r11)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Redme-12":
                self.ComboPrice.config(value=self.price_r12)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="RedmePro":
                self.ComboPrice.config(value=self.price_rpro)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="RealMe 12":
                self.ComboPrice.config(value=self.price_rel12)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="RealMe 13":
                self.ComboPrice.config(value=self.price_rel13)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="RealMe Pro":
                self.ComboPrice.config(value=self.price_relpro)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Oneplus1":
                self.ComboPrice.config(value=self.price_one1)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Oneplus2":
                self.ComboPrice.config(value=self.price_one2)
                self.ComboPrice.current(0)
                self.qty.set(1)

            if self.ComboProduct.get()=="Oneplus3":
                self.ComboPrice.config(value=self.price_one3)
                self.ComboPrice.current(0)
                self.qty.set(1)








if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()