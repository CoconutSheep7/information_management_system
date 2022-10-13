from cv2 import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont


class Library:
    def __init__(self, num, name, gender, system, mclass, phonenumber):
        """
        :param num: Student ID
        :param name: name
        :param gender: gender
        :param system: system
        :param mclass: class
        :param phonenumber: PhoneNumber
        """
        self.img = cv2.imread("Message_Library\\Example.png")
        self.num = num
        self.name = name
        self.gender = gender
        self.system = system
        self.mclass = mclass
        self.phonenumber = phonenumber
        self.puttext()

    def puttext(self):
        """
        :return:
        """
        file = "Image_Library\\" + str(self.num) + '.png'
        img_pil = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        fontText = ImageFont.truetype("font/simsun.ttc", 30, encoding="utf-8")
        draw.text((10, 20), 'xxxxxxxxx', (0, 0, 255), font=ImageFont.truetype("font/simsun.ttc", 40, encoding="utf-8"))
        draw.text((180, 100), 'xx:' + str(self.num), (0, 0, 0), font=fontText)
        draw.text((180, 150), 'xx:' + str(self.name), (0, 0, 0), font=fontText)
        draw.text((180, 200), 'xx:' + str(self.gender), (0, 0, 0), font=fontText)
        draw.text((180, 250), 'xx:' + str(self.system), (0, 0, 0), font=fontText)
        draw.text((180, 300), 'xx:' + str(self.mclass), (0, 0, 0), font=fontText)
        draw.text((180, 350), 'xx:' + str(self.phonenumber), (0, 0, 0), font=fontText)

        img_np = numpy.array(img_pil)
        img = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        img2 = cv2.imread("Message_Library\\1.png")
        img[100:310, 20:170] = img2
        cv2.imwrite(file, img)
