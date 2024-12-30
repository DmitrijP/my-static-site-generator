from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value:str, tag:str=None, props:dict[str,str]=None):
        super().__init__(value=value, tag=tag, props=props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return super().to_html()