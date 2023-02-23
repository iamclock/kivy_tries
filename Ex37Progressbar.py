from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.tabbedpanel import TabbedPanel
from kivy.animation import Animation
from random import uniform

# progressbar example exercise 37
class PB_CustLayout(Widget):

    def pb_pressed(self):
        # current_value = self.ids.cust_progress_bar.value
        rand_operand = uniform(.05, .28)
        print(rand_operand)
        self.ids.cust_progress_bar.value = round(
            ((self.ids.cust_progress_bar.value + rand_operand) % 1), 2)
        return


class Ex37Progressbar(App):
    pass


if __name__ == '__main__':
    Ex37Progressbar().run()