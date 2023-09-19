# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GlobalTheme(Component):
    """A GlobalTheme component.


Keyword arguments:

- children (optional):
    Provide the contents of your GlobalTheme.

- id (optional):
    Specify the DOM element ID of the top-level node.

- theme (optional):
    Specify the theme for your entire project."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_carbon_components'
    _type = 'GlobalTheme'
    @_explicitize_args
    def __init__(self, children=None, theme=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(GlobalTheme, self).__init__(children=children, **args)
