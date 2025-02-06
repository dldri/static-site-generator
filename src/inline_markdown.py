from textnode import TextNode, TextType


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
