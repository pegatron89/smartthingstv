"""Support for interface with an Samsung TV."""
import asyncio
import logging
import json
import voluptuous as vol

from .smartthingstv.api import smartthingstv as smarttv

from homeassistant import util
from homeassistant.components.media_player import (
    MediaPlayerDevice,
    PLATFORM_SCHEMA,
    DEVICE_CLASS_TV,
)
from homeassistant.components.media_player.const import (
    MEDIA_TYPE_CHANNEL,
    SUPPORT_NEXT_TRACK,
    SUPPORT_PAUSE,
    SUPPORT_PLAY,
    SUPPORT_PLAY_MEDIA,
    SUPPORT_PREVIOUS_TRACK,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_VOLUME_STEP,
    SUPPORT_VOLUME_SET,
    MEDIA_TYPE_APP,
)
from homeassistant.const import (
    CONF_NAME, CONF_API_KEY, CONF_DEVICE_ID,
)
import homeassistant.helpers.config_validation as cv
from homeassistant.util import dt as dt_util

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "SamsungTVRemote"

SUPPORT_SAMSUNGTV = (
    SUPPORT_PAUSE
    | SUPPORT_VOLUME_STEP
    | SUPPORT_VOLUME_MUTE
    | SUPPORT_VOLUME_SET
    | SUPPORT_PREVIOUS_TRACK
#    | SUPPORT_SELECT_SOURCE     could pull source list from 
    | SUPPORT_NEXT_TRACK
    | SUPPORT_TURN_OFF
    | SUPPORT_PLAY
    | SUPPORT_PAUSE
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_DEVICE_ID): cv.string
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Samsung TV platform."""
    name = config.get(CONF_NAME)
    api_key = config.get(CONF_API_KEY)
    device_id = config.get(CONF_DEVICE_ID)
    add_entities([smartthingstv(name, api_key, device_id)])



class smartthingstv(MediaPlayerDevice):
    """Representation of a Samsung TV."""

    def __init__(self, name, api_key, device_id):
        """Initialize the Samsung device."""

        # Save a reference to the imported classes
        self._name = name
        self._device_id = device_id
        self._api_key = api_key
        self._volume = 1
        self._muted = False
        self._playing = False
        self._state = "on"
        self._source = ""
        self._channel = 2
        self._channel_name = ""

    def update(self):
        """Update state of device."""
        smarttv.device_update(self)
    def turn_off(self):
        smarttv.device_power_off(self)
    def mute_volume(self, mute):
        """Send mute command."""
        if self._muted == False:
           smarttv.device_mute(self)
        else:
           smarttv.device_unmute(self)

    def volume_up(self):
        smarttv.device_volume_up(self)

    def volume_down(self):
        smarttv.device_volume_down(self)

    def media_play_pause(self):
        """Simulate play pause media player."""
        if self._playing:
            smarttv.device_pause(self)
        else:
            smarttv.device_play(self)



    @property
    def device_class(self):
        """Set the device class to TV."""
        return DEVICE_CLASS_TV
    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_SAMSUNGTV

    @property
    def name(self):
        """Return the name of the device."""

        return self._name
    @property
    def media_title(self):
        """Title of current playing media."""
        self._media_title = self._channel_name
        return self._media_title
    @property
    def state(self):
        """Return the state of the device."""
        return self._state
    @property
    def is_volume_muted(self):
        """Boolean if volume is currently muted."""

        return self._muted
    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        return self._volume
    @property
    def source(self):

        return self._source
    @property
    def channel(self):

        return self._channel
    @property
    def channel_name(self):

        return self._channel_name

    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        return self._volume
