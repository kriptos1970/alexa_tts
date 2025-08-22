# alexa_tts

<p align="center">
  <img src="./assets/logo.png" alt="Alexa TTS Logo" width="200"/>
</p>

# Alexa TTS – Custom Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)  
![version](https://img.shields.io/badge/version-0.3.0-blue.svg)  
![maintenance](https://img.shields.io/maintenance/yes/2025.svg)

Questa integrazione aggiunge un **motore TTS (Text-to-Speech)** personalizzato in Home Assistant che utilizza l’integrazione [Alexa Media Player](https://github.com/custom-components/alexa_media_player) per inviare messaggi vocali ai dispositivi 

**Amazon Echo**.  
In pratica, espone un’entità `tts.alexa_tts` che puoi usare come qualsiasi altro TTS (es. Google o Nabu Casa), ma invece di generare un file audio invia direttamente il messaggio come **annuncio vocale** ad Alexa.

---

## ✨ Funzionalità
- Espone un’entità **`tts.alexa_tts`** in Home Assistant.  
- I messaggi inviati diventano **annunci vocali** riprodotti dai dispositivi Echo.  
- Configurazione tramite **UI (Config Flow)**: non serve toccare `configuration.yaml`.  
- Puoi configurare una lista di target di default (Echo a cui inviare sempre il messaggio).  
- Supporta override: puoi passare `entity_id` ad ogni chiamata per inviare il messaggio solo ad uno specifico Echo.  

---

## 📦 Installazione
1. Copia la cartella `alexa_tts` dentro `custom_components/` nella tua installazione di Home Assistant:  

```text
custom_components/alexa_tts/
├── init.py
├── manifest.json
├── config_flow.py
├── tts.py
└── const.py
```

2. Riavvia Home Assistant.  
3. Vai su **Impostazioni → Dispositivi e Servizi → Aggiungi integrazione**.  
4. Cerca **Alexa TTS** e inserisci i target di default (esempio: `media_player.echo_cucina, media_player.echo_camera`).  

> ⚠️ È necessario avere già configurato l’integrazione **Alexa Media Player** per far funzionare l’invio degli annunci.

---

## 🛠️ Utilizzo

### Esempio base (usa i target di default configurati)
```python
service: tts.alexa_tts_say
data:
message: "Buongiorno Primo!"
Override target (invio solo ad un Echo specifico)
service: tts.alexa_tts_say
data:
  entity_id: media_player.echo_camera
  message: "Questo lo sente solo la camera!"
```

---
⚙️ Opzioni supportate
* message → testo da leggere
* entity_id (opzionale) → target singolo, se non passato usa quelli configurati di default
---
🚧 Limitazioni
* Non genera un file audio: Home Assistant si aspetta comunque un output, ma l’audio restituito è un placeholder.
* Funziona solo se l’integrazione Alexa Media Player è installata e configurata.
* Attualmente supporta annunci vocali (type: announce); non supporta ancora altre modalità Alexa (es. tts silenzioso, push).
---
🙏 Crediti
Home Assistant
Alexa Media Player
Ispirazione dal funzionamento di altre piattaforme TTS custom