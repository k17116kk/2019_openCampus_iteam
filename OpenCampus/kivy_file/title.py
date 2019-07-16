from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from .game import Game
from kivy.config import Config 

class Title(FloatLayout):

    def Size_Change(self):
        width = self.width
        height = self.height
        
        for k in self.ids:
            self.ids[k].font_size = width * 0.03;
