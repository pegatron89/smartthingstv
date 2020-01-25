# Controlling samsungtv via smartthings api
import requests
import json
API_BASEURL = "https://api.smartthings.com/v1"
API_DEVICES = API_BASEURL + "/devices/"
#DEVICE_ID = "xxx" #temp Will save these 2 file in get_devices and read it in get_device_state
#DEVICE_ID = "xxx" 
API_DEVICE = API_DEVICES + DEVICE_ID
API_DEVICE_STATUS = API_DEVICE + "/status"
API_COMMAND = API_DEVICE + "/commands"
API_KEY = "xxxx"
REQUEST_HEADERS = {"Authorization": "Bearer " + API_KEY}
COMMAND_POWER_ON = ""
COMMAND_POWER_OFF = "{'commands': [{'component': 'main','capability': 'switch','command': 'on'}]}"
COMMAND_CHANGE_SOURCE = "{'commands':[{'component': 'main','capability': 'mediaInputSource','command': 'inputSource''arguments' : 'HDMI2' }]}"
COMMAND_VOL_UP = ""
COMMAND_REFRESH = "{'commands':[{'component': 'main','capability': 'refresh','command': 'refresh'}]}"
COMMAND_MUTE = "{'commands':[{'component': 'main','capability': 'refresh','command': 'refresh'}]}"

def get_devices():
  resp = requests.get(API_DEVICES,headers=REQUEST_HEADERS)
  data = resp.json()
  test = data["items"]
  for item in test:
   device_type = item['deviceTypeName']
   device_name = item['name']
   device_id = item['deviceId']
   if device_type == "Samsung OCF TV":
     print(device_name + " " + device_id + " " + device_name )

def get_device_state():
# need to send refresh command FIRST so the data updates. Doesnt update on smarthings.com untill refresh_device() 
  refresh_device()
  resp = requests.get(API_DEVICE_STATUS,headers=REQUEST_HEADERS)
  data = resp.json()
  device_volume = data['components']['main']['audioVolume']['volume']['value']
  device_source = data['components']['main']['mediaInputSource']['inputSource']['value']
  device_state = data['components']['main']['switch']['switch']['value']
  device_tv_chan = data['components']['main']['tvChannel']['tvChannel']['value']
  device_tv_chan_name = data['components']['main']['tvChannel']['tvChannelName']['value']
  print(device_volume)
  print(device_source)
  print(device_state)
  print(device_tv_chan)
  print(device_tv_chan_name) #shows current app running

def refresh_device():
  cmdurl = requests.post(API_COMMAND,data=COMMAND_REFRESH ,headers=REQUEST_HEADERS)
def power_off_device():
  cmdurl = requests.post(API_COMMAND,data=COMMAND_POWER_OFF ,headers=REQUEST_HEADERS)
def mute_device():
  cmdurl = requests.post(API_COMMAND,data=COMMAND_MUTE ,headers=REQUEST_HEADERS)
def vol_up():
  cmdurl = requests.post(API_COMMAND,data=COMMAND_MUTE ,headers=REQUEST_HEADERS)
def vol_down():
  cmdurl = requests.post(API_COMMAND,data=COMMAND_MUTE ,headers=REQUEST_HEADERS)




#get_devices()
#get_device_state()
#refresh_device()
#power_off_device()
