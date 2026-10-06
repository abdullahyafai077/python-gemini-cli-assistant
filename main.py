import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"),http_options=types.HttpOptions(timeout=15000))

def run_ai_assistant():
    print("="*50)
    print("🤖 SMART TERMINAL AI ASSISTANT INITIALIZED")
    print("="*50)

    print("Please Write your topic of interest that you want to know more about:")

    context_topic = input("Enter your topic: ").strip()

    if not context_topic:
            print("Please enter a valid topic.")
            return

    print(f" \nyour toppic {context_topic} is saved now you can ask me anything about it")
    print("write exit to stop the assistant")

    while True:
        user_input = input("your question:").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye! Thank you for using the AI assistant.")
            break

        if not user_input:
            continue

        print("\n🔍 Processing your question...")

        try:
            prompt = f"""
            Your are a smart AI assistant that can answer questions about the topic: {context_topic} if the user ask you about something else that is not related to the topic, you should say that you are not sure about that and you should ask the user to ask you about the topic.
            You should answer the question in a way that is easy to understand and in a way that is helpful to the user.
            You should answer the question in a way that is concise and to the point.
            You should answer the question in a way that is informative and in a way that is helpful to the user.
            You should answer the question in a way that is engaging and in a way that is helpful to the user.
            You should answer the question in a way that is helpful to the user.

            user = {user_input}
            """    

            response = client.models.generate_content_stream(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            for chunk in response:
                if chunk.text:
                    print(chunk.text, end="", flush=True)

            print("\n" + "-" * 50)

        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    run_ai_assistant()