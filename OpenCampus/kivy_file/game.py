from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from python import findrectHSV2
from kivy.properties import StringProperty
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

    def button_press(self,root):

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
        #i = 5
        #print("答えは")


        if (i >= 5):
            print ("正解!!")
            #root.source_h = "./data/seikai.jpg"
            root.hantei.ids["disp"].source = "./data/seikai.jpg"
            print(root.source_h)

        else :
            #print ("残念")
            #self.app.root.hantei.ids["disp"].source = './data/zannen.jpg'
            #MainRoot.change_disp_title()
            root.hantei.ids["disp"].source = "./data/zannen.jpg"
            print(root.source_h)
