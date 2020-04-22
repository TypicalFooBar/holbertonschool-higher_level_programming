#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n").replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    # Remove all extra white space after "\n\n"
    while True:
        newText = text.replace("\n\n ", "\n\n")

        # If no change was made, then we're done
        if (newText == text):
            break
        else:
            text = newText

    print(text, end="")
