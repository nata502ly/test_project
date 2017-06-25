class Role:
    def __init__(self, name=None, type=None, level=None, book=None, id=None):
        self.name = name
        self.type = type
        self.level = level
        self.book = book
        self.id = id
        self.url = "roles"
    def get_dict(self):
        full_dict = self.__dict__
        return {key:full_dict[key]
                for key in full_dict
                if full_dict is not None and key != "url"}

if __name__ == "__main__":
    b = Role(name = "Underwood", type = "good personage", level = "4", book = "House of Cards", id = 4)
    print(b.__dict__)
    print((b.get_dict()))
