def encapsulated(*a, **k):
    def decorator(cls):
        class Proxy:
            def __init__(self, *args, **kwargs):
                self.inst = cls(*args, **kwargs)
                if "strict" in k:
                    self.__dict__['strict'] = k['strict']
                else:
                    self.__dict__['strict'] = False
                
            def __call__(self, cls, *args, **kwargs):
                return self.inst

            def __getattr__(self, attr, *args, **kwargs):
                if attr.startswith("__") and not attr.endswith("__") or \
                attr.startswith("_" + self.__class__.__name__ + "__"):
                    raise AttributeError("cannot get private member " + attr + " from here")
                elif attr.startswith("_"):
                    if self.__class__.__qualname__ != "encapsulation.<locals>.decorator.<locals>.Proxy":
                        return getattr(self.inst, attr)
                    else:
                        raise AttributeError("cannot get protected member " + attr + " from here")
                else:
                    return getattr(self.inst, attr)
                
            def __setattr__(self, attr, val):
                # Allow access inside the class
                if attr == 'inst':
                    self.__dict__[attr] = val
                else:
                    if attr.startswith("__") and not attr.endswith("__") or \
                    attr.startswith("_" + self.__class__.__name__ + "__"):
                        raise AttributeError("cannot set private member " + attr + " from here")
                    elif attr.startswith("_"):
                        if self.__class__.__qualname__ != "encapsulation.<locals>.decorator.<locals>.Proxy":
                            if attr in self.inst.__dict__ or not self.__dict__['strict']:
                                self.inst.__dict__[attr] = val
                            else:
                                raise AttributeError(attr + " is not allowed to be added to this class")
                        else:
                            raise AttributeError("cannot set protected member " + attr + " from here")
                    else:
                        if attr in self.inst.__dict__ or not self.__dict__['strict']:
                            self.inst.__dict__[attr] = val
                        else:
                            raise AttributeError(attr + " is not allowed to be added to this class")
           
            def __str__(self):
                return self.inst.__str__()

            def __repr__(self):
                return self.inst.__repr__()
        
        return Proxy
    
    return decorator
