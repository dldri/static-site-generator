class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        
        return string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Node MUST have a value.")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Node MUST have a tag.")
        if not self.children:
            raise ValueError("Parent Node MUST have at least one child.")
    
        child_html_list = []
        
        for child in self.children:
            child_html_list.append(child.to_html())

        children_html = "".join(child_html_list)

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"