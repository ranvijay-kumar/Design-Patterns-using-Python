# text = "hello"
# parts=["<p>",text,"</p>"]
# print("".join(parts))

# words = ["hello","world"]
# parts = ['<ul>']
# for w in words:
#     parts.append(f' <li>{w}</li>')
# parts.append('</ul>')
# print('\n'.join(parts))

class HtmlElement:
    indent_size = 2

    def __init__(self, name="",text="") -> None:
        self.text=text
        self.name=name
        self.elements=[]

    def __str(self,indent) -> str:
        lines=[]
        i=' '*(indent*self.indent_size)
        lines.append(f'{i}<{self.name}>')
        i1 = ' '*((indent+1)*self.indent_size)
        if self.text:
            lines.append(f'{i1}{self.text}')
        for e  in self.elements:
            lines.append(e.__str(indent+1))
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    def __str__(self) -> str:
        return self.__str(0)
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    def __init__(self,root_name) -> None:
        self.root_name=root_name
        self.__root=HtmlElement(name=root_name)

    def add_child(self,child_name,child_text):
        self.__root.elements.append(HtmlElement(child_name,child_text))


    def __str__(self) -> str:
        return str(self.__root)

builder = HtmlElement.create('ul')
builder.add_child('li','hello')
builder.add_child('li','world')
print(builder)