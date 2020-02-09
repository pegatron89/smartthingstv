# smartthingstv
For Controlling a Samsung TV via Smart Things

I am not a developer at all, I am learning python and wanted to try this. Let me know any improvements or issues and i will try help. This is still a WIP.

# Features

**Update 

I have added WOL, You will need to add your MAC address to your configuration. Volume and source list issue fixed and current state thanks to @jaruba . 

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
-   Add WOL



Todo:
-  Current digital channel should work but have no way of testing.
-  Add ping method for state
-  Automatically populate device IDs
-  Play Pause work


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
    mac: "YOUR MAC ADDRESS"
    expand_sources: True
```

Tested on:

UE55NU7100 - Tizen 4.0 - Lan
UE49MU6400 - Tizen 3.0 - Wifi




