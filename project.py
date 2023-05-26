import os
import sys
import re
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="md2html",
        description="Takes Markdown syntax as input and translates it into HTML code",
        epilog="Example usage: python3 md2html.py -i input.md -o output.html",
    )
    parser.add_argument(
        "-i", "--input", help="path to input Markdown file", required=True
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.html",
        help="path to output HTML file",
    )
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"error: invalid file path {args.input} doesn't exist.")
        sys.exit(1)
    if not valid_markdown(os.path.basename(args.input)):
        print("error: invalid filename.")
        sys.exit(1)
    if os.path.exists(args.output):
        print(f"Warning: {args.output} will be overwritten!")
        while True:
            agree = input("Continue? [y/N] ")
            if not agree or agree.lower() == "n":
                sys.exit(1)
            if agree.lower() == "y":
                break
    html = markdown_to_html(args.input)
    with open(args.output, "w") as out:
        out.write(html)


def valid_markdown(filename: str):
    """
    Check if the input has the correct markdown filename and return a bool
    """
    if len(filename) < 4:
        return False
    if not filename.endswith(".md"):
        return False
    if not filename[:-3].isalnum():
        return False
    return True


def load_markdown(file_path: str):
    """
    Read the markdown file from the given file path and return its contents as a list
    """
    result = []
    with open(file_path) as f:
        for line in f:
            line = line.replace("\n", "")
            result.append(line)
    return result


def parse_headers(line: str):
    """
    Parse any headers in the given string and return the modified line with header tags
    """
    line = line.strip()
    if line.startswith("# "):
        return f"<h1>{line[2:]}</h1>"
    elif line.startswith("## "):
        return f"<h2>{line[3:]}</h2>"
    elif line.startswith("### "):
        return f"<h3>{line[4:]}</h3>"
    elif line.startswith("#### "):
        return f"<h4>{line[5:]}</h4>"
    elif line.startswith("##### "):
        return f"<h5>{line[6:]}</h5>"
    elif line.startswith("###### "):
        return f"<h6>{line[7:]}</h6>"
    else:
        return line


def parse_bold_italic(line: str):
    """
    Parse any bold and italic markup in the given string and return with HTML tags
    """
    italic = r"\*([^\s*][^\*]*[^\s*])\*"
    bold = r"\*\*([^\s*][^\*]*[^\s*])\*\*"
    line = re.sub(bold, r"<b>\1</b>", line)
    line = re.sub(italic, r"<i>\1</i>", line)
    return line


def parse_unordered(lines: list):
    """
    Parse unordered list markup in the given list of lines and return with HTML tags
    """
    result, count = [], False
    for line in lines:
        if not line.startswith("- ") and count:
            result.append("</ul>")
        if line.startswith("- "):
            if not result or result and not count:
                result.append("<ul>")
            count = True
            result.append(f"<li>{line[2:]}</li>")
            continue
        count = False
        result.append(line)
    if result and count:
        result.append("</ul>")
    return result


def parse_ordered(lines: list):
    """
    Parse ordered list markup in the given list of lines and return with HTML tags
    """
    result, count = [], False
    for line in lines:
        if not re.search(r"^\d+\. ", line) and count:
            result.append("</ol>")
        if match := re.search(r"^(\d+\. )", line):
            if not result or result and not count:
                result.append("<ol>")
            count = True
            result.append(f"<li>{line[len(match.group(1)) + 1:]}</li>")
            continue
        count = False
        result.append(line)
    if result and count:
        result.append("</ol>")
    return result


def parse_links(line: str):
    """
    Parse any link or image markup in the given string and return the modified with HTML tags
    """
    image = r"\!\[([\w\s]+)\]\(([^)]+)\)"
    link = r"\[([\w\s]+)\]\(([^)]+)\)"
    line = re.sub(image, r'<img src="\2" alt="\1">', line)
    line = re.sub(link, r'<a href="\2">\1</a>', line)
    return line


def convert_to_html(lines: list):
    """
    Convert the given list of lines to HTML format.
    """
    result = []
    lines = parse_unordered(lines)
    lines = parse_ordered(lines)
    for line in lines:
        line = line.strip()
        line = parse_bold_italic(line)
        line = parse_links(line)
        if line.startswith("#"):
            line = parse_headers(line)
            result.append(line)
            continue
        if not line:
            result.append("<br>")
            continue
        if not line.startswith("<"):
            result.append(f"<p>{line}</p>")
            continue
        result.append(line)
    return result


def markdown_to_html(input_file_path: str):
    """
    Convert the markdown file at the given input file path to HTML format and return as string.
    """
    loaded = load_markdown(input_file_path)
    lines = convert_to_html(loaded)
    html = "\n".join(str(line) for line in lines)
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    {html}
    </body>
    </html>
    """


if __name__ == "__main__":
    main()
