"""
Generic provides a set of generic abstract entities not covered by the platform specific node types.
"""

from diagrams import Node


class _Generic(Node):
    _provider = "generic"
    _icon_dir = "resources/generic"

    fontcolor = "#2d3436"
