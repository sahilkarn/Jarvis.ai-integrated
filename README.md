## JARVIS 
## AI Integrated Voice Assistant

JARVIS is a Python-based personal AI assistant that combines voice recognition, text-to-speech, web utilities, and local AI conversation.

The project is designed to act as a voice-controlled assistant capable of listening to commands, responding using AI, speaking responses aloud, and performing useful tasks.

## Features

* Voice command recognition
*  Natural voice responses using Edge TTS
* AI-powered conversations using Ollama
* Conversation memory
* Web browsing/search functionality
* Wikipedia integration
* Joke generation
* Time and date responses
* Audio playback using Pygame

## Technologies Used

* Python
* SpeechRecognition
* Ollama
* Edge TTS
* Pygame
* Wikipedia
* PyJokes

## Project Structure

```text
jarvis.ai-integrated/
│
├── README.md           # Project documentation
├── jarvis.cpython-314.pyc  #It is a system created cache file so you can skip this one tbh
├── jarvis.py           # Main JARVIS program
├── jarvis_backup.py    # Backup version
└── testai.py           # AI testing script
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/jarvis.ai-integrated.git
```

Move into the project directory:

```bash
cd jarvis.ai-integrated
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Ollama Setup

JARVIS uses Ollama for local AI conversations.

Install Ollama and make sure the required model is available:

```bash
ollama pull gemma3:4b
```

Then make sure Ollama is running before starting JARVIS.

## Running JARVIS

Run the main program:

```bash
python jarvis.py
```

JARVIS will listen for voice commands and respond using its voice and AI capabilities.

## Notes

Some features require:

* A working microphone
* Internet access for certain services
* Ollama running locally
* The `gemma3:4b` model
* Appropriate audio permissions

## Project Status

This project is actively being developed and improved.

More features and integrations may be added in future versions.

## Author

Sahil



If you find this project interesting, consider starring the repository!
