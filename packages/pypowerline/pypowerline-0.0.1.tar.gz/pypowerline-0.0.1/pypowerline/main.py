"""
main
"""
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch

from pypowerline.static import DESCRIPTION, APP_NAME, VERSION_STR


@register_endpoint(
    configs=[],
    description="do bash",
)
def bash() -> None:
    print("pypowerline> ", end="")


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
