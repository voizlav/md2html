# Usage:
#   docker run -v /absolute/path/to/input:/input \
#              -v /absolute/path/to/output:/output \
#              md2html -i /input/input.md -o /output/output.html
#
# Description:
#   This command runs the Markdown to HTML parser Docker container.
#   You can mount /test_samples directory containing Markdown files to /input
#   and specify /output to store the resulting HTML files.


FROM python:3.12.0-slim

WORKDIR /app

COPY ./project.py /app

ENTRYPOINT ["python", "project.py"]