# Titulo del proyecto

2199 - Python y Gemini: Orquestando LLMs con LangChain

## Funcionalidades del proyecto

En este proyecto, utilizaremos LangChain como framework principal para orquestar una solucion integrada de analisis de imagenes con Gemini. LangChain permite conectar y gestionar flujos que combinan IA multimodal y modelos de lenguaje de forma modular.

## Tecnicas y tecnologias utilizadas

- Programacion en Python
- Uso de la API Gemini
- Uso del framework LangChain
- Analisis multimodal de imagenes
- Variables de entorno con python-dotenv

## Abrir y ejecutar el proyecto

Despues de descargar el proyecto, puedes abrirlo con Visual Studio Code. El proyecto usa un solo entorno virtual llamado `.venv`.

### venv en Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### venv en Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Despues, instala los paquetes:

```bash
pip install -r requirements.txt
```

## Configurar API keys

Crea un archivo `.env` en la raiz del proyecto:

```env
GEMINI_API_KEY=TU_API_KEY_AQUI
COHERE_API_KEY=TU_API_KEY_AQUI
```

## Ejecutar

```bash
python lang_chain.py
```
