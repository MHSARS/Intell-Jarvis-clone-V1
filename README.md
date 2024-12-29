# INTELL - Voice Assistant

INTELL is a Python-based voice assistant that can perform various tasks through voice commands. It uses speech recognition and text-to-speech capabilities to interact with users naturally.

## Features

- **Voice Control**: Activate/deactivate using keyboard shortcuts (Ctrl+Alt+K to start, Ctrl+Alt+P to pause)
- **System Operations**:
  - Open Command Prompt
  - Open Visual Studio Code
  - Open WebStorm
  - Open Notepad
  - Open Discord

- **Web Operations**:
  - Get IP address
  - Search YouTube videos
  - Google search
  - Wikipedia search
  - Send emails
  - Get latest news
  - Weather forecasts
  - Amazon navigation

- **Entertainment**:
  - Movie information (using IMDb)
  - Weather updates
  - News updates

- **Calculations & Information**:
  - Mathematical calculations
  - General knowledge queries using WolframAlpha

## Prerequisites

pip install -r requirements.txt


Required Python packages:
- pyttsx3
- requests
- speech_recognition
- keyboard
- imdb
- wolframalpha
- pyautogui
- webbrowser
- python-decouple
- wikipedia
- pywhatkit

## Configuration

1. Create a `.env` file in the project root with:
USER = "YOUR_NAME"
BOT = "INTELL"


2. Set up email credentials in `online.py` for email functionality
3. Configure API keys for:
   - WolframAlpha
   - News API
   - Weather API

## Usage

1. Run the main script:
python main.py

2. Use voice commands:
- "Open command prompt"
- "What's the weather?"
- "Send an email"
- "Give me news"
- "Open Amazon"
- etc.

3. Use keyboard shortcuts:
- `Ctrl+Alt+K`: Start listening
- `Ctrl+Alt+P`: Pause listening

## Voice Commands

Here are some example commands:
- "How are you"
- "Open command prompt"
- "Open visual studio"
- "What's my IP address"
- "Open YouTube"
- "Search on Wikipedia"
- "Send an email"
- "Give me news"
- "Weather forecast"
- "Movie information"
- "Calculate [math expression]"
- "What is [query]"
- "Open Amazon"

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all the open-source libraries used in this project
- Special thanks to the Python community for the excellent documentation

## Note

Make sure to configure all API keys and credentials before running the application. Some features may require additional setup or API access.
