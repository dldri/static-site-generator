from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    test1 = TextNode("test1", TextType.TEXT)
    test2 = TextNode("link", TextType.LINK, "https://www.boot.dev")

    print(test1.__repr__())
    print(test2.__repr__())

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text).to_html()
        case TextType.BOLD:
            return LeafNode("b", text_node.text).to_html()
        case TextType.ITALIC:
            return LeafNode("i", text_node.text).to_html()
        case TextType.CODE:
            return LeafNode("code", text_node.text).to_html()            
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url}).to_html()            
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}).to_html()
        
    raise ValueError(f"Invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node.__repr__())
        else:
            split_nodes = old_node.text.split(delimiter)
            if len(split_nodes) % 2 == 0:
                raise Exception(f"Missing closing/opening delimiter \'{delimiter}\'. Invalid Markdown syntax.")
            for i in range(len(split_nodes)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_nodes[i], text_type))

    return new_nodes


main()