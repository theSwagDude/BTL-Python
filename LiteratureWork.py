class Work:
    def __init__(self, grade, id, name, year, category, author_name, author_birth, author_death, author_home):
        self.grade = grade
        self.name = name
        self.year = year
        self.category = category
        self.author_name = author_name
        self.author_birth = author_birth
        self.author_death = author_death
        self.author_home = author_home
        self.img = "images/" + str(grade) + str(id) + ".jpg"
    def __str__(self):
        return "work"