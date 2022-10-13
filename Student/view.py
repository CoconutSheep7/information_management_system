import tkinter
from tkinter import *
from tkinter import ttk
from ImageLibrary import *
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import os
import pymysql


class InputFrame(Frame):
    def __init__(self, master=None):
        """
        :param master:
        """
        Frame.__init__(self, master)
        self.root = master
        self.StdNum = StringVar()
        self.StdName = StringVar()
        self.Gender = StringVar()
        self.System = StringVar()
        self.Class = StringVar()
        self.PhoneNumber = StringVar()
        self.createPage()

    def createPage(self):
        """
        :return:
        """
        self.msg()
        tkinter.Button(self,text='XX', command=self.getbutton).grid(row=7, column=1, stick=E, pady=10)

    def getbutton(self):
        """
        :return:
        """
        flag = 0
        stdnum = self.StdNum.get()
        stdname = self.StdName.get()
        gender = self.Gender.get()
        system = self.System.get()
        mclass = self.Class.get()
        phonenumber = self.PhoneNumber.get()
        if len(stdnum) != 10:
            messagebox.showinfo('XX！', 'XXXXX！')
            self.StdNum.set("")
            flag = 1
        if stdname == '' or gender == '' or system == '' or mclass == '' or phonenumber == '' or flag == 0:
            messagebox.showinfo('XX！', 'XXX！')
            flag = 1
        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        sql_select = "SELECT * FROM student WHERE sno = '%s'" % stdnum
        if flag == 0:
            try:
                cursor.execute(sql_select)
                if cursor.fetchall() == ():
                    messagebox.showinfo('XX！', 'XX！')
                    flag = 1
            except:
                db.rollback()
                messagebox.showinfo('XX！', 'XX！')

        if flag == 0:
            sql = "INSERT INTO student (sno, sname, ssex, scollege, sclass, sphone) VALUES ('%s', '%s', '%s', '%s','%s','%s')"\
                  % (stdnum, stdname, gender, system, mclass, phonenumber)
            try:
                cursor.execute(sql)
                db.commit()
                messagebox.showinfo('XX！', 'XX！')
                Library(stdnum, stdname, gender, system, mclass, phonenumber)
            except:
                db.rollback()
                messagebox.showinfo('XX！', 'XX！')
        db.close()

    def msg(self):
        """
        :return:
        """
        Label(self, text='XX: ').grid(row=1, stick=W, pady=10)
        tkinter.Entry(self, textvariable=self.StdNum).grid(row=1, column=1, stick=E)
        Label(self, text='XX: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.StdName).grid(row=2, column=1, stick=E)
        Label(self, text='XX: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.Gender).grid(row=3, column=1, stick=E)
        Label(self, text='XX: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.System).grid(row=4, column=1, stick=E)
        Label(self, text='XX: ').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.Class).grid(row=5, column=1, stick=E)
        Label(self, text='XX: ').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.PhoneNumber).grid(row=6, column=1, stick=E)


class QueryFrame(Frame):
    def __init__(self, master=None):
        """
        :param master:
        """
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.StdNum = StringVar()
        self.StdName = StringVar()
        self.Gender = StringVar()
        self.System = StringVar()
        self.Class = StringVar()
        self.PhoneNumber = StringVar()
        self.createPage()
        self.var = StringVar()
        self.shou_img = ShowImg()

    def createPage(self):
        """
        :return:
        """
        Label(self, text='XX: ').grid(row=1, pady=10)
        tkinter.Entry(self, textvariable=self.itemName).grid(row=1, column=1)
        self.msg()
        tkinter.Button(self, text='XX', command=self.getbutton1).grid(row=2, column=2, pady=10)

    def getbutton1(self):
        """
        :return:
        """
        flag = 1
        sno = self.itemName.get()
        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        sql_select = "SELECT * FROM student WHERE sno = '%s'" % sno
        try:

            cursor.execute(sql_select)
            if cursor.fetchall() == ():
                flag = 0
                messagebox.showinfo('XX！', 'XX！')
        except:
            db.rollback()
            messagebox.showinfo('XX！', 'XX！')
        if flag == 1:
            try:
                sql = "SELECT * FROM student WHERE sno = '%s'" % sno
                cursor.execute(sql)
                results = cursor.fetchall()
                self.show_student(results[0])
                tkinter.Button(self, text='UPDATE', command=self.getbutton2).grid(row=2, column=3, pady=10)
                tkinter.Button(self, text='DELETE', command=self.getbutton3).grid(row=2, column=4, pady=10)
                self.shou_img.show_img(results[0][0])
            except:
                print("Error: unable to fecth data")
                messagebox.showinfo('XX！', 'XX！')
        db.close()

    def getbutton2(self):
        """
        :return:
        """
        stdname = self.StdName.get()
        gender = self.Gender.get()
        system = self.System.get()
        mclass = self.Class.get()
        phonenumber = self.PhoneNumber.get()
        id = self.itemName.get()
        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        sql = "UPDATE student SET sname = '%s', ssex = '%s', scollege = '%s' , sclass = '%s', sphone = '%s'\
                        WHERE sno = '%s'" % (stdname, gender, system, mclass, phonenumber, id)
        try:
            cursor.execute(sql)
            db.commit()
            Library(id, stdname, gender, system, mclass, phonenumber)
            messagebox.showinfo('XX！', 'XX！')
        except:
            db.rollback()
            messagebox.showinfo('XX！', 'XX！')
        db.close()

    def getbutton3(self):
        """
        :return:
        """
        sno = self.itemName.get()
        flag = 1
        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        sql_select = "SELECT * FROM student WHERE sno = '%s'" % sno
        try:

            cursor.execute(sql_select)
            if cursor.fetchall() == ():
                flag = 0
                messagebox.showinfo('XX！', 'XX！')
        except:
            db.rollback()
            messagebox.showinfo('XX！', 'XX！')
        if flag == 1:
            try:
                sql_delete = "DELETE FROM student WHERE sno = '%s'" % sno
                cursor.execute(sql_delete)
                db.commit()
                try:
                    file = "Image_Library\\" + str(sno) + '.png'
                    os.remove(file)
                    messagebox.showinfo('xx！', 'xx！')
                except:
                    messagebox.showinfo('xx！', 'xx,xx！')
            except:
                db.rollback()
                messagebox.showinfo('xx！', 'xx！')
        db.close()
        self.StdName.set("")
        self.Gender.set("")
        self.System.set("")
        self.Class.set("")
        self.PhoneNumber.set("")

    def show_student(self, lst):
        """
        :param lst:
        :return:
        """
        if len(lst) == 0:
            return
        else:
            item = lst
            self.StdName.set(item[1])
            self.Gender.set(item[2])
            self.System.set(item[3])
            self.Class.set(item[4])
            self.PhoneNumber.set(item[5])

    def msg(self):
        """
        :return:
        """
        Label(self, text='xx: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.StdName).grid(row=4, column=1, stick=E)
        Label(self, text='xx: ').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.Gender).grid(row=5, column=1, stick=E)
        Label(self, text='xx: ').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.System).grid(row=6, column=1, stick=E)
        Label(self, text='xx: ').grid(row=7, stick=W, pady=10)
        Entry(self, textvariable=self.Class).grid(row=7, column=1, stick=E)
        Label(self, text='xx: ').grid(row=8, stick=W, pady=10)
        Entry(self, textvariable=self.PhoneNumber).grid(row=8, column=1, stick=E)


