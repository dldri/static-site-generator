from textnode import TextNode, TextType

def main():
    test1 = TextNode("test1", TextType.NORMAL)
    test2 = TextNode("link", TextType.LINKS, "https://www.boot.dev")

    print(test1.__repr__)
    print(test2.__repr__)

main()