"""Integrazione custom Alexa TTS per Home Assistant."""
from homeassistant.core import HomeAssistant
from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: dict):
    """Setup base (non usato, config_flow gestisce tutto)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry):
    """Setup da Config Entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    return True


async def async_unload_entry(hass: HomeAssistant, entry):
    """Unloading entry."""
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
