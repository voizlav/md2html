# Markdown to HTML parser
#### Video Demo:  TODO

## Overview
Markdown to HTML is a command line program that allows for easy transformation of basic Markdown syntax into HTML tags. With its straightforward functionality, users can quickly convert text files from one format to another. The program requires the input file to be passed when initiated, and the output file, if not specified, will be generated automatically as `output.html`

## Supported Syntax
- Headers: `#` for H1, `##` for H2, and so on
- Bold and italic text: use `*` or `**` to surround the text
- Lists: use `*` or `-` to create bullet points and `1.` to create numbered lists
- Links: use `[` and `]` to create a link text and `()` to create the URL
- Images: use `!` before the link markup to create an image instead of a link

## Future Improvements
The initial version of Markdown to HTML is limited to supporting only basic syntax. There are plans for future development and expansion of the program's capabilities.
Extended syntax features such as tables, code blocks highlighting, and emojis `:joy:` are intended to be added in upcoming versions of the program.

## Installation
Markdown to HTML has been designed to be a lightweight and self-contained program, with no dependencies on any external libraries or packages. By relying solely on the basic Python language and standard library modules like `sys`, `os`, and `regex`
1. Download the source code repository: `git clone https://github.com/voizlav/md2html.git`
2. Ensure that you have [Python 3](https://www.python.org/downloads/) installed on your system. If not, download and install it from the official Python website.
3. Open a command prompt or terminal window and navigate to the directory to run `project.py`


## Examples
Run the program using the following command:
```
$ python3 project.py --input test_samples/test.md --ouput example.html
```

## Files and Structure
The file structure is simplified to only include the main program and unit tests, which are written using [pytest](https://docs.pytest.org). There is also the [Black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) VSC extension provided by Microsoft to ensure consistent code formatting.
- `main` Checks the arguments passed, whether the path exists, and runs the main logic of the program
- `valid_markdown(filename: str)` Check if the input has the correct markdown filename and return a bool
- `load_markdown(file_path: str)` Read the markdown file from the given file path and return its contents as a list
- `parse_headers(line: str)` Parse any headers in the given string and return the modified line with header tags
- `parse_bold_italic(line: str)` Parse any bold and italic markup in the given string and return with HTML tags
- `parse_unordered(lines: list)` Parse unordered list markup in the given list of lines and return with HTML tags
- `parse_ordered(lines: list)` Parse ordered list markup in the given list of lines and return with HTML tags
- `parse_links(line: str)` Parse any link or image markup in the given string and return the modified with HTML tags
- `convert_to_html(lines: list)` Convert the given list of lines to HTML format
- `markdown_to_html(input_file_path: str)` Convert the markdown file at the given input file path to HTML format and return as string


## MIT License
Copyright (c) 2023 Vojislav Trujkić

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.