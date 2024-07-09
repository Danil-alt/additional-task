students = {'Maksim', 'Denis', 'Artem', 'Natasha', 'Vlad', "Camila"}
grades = [[3,5,4,4,4,5], [4,4,5,5,4,3,], [2,3,3,3,4,2], [5,5,5,4,5,4], [4,4,3,5,4,4], [5,4,5,4,4,3]]
grades_s = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]), sum(grades[5])/len(grades[5])]
students_sor = sorted(students)
a = dict(zip(students_sor,grades_s))
print(a)