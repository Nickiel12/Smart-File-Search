import shelve
import wx

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG,
     format= '%(asctime)s - %(levelname)s - %(message)s')

def run():
    app = wx.App(False)
    Gui = GuiFrame()
    app.MainLoop()

class GuiFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent = None,
                        title = 'Command Editor')
        self.panel = SongPathPanel(self)
        self.create_menu()
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(
            wx.ID_ANY, 'Open Folder', 
            'Open a folder with MP3s'
        )
        menu_bar.Append(file_menu, '&File')
        self.Bind(
            event=wx.EVT_MENU, 
            handler=self.on_open_file,
            source=open_folder_menu_item,
        )
        self.SetMenuBar(menu_bar)

    def on_open_file(self, event):
        title = "Choose a song file"
        dirDialog = wx.FileDialog(self, title,
                            style = wx.DD_DEFAULT_STYLE)
        if dirDialog.ShowModal() == wx.ID_OK:
            self.panel.add_path(dirDialog.GetPath())
        dirDialog.Destroy()

class SongPathPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_cntrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
            )
        self.list_cntrl.InsertColumn(0, "Song Keyword", width=150)
        self.list_cntrl.InsertColumn(1, "Path to Song", width=500)

        self.main_sizer.Add(self.list_cntrl, 0, wx.ALL | wx.EXPAND, 5)
        self.edit_button = wx.Button(self, label='Edit')
        self.edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        self.main_sizer.Add(self.edit_button, 0, wx.ALL | wx.CENTER, 5)        
        self.SetSizer(self.main_sizer)
    
    def on_edit(self, event):
        print("in on edit")

    def add_path(self, path):
        print(path)

if __name__ == "__main__":
    run()