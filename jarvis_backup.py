import datetime
import webbrowser
import urllib.parse




import speech_recognition as sr
import wikipedia
import pyjokes

import asyncio
import edge_tts
import pygame
import os
import tempfile

#INTEGRATING AI
from ollama import chat

def ask_ai(prompt):
    response = chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are JARVIS, a personal AI assistant. "
                    "Be helpful, intelligent, and concise. "
                    "Your responses will be spoken aloud, so avoid "
                    "unnecessary formatting and keep answers natural."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content





# JARVIS VOICE ENGINE


VOICE = "en-US-AvaNeural"
RATE = "-12%"
VOLUME = "+0%"


def speak(text):
    """Make JARVIS speak using a natural female neural voice."""

    print(f"JARVIS: {text}")

    async def generate_voice():

        communicate = edge_tts.Communicate(
            text,
            VOICE,
            rate=RATE,
            volume=VOLUME
        )

        temp_file = tempfile.NamedTemporaryFile(
            suffix=".mp3",
            delete=False
        )

        temp_file.close()

        await communicate.save(temp_file.name)

        return temp_file.name

    audio_file = asyncio.run(generate_voice())

    try:

        pygame.mixer.init()

        pygame.mixer.music.load(audio_file)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():

            pygame.time.Clock().tick(10)

        pygame.mixer.quit()

    finally:

        if os.path.exists(audio_file):

            os.remove(audio_file)



# LISTEN


def listen():
    """Listen to the microphone and convert speech to text."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return ""

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print(f"You: {command}")

        return command.lower()

    except sr.UnknownValueError:

        print("I couldn't understand you.")

        return ""

    except sr.RequestError:

        speak("The speech recognition service is unavailable.")

        return ""



# TIME

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"The current time is {current_time}")



# DATE


def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    speak(f"Today is {current_date}")



# OPEN WEBSITE

def open_website(command):

    websites = {

        "youtube": "https://www.youtube.com",

        "google": "https://www.google.com",

        "github": "https://github.com",

        "linkedin": "https://www.linkedin.com",

        "gmail": "https://mail.google.com",

        "chatgpt": "https://chatgpt.com",

    }

    for name, url in websites.items():

        if name in command:

            speak(f"Opening {name}")

            webbrowser.open(url)

            return True

    return False






# GOOGLE SEARCH

def google_search(command):

    search_words = [
        "search for",
        "search",
        "google",
        "look up"
    ]

    query = command

    for word in search_words:

        query = query.replace(word, "")

    query = query.strip()

    if query:

        speak(f"Searching Google for {query}")

        encoded_query = urllib.parse.quote(query)

        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open(url)

        return True

    speak("What would you like me to search for?")

    return False


# WIKIPEDIA


def wikipedia_search():

    speak("What would you like me to search on Wikipedia?")

    query = listen()

    if not query:
        return

    try:

        speak(f"Searching Wikipedia for {query}")

        result = wikipedia.summary(
            query,
            sentences=2
        )

        speak(result)

    except wikipedia.exceptions.DisambiguationError:

        speak(
            "There are multiple results for that topic. "
            "Please be more specific."
        )

    except wikipedia.exceptions.PageError:

        speak("I could not find that topic on Wikipedia.")

    except Exception:

        speak("Something went wrong while searching Wikipedia.")



# JOKE

def tell_joke():

    joke = pyjokes.get_joke()

    speak(joke)



# GREETING


def greeting():

    hour = datetime.datetime.now().hour

    if hour < 12:

        speak("Good morning.")

    elif hour < 18:

        speak("Good afternoon.")

    else:

        speak("Good evening.")

    speak("How can I help you?")


# COMMAND PROCESSOR


def process_command(command):

    
    # EXIT
   

    if any(word in command for word in [
        "stop",
        "exit",
        "quit",
        "goodbye",
        "shut down"
    ]):

        speak("Goodbye.")

        return False


 
    # GREETING
    

    elif any(word in command for word in [
        "hello",
        "hi",
        "hey"
    ]):

        greeting()


    
    # TIME
    

    elif "time" in command:

        tell_time()


    
    # DATE
    

    elif "date" in command or "today" in command:

        tell_date()


   
    # IDENTITY
    

    elif "who are you" in command:

        speak(
            "I am Jarvis, your personal voice assistant my dear Sahil."
        )

    


    
    # JOKE
    

    elif "joke" in command:

        tell_joke()


    
    # WIKIPEDIA
    

    elif "wikipedia" in command:

        wikipedia_search()


    
    # GOOGLE SEARCH
    

    elif (
        "search for" in command
        or "search" in command
        or "google" in command
        or "look up" in command
    ):

        google_search(command)


    
    # WEBSITES
    

    elif any(
        website in command
        for website in [
            "youtube",
            "github",
            "linkedin",
            "gmail",
            "chatgpt"
        ]
    ):

        open_website(command)


    
    # UNKNOWN COMMAND
    

    else:

        speak(
            "I don't know how to do that yet."
        )

    return True



# MAIN


def main():

    greeting()

    while True:

        command = listen()

        if command == "":
            continue

        should_continue = process_command(command)

        if not should_continue:
            break



# START PROGRAM


if __name__ == "__main__":

    main()