from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextFieldRect

Window.size = (370, 500)

class MainApp(MDApp):

    def clear(self, args):
        self.input.text = ""

    # def signs(self,sign):
    #     prev_Number = self.input.text
    #     self.input.text = f"{prev_Number}{sign}"

    def button_value(self,number):
        prev_Number = self.input.text

    #     if "Error" in prev_Number:
    #         prev_Number = ""

    #     if prev_Number == "0":
    #         self.input.text = ""
    #         self.input.text = f"{number}"
    #     else:
    #         self.input.text = f"{prev_Number}{number}"

    # def remove(self,args):
    #     prev_Number = self.input.text
    #     prev_Number = prev_Number[:-1]
    #     self.input.text = prev_Number
    #     if self.input.text == "":
    #         self.input.text  = "0"


    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"

        self.input = MDTextFieldRect(text = "0",
                            halign = "right",
                            hint_text='0',
                            height="30dp",
                            size_hint=(0.99, 0.22),
                            multiline=False,
                            font_size=43,
                            pos_hint={
                                "center_x": 0.5,
                                "center_y": 0.885
                            },
                            foreground_color="white",
                            background_color = "black",
                            )
        screen.add_widget(self.input)
        screen.add_widget(
            MDRectangleFlatButton(text="0",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.38,
                                      "center_y": 0.08
                                  },
                                  on_press = self.button_value(0)
                                  ))

        screen.add_widget(
            MDRectangleFlatButton(text="1",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.13,
                                      "center_y": 0.24
                                  },
                                  on_press=self.button_value(1)))
        screen.add_widget(
            MDRectangleFlatButton(text="2",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.38,
                                      "center_y": 0.24
                                  },
                                  on_press=self.button_value(2)))
        screen.add_widget(
            MDRectangleFlatButton(text="3",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.63,
                                      "center_y": 0.24
                                  },
                                  on_press=self.button_value(3)))


        screen.add_widget(
            MDRectangleFlatButton(text="4",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.13,
                                      "center_y": 0.40
                                  },
                                  on_press=self.button_value(4)))
        screen.add_widget(
            MDRectangleFlatButton(text="5",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.38,
                                      "center_y": 0.40
                                  },
                                  on_press=self.button_value(5)))
        screen.add_widget(
            MDRectangleFlatButton(text="6",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.63,
                                      "center_y": 0.40
                                  },
                                  on_press=self.button_value(6)))


        screen.add_widget(
            MDRectangleFlatButton(text="7",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.13,
                                      "center_y": 0.56
                                  },
                                  on_press=self.button_value(7)))

        screen.add_widget(
            MDRectangleFlatButton(text="8",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.38,
                                      "center_y": 0.56
                                  },
                                  on_press=self.button_value(8)))
        screen.add_widget(
            MDRectangleFlatButton(text="9",
                                  line_color=("#CCCCCC"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  text_color="#828282",
                                  pos_hint={
                                      "center_x": 0.63,
                                      "center_y": 0.56
                                  },
                                  on_press=self.button_value(9)))

        screen.add_widget(
            MDRectangleFlatButton(text="C",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.12),
                                  pos_hint={
                                      "center_x": 0.13,
                                      "center_y": 0.71
                                  },
                                  on_press= self.clear))

        screen.add_widget(
            MDRectangleFlatButton(text="%",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.12),
                                  pos_hint={
                                      "center_x": 0.38,
                                      "center_y": 0.71
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text="‹‹",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.12),
                                  pos_hint={
                                      "center_x": 0.63,
                                      "center_y": 0.71
                                  },
                                  on_press= self.remove))

        screen.add_widget(
            MDRectangleFlatButton(text="+",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.12),
                                  pos_hint={
                                      "center_x": 0.88,
                                      "center_y": 0.71
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text="-",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  pos_hint={
                                      "center_x": 0.88,
                                      "center_y": 0.56
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text="×",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  pos_hint={
                                      "center_x": 0.88,
                                      "center_y": 0.40
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text="÷",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  pos_hint={
                                      "center_x": 0.88,
                                      "center_y": 0.24
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text="=",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  pos_hint={
                                      "center_x": 0.88,
                                      "center_y": 0.08
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text=".",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  pos_hint={
                                      "center_x": 0.63,
                                      "center_y": 0.08
                                  }))

        screen.add_widget(
            MDRectangleFlatButton(text="EXIT",
                                  text_color=("#5018A8"),
                                  line_color=("#E5E5E5"),
                                  font_size=22,
                                  size_hint=(0.1, 0.15),
                                  pos_hint={
                                      "center_x": 0.13,
                                      "center_y": 0.08
                                  }))


        

        return screen



if __name__ == "__main__":
    MainApp().run()
