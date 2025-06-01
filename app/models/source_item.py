class SourceItem:
    """
    Represents a trusted source item loaded from YAML.
    """
    def __init__(self, name, url, description=None, **kwargs):
        self.name = name
        self.url = url
        self.description = description
        # Store any additional fields
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"<SourceItem name={self.name} url={self.url}>"