class CountFrame(Frame):
    def __init__(self, master=None):
        """
        :param master:
        """
        Frame.__init__(self, master)
        self.frame_center = tkinter.Frame(width=500, height=400)
        self.root = master
        self.show_img = ShowImg()
        self.tableColumns = ("xx", "xx", "xx", "xx", "xx", "xx")
        self.tree = ttk.Treeview(
            self,
            columns=self.tableColumns,
            height=30,
            show='headings',
            style = 'Treeview',
        )
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)
        self.tree.column("xx", width=100, anchor='center')
        self.tree.column("xx", width=100, anchor='center')
        self.tree.column("xx", width=40, anchor='center')
        self.tree.column("xx", width=100, anchor='center')
        self.tree.column("xx", width=100, anchor='center')
        self.tree.column("xx", width=100, anchor='center')
        self.get_tree()
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

    def createPage(self):
        """
        :return:
        """
        Label(self, text='xx').grid(row=0, stick=W, pady=10)

    def get_tree(self):
        """
        :return:
        """
        for _ in map(self.tree.delete, self.tree.get_children("")):
            pass
        self.sno = []
        self.sname = []
        self.sgender = []
        self.scollege = []
        self.sclass = []
        self.sphone = []

        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.sno.append(row[0])
                self.sname.append(row[1])
                self.sgender.append(row[2])
                self.scollege.append(row[3])
                self.sclass.append(row[4])
                self.sphone.append(row[5])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('xx！', 'xx！')
        db.close()
        for i in range(min(len(self.sno), len(self.sname), len(self.sgender), len(self.scollege), len(self.sclass),
                           len(self.sphone))):
            self.tree.insert('', i, values=(self.sno[i], self.sname[i], self.sgender[i], self.scollege[i], self.sclass[i], self.sphone[i]))
        for col in self.tableColumns:
            self.tree.heading(col, text=col,command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        self.tree.bind('<Double-1>', self.OnDubleClick)
        self.tree.after(10000, self.get_tree)

    def OnDubleClick(self,q=None):
        """
        :param q:
        :return:
        """
        item = self.tree.focus()
        if item:
            a = self.tree.item(item, 'values')
            if a[0]:
                self.show_img.show_img(a[0])

    def tree_sort_column(self, tv, col, reverse):
        """
        :param tv:
        :param col:
        :param reverse:
        :return:
        """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))


class ShowImg():
    def show_img(self, path):
        """
        :return:
        """
        self.top1 = tkinter.Toplevel()
        file = "Image_Library\\" + str(path) + ".png"
        image = Image.open(file)
        img = ImageTk.PhotoImage(image)
        canvas = tkinter.Canvas(self.top1, width=image.width, height=image.height, bg='white')
        canvas.create_image(0, 0, image=img, anchor='nw')
        canvas.pack()
        self.top1.mainloop()
