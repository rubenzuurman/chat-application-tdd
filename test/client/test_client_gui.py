import unittest

import wx

from src.client.client_gui import ClientLogin, ClientGUI

class TestClientGUI(unittest.TestCase):

	def setUp(self):
		#app = wx.App(False)
		#self.client_gui = ClientGUI(parent=None, title="Chat Application")
		pass

	def test_get_global_sizer_returns_sizer(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		sizer = self.client_gui.get_global_sizer()
		self.assertIsInstance(sizer, wx.Sizer)

	def test_get_title_textfield_sizer_returns_sizer(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		sizer = self.client_gui.get_title_textfield_sizer()
		self.assertIsInstance(sizer, wx.Sizer)

	def test_get_main_sizer_returns_sizer(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		sizer = self.client_gui.get_main_sizer()
		self.assertIsInstance(sizer, wx.Sizer)

	def test_get_chat_sizer_returns_sizer(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		sizer = self.client_gui.get_chat_sizer()
		self.assertIsInstance(sizer, wx.Sizer)

	def test_get_chat_input_sizer_returns_sizer(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		sizer = self.client_gui.get_chat_input_sizer()
		self.assertIsInstance(sizer, wx.Sizer)