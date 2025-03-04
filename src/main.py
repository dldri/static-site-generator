import os
import sys
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from markdown_blocks import markdown_to_html_node
from copystatic import (
    copy_static,
    delete_docs
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
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    delete_docs()
    copy_static()
    generate_pages_recursive("content", "template.html", "docs", basepath)


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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    with file_read(template_path) as template:
        template_content = template.get("connection").read()

    for root, dirs, files in os.walk(dir_path_content):
        for name in dirs:  # Crawl folders and create one in destination
            og_directory_path = os.path.join(root, name)
            new_directory_path = og_directory_path.replace(
                dir_path_content, dest_dir_path)
            os.makedirs(new_directory_path)
            print(f"{new_directory_path} folder created")
        for name in files:
            if name.endswith(".md"):
                src_path = os.path.join(root, name)
                dest_path = src_path.replace(
                    dir_path_content, dest_dir_path).replace("md", "html")

                with file_read(src_path) as src:
                    src_markdown = src.get("connection").read()

                html_content = markdown_to_html_node(src_markdown).to_html()
                title = extract_title(src_markdown)

                # Replace placeholders {{ Title }} and {{ Content }}
                html_export = template_content.replace("{{ Title }}", title)
                html_export = html_export.replace(
                    "{{ Content }}", html_content)
                html_export = html_export.replace(
                    'href="/', f'href="{basepath}')
                html_export = html_export.replace(
                    'src="/', f'src="{basepath}')

                # Creates index.html or overwrites exisiting one
                with file_write(dest_path) as dest:
                    dest.get("connection").write(html_export)

                print(f"{dest_path} generated from {src_path}")


main()
