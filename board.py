import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        label = Button(text="Test")
        return label


if __name__=="__main__":
    mytest = MyApp()
    mytest.run()
