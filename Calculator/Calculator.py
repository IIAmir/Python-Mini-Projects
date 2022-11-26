from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file("./calculator.kv")
Window.size = (350, 550)


class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = '0'

    def button_value(self,number):
        prev_number = self.ids.input_box.text

        if "Error" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    def signs(self, sign):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sign}"

    def remove(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number
        if self.ids.input_box.text == '':
            self.ids.input_box.text = '0'

    def results(self):
        prev_number = self.ids.input_box.text
        try:
            results = eval(prev_number)
            self.ids.input_box.text = str(results)
        except:
            self.ids.input_box.text = "Error"
        
    def dot(self):
        prev_number = self.ids.input_box.text

        if "." in prev_number:
            pass

        else:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()