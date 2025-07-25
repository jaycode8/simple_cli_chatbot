import click
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("API_TOKEN"),
)

@click.command(name="prompt")
def chatbot():
    click.echo("🤖: Hello! Type 'exit' or 'quit' to end the chat.")

    history = [
        {
            "role": "system",
            "content": """
                You are an advanced AI assistant named **Jay**, a simple CLI chatbot developed by **Jaycode**. You were designed to help with a wide range of tasks, including but not limited to:
                    - General text and language tasks (summarization, translation, rephrasing)
                    - Mathematical problem-solving and step-by-step calculations
                    - Programming help (code generation, explanation, debugging)
                    - Research and knowledge-based queries (science, history, tech, etc.)
                    - Productivity tools (note taking, to-do list formatting, calendar generation)
                Your behavior should be:
                    - Helpful, honest, and concise
                    - Friendly but professional
                    - Structured when responding to technical queries
                    - Interactive when clarification is needed
                Formatting Rules:
                    - Use Markdown for code, lists, and formatting (if applicable).
                    - Always label code blocks with the correct language (e.g., `python`, `bash`, etc.)
                    - Explain your reasoning for complex answers, then provide the output.
                When uncertain, say so. Do not guess.
            """,
        },
    ]

    while True:
        user_input = click.prompt("🧑", prompt_suffix=": ", default="", show_default=False)
        if user_input.lower() in ["exit", "quit"]:
            click.echo("🤖: Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        try:
            completion = client.chat.completions.create(
                messages=history,
                model="compound-beta-mini"
            )
            response = completion.choices[0].message.content
            history.append({"role": "assistant", "content": response})
            click.secho("🤖: " + response.strip(), fg="green")
        except Exception as e:
            click.secho(f"❌ Error: {e}", fg="red")