from htmlnode import (
    HTMLNode,
    ParentNode
)
from inline_markdown import text_to_textnodes
from textnode import (
    text_node_to_html_node,
    TextType,
    TextNode
)
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    markdown_split = markdown.split("\n\n")
    for block in markdown_split:
        if block == "":
            continue
        block_lines = block.strip()
        blocks.append(block_lines)

    return blocks


def block_to_block_type(block):

    # Check case for heading
    if (
            block.startswith("#")
            and block[block.count("#")] == " "
            and block.count("#") <= 6
    ):
        return block_type_heading

    # Check case for code
    if (
        block.startswith("```")
        and block.endswith("```")
    ):
        return block_type_code

    # Check case for quote and lists
    lines = block.split("\n")

    # quote
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return block_type_quote

    # unordered list
    is_unordered_list = True
    for line in lines:
        if not (
            line.startswith("* ")
            or line.startswith("- ")
            or line.startswith("+ ")
        ):
            is_unordered_list = False
            break
    if is_unordered_list:
        return block_type_ulist

    # ordered lists
    is_ordered_list = True
    expected_number = 1
    for line in lines:
        if not (line.startswith(f"{expected_number}. ")):
            is_ordered_list = False
            break
        expected_number += 1
    if is_ordered_list:
        return block_type_olist

    return block_type_paragraph


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    raise ValueError(f"Unrecognised {block_type} block type detected.")


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = len(block) - len(block.lstrip("#"))
    if level > 6:
        raise ValueError(f"Invalid heading level: {level}")
    children = text_to_children(block.lstrip("#").strip(" "))
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    code_text = block[4:-3]
    code_text = "\n".join(code_text)
    children = text_to_children(code_text)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code_node])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    pattern = r"^\>\s+"
    for line in lines:
        new_lines.append(re.sub(pattern, "", line))
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    pattern = r"^\d+\.\s+"
    for item in items:
        if not item:
            continue
        content = re.sub(pattern, "", item)
        children = text_to_children(content)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    pattern = r"^[\*\-\+]\s+"
    for item in items:
        if not item:
            continue
        content = re.sub(pattern, "", item)
        children = text_to_children(content)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children
