from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json
import time
import sqlite3

# Color the background
Window.clearcolor = get_color_from_hex("#f4f4f4")

class ProductListButton(ListItemButton):
    pass

class AddNewPopup(Popup):

    product_name = ObjectProperty()
    product_category = ObjectProperty()
    product_list = ObjectProperty()

    shoplist = None
    categories = None

    def open(self):
        '''
        Initialize the Popup
        '''
        self.shoplist = dict()
        self.categories = set()
        super(AddNewPopup, self).open()


    def add_to_list(self, item_name, category):
        '''
        Add new item to shoppling list
        '''
        if item_name == "" or item_name == None:
            pass
        else:
            # When the new category already exists in the shoplist
            if category in self.categories:
                self.shoplist[category].append(item_name)
            else:
                self.categories.add(category)
                new_category = []
                new_category.append(item_name)
                self.shoplist[category] = new_category

            print(self.shoplist)

            # Rend the added item on the screen
            # todo new method will be created!
            box = BoxLayout(orientation="horizontal")
            btn_item = Label(text=category + ":" + item_name)
            btn_del = Button(text="Delete")
            btn_del.bind(on_press=self.delete_item)
            box.add_widget(btn_item)
            box.add_widget(btn_del)
            self.ids.added_item.add_widget(box)


    def delete_item(self, btn):
        '''
        Delete added item from list
        '''
        print(self.ids)
        print(self)
        print(btn)
        print("delete_item called")
        for item in self.shoplist:
            print(item)


    def save_list(self):
        '''
        Save the item to Json file
        '''
        # Append new shoplist to the json file
        # When the shoplist not empty
        if self.shoplist:
            data = None
            with open("shoppingList.json", "r") as rf:
                data = json.load(rf)
            with open("shoppingList.json", "w") as wf:
                data["shoppingList"][time.strftime("%Y-%m-%d", time.localtime())] = self.shoplist
                json.dump(data, wf)

            self.dismiss()
        else:
            pass


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

# ###########################################################
if __name__ == '__main__':
    ShopListApp().run()
