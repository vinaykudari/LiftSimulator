from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class LayoutView(Widget):
    pass

class LiftSimulator(App):

    def build(self):
        return LayoutView()

if __name__ == "__main__":
    LiftSimulator().run()