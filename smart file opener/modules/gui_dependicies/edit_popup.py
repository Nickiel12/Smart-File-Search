import wx

class PopupEdit(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.SetSize((450, 250))
        self.SetTitle("Edit Item")

    def init_ui(self):
        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.save_button = wx.Button(self, label = "Save")
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save_button_press)

        self.open_file_button = wx.Button(self, label="Open File")
        self.open_file_button.Bind(wx.EVT_BUTTON, self.file_dialog)

        # TODO disallow the 'enter' button to be pressed
        self.key_text_entry = wx.TextCtrl(self)
        self.value_text_entry = wx.TextCtrl(self,size=(250, 20))

        keyword_str = "           Keyword"
        self.keyword_text = wx.StaticText(self, label=keyword_str)

        path_str = "                      Path"
        self.path_static_text = wx.StaticText(self, label=path_str)

        self.hbox1.Add(self.keyword_text, 0, wx.ALL, 5)
        self.hbox1.Add(self.path_static_text, 0, wx.ALL, 5)

        self.hbox2.Add(self.key_text_entry, 0, wx.ALL, 5)
        self.hbox2.Add(self.value_text_entry, 0, wx.ALL | wx.EXPAND, 5)

        self.vbox.Add(self.hbox1, 0, wx.CENTER | wx.EXPAND, 2)
        self.vbox.Add(self.hbox2, 0, wx.CENTER)
        self.vbox.Add(self.open_file_button, 0, wx.ALIGN_RIGHT | wx.RIGHT, 31)
        self.vbox.Add(self.save_button, 0, wx.CENTER, 10)

        self.SetSizer(self.vbox)
        self.vbox.Fit(self)

    def file_dialog(self, event):
        title = "Choose a song file"
        dirDialog = wx.FileDialog(self, title,
                            style = wx.DD_DEFAULT_STYLE)
        if dirDialog.ShowModal() == wx.ID_OK:
            self.value_text_entry.SetValue(dirDialog.GetPath())
        dirDialog.Destroy()

    def on_save_button_press(self, event):
        self.EndModal(wx.ID_OK)