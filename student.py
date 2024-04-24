from mrjob.job import MRJob
from statistics import mean

def get_letter_grade(grade):
    if grade >= 90:
        return 'A+'
    elif grade >= 80:
        return 'A'
    elif grade >= 70:
        return 'B'
    elif grade >= 60:
        return 'C'
    elif grade >= 50:
        return 'D'
    else:
        return 'F'

class GradeConverter(MRJob):

    def mapper(self, _, line):
        if line.strip():
            student_id, grade = map(int, line.split(','))
            yield student_id, grade
        

    def reducer(self, key, grades):
        all_grades = list(grades)
        for i in all_grades:
            yield f'Letter Grade for {key}: ', get_letter_grade(i)
        average_grade = mean(all_grades)
        # yield 'Average Grade:', average_grade
        # yield 'Letter Grade:', get_letter_grade(grades)

if __name__ == '__main__':
    GradeConverter.run()



# python student.py input.txt