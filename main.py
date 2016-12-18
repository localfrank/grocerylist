from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.uix.popup import Popup

# Color the background
Window.clearcolor = get_color_from_hex("#f4f4f4")

class CustomPopup(Popup):
    pass

class AppRootLayout(BoxLayout):

    # Popup
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

class ShopListApp(App):

    def build(self):
        return AppRootLayout()

if __name__ == '__main__':
    ShopListApp().run()
