class Observable:
    def __init__(self):
        self.__observers = set()

    def subscribe(self, observer):
        self.__observers.add(observer)

    def unsubscribe(self, observer):
        self.__observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.__observers:
            if args and kwargs:
                observer(*args, **kwargs)
            elif args:
                observer(*args)
            elif kwargs:
                observer(**kwargs)
            else:
                observer()

    def observers(self):
        return self.__observers.copy()
    
    def __len__(self):
        return len(self.__observers)
    
    def __bool__(self):
        return bool(self.__observers)

    def __repr__(self):
        return f"Observable({self.__observers})"
    
    def __str__(self):
        return self.__repr__()
    
    def __contains__(self, observer):
        return observer in self.__observers
