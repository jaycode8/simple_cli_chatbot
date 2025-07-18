import click
import requests
import os
from dotenv import load_dotenv

load_dotenv()

URI = "https://api.groq.com/openai/v1/chat/completions"
token = os.environ.get('API_TOKEN')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


@click.command(name="prompt")
def chatbot():
    click.echo("🤖: Hello! Type 'exit' or 'quit' to end the chat.")

    history = []

    while True:
        user_input = click.prompt("🧑", prompt_suffix=": ", default="", show_default=False)
        if user_input.lower() in ["exit", "quit"]:
            click.echo("🤖: Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        payload = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": history
        }

        try:
            response = requests.post(URI, headers=headers, json=payload)
            message = response.json()["choices"][0]["message"]
            history.append(message)
            click.secho("🤖: " + message["content"].strip(), fg="green")
        except Exception as e:
            print(e)
            click.secho(f"❌ Error: {e}", fg="red")