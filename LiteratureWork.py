class Work:
    def __init__(self, name, year, category, author_birth, author_death, author_home):
        self.name = name
        self.year = year
        self.category = category
        self.author_birth = author_birth
        self.author_death = author_death
        self.author_home = author_home
    def __str__(self):
        return "work"