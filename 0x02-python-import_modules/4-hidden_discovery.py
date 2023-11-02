#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    import sys

    def get_defined_names(filename):
        with open(filename, 'rb') as file:
            code = compile(file.read(), filename, 'exec')
            names = []
            for instr in dis.get_instructions(code):
                if instr.opname == 'STORE_NAME':
                    name = instr.argval
                    if not name.startswith('__'):
                        names.append(name)
            return names
    if len(sys.argv) != 2:
        print("Usage: python 4-hidden_discovery.py <compiled_module.pyc>")
        sys.exit(1)

    filename = sys.argv[1]
    defined_names = get_defined_names(filename)

    for name in sorted(defined_names):
        print(name)
