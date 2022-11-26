import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from kivy.lang import Builder

Window.size = (320,600)

class MusicScreen(Screen):
    pass

class SongCover(MDBoxLayout):
    angle = NumericProperty()
    anim = Animation(angle= 360, d= 5 , t= 'linear')
    anim += Animation(angle=0, d=0, t='linear')
    progress = Animation(value = 100,d = 100, t = 'linear')
    anim.repeat = True
    def rotate(self):
        if self.anim.have_properties_to_animate(self):
            self.anim.stop(self)
            self.progress.stop(self.widget)

        else:
            self.anim.start(self)
            self.progress.start(self.widget)

    def play(self,widget):
        self.widget = widget
        self.progress.start(widget)
        self.rotate()

class MainApp(MDApp):
    def build(self):
        return MusicScreen()

MainApp().run()