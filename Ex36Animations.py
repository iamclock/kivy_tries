from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.tabbedpanel import TabbedPanel
from kivy.animation import Animation
from random import uniform

# animations example exercise 36
class CustLayout(Widget):

    def do_callback(self, *args):
        self.ids.cust_label.text = "What a Sh*t!"
        return

    def buttn_released(self, widget, *args):
        animate = Animation(background_color=(0, 0, 1, 1), duration=2)
        animate += Animation(size_hint=(1, 1))
        animate += Animation(size_hint=(.5, .5))
        animate.start(widget)
        animate.bind(on_complete=self.do_callback)
        return


class Ex36Animations(App):
    pass


if __name__ == '__main__':
    Ex36Animations().run()