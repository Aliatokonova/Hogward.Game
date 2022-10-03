class Hogwarts:
    faculties = {
        'courage' :'Griffindor',
        'intelligence': 'Ravenclaw',
        'justice': 'Hufflepuff',
        'ambitian':'Slytherin'
    }


    def __init__(self,courage,intelligence,justice,ambitian):
        self.courage = courage
        self.intelligence = intelligence
        self.justice = justice
        self.ambitian = ambitian
        self.faculties_dictionary = locals()
        


    def sorting_hat(self):
        dictionary = {val:key for key,val in self.faculties_dictionary.items() if type(val) == int}
        maximum_point = max(dictionary.keys())
        maximum_quality= dictionary[maximum_point]
        self.faculty = Hogwarts.faculties[maximum_quality]
        print(f'{self.faculty}!!')

student = Hogwarts(5,8,6,7)
student1 = Hogwarts(10,8,6,12)
student3 = Hogwarts(5,8,10,7)
student = Hogwarts(5,16,6,17)


student.sorting_hat()
student1.sorting_hat()
student3.sorting_hat()