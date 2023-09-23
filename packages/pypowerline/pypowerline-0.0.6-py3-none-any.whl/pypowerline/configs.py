"""
All configurations for pypowerline
"""
import os

from pytconf import Config, ParamCreator


class ConfigDummy(Config):
    """
    Parameters for configuring the separator
    """
    separator = ParamCreator.create_str(
        help_string="What is the path separator?",
        default=os.pathsep,
    )
