# smartthingstv
For Controlling a Samsung TV via Smart Things

I am not a developer at all, I am learning python and wanted to try this. Let me know any improvements or issues and i will try help. This is still a WIP.

# Features

**Update 

Removed the commands except turn off. 

Can:
-   Turn the TV off
-   Show current state on / off
-   Show current source (Digital TV, HDMI 1, HDMI2, APP NAME)
-   Show current volume


Todo:
-  **Make 1 function to handle all commands
-  Add WOL
-  Play Pause work
-  Set volume to X
-  Step Volume up / down
-  Toggle mute
-  Set source to X
-  Current digital channel should work but have no way of testing.
-  Add source list
-  Add ping method for state
-  Automatically populate device IDs


Cant:
- **Turn on via WIFI**
- Launch an app via smartthings api (may have work around)
- Switch to HDMI if an app is open (work around)

# Set up
Make sure your TV is logged into your smart things account.

Obtain an API key from https://account.smartthings.com/tokens

Go [here](https://graph-eu01-euwest1.api.smartthings.com/device/list) for your device id for each device. Click on the name of your TV and the device id will be in the URL

> https://graph-eu01-euwest1.api.smartthings.com/device/show/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX

In your configuration.yaml add:

```
media_player:
  - platform: smartthingstv
    name: My TV name
    api_key: "YOUR API KEY"
    device_id: "YOUR DEVICE ID"
```






