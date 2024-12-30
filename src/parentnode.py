
from typing import Dict, List
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:List[HTMLNode], props:dict[str:str] = None):
        super().__init__(tag, children, props)
        
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        return super().to_html()