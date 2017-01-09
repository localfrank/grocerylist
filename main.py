from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
import json
import time

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
        if self.product_name.text == "" or self.product_name.text is None:
            pass
        else:
            selected_category = self.product_category.text
            input_item_name = self.product_name.text

            # When the new category already exists in the shoplist
            if selected_category in self.categories:
                self.shoplist[selected_category].append(input_item_name)
                self.rend_item(selected_category, input_item_name)
            else:
                self.categories.add(selected_category)
                new_category = []
                new_category.append(input_item_name)
                self.shoplist[selected_category] = new_category
                self.rend_item(selected_category, input_item_name)

            '''
            self.product_list.adapter.data.extend([selected_category + " : " + input_item_name])
            print(type(self.product_list.adapter.data)) # <class 'kivy.properties.ObservableList'>
            print(len(self.product_list.adapter.data))
            for item in self.product_list.adapter.data:
                print(item)
            print("=====================")
            self.product_list._trigger_reset_populate()
            '''

    def rend_item(self, selected_category, input_item_name):
        '''
        Rend the added item to the view list
        '''
        self.product_list.adapter.data.extend([selected_category + " : " + input_item_name])
        print(type(self.product_list.adapter.data))
        print(len(self.product_list.adapter.data))
        for item in self.product_list.adapter.data:
            print(item)
        print("=====================")
        self.product_list._trigger_reset_populate()


    def delete_item(self, btn):
        '''
        Delete added item from list
        '''
        # If item in the list being selected
        if self.product_list.adapter.selection:
            # Getting the text of the item selected
            selection = self.product_list.adapter.selection[0].text
            # Remove the matching item
            self.product_list.adapter.data.remove(selection)
            # Reset the listview
            self.product_list._trigger_reset_populate()


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
    with open("shoppingList.json", "r") as rf:
        shoplist = json.load(rf)
        for item in shoplist:
            print(item)


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

    def display_shoplist(self):
        '''
        Display the saved shopping list
        '''
        get_item_list()


class ShopListApp(App):

    def build(self):
        return AppRootLayout()

    def getDate(self):
        return (time.strftime("%Y-%m-%d", time.localtime()))


# ###########################################################
if __name__ == '__main__':
    ShopListApp().run()
