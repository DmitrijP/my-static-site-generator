from typing import Self


class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list[Self]=None, props:dict[str,str]=None):
        if children is None:
            children = []
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        value = ""
        if self.value is not None:
            value = self.value
        if self.tag is None:
            return f"{value}{self.children_to_html()}"
        
        return f"<{self.tag}{self.props_to_html()}>{value}{self.children_to_html()}</{self.tag}>"

    def props_to_html(self) -> str:
        propsStr = ""
        if self.props is not None:
            for key in self.props:
                propsStr +=  f' {key}="{self.props[key]}"'
        return propsStr

    def children_to_html(self) -> str:
        childrenStr = ""
        if self.children is not None:
            for child in self.children:
                childrenStr += child.to_html()
        return childrenStr

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
