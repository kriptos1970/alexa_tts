"""Config flow per Alexa TTS."""
from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, CONF_TARGETS


class AlexaTTSFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Alexa TTS", data=user_input)

        schema = vol.Schema({
            # esempio: media_player.echo_cucina,media_player.echo_camera
            vol.Required(CONF_TARGETS): str,
        })

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
