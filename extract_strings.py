""" This module extracts all string literals from a Python source file.
It should work for both py2 and py3 (you should run it with the version
of Python matching the version of the source file you want to parse).
"""
from __future__ import print_function
import ast
import sys

class StringLister(ast.NodeVisitor):
    def visit_Str(self, node):
        print(node.s)
        self.generic_visit(node)

def extract_strings(path):
    tree = None
    with open(path, 'r') as source_file:
        tree = ast.parse(source_file.read())
    StringLister().visit(tree)

if __name__ == '__main__':
    extract_strings(sys.argv[1])
