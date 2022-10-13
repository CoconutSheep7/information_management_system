from view import *


class MainPage(object):
    def __init__(self, master=None):
        """
        :param master:
        """
        self.root = master
        self.root.geometry('%dx%d' % (600, 400))
        self.createPage()

    def createPage(self):
        """
        :return:
        """
        self.inputPage = InputFrame(self.root)
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)

        self.inputPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label='SELECT', command=self.inputData)
        menubar.add_command(label='UPDATE AND DELETE', command=self.queryData)
        menubar.add_command(label='ALL', command=self.countData)
        self.root['menu'] = menubar

    def inputData(self):
        """
        :return:
        """
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()

    def queryData(self):
        """
        :return:
        """
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()

    def countData(self):
        """
        :return:
        """
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
