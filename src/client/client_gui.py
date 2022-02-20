import wx

class ClientLogin(wx.Dialog):

	def __init__(self, parent, title):
		pass

class ClientGUI(wx.Frame):

	def __init__(self, parent, title):
		# Initialize superclass.
		wx.Frame.__init__(self, parent, title=title, size=(1280, 720))

		self.panel = wx.Panel(self)
		global_sizer = self.get_global_sizer()
		self.panel.SetSizer(global_sizer)

		# Center and show.
		self.Center()
		self.Show()

	def get_global_sizer(self):
		# Create global sizer.
		global_sizer = wx.BoxSizer(wx.VERTICAL)

		# Create title textfield.
		title_text_sizer = self.get_title_textfield_sizer()

		# Get main sizer.
		main_sizer = self.get_main_sizer()

		# Add components to global sizer.
		global_sizer.Add(title_text_sizer, proportion=0, \
			flag=wx.EXPAND | wx.ALL, border=5)
		global_sizer.Add(main_sizer, proportion=1, flag=wx.EXPAND | wx.ALL, \
			border=0)

		# Return sizer.
		return global_sizer

	def get_title_textfield_sizer(self):
		# Create statictext object.
		title_textfield = wx.StaticText(self.panel, label="Chat program")

		# Create title text font and apply it to the title textfield.
		title_font = wx.Font(30, wx.FONTFAMILY_DECORATIVE, \
			wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		title_textfield.SetFont(title_font)

		# Create horizontal sizer and add the text at the center.
		horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
		horizontal_sizer.Add(title_textfield, proportion=1, flag=wx.CENTER)

		# Create vertical sizer and add the horizontal sizer at the center.
		vertical_sizer = wx.BoxSizer(wx.VERTICAL)
		vertical_sizer.Add(horizontal_sizer, proportion=1, flag=wx.CENTER)

		# Return sizer.
		return vertical_sizer

	def get_main_sizer(self):
		# Create main sizer.
		main_sizer = wx.BoxSizer(wx.HORIZONTAL)

		# Get connected user sizer.
		self.connected_users_listbox = wx.ListBox(self.panel, \
			choices=[], style=wx.LB_SORT)

		# Get chat sizer.
		chat_sizer = self.get_chat_sizer()

		# Add components to main sizer.
		main_sizer.Add(self.connected_users_listbox, proportion=0, \
			flag=wx.EXPAND | wx.ALL, border=5)
		main_sizer.Add(chat_sizer, proportion=8, \
			flag=wx.EXPAND | wx.TOP | wx.RIGHT | wx.BOTTOM, border=5)

		# Return sizer.
		return main_sizer

	def get_chat_sizer(self):
		# Create chat sizer.
		chat_sizer = wx.BoxSizer(wx.VERTICAL)

		# Create chat messages window.
		self.chat_messages_textctrl = wx.TextCtrl(self.panel, \
			style=wx.TE_READONLY | wx.TE_MULTILINE)

		# Get chat input and send sizer.
		chat_input_sizer = self.get_chat_input_sizer()

		# Add components to chat sizer.
		chat_sizer.Add(self.chat_messages_textctrl, proportion=1, \
			flag=wx.EXPAND | wx.BOTTOM, border=5)
		chat_sizer.Add(chat_input_sizer, proportion=0, \
			flag=wx.EXPAND, border=0)

		# Return sizer.
		return chat_sizer

	def get_chat_input_sizer(self):
		# Create chat input sizer.
		chat_input_sizer = wx.BoxSizer(wx.HORIZONTAL)

		# Create chat message input textbox.
		self.chat_message_input_textbox = wx.TextCtrl(self.panel)

		# Create send message button.
		self.send_message_button = wx.Button(self.panel, label="Send")

		# Add components to chat input sizer.
		chat_input_sizer.Add(self.chat_message_input_textbox, proportion=9, \
			flag=wx.EXPAND | wx.ALL, border=0)
		chat_input_sizer.Add(self.send_message_button, proportion=1, \
			flag=wx.EXPAND | wx.LEFT, border=5)

		# Return sizer.
		return chat_input_sizer

def main():
	app = wx.App(False)
	window = ClientGUI(None, "Chat Application")
	app.MainLoop()

if __name__ == "__main__":
	main()