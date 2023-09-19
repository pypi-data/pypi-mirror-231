from pimp.common import *

import rich_click as click

logger = logging.getLogger(__name__)

@click.group(name="ts")
@click.pass_context
def run_ts(ctx: click.core.Context):
    ...

@run_ts.command(name="parse")
# @click.option("--language", "--lang", default="english", help="Mnemonic language")
@click.argument("path", type=click.Path(exists=True))
@click.pass_context
def ts_parse(
    ctx: click.core.Context,
    path: plib.Path,
):
    """
    Parse a file.
    """
    print("ts parse")
    from tree_sitter import Language, Parser
    
    Language.build_library(
      # Store the library in the `build` directory
      'build/my-languages.so',
    
      # Include one or more languages
      [
        # 'vendor/tree-sitter-go',
        # 'vendor/tree-sitter-javascript',
        # 'vendor/tree-sitter-python'
        'tree-sitter-python'
      ]
    )
    PY_LANGUAGE = Language('build/my-languages.so', 'python')
    parser = Parser()
    parser.set_language(PY_LANGUAGE)
    tree = parser.parse(bytes("""
def foo():
    if bar:
        baz()
""", "utf8"))
    root_node = tree.root_node
    # assert root_node.type == 'module'
    # assert root_node.start_point == (1, 0)
    # assert root_node.end_point == (3, 13)
    #
    # function_node = root_node.children[0]
    # assert function_node.type == 'function_definition'
    # assert function_node.child_by_field_name('name').type == 'identifier'
    #
    # function_name_node = function_node.children[1]
    # assert function_name_node.type == 'identifier'
    # assert function_name_node.start_point == (1, 4)
    # assert function_name_node.end_point == (1, 7)
    
    print(root_node.sexp())
    # assert root_node.sexp() == "(module "
    # "(function_definition "
    #    "name: (identifier) "
    #    "parameters: (parameters) "
    #    "body: (block "
    #        "(if_statement "
    #            "condition: (identifier) "
    #            "consequence: (block "
    #                "(expression_statement (call "
    #                    "function: (identifier) "
    #                    "arguments: (argument_list))))))))"
