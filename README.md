# MathDiscordBot
The Discord Math Bot is a Python-based bot designed to facilitate mathematical expression formatting within Discord servers. It aims to address the limitations of Discord's text formatting capabilities, particularly for educational or math-related discussions.

<br>

## Usage
To interact with the bot, users can send direct messages or communicate with it in servers where both the user and the bot are present. The bot responds to commands prefixed with `$math`. Here's an example usage:
``` bash
$math x^2 + 3y - 5z
```
This command would result in the bot replying with the formatted mathematical expression `x² + 3y - 5z`.

For more information on supported syntax and commands, users can type `$math help`.
Or look at the `knowledge.py` file to see what it can detect.

<br>

## Features

* **Mathematical Expression Formatting:**
   * Users can input mathematical expressions using standard notation, including superscripts, subscripts, Greek letters, and complex powers.
* **Multiple Expressions in a Single Command:**
   * Users can input multiple mathematical expressions in a single command, and the bot will process each one individually.
* **Support for Basic and Advanced Mathematics:** 
   * ###### The bot supports basic arithmetic operations as well as advanced functions like trigonometry, logarithms, and calculus notations (e.g., differentiation).
   * Powers - numeric
      * Use the carrot (`^`) immidiately followed by the number (`19`).
      * Ex: `$math x^19` -> `x¹⁹`
   * Powers - non-numeric
      * Use the folowing syntax: `^[power]` where the `power` can be any of the following chars: decimal(`0123456789`), lower(`a-z`), upper(`A-Z`), symbols(`+-* ()`), a_few_lower_greek_letters(`<alpha-lower><beta-lower><gamma-lower><delta-lower><epsilon-lower><zeta-lower><eta-lower><theta-lower><iota-lower><kappa-lower>`)
      * Does not support all symbols due to [unicode restrictions](https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts).
   * Greek Letters - Upper and Lower
      * For upper greek letters type the name of the letter as follows: `<alpha>` for `Α`, `<delta>` for `Δ` etc...
      * For lower greek letters type the name of the letter as follows: `<alpha-lower>` for `α`, `<delta-lower>` for `δ` etc...
      * Note: no spaces or other syntax needed... Ex: `$math texttexttext<gamma>text` -> `texttexttextΓtext`
   * Set Theory Symbols
      * Set theory names must be between `less than`(<) and `greater than`(>) signs. (i.e. `'<empty-set>'` for `Ø`)
      * For more info as to which set theory names are recognized type `$math help compare`
   * Integrals
      * Integral names, like set theory names, must be between `less than`(<) and `greater than`(>) signs. (i.e. `summation-with-integral` for `⨋`)
      * For more info as to which integral names are recognized type `$math help integrals`
   * Miscellaneous
      * `$math <x-bar>` for `x̄`
      * `$math <sqrt>()` for `√()` (parenthasis not required)
      * `$math x<subscript-i>` or `$math x<sub-i>` for `xᵢ` (`x` not required)
      * `$math *` for `⋅`
      * `$math <divide>` for `÷`
* **Error Handling:** 
   * The bot hides syntax errors and provides users with formatted expressions without feedback on invalid input.
* **Ignored Non-Mathematical Text:** 
   * The bot ignores non-mathematical text, allowing users to mix math expressions with regular text seamlessly.
   * Ex: `$math I know 7.333333<pi-lower> aprox/ 23.04 but it's really closer to 23.0383450791 acording to goolge. I also know that x^2 >= x`
      * Response: `I know 7.333333π ≈ 23.04 but it's really closer to 23.0383450791 acording to goolge. I also know that x² ≥ x`

<br>

## Limitations
**Fractions:** The bot does not currently support formatting fractions due to Discord's limitations on rich text formatting.

<br>

## License
This project is licensed under the MIT License - see [LICENSE](https://opensource.org/license/mit) for details.
