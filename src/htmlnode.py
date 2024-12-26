class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        value = ""
        if self.value is not None:
            value = self.value
        if self.tag is None:
            return f"{value}{self.children_to_html()}"
        
        return f"<{self.tag}{self.props_to_html()}>{value}{self.children_to_html()}</{self.tag}>"

    def props_to_html(self):
        propsStr = ""
        if self.props is not None:
            for key in self.props:
                propsStr +=  f' {key}="{self.props[key]}"'
        return propsStr

    def children_to_html(self):
        childrenStr = ""
        if self.children is not None:
            for child in self.children:
                childrenStr += child.to_html()
        return childrenStr

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"