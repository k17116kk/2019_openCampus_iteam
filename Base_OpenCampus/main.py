# -*- coding: utf-8 -*
import os
import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
#FloatLayoutを使うと動的に座標位置を指定できる
from kivy.uix.floatlayout import FloatLayout

#日本語フォント適応
from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, "./data/ipaexg.ttf")

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder

#各画面のロード
Builder.load_file('./kivy_file/title.kv')
Builder.load_file('./kivy_file/asobikata.kv')
Builder.load_file('./kivy_file/game.kv')
Builder.load_file('./kivy_file/hantei.kv')
Builder.load_file('./kivy_file/zannen.kv')

#game.pyをインポートする
from kivy_file.game import *
from kivy_file.hantei import *
#from python.findrectHSV2 import *

class MainRoot(FloatLayout):
    title = None
    asobikata = None
    game = None
    hantei = None
    zannen = None

    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.title = Factory.Title()
        self.asobikata = Factory.Asobikata()
        self.game = Factory.Game()
        self.hantei = Factory.Hantei()
        self.zannen = Factory.Zannen()
        super(MainRoot, self).__init__(**kwargs)
        #最初に表示をするスクリーンの指定（タイトル）
        self.change_disp_title()

        #画面切り替えの動作の定義
    def change_disp_title(self):
        #今まで表示されていたウィジェット（スクリーン）の削除
        self.clear_widgets()
        self.add_widget(self.title)

    def change_disp_asobikata(self):
        self.clear_widgets()
        self.add_widget(self.asobikata)

    def change_disp_game(self):
        self.clear_widgets()
        self.add_widget(self.game)

    def change_disp_hantei(self):
        self.clear_widgets()
        self.add_widget(self.hantei)

    def change_disp_zannen(self):
        self.clear_widgets()
        self.add_widget(self.zannen)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'つみきゲーム'
    pass

if __name__ == "__main__":
    MainApp().run()
