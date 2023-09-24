import pyttsx3


def speakWin(msg):
    """
    Converts a given text message into speech using the 'sapi5' speech engine on Windows.

    Parameters:
    - msg (str): The text message to be converted into speech.

    Usage:
    - Call this function with the desired text message to have it spoken aloud using the default
      Windows voice.

    Example:
    ```
    message = "Hello, World!"
    speakWin(message)
    ```

    Dependencies:
    - This function relies on the pyttsx3 library for text-to-speech conversion. Make sure to
      install it using 'pip install pyttsx3' before using this function.
    
    Note:
    - You can customize the speech engine, voice, and speech rate by modifying the function's
      settings within the code.
    """
    ENG = pyttsx3.init('sapi5')
    voices = ENG.getProperty('voices')
    ENG.setProperty('voices', voices[0].id)
    ENG.setProperty('rate', 170)
    print(f"You: {msg}")
    ENG.say(msg)
    ENG.runAndWait()

