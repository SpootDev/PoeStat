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

from datetime import datetime


def com_chat_load_file(file_name='E:/Steam/steamapps/common/Path of Exile/logs/Client.txt',
                       last_position=0):
    client_file_handle = open(file_name, 'r', encoding='utf-8')
    client_file_handle.seek(last_position)
    while 1:
        client_line = client_file_handle.readline()
        last_position = client_file_handle.tell()
        try:
            # this verifies that it's a normal message
            datetime.strptime(client_line.split(' ', 1)[0], "%Y-%m-%d")
        except ValueError:
            # "skip" back to the while clause as it's a message we don't care about
            continue
        # split off all the header information
        text_to_process = client_line.split('] ', 1)[1]
        if text_to_process[0] == '#':
            # general chat message (global)
            '''
            2019/01/26 19:39:46 15730314 a21 [INFO Client 9756] #playername: message
            2019/01/26 20:02:09 17073295 a21 [INFO Client 9756] #<guildname> playername: message

            '''
            # TODO alert on trade messages that matches filter
            ## for sniping add to clipboard automatically - might need xclip in linux installed
            ## toClip = "@%s Hi I would like to buy your %s listed for %s" %(x['accountName'], y['typeLine'], y['note'])
            ## pyperclip.copy(toClip)
            if text_to_process.startswith('@From'):
                # TODO alert on whisper
                # TODO for alerts.....do the OS alert
                pass
        elif text_to_process[0] == ':':
            # game information (location change, level, death, passive allocate, etc)
            '''
            2019/01/26 20:14:04 17788123 a21 [INFO Client 9756] : You have received a Passive Skill Point.
            2019/01/26 20:14:04 17788123 a21 [INFO Client 9756] : You have received 2 Passive Respec Points.
            2019/01/26 20:14:15 17798840 a21 [INFO Client 9756] : Item on cursor destroyed
            2019/01/27 01:47:31 37794939 a21 [INFO Client 6748] : Trade accepted.
            2019/01/27 02:06:22 38925931 a21 [INFO Client 6748] : Open the eye of the storm.
            2019/01/27 02:07:05 38969268 a21 [INFO Client 6748] : Shroud your path in the fog of war.
            2019/01/27 03:28:39 43863113 a21 [INFO Client 6748] : Icebitchie has been slain.
            2019/01/26 19:41:53 15856721 a21 [INFO Client 9756] : Icebitchie (Witch) is now level 28

            2019/01/26 20:10:47 17591359 a21 [INFO Client 9756] : You have entered The Marketplace.
            '''
            if text_to_process.startswith(': You have entered'):
                # This will provide the location the character has entered (map, act area, etc)
                # the -1 is to drop off the trailing period
                new_location = text_to_process.split(': You have entered ', 1)[1][:-1]
                # TODO Map runs and times
                # TODO Act runs and times
        else:
            # other misc message like npcs, etc
            '''
            2019/01/26 19:43:42 15966452 a21 [INFO Client 9756] Izaro: Allow your wisdom to be tempered by the flames of the past.
            2019/01/26 19:44:40 16024001 9d [INFO Client 9756] Successfully allocated passive skill id: dexterity869, name: Dexterity
            2019/01/26 20:14:27 17811180 cea [DEBUG Client 9756] Got Instance Details from login server
            2019/01/26 20:14:27 17811195 d07 [INFO Client 9756] Just before calling client instance session
            2019/01/26 20:14:27 17811195 dc [INFO Client 9756] Connecting to instance server at 63.251.241.244:6112
            2019/01/26 20:14:28 17811866 164 [DEBUG Client 9756] Connect time to instance server was 31m
            2019/01/27 02:26:10 40114284 17f [DEBUG Client 6748] Non-Positioned Sound set up as Positioned Sound :Audio/Dialogue/NPC/AvariusStereo/Stereo_Av05_Edit.dialogue.ogg

            '''
            pass

        # TODO Sound notifications on match
        # TODO System-Tray notifications on match
        # TODO add chat records to database from client.txt
        # TODO Blacklist users so you don't get notified of their messages


com_chat_load_file()

'''
exmples of client.txt

# the following has ^M
2019/01/27 02:34:04 40587700 a21 [INFO Client 6748] Utula: Cup your hands, children of Kitava.
Drink of the hot, sweet wine of Oriath.
And let us stay ourselves from the feast no longer.
For our king is ravenous!

'''
