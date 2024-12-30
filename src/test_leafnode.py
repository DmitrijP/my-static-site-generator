import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_raises_type_err_on_empty_val(self):
        with self.assertRaises(TypeError):
            LeafNode()
            
    def test_leaf_node_raises_type_err_on_empty_val_with_tag(self):
        with self.assertRaises(TypeError):
            LeafNode(tag='a')
    
    def test_leaf_node_with_value(self):
        node = LeafNode("Test Value")
        res = node.to_html()
        self.assertEqual(res, "Test Value")
        
    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode(tag='p', value='Test Value')
        res = node.to_html()
        self.assertEqual(res, "<p>Test Value</p>")
        
    def test_leaf_node_with_tag_and_value_and_props(self):
        node = LeafNode(tag='p', value='Test Value', props={'class':'dog'})
        res = node.to_html()
        self.assertEqual(res, '<p class="dog">Test Value</p>')
        
    def test_leaf_node_with_tag_and_value_and_mult_props(self):
        node = LeafNode(tag='p', value='Test Value', props={'class':'dog', 'id':'123', 'X-ABS':'gugu'})
        res = node.to_html()
        self.assertEqual(res, '<p class="dog" id="123" X-ABS="gugu">Test Value</p>')
        
if __name__ == "__main__":
    unittest.main()