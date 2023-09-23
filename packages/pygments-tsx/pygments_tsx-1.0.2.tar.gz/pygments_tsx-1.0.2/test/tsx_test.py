import os

import pygments
from pygments import lexers
from pygments.token import _TokenType
from pygments_tsx.tsx import TypeScriptXLexer, patch_pygments

parent = os.path.dirname(__file__)
file_path = os.path.join(parent, 'Blank.tsx')


def test_lexer_on_Blank():
    tsx_lexer = TypeScriptXLexer()
    with open(file_path) as f:
        txt = f.read()
        tokens = pygments.lex(txt, lexer=tsx_lexer)
        tokens = list(tokens)
        for idx, token in enumerate(tokens):
            print(idx)
            print(token)
        assert tokens[27][1] == 'div'
        assert isinstance(tokens[27][0], _TokenType)


def test_patch_pygments():
    patch_pygments()
    lexers.get_lexer_for_filename(file_path)
    assert True


def test_pygmemts():
    assert True
