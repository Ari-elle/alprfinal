class Driver:
    """
    Driver data
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def clone(self):
        d = {}
        for x in self.attributeNames:
            d[x] = getattr(self, x, None)
        return Driver(**d)


  
    
