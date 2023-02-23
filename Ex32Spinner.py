from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.tabbedpanel import TabbedPanel
from kivy.animation import Animation
from random import uniform

# Spinner example exercise 32
# Builder.load_file("Ex32Spinner.kv")


class CustomLayout(Widget):

    def spinner_clicked(self, value):
        self.ids.click_label.text = f"Issuer: {value}"


class Ex32Spinner(App):

    def build(self):
        # main_widget = CustomLayout()
        # main_widget.ids.click_label.text = "Issuer: ???"
        # return main_widget
        return CustomLayout()


if __name__ == '__main__':
    Ex32Spinner().run()