import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "content", props={"href": "https://boot.dev"})
        node2 = HTMLNode("p", "content", props={"src": "https://image.png"})
        node3 = HTMLNode("a", "value", node, {"href": "test", "a": "another test", "third_prop": "third"})
        print(node.props_to_html())
        print(node2.props_to_html())
        print(node3.props_to_html())


if __name__ == "__main__":
    unittest.main()