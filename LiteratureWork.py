class Work:
    def __init__(self, name, grade, year, category, author_birth, author_death):
        self.name = name
        self.grade = grade
        self.year = year
        self.category = category
        self.author_birth = author_birth
        self.author_death = author_death
    def __str__(self):
        return "work"