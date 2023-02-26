# Alert Dialog Boxes example exercise 48
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class Ex48MdAlertDialogBoxes(MDApp):

    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("Ex48MdAlertDialogBoxes.kv")

    def close_dialog(self, obj) -> None:
        self.dialog.dismiss()
        return

    def neat_dialog(self, obj) -> None:
        self.dialog.dismiss()
        self.root.ids.my_label.text = "Some another text"
        return

    def showing_alert_dialog(self) -> None:
        if not self.dialog:
            buttons_ = (MDFlatButton(text="CANCEL", text_color="blue", on_release=self.close_dialog),
                        MDRectangleFlatButton(text="shsdash", text_color="blue", on_release=self.neat_dialog))
            self.dialog = MDDialog(title="This is title", text="this is text", buttons=buttons_)
        self.dialog.open()
        return


if __name__ == "__main__":
    Ex48MdAlertDialogBoxes().run()
