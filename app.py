from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Layout(GridLayout):

    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name : "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)

class LiftSimulator(App):

    def build(self):
        return Layout()

if __name__ == "__main__":
    LiftSimulator().run()