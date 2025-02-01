from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    test1 = TextNode("test1", TextType.TEXT)
    test2 = TextNode("link", TextType.LINK, "https://www.boot.dev")

    print(test1.__repr__)
    print(test2.__repr__)

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


main()