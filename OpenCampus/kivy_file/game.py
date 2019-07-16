from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from python import findrectHSV2
#import ..python.findrectHSV2
import cv2
from .hantei import Hantei

class Game(FloatLayout):

    flag = False

    def Size_Change(self):
        width = self.width
        height = self.height
        
        for k in self.ids:
            self.ids[k].font_size = width * 0.03

    def button_press(self):

        path = "./data/"
        #画像読み込み
        pic = cv2.imread("./data/tsumiki.png",1)
        camera = self.ids['Camera']
        camera.export_to_png("./data/img.png")
        #トリミング
        #tri = pic[60:456,4:532]
        #保存
        #cv2.imwrite(path+"tri.png",tri)
        #img = cv2.imread(path+"tri.jpg")
        #cv2.imwrite(path+"img.jpg",img)

        i = findrectHSV2.hantei()

        #print("答えは")


        if (i >= 5):
            #print ("正解!!")
            Hantei.judge = True;
            hantei = cv2.imread(path+"seikai.jpg")
            cv2.imwrite(path+"hantei.jpg",hantei)

        else :
            #print ("残念")
            hantei = cv2.imread(path+"zannen.jpg")
            cv2.imwrite(path+"hantei.jpg",hantei)
            #MainRoot.change_disp_title()

    
