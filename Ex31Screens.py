from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.tabbedpanel import TabbedPanel
from kivy.animation import Animation
from random import uniform


# Screens
class MainWindow(Screen):
    pass


class RequestSatisfaction(Screen):
    pass


class CertificateConverter(Screen):
    pass


class WindowsManager(ScreenManager):
    pass


class Ex31Screens(App):
    def build(self):
        return kv  # For screenmanager


if __name__ == '__main__':
    Ex31Screens().run()