from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json
import time

# Color the background
Window.clearcolor = get_color_from_hex("#f4f4f4")

def delete_item(self):
    '''
    Delete added item from list
    '''
    print("delete_item called")

class AddNewPopup(Popup):

    def add_to_list(self, item_name, category):
        '''
        Add new item to shoppling list
        '''
        if item_name == "" or item_name == None:
            pass
        else:
            # Add the item to shoppling list
            item = dict()
            __shopplist = []
            item[category] = item_name
            __shopplist.append(item)

            # Rend the added item on the screen
            for item in __shopplist:
                box = BoxLayout(orientation="horizontal")
                for k, v in item.items():
                    btn_item = Label(text=k + " " + v)

                btn_del = Button(text="Delete")
                btn_del.bind(on_press=delete_item)
                box.add_widget(btn_item)
                box.add_widget(btn_del)
                self.ids.added_item.add_widget(box)


    def save_list(self, item, category):
        '''
        Save the item to Json file
        '''
        if item == "" or item == None:
            pass
        else:
            with open("shoppingList.json", "a") as f:
                data = {"time.localtime()" : item + ","}
                json.dump(data, f)
            self.dismiss()

    def category_clicked(self, category):
        '''
        Select the category of the item
        '''
        pass

class ClearPopup(Popup):

    def clear_all(self):
        '''
        Clear all items
        '''
        # todo
        pass

    def clear_done(self):
        '''
        Clear done items
        '''
        # todo
        pass

def my_callback(instance):
    print('Popup', instance, 'is being dismissed but is prevented!')
    return True


def get_item_list():
    '''
    Get the shopping list when opening the app
    '''
    with open("shoppingList.json", "a+") as f:
        item_lsit = json.load(f)
        return item_lsit


class AppRootLayout(BoxLayout):

    def open_addnew_popup(self):
        '''
        Popup when Adding new item
        '''
        the_popup = AddNewPopup()
        # the_popup.bind(on_dismiss=my_callback)
        the_popup.open()

    def clear_items_popup(self):
        '''
        Popup when tick the item which are have been done
        '''
        clear_popup = ClearPopup()
        clear_popup.open()


class ShopListApp(App):

    def build(self):
        return AppRootLayout()

    def getDate(self):
        return (time.strftime("%Y-%m-%d", time.localtime()))

if __name__ == '__main__':
    ShopListApp().run()
