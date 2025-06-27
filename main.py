import pyttsx3

content = ""

with open("input.txt", "r") as file:
    content += file.read()

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)     # Speed (words per minute)
engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

# Choose a voice (0 = male, 1 = female, depending on system)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak it
engine.say(content)
engine.runAndWait()
