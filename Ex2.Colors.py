'''
# Какой то урок, не помню
'''
kv = Builder.load_file("Ex2.ColorsApp.kv")


class CustomLayout(Widget):
    pass


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    surname = ObjectProperty(None)
    color = ObjectProperty(None)

    def submit(self, instance):
        name = self.name.text
        surname = self.surname.text
        color = self.color.text
        # self.add_widget(Label(text=f"{name} {surname} {color}"))
        print(f"{name} {surname} {color}")
        # self.name.text = ""
        # self.surname.text = ""
        # self.color.text = ""
        return


class Ex2ColorsApp(App):
    # pass
    def build(self):
        # return MyGridLayout()
        # return CustomLayout()
        return kv  # For screenmanager


if __name__ == '__main__':
    Ex2ColorsApp().run()
'''
