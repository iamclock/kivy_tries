from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.tabbedpanel import TabbedPanel
from kivy.animation import Animation
from random import uniform



# Switches example exercise 39
class SW_CustLayout(Widget):

    def switched(self, switch_obj, switch_value):
        # self.ids.cust_label2.disabled = not switch_value
        return


class Ex39Switches(App):
    pass


if __name__ == '__main__':
    Ex39Switches().run()