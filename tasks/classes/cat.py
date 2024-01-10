class Cat:
  def __init__(self, input_name, input_breed, input_age = 0, \
    input_cuddly=True, input_friendly=True):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = input_cuddly
    self.is_friendly = input_friendly
    self.friends = []
  

  def __repr__(self):
    description = f'This {self.breed} cat named {self.name} \
is {self.age} years old.'
    if self.is_cuddly:
      description += f' {self.name} is cuddly cat!'
      description += f' {self.name} has {len(self.friends)} friends!'
    else:
      description += f' {self.name} is not cuddly cat!'
      description += f' {self.name} has {len(self.friends)} friends!'

    return description


  def have_birthday(self):
    self.age += 1
    print(f'{self.name} had a birthday! {self.name} is {self.age} year(s) old.')
  

  def become_friends(self, other_cat):
    if other_cat.is_friendly:
      self.friends.append(other_cat.name)
      print(f'{self.name} become friend with {other_cat.name}.')
    else:
      print(f'{self.name} try to become a friend with {other_cat.name}, \
but {other_cat.name} do not want to be his friend.')


  def number_of_friends(self):
    friends_num = len(self.friends)
    friend = 'friend.' if friends_num == 1 else 'friends.'

    message = f"{self.name} has {friends_num} {friend}"
    return message


cat_one = Cat("Leo", "Tabby", 3)
cat_two = Cat("Meo", "Bengal", 2, input_friendly=False, input_cuddly=False)


print(cat_one)
cat_one.have_birthday()
cat_one.become_friends(cat_two)
print(cat_one.number_of_friends())

print()

print(cat_two)
cat_two.have_birthday()
cat_two.become_friends(cat_one)
print(cat_two.number_of_friends())
