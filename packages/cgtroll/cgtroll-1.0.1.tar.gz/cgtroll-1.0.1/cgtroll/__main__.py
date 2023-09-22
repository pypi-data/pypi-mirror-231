#!/usr/bin/env python

import argparse
from jinja2 import Environment, FileSystemLoader

def main():
    parser = argparse.ArgumentParser(
        description="Convert your python code to any language supported by codingame to troll the language ranking.", prog="cgtroll"
    )
    parser.add_argument(
        "language",
        help="The language you want to make your code look like.",
        choices=["bash", "python3"]
    )
    parser.add_argument(
        "file",
        help="The file containing your python code.",
        type=argparse.FileType('r')
    )

    args = parser.parse_args()
    environment = Environment(loader=FileSystemLoader("./templates/"))
    template = environment.get_template(args.language + ".j2")
    
    troll_code = template.render(args.file, code=args.file.read())
    print(troll_code)
    args.file.close()


if __name__ == "__main__":
    main()