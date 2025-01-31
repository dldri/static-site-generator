import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "content", props={"href": "https://boot.dev"})
        node2 = HTMLNode("p", "content", props={"src": "https://image.png"})
        node3 = HTMLNode("a", "value", node, {"href": "test", "a": "another test", "third_prop": "third"})
        node4 = HTMLNode(value="test")
        print(node.props_to_html())
        print(node2.props_to_html())
        print(node3.props_to_html())
        print(node4.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leafnode1 = LeafNode("p", "this is a paragraph")
        leafnode2 = LeafNode("a", "link", {"href": "https://boot.dev"})
        leafnode3 = LeafNode("img", "image", {"src": "/dog.png"})
        leafnode4 = LeafNode(None, "raw text")
        
        print(leafnode1.to_html())
        print(leafnode2.to_html())
        print(leafnode3.to_html())
        print(leafnode4.to_html())
        


if __name__ == "__main__":
    unittest.main()