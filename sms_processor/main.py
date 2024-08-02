import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from obscure import encrypt_message, decrypt_message


class EncodedBox(TextInput):
    def __init__(self):
        super(EncodedBox, self).__init__()
        self.multiline = True
        self.hint_text = "Decode encrypted SMS"


class KeyInput(TextInput):
    def __init__(self):
        super(KeyInput, self).__init__()
        self.hint_text = "Enter key"
        self.password = True
        self.multiline = False


class ConvertButton(Button):
    def __init__(self):
        super(ConvertButton, self).__init__()
        self.text = "Encrypt/Decrypt"


class ControlBox(BoxLayout):
    def __init__(self):
        super(ControlBox, self).__init__()
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 40

        self.key_input = KeyInput()
        self.convert_button = ConvertButton()

        self.add_widget(self.key_input)
        self.add_widget(self.convert_button)


class DecodedBox(TextInput):
    def __init__(self):
        super(DecodedBox, self).__init__()
        self.multiline = True
        self.hint_text = "Create encrypted SMS"


class Container(BoxLayout):
    def __init__(self):
        super(Container, self).__init__()
        self.orientation = "vertical"

        self.encoded_box = EncodedBox()
        self.control_box = ControlBox()
        self.decoded_box = DecodedBox()


        self.add_widget(self.encoded_box)
        self.add_widget(self.control_box)
        self.add_widget(self.decoded_box)


class MyApp(App):
    def convert(self, instance):
        encoded_message = self.container.encoded_box.text
        decoded_message = self.container.decoded_box.text
        key = self.container.control_box.key_input.text

        if encoded_message == "" and decoded_message != "":
            # encode message 
            self.container.encoded_box.text = encrypt_message(decoded_message, key)

        elif encoded_message != "" and decoded_message == "":
            # decode message
            self.container.decoded_box.text = decrypt_message(encoded_message, key)
            
        else:
            self.container.encoded_box.text = ""
            self.container.decoded_box.text = ""

    def build(self):
        self.container = Container()
        self.container.control_box.convert_button.bind(on_press=self.convert)
        return self.container


if __name__=="__main__":
    MyApp().run()
