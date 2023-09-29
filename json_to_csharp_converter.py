import json
import textwrap
import argparse


def json_to_csharp(json_str, var_name='abi', max_line_length=100):
    """
    Convert a JSON string to a C# formatted string.

    Parameters:
    - json_str: The input JSON string.
    - var_name: The variable name to use in C#. Default is 'abi'.
    - max_line_length: Maximum length of a line in the C# string.

    Returns:
    - A C# formatted string.
    """
    try:
        json_obj = json.loads(json_str)
        single_line_json = json.dumps(json_obj)
        single_line_json_escaped = single_line_json.replace('"', '""')

        wrapped_lines = textwrap.wrap(
            single_line_json_escaped, width=max_line_length)
        wrapped_lines_with_quotes = [f'@"{line}"' for line in wrapped_lines]

        return f'private string {var_name} = ' + ' +\n    '.join(wrapped_lines_with_quotes) + ";"
    except json.JSONDecodeError:
        raise ValueError("Provided string is not a valid JSON.")


def main():
    parser = argparse.ArgumentParser(
        description="Convert a JSON string to a C# formatted string.")
    parser.add_argument('json_string', type=str, help="Input JSON string.")
    parser.add_argument('--var_name', type=str,
                        default='abi', help="Variable name for C# output.")
    parser.add_argument('--max_line_length', type=int, default=100,
                        help="Maximum length of a line in the C# string.")
    
    args = parser.parse_args()
    result = json_to_csharp(args.json_string, args.var_name, args.max_line_length)
    print(result)


if __name__ == "__main__":
    main()
