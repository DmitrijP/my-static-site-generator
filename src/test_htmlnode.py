import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_none_to_html(self):
        node = HTMLNode()
        text = node.props_to_html()
        self.assertEqual(text, "")
        
    def test_one_props_to_html(self):
        props = {
            'href' : 'http://www.boot.dev'
        }
        node = HTMLNode(props=props)
        text = node.props_to_html()
        self.assertEqual(text, ' href="http://www.boot.dev"')
    
    def test_two_props_to_html(self):
        props = {
            'href' : 'http://www.boot.dev',
            'target' : '_blank'
        }
        node = HTMLNode(props=props)
        text = node.props_to_html()
        self.assertEqual(text, ' href="http://www.boot.dev" target="_blank"')
        
    def test_to_html(self):
        node = HTMLNode()
        text = node.props_to_html()
        self.assertEqual(text, "")
        
    def test_tag_only_to_html(self):
        node = HTMLNode(tag="p", value="Hallo wie geht es dir?")
        text = node.to_html()
        self.assertEqual(text, "<p>Hallo wie geht es dir?</p>")
    
    def test_tag_with_one_prop_to_html(self):
        props = {
            'href' : 'http://www.boot.dev'
        }
        node = HTMLNode(tag="a", value="Hallo wie geht es dir?", props=props)
        text = node.to_html()
        self.assertEqual(text, '<a href="http://www.boot.dev">Hallo wie geht es dir?</a>')
    
    def test_tag_two_props_to_html(self):
        props = {
            'href' : 'http://www.boot.dev',
            'target' : '_blank'
        }
        node = HTMLNode(tag="a", value="Hallo wie geht es dir?", props=props)
        text = node.to_html()
        self.assertEqual(text, '<a href="http://www.boot.dev" target="_blank">Hallo wie geht es dir?</a>')
        
    def test_tag_two_props_and_child_to_html(self):
        props = {
            'href' : 'http://www.boot.dev',
            'target' : '_blank'
        }
        node2 = HTMLNode(tag="a", value="Hallo wie geht es dir?", props=props)
        node = HTMLNode(tag="a", value="Hallo wie geht es dir?", props=props, children=[node2])
        text = node.to_html()
        self.assertEqual(text, '<a href="http://www.boot.dev" target="_blank">Hallo wie geht es dir?</a>')
        
