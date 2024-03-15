# MathDiscordBot
The Discord Math Bot is a Python-based bot designed to facilitate mathematical expression formatting within Discord servers. It aims to address the limitations of Discord's text formatting capabilities, particularly for educational or math-related discussions.

<br>

## Features

* **Mathematical Expression Formatting:**
    * Users can input mathematical expressions using standard notation, including superscripts, subscripts, Greek letters, and complex powers.
* **Multiple Expressions in a Single Command:**
    * Users can input multiple mathematical expressions in a single command, and the bot will process each one individually.
* **Support for Basic and Advanced Mathematics:** 
    * The bot supports basic arithmetic operations as well as advanced functions like trigonometry, logarithms, and calculus notations (e.g., differentiation).
* **Error Handling:** 
    * The bot hides syntax errors and provides users with formatted expressions without feedback on invalid input.
* **Ignored Non-Mathematical Text:** 
    * The bot ignores non-mathematical text, allowing users to mix math expressions with regular text seamlessly.

<br>

## Usage
To interact with the bot, users can send direct messages or communicate with it in servers where both the user and the bot are present. The bot responds to commands prefixed with `$math`. Here's an example usage:
``` bash
$math x^2 + 3y - 5z
```
This command would result in the bot replying with the formatted mathematical expression `x² + 3y - 5z`.

For more information on supported syntax and commands, users can type `$math help`.

<br>

## Limitations
**Fractions:** The bot does not currently support formatting fractions due to Discord's limitations on rich text formatting.

<br>

## License
This project is licensed under the MIT License - see [LICENSE](https://opensource.org/license/mit) for details.
