import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognizer
r = sr.Recognizer()

def get_voice_input():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please repeat.")
        return None
    except sr.RequestError:
        speak("Network error.")
        return None

def calculate(command):
    try:
        command = command.replace("+", " plus ")
        command = command.replace("-", " minus ")
        command = command.replace("*", " multiplied ")
        command = command.replace("x", " multiplied ")
        command = command.replace("X", " multiplied ")
        command = command.replace("/", " divided ")

        if "plus" in command or "add" in command:
            nums = [float(s) for s in command.split() if s.replace('.', '', 1).isdigit()]
            return sum(nums)
        elif "minus" in command or "subtract" in command:
            nums = [float(s) for s in command.split() if s.replace('.', '', 1).isdigit()]
            return nums[0] - nums[1]
        elif "multiply" in command or "multiplied" in command or "times" in command:
            nums = [float(s) for s in command.split() if s.replace('.', '', 1).isdigit()]
            return nums[0] * nums[1]
        elif "divide" in command or "divided" in command or "by" in command:
            nums = [float(s) for s in command.split() if s.replace('.', '', 1).isdigit()]
            if nums[1] == 0:
                return "Error! Division by zero."
            return nums[0] / nums[1]
        else:
            return "Sorry, I couldn't understand the operation."

    except Exception as e:
        return f"Error: {str(e)}"

def main():
    speak("Welcome to VoiceCalci! You can say things like '5 plus 2' or '10 divided by 2'.")
    while True:
        speak("Please say your calculation or say 'exit' to quit.")
        command = get_voice_input()

        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            result = calculate(command)
            speak(f"The result is {result}")

if __name__ == "__main__":
    main()
