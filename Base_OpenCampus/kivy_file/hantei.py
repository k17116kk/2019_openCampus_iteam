from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

class Hantei(FloatLayout):

    source = StringProperty('./data/siro.jpg')

    def buttonClicked(self):
        self.source= './data/hantei.jpg'

    def buttonClicked2(self):
        self.source= './data/siro.jpg'
