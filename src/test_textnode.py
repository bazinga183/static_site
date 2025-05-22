import unittest
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_node(self):
        node1 = split_nodes_delimiter(
            [TextNode("This is text with a **bold** word", TextType.TEXT)],
            "**",
            TextType.BOLD
            )
        node2 = split_nodes_delimiter(
            [TextNode("This is text with a _italic_ word", TextType.TEXT)],
            "_",
            TextType.ITALIC
            )

        node3 = split_nodes_delimiter(
            [TextNode("This is text with a `code` word", TextType.TEXT)], 
            "`",
            TextType.CODE
            )
        node4 = split_nodes_delimiter(
            [TextNode("This is text with a text word", TextType.TEXT)], 
            "`",
            TextType.CODE
            )
        test1 = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" word", TextType.TEXT, None)
            ]
        test2 = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word", TextType.TEXT, None)
            ]
        test3 = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("code", TextType.CODE, None),
            TextNode(" word", TextType.TEXT, None)
            ]
        test4 = [
            TextNode("This is text with a text word", TextType.TEXT, None)
            ]
        self.assertEqual(node1, test1)
        self.assertEqual(node2, test2)
        self.assertEqual(node3, test3)
        self.assertEqual(node4, test4)

if __name__ == "__main__":
    unittest.main()