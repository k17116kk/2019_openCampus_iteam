from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.camera import Camera

#日本語フォント適応
from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")

#Widgetが入っているファイルのbuild
Builder.load_file("sample.kv")

#タイトル画面の宣言
class TitleScreen(Screen):
    pass

#あそびかた画面の宣言
class AsobikataScreen(Screen):
    pass

#ゲーム画面の宣言
class GameScreen(Screen):
    pass

class SeikaiScreen(Screen):
    pass

class ClearScreen(Screen):
    pass

#スクリーンマネージャー（画面遷移をするため）の起動
sm = ScreenManager()
sm.add_widget(TitleScreen(name='title'))
sm.add_widget(AsobikataScreen(name='asobikata'))
sm.add_widget(GameScreen(name='game'))
sm.add_widget(SeikaiScreen(name='seikai'))
sm.add_widget(ClearScreen(name='clear'))
#
class widget(App):
    def build(self):
        return sm

if __name__=="__main__":
    widget().run()
