import subprocess
from pathlib import Path


MODEL_NAME = "llama3.2:3b"

PROMPT_FILE = (
    Path(__file__).resolve().parent.parent
    / "prompts"
    / "ghost_prompt.txt"
)


def get_ghost_response(command, personality="Whispering Ghost"):

    try:
        base_prompt = PROMPT_FILE.read_text(
            encoding="utf-8"
        )

        personality_prompts = {
            "Whispering Ghost": """
Speak quietly and mysteriously.
Use eerie but friendly language.
Keep the response short.
""",

            "Angry Poltergeist": """
You are an angry poltergeist trapped inside the computer.
React dramatically to the user's command.
Be spooky, chaotic and funny, but not insulting.
Keep the response short.
""",

            "Ancient Programmer": """
You are the spirit of an ancient programmer
trapped inside an old computer.

Speak like a wise programmer from the past.
Mix programming wisdom with supernatural language.
Keep the response short.
"""
        }

        style = personality_prompts.get(
            personality,
            personality_prompts["Whispering Ghost"]
        )

        full_prompt = f"""
{base_prompt}

PERSONALITY:
{personality}

STYLE:
{style}

User command:
{command}

GhostShell response:
"""

        result = subprocess.run(
            ["ollama", "run", MODEL_NAME, full_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60
        )

        if result.returncode != 0:
            return f"💀 The spirit encountered an error:\n\n{result.stderr}"

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "👻 The spirit took too long to answer..."

    except FileNotFoundError:
        return "💀 Ollama could not be found."

    except Exception as error:
        return f"💀 Something disturbed the machine: {error}"