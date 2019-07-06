# -*- coding: utf-8 -*
import os
import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory

from kivy.uix.boxlayout import BoxLayout


#日本語フォント適応
from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder

Builder.load_file('window1.kv')
Builder.load_file('window2.kv')



class MainRoot(BoxLayout):
    window1 = None
    window2 = None

    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.window1 = Factory.Window1()
        self.window2 = Factory.Window2()
        super(MainRoot, self).__init__(**kwargs)
        self.change_disp()    # 追加


    def change_disp(self):
        self.clear_widgets()
        self.add_widget(self.window1)

    def change_disp2(self):
        self.clear_widgets()
        self.add_widget(self.window2)

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = '画面切り替えテスト'
    pass

if __name__ == "__main__":
    MainApp().run()
