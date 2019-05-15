'''
  Copyright (C) 2019 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

# great example for sending keys to active windows
# https://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html

# layer for ahk - don't want to use as dont' want users needing to install other apps
# https://pypi.org/project/ahk/

# monitor mouse/keyboard and send them too
# https://github.com/moses-palmer/pynput

# hot-key list for POE
# https://www.poelab.com/keyboard-shortcuts/


from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()


class CommonHotKeys(object):
    """
    Class for interfacing with pynput
    """

    def __init__(self):
        # collect events in a threaded manner
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def play_character_presses(self, press_character_string, chat_window=True):
        if chat_window:
            # bring up chat window
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        # loop through and send each keypress separately
        for single_character in press_character_string:
            keyboard.press(single_character)
            keyboard.release(single_character)

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))
        # F2 for HO return
        if keyboard.Key.f2:
            # enter /hideout to return to hideout
            self.play_character_presses('/hideout', chat_window=True)
        # F3 for item level
        if keyboard.Key.f3:
            # enter /itemlevel to display item level for item under cursor
            self.play_character_presses('/itemlevel', chat_window=True)
        elif keyboard.Key.f7:
            # enter /exit to go to character selection screen
            self.play_character_presses('/exit', chat_window=True)
        # elif key.from_char("s"):
        #     pass

    def on_release(self, key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
