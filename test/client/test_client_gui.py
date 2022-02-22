import unittest

import wx

from src.client.client_gui import ClientLogin, ClientGUI

class TestClientLogin(unittest.TestCase):

	def test_get_content_sizer_returns_sizer(self):
		app = wx.App(False)
		self.client_login = ClientLogin(parent=None, title="Connect")
		sizer = self.client_login.get_content_sizer()
		self.assertIsInstance(sizer, wx.Sizer)

class TestClientGUI(unittest.TestCase):

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


	def test_add_message_to_chatbox_empty_message_equal(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		contents_before = self.client_gui.chat_messages_textctrl.GetValue()
		self.client_gui.add_message_to_chatbox("")
		contents_after  = self.client_gui.chat_messages_textctrl.GetValue()
		self.assertEqual(contents_before, contents_after)

	def test_add_message_to_chatbox_non_empty_message_non_equal(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		contents_before = self.client_gui.chat_messages_textctrl.GetValue()
		self.client_gui.add_message_to_chatbox("test")
		contents_after  = self.client_gui.chat_messages_textctrl.GetValue()
		self.assertNotEqual(contents_before, contents_after)

	def test_add_message_to_chatbox_non_empty_message_endswith_message(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		self.client_gui.add_message_to_chatbox("another test\n")
		contents_after = self.client_gui.chat_messages_textctrl.GetValue()
		self.assertTrue(contents_after.endswith("another test\n"))


	def test_add_user_to_online_users_empty_user_equal(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		contents_before = self.client_gui.connected_users_listbox.GetStrings()
		self.client_gui.add_user_to_online_users("")
		contents_after  = self.client_gui.connected_users_listbox.GetStrings()
		self.assertEqual(contents_before, contents_after)

	def test_add_user_to_online_users_non_empty_user_not_equal(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		contents_before = self.client_gui.connected_users_listbox.GetStrings()
		self.client_gui.add_user_to_online_users("test")
		contents_after  = self.client_gui.connected_users_listbox.GetStrings()
		self.assertNotEqual(contents_before, contents_after)

	def test_add_user_to_online_users_non_empty_user_contains_user(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		self.client_gui.add_user_to_online_users("test")
		contents_after = self.client_gui.connected_users_listbox.GetStrings()
		self.assertTrue("test" in contents_after)

	def test_add_user_to_online_users_non_empty_user_does_not_contain_duplicate(self):
		app = wx.App(False)
		self.client_gui = ClientGUI(parent=None, title="Chat Application")
		self.client_gui.add_user_to_online_users("test")
		self.client_gui.add_user_to_online_users("test")
		contents_after = self.client_gui.connected_users_listbox.GetStrings()
		self.assertEqual(contents_after, ["test"])