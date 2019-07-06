from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from python import findrectHSV2
#import ..python.findrectHSV2
import cv2

class Game(FloatLayout):

    def button_press(self):

        path = "./data/"
        #画像読み込み
        pic = cv2.imread("./data/tsumiki.png",1)
        #トリミング
        tri = pic[60:456,4:532]
        #保存
        cv2.imwrite(path+"tri.jpg",tri)
        img = cv2.imread(path+"tri.jpg")
        cv2.imwrite(path+"img.jpg",img)

        i = findrectHSV2.hantei()

        #print("答えは")


        if (i >= 5):
            #print ("正解!!")
            hantei = cv2.imread(path+"seikai.jpg")
            cv2.imwrite(path+"hantei.jpg",hantei)

        else :
            #print ("残念")
            hantei = cv2.imread(path+"zannen.jpg")
            cv2.imwrite(path+"hantei.jpg",hantei)
            #MainRoot.change_disp_title()
