from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

BTN_WIDTH: int = 100
BTN_HEIGHT: int = 50

"Switchers"


class WidgetsEx(GridLayout):
    label_text_presets: tuple = ("Label", "Clicked", "Press", "Button")
    ind = 0
    label_text = StringProperty(label_text_presets[ind])
    is_count_btn_enabled = BooleanProperty(True)

    # slider_val = StringProperty("50")

    def on_button_clicked(self) -> None:
        # print("Clicked")
        self.ind: int = (self.ind + 1) % len(self.label_text_presets)
        self.label_text = self.label_text_presets[self.ind]
        return

    def on_toggle_button_clicked(self, widget) -> None:
        print(f"Toggle State: {widget.state}")
        self.is_count_btn_enabled: bool = False
        if widget.state == "down":
            self.is_count_btn_enabled = True
        return

    def on_switch_activated(self, widget) -> None:
        print(f"Switch State: {widget.active}")
        return

    def on_slider_value(self, widget) -> None:
        # print(f"Switch State: {widget.value}")
        # self.slider_val = f"{widget.value}"
        return


class StackLayoutEx2(StackLayout):

    btn_width: int = BTN_WIDTH
    btn_height: int = BTN_HEIGHT

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        btn_size: tuple = (dp(self.btn_width), dp(self.btn_height))
        for char in range(0, 100):
            self.add_widget(
                Button(text=str(char + 1),
                       size_hint=(None, None),
                       size=btn_size))
        return


class StackLayoutEx(StackLayout):

    btn_width: int = BTN_WIDTH
    btn_height: int = BTN_HEIGHT

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        size: tuple = (dp(self.btn_width), dp(self.btn_height))
        # 1st variant
        # btns = (Button(text="Tanos", size_hint=(.2, .2)),)
        # any(self.add_widget(btn) for btn in btns)
        for letter in range(65, 91):
            self.add_widget(
                Button(text=chr(letter), size_hint=(None, None), size=size))
        return


# Можно делать целиком из .kv файла описания
# class GridLayoutEx(GridLayout):
#     pass


class AnchorLayoutEx(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


# class BoxLayoutExample(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "vertical"
#         btns = (Button(text = "text_button1"), Button(text = "text_button2"))
#         any(self.add_widget(btn) for btn in btns)
#         return


class MainWidget(Widget):
    pass


class SwitchesApp(App):
    pass


if __name__ == "__main__":
    SwitchesApp().run()
