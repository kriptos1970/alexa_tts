"""Piattaforma TTS custom che invia notifiche ad Alexa tramite notify.alexa_media."""
import logging
from homeassistant.components.tts import Provider
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN, CONF_TARGETS

_LOGGER = logging.getLogger(__name__)


async def async_get_engine(hass: HomeAssistant, config, discovery_info=None):
    # Prendiamo la prima config entry
    if DOMAIN not in hass.data or not hass.data[DOMAIN]:
        _LOGGER.error("Nessuna configurazione Alexa TTS trovata.")
        return None

    entry_data = list(hass.data[DOMAIN].values())[0]
    targets = [x.strip() for x in entry_data.get(
        CONF_TARGETS, "").split(",") if x.strip()]
    return AlexaTTS(hass, targets)


class AlexaTTS(Provider):
    def __init__(self, hass: HomeAssistant, default_targets):
        self.hass = hass
        self._name = "Alexa Custom TTS"
        self._default_targets = default_targets

    @property
    def default_language(self):
        return "it"

    @property
    def supported_languages(self):
        return ["it", "en"]

    @property
    def supported_options(self):
        return ["entity_id"]

    @property
    def name(self):
        return self._name

    async def async_get_tts_audio(self, message, language, options):
        """Invia il messaggio TTS ad Alexa."""
        targets = []

        # Se l’utente passa entity_id → override
        if "entity_id" in options:
            targets = [options["entity_id"]]
        else:
            targets = self._default_targets

        if not targets:
            _LOGGER.error("Nessun target configurato o passato.")
            return ("mp3", b"")

        try:
            await self.hass.services.async_call(
                "notify",
                "alexa_media",
                {
                    "target": targets,
                    "message": message,
                    "data": {"type": "announce"},
                },
                blocking=True,
            )
            _LOGGER.debug(
                "Inviato messaggio TTS ad Alexa (%s): %s", targets, message)
        except Exception as e:
            _LOGGER.error("Errore Alexa TTS: %s", e)

        return ("mp3", b"")
