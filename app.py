from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class LayoutView(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def button_press(self):
        print("Name : ", self.name.text, " Email : ", self.email.text)

class LiftSimulator(App):

    def build(self):
        return LayoutView()

if __name__ == "__main__":
    LiftSimulator().run()