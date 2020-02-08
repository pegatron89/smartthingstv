# smartthingstv
For Controlling a Samsung TV via Smart Things

I am not a developer at all, I am learning python and wanted to try this. Let me know any improvements or issues and i will try help. This is still a WIP.

# Features

**Update 

Can now select sources i have manually set. Smart things api generates a supportedInputsources with all HDMI's on the tv but im having trouble with it in the sources in HA. It shows each character as a source rather than the sources itself. I will have another look. volume can also step up or down.

Can:
-   Turn the TV off
-   Set volume
-   Step volume up / down
-   Set mute / unmute
-   Show if muted / unmuted
-   Show current state on / off
-   Show current source (Digital TV, HDMI 1, HDMI2, APP NAME)
-   Show current volume
-   Add source list
-   Set source to X
-   Play Pause work


Todo:
-  Add WOL
-  Current digital channel should work but have no way of testing.
-  Add ping method for state
-  Automatically populate device IDs


Cant:
- **Turn on via WIFI**
- Launch an app via smartthings api (may have work around)

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






