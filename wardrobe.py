

class ClothingItem:

    SHORT_SLEEVE_SHIRT, LONG_SLEEVE_SHIRT, SHORTS, PANTS, SHOES, HAT, ACCESSORY = range(7)

    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

    def get_type(self):
        return self.type

    def get_colour(self):
        return self.colour



class Wardrobe:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

