#Smartthings TV integration#
import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import json
import os
API_BASEURL = "https://api.smartthings.com/v1"
API_DEVICES = API_BASEURL + "/devices/"
COMMAND_POWER_ON =  "{'commands': [{'component': 'main','capability': 'switch','command': 'on'}]}"
COMMAND_POWER_OFF = "{'commands': [{'component': 'main','capability': 'switch','command': 'off'}]}"
COMMAND_CHANGE_SOURCE = "{'commands':[{'component': 'main','capability': 'mediaInputSource','command': 'setInputSource', 'arguments':['HDMI1']}]}" # HDMI1 , HDMI2 , 
COMMAND_SET_VOLUME = "{'commands':[{'component': 'main','capability': 'audioVolume','command': 'setVolume','arguments': [15]}]}"
COMMAND_VOL_UP = "{'commands':[{'component': 'main','capability': 'audioVolume','command': 'volumeUp'}]}"
COMMAND_VOL_DOWN = "{'commands':[{'component': 'main','capability': 'audioVolume','command': 'volumeDown'}]}"
COMMAND_REFRESH = "{'commands':[{'component': 'main','capability': 'refresh','command': 'refresh'}]}"
COMMAND_MUTE = "{'commands':[{'component': 'main','capability': 'audioMute','command': 'mute'}]}"
COMMAND_UNMUTE = "{'commands':[{'component': 'main','capability': 'audioMute','command': 'unmute'}]}"
COMMAND_PAUSE = "{'commands':[{'component': 'main','capability': 'mediaPlayback','command': 'pause'}]}"
COMMAND_PLAY = "{'commands':[{'component': 'main','capability': 'mediaPlayback','command': 'play'}]}"
COMMAND_STOP = "{'commands':[{'component': 'main','capability': 'mediaPlayback','command': 'stop'}]}"
COMMAND_REWIND = "{'commands':[{'component': 'main','capability': 'mediaPlayback','command': 'rewind'}]}"
COMMAND_FAST_FORWARD = "{'commands':[{'component': 'main','capability': 'mediaPlayback','command': 'fastForward'}]}"

class smartthingstv:

  def __init__(self):
      self._state = "off"
      self._name = name
      self._muted = False
      self._volume = 10
      self._api_key = api_key
      self._device_id = device_id
  def __exit__(self, type, value, traceback):
      self.close()


  def device_update(self):
      API_KEY = self._api_key
      REQUEST_HEADERS = {"Authorization": "Bearer " + API_KEY}
      DEVICE_ID = self._device_id
      API_DEVICE = API_DEVICES + DEVICE_ID
      API_DEVICE_STATUS = API_DEVICE + "/status"
      API_COMMAND = API_DEVICE + "/commands"
      cmdurl = requests.post(API_COMMAND,data=COMMAND_REFRESH ,headers=REQUEST_HEADERS) # refreshes devicee
      resp = requests.get(API_DEVICE_STATUS,headers=REQUEST_HEADERS)
      data = resp.json()
      device_volume = data['components']['main']['audioVolume']['volume']['value']
      device_state = data['components']['main']['switch']['switch']['value']
      device_source = data['components']['main']['mediaInputSource']['inputSource']['value']
      device_tv_chan = data['components']['main']['tvChannel']['tvChannel']['value']
      device_tv_chan_name = data['components']['main']['tvChannel']['tvChannelName']['value']
      self._state = device_state
      self._volume = device_volume
      if device_tv_chan_name == "":
         self._source = device_source
      else:
         self._source = device_tv_chan_name
      self._channel = device_tv_chan
      self._channel_name = device_tv_chan_name


  def device_power_off(self): #send_command(self, command)
      API_KEY = self._api_key
      REQUEST_HEADERS = {"Authorization": "Bearer " + API_KEY}
      DEVICE_ID = self._device_id
      API_BASEURL = "https://api.smartthings.com/v1"
      API_DEVICES = API_BASEURL + "/devices/"
      API_DEVICE = API_DEVICES + DEVICE_ID
      API_DEVICE_STATUS = API_DEVICE + "/status"
      API_COMMAND = API_DEVICE + "/commands"
      cmdurl = requests.post(API_COMMAND,data=COMMAND_POWER_OFF ,headers=REQUEST_HEADERS)
  def device_power_on(self):
      #WOL



