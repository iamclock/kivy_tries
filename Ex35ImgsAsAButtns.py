from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.tabbedpanel import TabbedPanel
from kivy.animation import Animation
from random import uniform

# imgs as a buttns example exercise 35
class CustomLayout(Widget):

    def buttn_pressed(self):
        self.ids.cust_label.text = "Pressed"
        self.ids.cust_img.source = "imgs/btn_pressed.jpg"

    def buttn_released(self):
        self.ids.cust_label.text = "Unpressed"
        self.ids.cust_img.source = "imgs/btn.jpg"


class Ex35ImgsAsAButtns(App):
    pass


if __name__ == '__main__':
    Ex35ImgsAsAButtns().run()