from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from .game import Game
from kivy.config import Config

class Asobikata(FloatLayout):

    def Size_Change(self):
        width = self.width
        height = self.height

        f_size_w = width * 0.04;
        f_size_h = height * 0.06;

        #for k in self.ids:
            #self.ids[k].font_size = width * 0.03;
        if f_size_w < f_size_h:
            self.ids["btn"].font_size = f_size_w;
            self.ids["la1"].font_size = f_size_w;
            self.ids["la2"].font_size = f_size_w;
        else:
            self.ids["btn"].font_size = f_size_h;
            self.ids["la1"].font_size = f_size_h;
            self.ids["la2"].font_size = f_size_h;

        # self.ids["btn1"].markup = True
        # self.ids["btn1"].text = '[b]終わり[/b]'
