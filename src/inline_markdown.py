from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []

        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_image(old_nodes):
    if not isinstance(old_nodes, list):
        raise ValueError("Argument passed in not a list.")

    results =[]

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if not images:
            results.append(node)
            continue # move to the next node in the loop

        image_alt, image_link = images[0]
        sections = node.text.split(f"![{image_alt}]({image_link})", 1)
        if sections[0]:
            results.append(TextNode(sections[0], TextType.TEXT))
        results.append(TextNode(image_alt, TextType.IMAGE, image_link))
        
        # Recursion to check how many images could be in the original node
        if sections[1]:
            remaining_text = TextNode(sections[1], TextType.TEXT)
            results.extend(split_nodes_image([remaining_text]))

    return results

def split_nodes_link(old_nodes):
    if not isinstance(old_nodes, list):
        raise ValueError("Argument passed in not a list.")
    results =[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue # move to the next node in the loop
        
        links = extract_markdown_links(node.text)
        if not links:
            results.append(node)
            continue # move to the next node in the loop

        link_text, link_url = links[0]
        sections = node.text.split(f"[{link_text}]({link_url})", 1)
        if sections[0]:
          results.append(TextNode(sections[0], TextType.TEXT))
        results.append(TextNode(link_text, TextType.LINK, link_url))
        
        # Recursion to check how many links could be in the original node
        if sections[1]:
            remaining_text = TextNode(sections[1], TextType.TEXT)
            results.extend(split_nodes_link([remaining_text]))

    return results

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def extract_markdown_links(text):
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)