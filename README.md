# Bot de WhatsApp con Flask y Twilio

Este proyecto es un bot de WhatsApp simple que responde a los mensajes utilizando Flask y Twilio.

## Requisitos

- Python 3.x
- Una cuenta de Twilio
- `ngrok` para exponer tu servidor local a Internet

## Instalación

1. **Clona el repositorio**:

   ```sh
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

## Levantar servicios
- Se debe levantar nuestro servidor `app.py` donde configuraremos las respuestas automaticas y ejecutaremos la aplicación `ngrok` para exponerlo.
- Configuraremos el webhook en `Twilio` para que apunte a la URL pública proporcionada por `ngrok`.
