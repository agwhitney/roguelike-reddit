"""Item component. For starters, it doesn't need anything other than to be present.
"""


class Item:
    def __init__(self, use_function=None, **kwargs):
        self.use_function = use_function
        self.function_kwargs = kwargs
