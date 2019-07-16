# -*- coding: utf-8 -*
import os
import kivy
import cv2
import numpy as np
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
#FloatLayoutを使うと動的に座標位置を指定できる
from kivy.uix.floatlayout import FloatLayout

#日本語フォント適応
from kivy.core.text import LabelBase, DEFAULT_FONT
#LabelBase.register(DEFAULT_FONT, "./data/ipaexg.ttf")

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder


#gethsv = Builder.load_file('get_hsv.kv')

class get_hsvApp(App):
    file_n = ""
    a = 1
    global flg
    flg = False

    def prs(self, src):
        width = self.root.width
        height = self.root.height

        file_n = self.root.ids["txt"].text
        img_source = "./case/"+file_n;

        global img_cv 
        img_cv = cv2.imread(img_source)

        img_width = img_cv.shape[1]
        img_height = img_cv.shape[0]

        self.root.ids["img"].source = img_source
        self.root.ids["img"].pos_hint = {"center_x":0.5,"center_y":0.5}

        global flg 
        flg = True



        # self.root.ids["img"].size_hint = (2,2)

    def click_pos(self,w,p):
        global flg
        if flg:
            global img_cv
            img_hsv = cv2.cvtColor(img_cv,cv2.COLOR_BGR2HSV)

            i_height,i_width,channels = img_hsv.shape[:3]

            if (p[0] > 480) and (p[0] < (i_width + 480)) and (420 < p[1]) and (p[1] < (420 + i_height)) :
                #print(img_hsv[i_height - (int(p[1]) - 420),int(p[0]) - 480,0])
                hsv = img_hsv[i_height - (int(p[1]) - 420),int(p[0]) - 480]
                bgr = img_cv[i_height - (int(p[1]) - 420),int(p[0]) - 480]
                h = str(hsv[0])
                s = str(hsv[1])
                v = str(hsv[2])
                b = str(bgr[0])
                g = str(bgr[1])
                r = str(bgr[2])
            else:
                h = s = v = str(0)
                b = g= r = str(0)

            hsv_str =  "H : " + h + ", S : " + s + ", V : " + v
            bgr_str =  "B : " + b + ", G : " + r + ", R : " + r
            self.root.ids["colorLab"].text = hsv_str + "\n" + bgr_str
            #print(h)

        

    def build(self):
        root = self.root
        root.select_btn.bind(on_press = self.prs)
        from kivy.core.window import Window
        Window.bind(mouse_pos = self.click_pos)
        return root



if __name__ == '__main__':

    runMain = get_hsvApp()
    runMain.run()

