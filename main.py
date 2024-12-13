from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import json

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(hint_text='Enter some text')
        self.layout.add_widget(self.text_input)
        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.on_submit)
        self.layout.add_widget(self.submit_button)
        return self.layout

    def on_submit(self, instance):
        user_input = self.text_input.text
        data = {'input_text': user_input}
        with open('output.json', 'w') as f:
            json.dump(data, f)
        print('Text submitted:', user_input)

if __name__ == '__main__':
    MyApp().run()
