import copy
from pathlib import Path
from os.path import abspath
import shelve
import wx

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG,
     format= '%(asctime)s - %(levelname)s - %(message)s')

if __name__ != "__main__":
    from modules.gui_dependicies.edit_popup import PopupEdit
else:
    from gui_dependicies.edit_popup import PopupEdit

def run():
    app = wx.App(False)
    Gui = GuiFrame()
    app.MainLoop()

class GuiFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent = None,
                        title = 'Command Editor')
        self.panel = SongPathPanel(self)
        self.Show()

class SongPathPanel(wx.Panel):

    shelf_path = Path(str(abspath("../.")))/"modules"/"assistantVariables"/"local"
    current_item = 0
    new_key, new_value = 0, 0
    temp_dict = {}

    def __init__(self, parent):
        super().__init__(parent)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_cntrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
            )
        self.list_cntrl.InsertColumn(0, "Song Keyword", width=150)
        self.list_cntrl.InsertColumn(1, "Path to Song", width=500)

        self.delete_button = wx.Button(self, label="Delete") 
        self.delete_button.Bind(wx.EVT_BUTTON, self.on_delete)
        self.main_sizer.Add(self.delete_button, 4, wx.ALL | wx.CENTER, 4)     
        self.SetSizer(self.main_sizer)

        self.main_sizer.Add(self.list_cntrl, 0, wx.ALL | wx.EXPAND, 5)
        self.edit_button = wx.Button(self, label='Edit')
        self.edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        self.main_sizer.Add(self.edit_button, 0, wx.ALL | wx.CENTER, 5)

        
        self.list_cntrl.Bind(wx.EVT_LEFT_DCLICK, self.on_double_click)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected, self.list_cntrl)
        self.populate_list()

    def on_item_selected(self, event):
        self.current_item = event.Index

    def on_delete(self, event):
        index = self.current_item
        key = self.list_cntrl.GetItemText(index, 0)
        del self.temp_dict[key]
        self.list_cntrl.DeleteItem(self.list_cntrl.GetFocusedItem())
        self.sync_shelf()

    def populate_list(self):
        if self.open_shelf():
            self.temp_dict = dict(self.shelf)
            items = self.temp_dict.items()
            debug(items)
            for key, value in items:
                index = self.list_cntrl.InsertItem(self.list_cntrl.GetItemCount(), key)
                self.list_cntrl.SetItem(index, 1, value)

    def sync_shelf(self):
        self.shelf.sync()
        return True
        
    def open_shelf(self):
        self.shelf = shelve.open(str(self.shelf_path))
        return True

    def close_shelf(self):
        self.shelf.close()
        return True
    
    def on_edit(self, event):
        with PopupEdit(self) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                new_key = dlg.key_text_entry.GetValue()
                new_value = dlg.value_text_entry.GetValue()
                debug("New Key: " + new_key)
                debug("New value: "+ new_value)
                self.new_key = new_key.lower().strip().replace(' ', "_")
                self.new_value = new_value.lower().strip().replace(" ", "_")
                debug("New Key: " + self.new_key)
                debug("New value: "+ self.new_value)
                self.add_key(new_key, new_value)

    def add_key(self, key, value):
        index = self.list_cntrl.InsertItem(self.list_cntrl.GetItemCount(), key)
        debug(index)
        item = self.list_cntrl.GetItem(index)
        item.SetTextColour(wx.RED)
        self.list_cntrl.SetItem(item)

        self.list_cntrl.SetItem(index, 1, value)
        item = self.list_cntrl.GetItem(index)
        item.SetTextColour(wx.RED)
        self.list_cntrl.SetItem(item)
        self.temp_dict[key] = value

    def on_double_click(self, event):
        print("OnDoubleClick item %s\n" % self.list_cntrl.GetItemText(self.current_item))
        event.Skip()

if __name__ == "__main__":
    run()