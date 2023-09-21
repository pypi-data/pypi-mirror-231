"""
main
"""
import os
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch

from pypowerline.static import DESCRIPTION, APP_NAME, VERSION_STR


@register_endpoint(
    configs=[],
    description="do bash",
)
def bash() -> None:
    cwd = os.getcwd()
    print(f"{cwd} > ", end="")


@register_endpoint(
    configs=[],
    description="print special symbols (used for development)",
)
def dump_symbols() -> None:
    symbols = {
        'detached': '\u2693',
        'ahead': '\u2B06',
        'behind': '\u2B07',
        'staged': '\u2714',
        'changed': '\u270E',
        'new': '?',
        'conflicted': '\u273C',
        'stash': '\u2398',
        'git': '\uE0A0',
        'hg': '\u263F',
        'bzr': '\u2B61\u20DF',
        'fossil': '\u2332',
        'svn': '\u2446'
    }
    for k, v in symbols.items():
        print(k, v)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
