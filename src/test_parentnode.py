
import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_raises_type_err_on_empty_tag(self):
        with self.assertRaises(TypeError):
            ParentNode(children=[])
            
    def test_parent_node_raises_type_err_on_empty_children(self):
        with self.assertRaises(TypeError):
            ParentNode(tag="t")
            
    def test_parent_node(self):
        c = [
            LeafNode('b', "Bold text"),
            LeafNode(None, 'Normal text'),
            LeafNode('i', 'italic text'),
            LeafNode(None, 'Normal text'),
        ]
        node = ParentNode(tag="p", children=c)
        result = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        print(expected)
        print(result)
        self.assertEqual(expected, result)
            
if __name__ == "__main__":
    unittest.main()