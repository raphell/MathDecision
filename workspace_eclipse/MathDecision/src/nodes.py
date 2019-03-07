#encoding: UTF-8

#Method which permits to return a matrix of marks
def extractMarks(data_raw):
    marks = []

    for ligne in data_raw[1:]:
        ligne = ligne.split(',')[1:]
        marks.append(ligne)
    return marks


def initialize(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = tab[i][j].replace('\n',"")
    return tab

def upgrade(level, marks):  # enleve toutes les aretes du niveau donné en paramètre dans la matrice
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            if marks[i][j] == level:
                marks[i][j] = '-1'
    print("upgrade"+level)
    return marks

def deleteNode(eleve, marks): #Retourne la matrice avec le sommet rempli de -1
    for i in range(len(marks[eleve])):
        if marks[eleve][i] != '-1':
            marks[eleve][i] = '-1'

    for i in range(len(marks)):
        marks[i][eleve] = '-1'
    print("DELETE node : ", eleve)
    return marks


def listIngoingNodes(student, marks, levels, indexlevel, originalMarks, eleveDejaGroupe):
    print("ELEVE DEJA GROUPE : ", eleveDejaGroupe)
    print("calcul du nombre de noeud entrants au niveau : ", indexlevel)
    # srudent = student with degIn() = 0
    ingoingNodes = []
    bestLevel = 0  # The best level is by default on AR

    for i in range(len(marks[student])):  # We look for all the marks of the student
        #print("valeur de i: ", i)

        if marks[i][student] != '-1':
            ingoingNodes.append(i)
    return ingoingNodes


def haveOutgoingNode(student, marks):
    # srudent = student with degIn() = 0
    outgoingNodes = []
    bestLevel = 0  # The best level is by default on AR

    for i in range(len(marks[student])):  # We look for all the marks of the student
        haveOutDegree = False
        if marks[student][i] != '-1':
            haveOutDegree = True
    return haveOutDegree

def listOutgoingNodes(student, marks, levels, indexlevel, originalMarks, eleveDejaGroupe):
    print("ELEVE DEJA GROUPE : ", eleveDejaGroupe)
    print("calcul du nombre de noeud sortants au niveau : ", indexlevel)
    # srudent = student with degIn() = 0
    outgoingNodes = []
    bestLevel = 0  # The best level is by default on AR
    currentMark = bestLevel

    for i in range(len(marks[student])):  # We look for all the marks of the student
        #print("valeur de i: ", i)

        if marks[student][i] == 'AR':
            currentMark = 0
        if marks[student][i] == 'I':
            currentMark = 1
        elif marks[student][i] == 'P':
            currentMark = 2
        elif marks[student][i] == 'AB':
            currentMark = 3
        elif marks[student][i] == 'B':
            currentMark = 4
        elif marks[student][i] == 'TB':
            currentMark = 5


        if currentMark > bestLevel:
            bestLevel = currentMark
    #At the end of the for loop, we've got the best level on the row:
    maxLevel = levels[bestLevel]
    for i in range(len(marks[student])):
        if marks[student][i] == maxLevel:
            outgoingNodes.append(i)
            print(outgoingNodes)
    #Here we have all the students marked by the student at the top of his marking
    
    while(len(outgoingNodes)==0):
        print("on cherche plus profond")
        file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences
        data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
        
        originalMarks = extractMarks(data_raw)
        originalMarks = initialize(originalMarks)
        if indexlevel > 0:
            indexlevel = indexlevel-1 # Possible bug du niveau
        newMarks = list(originalMarks) # on recréé l'ancienne matrice     # POURQUOI FAIRE CETTE LIGNE A BASE DE LISTE ?????????
            
        for i in range(0,indexlevel):
            upgrade(levels[i], newMarks)
        
        for i in eleveDejaGroupe:
            deleteNode(i, newMarks)


        for i in newMarks:
            print(i)
        maxLevel = levels[indexlevel]
        
        for i in range(len(newMarks[student])):
            if newMarks[student][i] == maxLevel:
                outgoingNodes.append(i)
    print("OUTGOIN NODES : ",outgoingNodes)
    return outgoingNodes


levels = ['AR', 'P', 'I', 'AB', 'B', 'TB']
eleveDjaGroup = []
m = [
['-1', 'AB', 'AR','I'],
['B','-1', 'B', 'B'],
['AR','B', '-1', 'TB'],
['B','AR','B','-1']
]

print(listOutgoingNodes(0, m, levels, 0, m, eleveDjaGroup))
