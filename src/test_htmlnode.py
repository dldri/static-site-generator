import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

node = HTMLNode("p", "content", props={"href": "https://boot.dev"})
node2 = HTMLNode("p", "content", props={"src": "https://image.png"})
node3 = HTMLNode("a", "value", node, {"href": "test", "a": "another test", "third_prop": "third"})
node4 = HTMLNode(value="test")

leafnode1 = LeafNode("p", "this is a paragraph")
leafnode2 = LeafNode("a", "link", {"href": "https://boot.dev"})
leafnode3 = LeafNode("img", "image", {"src": "/dog.png"})
leafnode4 = LeafNode(None, "raw text")

children_list1 = [leafnode1, leafnode2]
children_list2 = [leafnode1, leafnode2, leafnode3]
children_list3 = [leafnode2, leafnode4]
children_list4 = [leafnode2, leafnode3, leafnode1, leafnode4]

parentnode1 = ParentNode("h2", children_list1)
parentnode2 = ParentNode("h3", children_list3, {"href": "https://www.google.com", "a": "https://www.yahoo.com"})
parentnode3 = ParentNode("h1", [parentnode1])
parentnode4 = ParentNode("h11", [parentnode1, parentnode2, leafnode1, leafnode3])
parentnode5 = ParentNode("h12", [leafnode1])

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        print(node.props_to_html())
        print(node2.props_to_html())
        print(node3.props_to_html())
        print(node4.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        
        print(leafnode1.to_html())
        print(leafnode2.to_html())
        print(leafnode3.to_html())
        print(leafnode4.to_html())

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        print(parentnode1.to_html())
        print(parentnode2.to_html())
        print(parentnode3.to_html())
        print(parentnode4.to_html())
        print(parentnode5.to_html())


if __name__ == "__main__":
    unittest.main()