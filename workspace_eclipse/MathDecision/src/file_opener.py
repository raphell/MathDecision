#encoding: UTF-8
import csv

#Method which permits to return a matrix of marks
def extractMarks(data_raw):
    marks = []

    for ligne in data_raw[1:]:
        ligne = ligne.split(',')[1:]
        marks.append(ligne)
    return marks

#Method which permits to return students numbers
def extractStudentsNumbers(data_raw):
    students_numbers = []
    students_numbers = csv.reader(data_raw, delimiter=',')
    return next(students_numbers)
