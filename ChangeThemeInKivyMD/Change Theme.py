from kivymd.app import MDApp
from kivy.lang import Builder

switchs = """
MDSwitch:
    cursor: "hand2"
    pos_hint : {"center_x":0.5,"center_y":0.5}
    width: dp(45)
    on_active: app.check(*args)
        """

class Test(MDApp):

    def build(self):
        switch = Builder.load_string(switchs)
        self.theme_cls.theme_style = "Light"
        return switch

    def check(self,checkbox,value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
if __name__ == "__main__":
    Test().run()