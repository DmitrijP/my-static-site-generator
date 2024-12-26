import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertEqual(node, node2)
    def test_eq_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_eq_not_equal_2(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_eq_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)

class TestTextType(unittest.TestCase):
    def test_text_type_bold(self):
        self.assertEqual(TextType.BOLD.value, "bold")
    def test_text_type_code(self):
        self.assertEqual(TextType.CODE.value, "code")
    def test_text_type_italic(self):
        self.assertEqual(TextType.ITALIC.value, "italic")
    def test_text_type_image(self):
        self.assertEqual(TextType.IMAGE.value, "image")
    def test_text_type_link(self):
        self.assertEqual(TextType.LINK.value, "link")
    def test_text_type_normal(self):
        self.assertEqual(TextType.NORMAL.value, "normal")
        
if __name__ == "__main__":
    unittest.main()