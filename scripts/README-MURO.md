# Publicar el muro solo

WhatsApp no tiene API en esta cuenta. El muro se actualiza así:

1. La gente manda foto/vídeo/texto a @Nexusmetadatabot (o Pepe reenvía el WhatsApp al bot).
2. Pepe responde SÍ o NO en ese chat.
3. En el Mac (volumen o repo `celebra`) corre `publicar-muro.sh`.
4. Si es SÍ, el script descarga el archivo, lo pone en `muro-media/`, actualiza `muro.json` y hace push. GitHub Pages lo enseña en 1 minuto.

Secretos: no van en git. En el Mac:

```
export TELEGRAM_BOT_TOKEN=...
export TELEGRAM_CHAT_ID=1891984663
```

Codex debe dejar este script en marcha (`launchd` cada minuto) en la máquina que ya tiene `gh` autenticado.
