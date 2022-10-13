from LoginPage import *
import pymysql

if __name__ == "__main__":
    try:
        db = pymysql.connect(host='xxxx', port="xxxx", db='xxxx', user='xxxx', password='xxxx')
        cursor = db.cursor()
        db.close()
        root = Tk()
        root.title('xxx')
        Loginpage(root)
        root.mainloop()

    except:
        print("xxxx")