class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_average(self):
    return sum(grade.score for grade in self.grades) / len(self.grades)


class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score >= self.minimum_passing:
      return True
    return False
  

roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(20))

for index, grade in enumerate(pieter.grades, start=1):
    print(f"{pieter.name}: idx: {index}, grade: {grade.score} - passing: {grade.is_passing()}")


print(f"{pieter.name}: avarage score: {pieter.get_average()}")