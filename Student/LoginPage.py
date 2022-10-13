from MainPage import *


class Loginpage:

    def __init__(self, master=None):
        """
        :param master:
        """
        self.root = master
        self.root.geometry('%dx%d' % (300, 180))
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        """
        :return:
        """
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='usermane: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='password: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='sing in', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='sing out', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        """
        :return:
        """
        username = self.username.get()
        password = self.password.get()
        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        sql = "SELECT * FROM users WHERE username = '%s'" % username
        try:

            cursor.execute(sql)

            results = cursor.fetchall()
            if password == results[0][1]:
                self.page.destroy()
                MainPage(self.root)


        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('xx！', 'xx！')
        db.close()
