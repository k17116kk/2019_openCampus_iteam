from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

#Widgetが入っているファイルのbuild
Builder.load_file("kvfile.kv")

#タイトル画面の宣言
class TitleScreen(Screen):
    pass

#もう一つの画面の宣言
class OtherScreen(Screen):
    pass

#画面遷移をするScreenManagerの宣言
sm = ScreenManager()
#各スクリーンに名前をつける
sm.add_widget(TitleScreen(name='title'))
sm.add_widget(OtherScreen(name='other'))

class widget(App):
    def build(self):
        return sm

if __name__=="__main__":
    widget().run()
