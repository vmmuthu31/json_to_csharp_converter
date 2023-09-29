# JSON to C# String Converter

Convert your JSON strings to C# formatted strings with ease.

## Description

The `json_to_csharp_converter` module provides a simple and efficient way to transform JSON strings into C# formatted strings. This utility can be especially useful for developers working with blockchain ABIs or other scenarios where they need to embed lengthy JSON strings directly into C# code.

## Features

- Convert JSON strings into C# string format with line breaks for readability.
- Specify a custom variable name for the C# string.
- Define a maximum line length for the C# string.
- Command-line interface for quick conversions.

## Installation

1. Ensure you have Python installed.
2. Clone this repository or download `json_to_csharp_converter.py`.

## Usage

### As a Python Module:

1. Import the module in your script:
   ```python
   from json_to_csharp_converter import json_to_csharp
   ```

2. Use the `json_to_csharp` function:
   ```python
   csharp_string = json_to_csharp('{"key": "value"}', var_name="myVar", max_line_length=80)
   print(csharp_string)
   ```

### Command-line Interface:

Run the script from the command line:

```bash
python json_to_csharp_converter.py '{"key": "value"}' --var_name myVar --max_line_length 80
```

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug reports, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

You can save the above content as `README.md` in the root directory of your project/repository. This will give users a clear guide on what the module does and how to use it. Adjustments can be made to fit the specifics of your project or any additional details you'd like to include.