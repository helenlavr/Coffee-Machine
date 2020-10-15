class Painting:
    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


painting = Painting(input(), input(), input())
print(f'"{painting.title}" by {painting.painter} ({painting.year}) hangs in the Louvre.')
