#Method which permits to return the incoming degree of a vertex ( = student)
def incomingDegree(student, marks):
    degree = 0
    columnStudent = []
    for ligne in marks:
        columnStudent.append(ligne[student])


    for i in range(0, len(columnStudent) ):
        if columnStudent[i] != '-1':
            degree = degree + 1
    #print("student %s degree %s",student, degree)
    return degree


#Method which returns true if it exists a node with a degree <= 2
def existsDegreeLessOrEqualTwo(marks, eleveDejaGroupe):
    i = 0
    found = False
    while i < len(marks) and not(found):
        if i not in eleveDejaGroupe:
            if incomingDegree(i, marks) <= 2:
                found = True
        i = i + 1
    return found


#Method which returns true if it exists at least a node with a degree == parameter
def existsDegreeEqual(degree, marks, eleveDejaGroupe):
    i = 0
    found = False
    while i < len(marks) and not(found):
        if i not in eleveDejaGroupe:
            if incomingDegree(i, marks) == degree:
                found = True
        i = i + 1
    return found


#Method which returns the list of vertex (students) with an incoming degree == to the parameter
def listNodesDegree(degree, marks, eleveDejaGroupe):
    nodesDegree = []

    for i in range(len(marks)):
        if i not in eleveDejaGroupe:
            if incomingDegree(i, marks) == degree:
                nodesDegree.append(i)
        
    return nodesDegree
