from speech_engine import listen, speak
from commands import execute_command
from nlp_engine import get_intent

def main():
    while True:
        print("Say 'assistant' to activate...")
        query = listen()
        if "assistant" in query.lower():
            speak("Yes, I am listening.")
            query = listen()
            if query:
                intent = get_intent(query)
                execute_command(intent, query)

if __name__ == "__main__":
    main()