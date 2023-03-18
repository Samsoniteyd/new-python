# class users:
#     def __init__(self, name, age, color, address):
#         self.name= name
#         self.age= age
#         self.color= color
#         self.address = address

#     def greetings(self):
#         return f'my name is {self.name}, i am {self.age} years old, i am {self.color} in completion, living in {self.address}'
    
#     # initialise

# user1= users('Timmy', 20 , 'dark', 'surulere')
# print(user1.greetings())



# class user2(users):
#     def __init__(self, name, age, color, address):
#         self.name= name
#         self.age= age
#         self.color=color
#         self.address= address
#         # self.sex= sex 

#     def gender(self, sex):
#         self.sex= sex

# sam= user2('segun', 20, 'brown', 'ajaokuta')
# sam.gender('female')
# print(sam.sex)        
            

# class cylinder:
#     def __init__(self, pi, radius, height ):
#         self.pi= pi
#         self.radius = radius
#         self.height = height
#         self.area= pi*radius*radius*height


#     def size(self):
#         return f'the area of the small cylinder will be {self.pi} * {self.radius} * {self.height} = {self.area}'
        
#     def med(self):
#         return f'the area of the medium cylinder will be {self.pi} * {self.radius} * {self.height} = {self.area}'
        
#     def big(self):
#         return f'the area of the medium cylinder will be {self.pi} * {self.radius} * {self.height} = {self.area}'
        
# small= cylinder(22/7, 3, 7)
# print(small.size())

# medium = cylinder(27/7, 5, 9)
# print(medium.med())

# bigger = cylinder(27/7, 6, 14)
# print(bigger.big())




class student:
    def __init__(self, first_attendance, second_attendance, third_attendance, forth_attendance):
        self.first_attendance= first_attendance
        self.second_attendance= second_attendance
        self.third_attendance = third_attendance
        self.forth_attendance = forth_attendance
       

        self.total= first_attendance + second_attendance + third_attendance + forth_attendance

        self.average = self.total/4

        self.present = self.total

    def grand(self):
        return f'the average score of the student is {self.first_attendance}+{self.second_attendance}+{self.third_attendance}+{self.forth_attendance} ={self.average}'
    
    def pres(self):
        return f'number of time present is {self.present}'
    
score= student(20, 30, 5, 6)
print(score.grand())

lok= student(20, 30, 5, 6)
print(lok.pres())

        





# class user2:
#     name = 'bless'
    
    
    
#     @classmethod
#     def call(cls):
#         return f'my name is '

# tola= user2()      
# # print(tola.call())
# print(tola.name)


import random


for i in range(4):
    chance=3
    num = random.randint(1, 10)
    guess = int(input('enter any number'))
    

    if (guess == num): 
        print('correct')
        break
    elif guess != num:
        print('incorrect guess')
        print(f'you have {chance-i} chances remaining')
        continue
    else:
        print(f'the correct number is{num}')




