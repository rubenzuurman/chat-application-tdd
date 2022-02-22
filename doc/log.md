# Log
### 22-02-2022
*18:09*: Start development.<br />
*18:12*: Added test for duplicate users for the function `add_user_to_online_users()` in the class `ClientGUI`.<br />
*18:27*: Add `connect()` function to class `ClientLogin`. This function should try to receive a first message from the server that says `ok` to make sure the server exists, is running and can accept new connections.
*18:28*: Stop development.<br /><br />

*19:38*: Start development.<br />


### 21-02-2022
*20:09*: Start development.<br />
*20:20*: Added function `add_user_to_online_users()` with testing.<br />
*20:59*: Started implementing the login dialog. The `wx.GridBagSizer` does not want to get centered so I'm going to leave it like this for now.<br />
*21:03*: Added function `ClientLogin.get_content_sizer()` including testing.<br />
*21:04*: Stop development.

### 20-02-2022
*11:01*: Start development.<br />
*11:01*: Created folder `test/`, which will hold all of our tests.<br />
*11:02*: Created subfolders `src/client/`, `src/server/`, `test/client`, and `test/server`, to separate development environments for the client and the server.<br />
*11:03*: Created file `test/__init__.py` to make the `test/` folder a package.<br />
*11:04*: Stop development.<br /><br />

*12:20*\~: Start development.<br />
*13:08*: Added chapter `Protocol` to `README.md`. Tested splitting a string by the unit separator character (ascii 31) which worked. This character will be the separator character from now on.<br />
*13:26*: Added contents to chapter `Milestones` in `README.md`, layout out the general roadmap.<br />
*13:57*: Read through `README.md` and made sure everything is clear and the quality of the document is where I want it to be.<br />
*14:02*: Commit changes to branch `main`.<br />
*14:03*: Stop development.<br /><br />

*14:37*: Start development.<br />
*14:59*: Just like with the `duolingo-data-gui` project, it took about 25 minutes to figure out how to install `wxpython` for python 3.10. You are supposed to install it (following this [issue](https://github.com/wxWidgets/Phoenix/issues/2089)) by executing the command `python -m pip install --force --pre -f https://wxpython.org/Phoenix/snapshot-builds wxPython`.<br />
*15:02*: Created files `src/client/client_gui.py` and `test/client/test_client_gui.py`.<br />
*15:05*: Created basic window in `src/client/client_gui.py`. The creation of the user interface can hardly fail, one thing I could do is to return `False` if any errors where raised at the end during the process, and otherwise return the `wx.Sizer` that was created. Then, in `test/client/test_client_gui.py`, assert `not not result` to be equal to `True` to indicate it got created successfully.<br />
*15:18*: Installed library `pytest`.<br />
*15:34*: Updated `doc/images/client_layout.png` to also include a list of connected users.<br />
*16:27*: Added testing for class `ClientGUI` and started implementing class `ClientGUI`. The layout is complete for the most part, I'm only tweaking the title text size and padding.<br />
*16:28*: Stop development.<br /><br />

*17:03*: Start development.<br />
*17:05*: Ticked the first two submilestones of the first milestone about the client front-end.<br />
*17:15*: Managed to center the title text horizontally and vertically by following [this stackoverflow question](https://stackoverflow.com/questions/27095479/wx-boxsizer-both-vertical-and-horizontal-centered). The title text looks good now and the global sizer function is cleaned up a bit, which is also nice.<br />
*17:27*: The online users listbox is no longer proportional. Appearantly, after some testing, the listbox grows in width according to the longest strings in the choices list. I also added the style flag `wx.LB_SORT`, which automatically sorts the list alphabetically.<br />
*17:30*: Stop development.<br /><br />

*21:12*: Start development.<br />
*21:17*: Made chat message textfield `wx.TE_READONLY` and `wx.TE_MULTILINE`, text can be added by calling the function `AppendText(string)` on it.<br />
*21:22*: Ticked the third submilestone of the first milestone about the client front-end.<br />
*21:24*: Commit changes to branch `main`.<br />
*20:30*: Create branch `client-backend`.<br />
*21:49*: Added function `add_message_to_chatbox()` with testing and added function `send_message_event()` with no testing yet.<br />
*21:50*: Stop development.

### 19-02-2022
*20:12*: Start development.<br />
*20:14*: Create git repository.<br />
*20:16*: Clone repository and create folders `src/`, `res/` and `doc/`.<br />
*21:00*: Added chapters `TLDR`, `Introduction` and `Requirements` to `README.md`.<br />
*21:02*: Create `doc/log.md`.<br />
*21:02*: The next thing to do is to add text to the chapter `Milestones` to sketch an overview of the roadmap to success.<br />
*21:04*: Initialize virtual environment in folder `venv/`.<br />
*21:06*: Commit changes to branch `main`.<br />
*21:07*: Stop development.<br />