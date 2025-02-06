from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    test1 = TextNode("test1", TextType.TEXT)
    test2 = TextNode("link", TextType.LINK, "https://www.boot.dev")

    print(test1.__repr__())
    print(test2.__repr__())

main()