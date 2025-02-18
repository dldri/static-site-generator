from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from markdown_blocks import markdown_to_html_node
from copystatic import (
    copy_static,
    delete_public
)
from contextlib import contextmanager


@contextmanager
def file_read(path: str):
    try:
        connection = open(path, "r")
        yield {"connection": connection}
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        connection.close()


@contextmanager
def file_write(path: str):
    try:
        connection = open(path, "w")
        yield {"connection": connection}
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        connection.close()


def main():
    delete_public()
    copy_static()
    generate_page("content/index.md", "template.html", "public/index.html")


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if (
            line.startswith("#")
            and line.count("#") == 1
            and line[line.count("#")] == " "
        ):
            return line.strip("#").strip()
    raise LookupError("h1 header not found")


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")

    with file_read(from_path) as src:
        src_markdown = src.get("connection").read()

    with file_read(template_path) as template:
        template_content = template.get("connection").read()

    html_content = markdown_to_html_node(src_markdown).to_html()
    title = extract_title(src_markdown)

    # Replace placeholders {{ Title }} and {{ Content }}
    index_html = template_content.replace("{{ Title }}", title)
    index_html = index_html.replace("{{ Content }}", html_content)

    # Creates index.html or overwrites exisiting one
    with file_write(dest_path) as dest:
        dest.get("connection").write(index_html)


main()
