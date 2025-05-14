from typing import List
from prompt_toolkit.styles import Style
import questionary
from questionary import Style as QuestionaryStyle
import sys


async def show_menu(title: str, options: List[str]) -> str:
    """
    Displays an interactive menu with the given options and returns the selected option.
    """
    try:
        # Add empty lines for spacing
        print("\n")

        # Create custom style with larger text
        custom_style = QuestionaryStyle(
            [
                ("question", "fg:#B8860B bold"),  # Title color - muted gold
                ("answer", "fg:#ffffff bold"),  # Selected option color - white
                ("pointer", "fg:#B8860B bold"),  # Pointer color - muted gold
                (
                    "highlighted",
                    "fg:#B8860B bold",
                ),  # Highlighted option color - muted gold
                ("instruction", "fg:#666666"),  # Instruction text color - gray
            ]
        )

        print()

        # Show the menu with custom style
        result = await questionary.select(
            title,
            choices=options,  # Используем options напрямую, так как эмодзи уже есть
            style=custom_style,
            qmark="🎯",  # Custom pointer
            instruction="(Use arrow keys and Enter to select)",
        ).ask_async()

        return result

    except KeyboardInterrupt:
        print("\n\nExiting program... Goodbye! 👋")
        sys.exit(0)
