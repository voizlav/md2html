from project import valid_markdown
from project import parse_bold_italic
from project import parse_headers
from project import parse_links


def test_invalid_markdown():
    assert valid_markdown("foo") == False
    assert valid_markdown("foo.txt") == False
    assert valid_markdown("foo.md.txt") == False
    assert valid_markdown("foo_bar.md") == False
    assert valid_markdown(".md") == False
    assert valid_markdown("foo.mp4") == False
    assert valid_markdown("!#@$#.md") == False


def test_valid_markdown():
    assert valid_markdown("foo.md") == True
    assert valid_markdown("123.md") == True
    assert valid_markdown("foo123.md") == True
    assert valid_markdown("README.md") == True
    assert valid_markdown("привет.md") == True


def test_parse_bold_italic():
    output = "Lorem ipsum <i><b>dolor sit amet</b></i>"
    test_input = "Lorem ipsum ***dolor sit amet***"
    assert parse_bold_italic(test_input) == output

    output = "Lorem ipsum <b>dolor sit amet</b>"
    test_input = "Lorem ipsum **dolor sit amet**"
    assert parse_bold_italic(test_input) == output

    output = "Lorem ipsum <i>dolor sit amet</i>"
    test_input = "Lorem ipsum *dolor sit amet*"
    assert parse_bold_italic(test_input) == output

    output = "<i>Lorem ipsum</i> <b>dolor sit amet</b>"
    test_input = "*Lorem ipsum* **dolor sit amet**"
    assert parse_bold_italic(test_input) == output


def test_parse_bold_italic_nested():
    output = "Lorem ipsum **dolor sit <i>amet</i><i>, consectetur</i>"
    test_input = "Lorem ipsum **dolor sit *amet**, consectetur*"
    assert parse_bold_italic(test_input) == output

    output = "Lorem ipsum **dolor <i>sit amet,</i>* consectetur*"
    test_input = "Lorem ipsum **dolor *sit amet,** consectetur*"
    assert parse_bold_italic(test_input) == output


def test_parse_headers_h1():
    output = "<h1>Lorem Ipsum</h1>"
    test_input = "# Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h1>Lorem Ipsum</h1>"
    test_input = " # Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h1>Lorem Ipsum ## Foo</h1>"
    test_input = "# Lorem Ipsum ## Foo"
    assert parse_headers(test_input) == output

    output = "<h1>Lorem Ipsum ## Foo ### Bar #### Baz</h1>"
    test_input = "# Lorem Ipsum ## Foo ### Bar #### Baz"
    assert parse_headers(test_input) == output


def test_parse_headers_h2():
    output = "<h2>Lorem Ipsum</h2>"
    test_input = "## Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h2>Lorem Ipsum</h2>"
    test_input = " ## Lorem Ipsum"
    assert parse_headers(test_input) == output


def test_parse_headers_h3():
    output = "<h3>Lorem Ipsum</h3>"
    test_input = "### Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h3>Lorem Ipsum</h3>"
    test_input = " ### Lorem Ipsum"
    assert parse_headers(test_input) == output


def test_parse_headers_h4():
    output = "<h4>Lorem Ipsum</h4>"
    test_input = "#### Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h4>Lorem Ipsum</h4>"
    test_input = " #### Lorem Ipsum"
    assert parse_headers(test_input) == output


def test_parse_headers_h5():
    output = "<h5>Lorem Ipsum</h5>"
    test_input = "##### Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h5>Lorem Ipsum</h5>"
    test_input = " ##### Lorem Ipsum"
    assert parse_headers(test_input) == output


def test_parse_headers_h6():
    output = "<h6>Lorem Ipsum</h6>"
    test_input = "###### Lorem Ipsum"
    assert parse_headers(test_input) == output

    output = "<h6>Lorem Ipsum</h6>"
    test_input = " ###### Lorem Ipsum"
    assert parse_headers(test_input) == output


def test_parse_links_image():
    output = '<img src="bar" alt="Foo">'
    test_input = "![Foo](bar)"
    assert parse_links(test_input) == output

    output = 'Foo <img src="bar" alt="Baz">'
    test_input = "Foo ![Baz](bar)"
    assert parse_links(test_input) == output

    output = '<img src="baz" alt="Foo bar">'
    test_input = "![Foo bar](baz)"
    assert parse_links(test_input) == output

    output = '<img src="https://example.org/image" alt="Lorem ipsum image">'
    test_input = "![Lorem ipsum image](https://example.org/image)"
    assert parse_links(test_input) == output


def test_parse_links_link():
    output = '<a href="foo">Bar</a>'
    test_input = "[Bar](foo)"
    assert parse_links(test_input) == output

    output = 'Foo <a href="bar">baz</a>'
    test_input = "Foo [baz](bar)"
    assert parse_links(test_input) == output

    output = '<a href="https://example.org">Example</a>'
    test_input = "[Example](https://example.org)"
    assert parse_links(test_input) == output

    output = '<a href="https://example.org">Lorem ipsum hyperlink</a>'
    test_input = "[Lorem ipsum hyperlink](https://example.org)"
    assert parse_links(test_input) == output


def test_parse_links_nested():
    output = 'Hello <a href="foo">Bar</a> world <img src="foo" alt="Bar">'
    test_input = "Hello [Bar](foo) world ![Bar](foo)"
    assert parse_links(test_input) == output
