import pyttsx3

def pronounce_names(names):
    engine = pyttsx3.init()

    for name in names:
        text = f"Hello, {name}, How are you?"
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    names_list = ["Aman", "Adnan", "Manaf"]
    pronounce_names(names_list)