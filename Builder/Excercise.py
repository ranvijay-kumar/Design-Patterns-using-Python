class CodeBuilder:
    def __init__(self, root_name):
        # todo
        self.root_name = root_name
        self.fields={}

    def add_field(self, type, name):
        # todo
        self.fields[type]=name
        return self

    def __str__(self):
        # todo
        root_indentation = 2
        lines = []
        lines.append(f'class {self.root_name}:')
        indent = " " * (root_indentation)
        if len(self.fields)!=0:
            lines.append(f'{indent}def __init__(self):')
        else:
            lines.append(f'{indent}pass')
        indent = " " * (root_indentation*(2))
        for idx,(key,value) in enumerate(self.fields.items()):
            lines.append(f'{indent}self.{key} = {value}')
        return "\n".join(lines)

if __name__=="__main__":
    cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
    print(cb)