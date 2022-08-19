from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("Groceries Bill Generator")
        bg_color="SlateBlue"
        title=Label(self.root,text="Groceries Bill Generator",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=====================variable ==============================
        #================Cosmetics Frames=======================
        self.soap=IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        #===================== GROCERYS =============================

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.wheat = IntVar()

        #===============================COLD DRINKS=======================================

        self.mirinda = IntVar()
        self.maza = IntVar()
        self.cococola = IntVar()
        self.sprite = IntVar()
        self.red_bull = IntVar()
        self.rio = IntVar()

        #===================== TOTAL PRODUCT PRICE & TAX VARIABLE ===========================

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosematic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #======================================== CUSTOMER ==============================================
        self.c_name = StringVar()
        self.c_phon = StringVar()

        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        #===================================Customer Detail Frame=====================================================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="#00ff40",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No", bg=bg_color, fg="black", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="black", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #========================================= Cosmetics Frames ==============================================================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="#00ff40",bg=bg_color)
        F2.place(x=5,y=180,width=345,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_Cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        Face_Cream_txt = Entry(F2, width=10, textvariable=self.face_cream,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)
        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10, textvariable=self.face_wash,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Bath Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10, textvariable=self.spray,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gell,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.loshan,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        #================================= Grocery Frames ============================================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocerys", font=("times new roman", 15, "bold"),
                        fg="#00ff40", bg=bg_color)
        F3.place(x=362, y=180, width=345, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oils", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="yellow").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)
        g3_lbl = Label(F3, text="Daals", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="yellow").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.daal,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        g4_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="yellow").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.sugar,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        g5_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="yellow").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.tea,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        g6_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="yellow").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.wheat,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        #================================= Cold Drinks Frames ===========================================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg="#00ff40", bg=bg_color)
        F4.place(x=715, y=180, width=345, height=380)

        c1_lbl = Label(F4, text="Mirinda", font=("times new roman", 16, "bold"), bg=bg_color, fg="yellow").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.mirinda,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        c2_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="yellow").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.maza,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)
        c3_lbl = Label(F4, text="Cocacola", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="yellow").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.cococola,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        c4_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="yellow").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.sprite,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        c5_lbl = Label(F4, text="Red Bull", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="yellow").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.red_bull,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        c6_lbl = Label(F4, text="Rio", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="yellow").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.rio,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)


        #========================================= BILL AREA ==============================================

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1085, y=180, width=350, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 18 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #====================================== BUTTON FRAME ================================================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="#00ff40", bg=bg_color)
        F6.place(x=0, y=560, relwidth=325, height=230)
        m1_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="black",font=("times new roman", 14, "bold")).grid(row=0,column=0,padx=20,pady=2,sticky="w")
        m1_lbl=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="black",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=2, sticky="w")
        m2_lbl = Entry(F6, width=18, textvariable=self.grocery_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=2)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="black",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=2, sticky="w")
        m3_lbl = Entry(F6, width=18, textvariable=self.cold_drink_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=2)

        #===================================================================================================
        c1_lbl = Label(F6, text="Cosmetics Tax", bg=bg_color, fg="black",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=2, sticky="w")
        c1_lbl = Entry(F6, width=18, font="arial 10 bold", textvariable=self.cosematic_tax,bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=2)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="black",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=2, sticky="w")
        c2_lbl = Entry(F6, width=18, font="arial 10 bold", textvariable=self.grocery_tax,bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=2)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="black",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=2, sticky="w")
        c3_lbl = Entry(F6, width=18, textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=2)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=760,width=680,height=185)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="#ff6666",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F,command=self.bill_area,text="Generate Bill",bg="#20b2aa", fg="white", bd=2, pady=15, width=11,
                           font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="#5fc672", fg="white", bd=2, pady=15, width=11,
                           font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app,bg="#f93949", fg="white", bd=2, pady=15, width=11,
                           font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get() * 120
        self.c_fw_p=self.face_wash.get() * 70
        self.c_hs_p=self.spray.get() * 180
        self.c_hg_p=self.gell.get() * 50
        self.c_bl_p=self.loshan.get() * 60
        self.total_cosmetic_price= float(
                                     self.c_s_p+
                                     self.c_fc_p+
                                     self.c_fw_p+
                                     self.c_hs_p+
                                     self.c_hg_p+
                                     self.c_bl_p
                                     )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosematic_tax.set("Rs."+str(self.c_tax))

        self.g_r_p=self.rice.get() * 80
        self.g_f_p=self.food_oil.get() * 160
        self.g_d_p=self.daal.get() * 120
        self.g_s_p=self.sugar.get() * 40
        self.g_t_p=self.tea.get() * 80
        self.g_w_p=self.wheat.get() * 60

        self.total_grocery_price = float(
                                      self.g_r_p+
                                      self.g_f_p+
                                      self.g_d_p+
                                      self.g_s_p+
                                      self.g_t_p+
                                      self.g_w_p
                                     )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.05),2)
        self.grocery_tax.set("Rs." + str(self.g_tax))

        self.d_mi_p=self.mirinda.get() * 90
        self.d_m_p=self.maza.get() * 85
        self.d_c_p=self.cococola.get() * 80
        self.d_s_p=self.sprite.get() * 90
        self.d_rb_p=self.red_bull.get() * 80
        self.d_r_p=self.rio.get() * 35

        self.total_drink_price = float(
                                      self.d_mi_p+
                                      self.d_m_p+
                                      self.d_c_p+
                                      self.d_s_p+
                                      self.d_rb_p+
                                      self.d_r_p
                                     )
        self.cold_drink_price.set("Rs. "+str(self.total_drink_price))
        self.cd_tax=round((self.total_drink_price * 0.05),2)
        self.cold_drink_tax.set("Rs." + str(self.cd_tax))

        self.Total_bill=float(
                                      self.total_cosmetic_price+
                                      self.total_grocery_price+
                                      self.total_drink_price+
                                      self.c_tax+
                                      self.g_tax+
                                      self.cd_tax
                             )


    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Renu Retail")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n=====================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n=====================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product purchased")
        else:
            self.welcome_bill()
            #================================ COSMETICS =======================================
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get() != 0:
                self.txtarea.insert(END, f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")

            #================================= GROCERY ===========================================
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food oils\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daals\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            #================================ COLD DRINKS ==========================================
            if self.mirinda.get() != 0:
                self.txtarea.insert(END, f"\n Mirinda\t\t{self.mirinda.get()}\t\t{self.d_mi_p}")
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.cococola.get() != 0:
                self.txtarea.insert(END, f"\n Cocacola\t\t{self.cococola.get()}\t\t{self.d_c_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.red_bull.get() != 0:
                self.txtarea.insert(END, f"\n Red Bull\t\t{self.red_bull.get()}\t\t{self.d_rb_p}")
            if self.rio.get() != 0:
                self.txtarea.insert(END, f"\n Rio\t\t{self.rio.get()}\t\t{self.d_r_p}")

            self.txtarea.insert(END, f"\n-------------------------------------")
            if self.cosematic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t{self.cosematic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\nTotal Bill : \t\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n-------------------------------------")

            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Custbills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully!")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("Custbills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Custbills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to clear?")
        if op > 0:
            # ================Cosmetics Frames=======================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

            # ===================== GROCERYS =============================

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.wheat.set(0)

            # ===============================COLD DRINKS=======================================

            self.mirinda.set(0)
            self.maza.set(0)
            self.cococola.set(0)
            self.sprite.set(0)
            self.red_bull.set(0)
            self.rio.set(0)

            # ===================== TOTAL PRODUCT PRICE & TAX VARIABLE ===========================

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosematic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ======================================== CUSTOMER ==============================================
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
root = Tk()
obj = Bill_App(root)
root.mainloop()