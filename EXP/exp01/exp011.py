class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return '他的名字是%s,住在%s' % (self.name, self.city)

    def moveto(self, newCity):
        self.city = newCity

    def __lt__(self, other):
        return self.city < other.city


a = People('a', 'cz')
b = People('b', 'sz')
c = People('c', 'wx')
d = People('d', 'nj')
lst1 = [a, b, c, d]
lst1.sort()


class Teacher(People):
    def __init__(self, name, city, school):
        super().__init__(name, city)
        self.school = school

    def moveto(self, newschool):
        self.school = newschool

    def __str__(self):
        return '他的名字是%s,住在%s,在%s就读' % (self.name, self.city, self.school)

    def __lt__(self, other):
        return self.school < other.school


e = Teacher('e', 'cz', 'a')
f = Teacher('f', 'nj', 'b')
g = Teacher('g', 'wx', 'c')
h = Teacher('h', 'sz', 'd')
lst2 = [e, f, g, h]
lst2.sort()
print(e)
e.moveto('Soochow university')
print(e)
