#encoding:UTF_8
from src.degree import *
from src.combinations import *
from src.medianCal import *
from src.file_opener import *
from src.nodes import *
import copy


#Méthode qui fait l'appel récursif(marks)
#Si je n'ai plus personne à caser càd si toutes les cases sont à -1 : j'ai terminé je retourne une liste vide

#sinon (càd j'ai encore des sommets qui n'ont pas été affecté)
#    si je n'ai aucun sommet avec un degré entrant <= 2 : augmente le niveau sur la matrice marks donnée en paramètre (supprimer toutes les âretes du mauvais niveau)

#    si j'ai quelqu'un avec un degré = 0 :
#        je prends la meilleure valeur qui sort de lui (on va l'appeler A) et les sommets concernés (parce qu'il peut y en avoir plusieurs ex : B - C)
#        Je crée une liste avec toutes les combinaisons de 2 et 3 possibles qui contiennent A et ceux de l'autre liste : AB, AC, ABC que j'appelle groupesPossibles

#        je lance un appel récursif sur chaque elements de la liste groupesPossibles
#        pour chaque appel récursif, récupérer la médiane et la comparer aux autres et garder le groupe qui a la meilleure médiane

def initialize(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = tab[i][j].replace('\n',"")
    return tab


def deleteNode(eleve, marks): #Retourne la matrice avec le sommet rempli de -1
    for i in range(len(marks[eleve])):
        if marks[eleve][i] != '-1':
            marks[eleve][i] = '-1'

    for i in range(len(marks)):
        marks[i][eleve] = '-1'
    return marks


def studentAvailable(marks, eleveDejaGroupe):
    available = False
    for student in marks:
        for elem in student:
            if elem != '-1':
                available = True
    if(len(eleveDejaGroupe)!=len(marks)):
        available = True
    return available

def upgrade(level, marks):  # enleve toutes les aretes du niveau donné en paramètre dans la matrice
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            if marks[i][j] == level:
                marks[i][j] = '-1'
    print("upgrade"+level)
    return marks

def createGroup(group, marks): # Delete all nodes from the list of students putted in entry
    print("createGROUPE : ")
    for i in  group:
        print(i)
    print("CREE" )
    for eleve in group:  # Pour chaque élève du group que l'on souhaite former
        marks = deleteNode(eleve,marks)
    return marks




def groupRepartition(marks, levels, index_level, eleveDejaGroupe, originalMarks):
    file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences
    data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
    #print("MATRICE : ")
    #for i in marks:
    #    print(i)
    
    
    originalMarks = extractMarks(data_raw)
    originalMarks = initialize(originalMarks)
    print("NEW ITERATION")
    if not(studentAvailable(marks, eleveDejaGroupe)):
        return []

    else:
        #cas où je n'ai personne qui a de degré inf ou égal à 2

        if not(existsDegreeLessOrEqualTwo(marks, eleveDejaGroupe)):
            print("Pas de DEGRE<2")
            marksUpgraded = upgrade(levels[index_level], marks)
            return groupRepartition(marksUpgraded, levels, index_level+1, eleveDejaGroupe, originalMarks)

        #cas où j'ai quelqu'un avec un degré = 0
        if (existsDegreeEqual(0,marks, eleveDejaGroupe)): # Est-ce quelqu'un a un degré entrant = 0?
            print("y'a un avec 0 arc entrant")
            trees = []
            listIngoingNodesNodes = []
            nodesZero = listNodesDegree(0, marks, eleveDejaGroupe) #get the nodes with a degree = 0
            print("nodes zero : ",nodesZero)
            if len(nodesZero) != 0: # On a d'autre éléments que ceux placés avec un degré inferieur à 0
                listIngoingNodesNodes = listIngoingNodes(nodesZero[0], marks, levels, index_level, originalMarks, eleveDejaGroupe)

                listPossibleCombinations = possibleCombinations(nodesZero[0], listIngoingNodesNodes)
                if(len(listPossibleCombinations)==0):
                    listOutgoingNodesNodes = listOutgoingNodes(nodesZero[0], marks, levels, index_level, originalMarks, eleveDejaGroupe)
                    listPossibleCombinations = possibleCombinations(nodesZero[0], listOutgoingNodesNodes)
                print("possibilités : ")
                for i in  listPossibleCombinations:
                    print(i)
                mediansTrees = []


                #je lance un appel récursif sur chaque elements de la liste groupesPossibles
                for group in listPossibleCombinations:
                    if studentAvailable(marks, eleveDejaGroupe):
                        tempMark = copy.deepcopy(marks)
                        newMarks = createGroup(group, tempMark)
                        #newMarks = upgrade(levels[index_level], newMarks)
                        if studentAvailable(marks, eleveDejaGroupe):
                            print("DEJA GROUPE : ", len(eleveDejaGroupe+group))
                            if (len(eleveDejaGroupe+group)!=len(originalMarks)-1):
                                groupToAdd = groupRepartition(newMarks, levels, index_level, eleveDejaGroupe+group, originalMarks)
                                print("group to add : ",groupToAdd)
                                tree=[]
                                tree.append(group)
                                if(groupToAdd!=[]):
                                    for i in groupToAdd:
                                        if(i!=[]):
                                            tree.append(i)
                                #tree = group + groupToAdd
                                print(tree," AJOUTE A TREES")
                                trees.append(tree)
                            else:
                                print("PAS D AJOUT")
                                tree=[]
                                tree.append([-1,-1])
                                trees.append(tree)

                #pour chaque appel récursif, récupérer la médiane et la comparer aux autres et garder le groupe qui a la meilleure médiane
                #pour chaque appel récursif, on a une répartition. On compare la médiane de chaque répartition et on return la meilleure d'entre elle
                if studentAvailable(marks, eleveDejaGroupe):
                    print("TREEEEEEEES : ", trees)
                    groupe = bestGroup(trees, originalMarks)
                    print("GROUPE choisi comme best: ",groupe)
                    return groupe

        #cas où j'ai quelqu'un avec un degré = 1
        if (existsDegreeEqual(1, marks, eleveDejaGroupe)):

            nodesOne = listNodesDegree(1, marks, eleveDejaGroupe)
            print("y'a un avec 1 arc entrant")
            print("nodes one : ",nodesOne)
            listIngoingNodesNodes = []
            listIngoingNodesNodes = listIngoingNodes(nodesOne[0], marks, levels, index_level, originalMarks, eleveDejaGroupe)
            listPossibleCombinations = possibleCombinations(nodesOne[0], listIngoingNodesNodes)
            print("possibilités : ")
            for i in  listPossibleCombinations:
                print(i)
            trees = []

            for group in listPossibleCombinations:
                if studentAvailable(marks, eleveDejaGroupe):
                    if (len(eleveDejaGroupe+group)!=len(originalMarks)-1):
                        tempMark = copy.deepcopy(marks)
                        newMarks = createGroup(group, tempMark) # On ajoute le nouveau groupe
                        #newMarks = upgrade(levels[index_level], newMarks)
                        #print("group will be added to tree")
                        tree = []
                        tree.append(group)
                        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        groupToAdd = groupRepartition(newMarks, levels, index_level, eleveDejaGroupe+group, originalMarks)
                        print("group to add : ",groupToAdd)
                        if(groupToAdd!=[]):
                            for i in groupToAdd:
                                if(i!=[]):
                                    tree.append(i)
                        #tree = group + groupRepartition(newMarks, levels, index_level, eleveDejaGroupe+group, originalMarks)
                        print("THE TREE CREATED : ",tree)
                        print(tree," AJOUTE A TREES")
                        trees.append(tree)
                    else:
                        print("PAS D AJOUT")
                        tree = []
                        tree.append([-1, -1])
                        trees.append(tree)
                        

            if studentAvailable(marks, eleveDejaGroupe):
                groupe = bestGroup(trees, originalMarks)
                #print("GROUPE : "+groupe)
                return groupe

        #cas où j'ai quelqu'un avec un degré = 2
        if (existsDegreeEqual(2, marks, eleveDejaGroupe)):
            nodesTwo = listNodesDegree(2, marks, eleveDejaGroupe) #On cherche les noeuds avec un degré entrant égal à 2
            print("y'a un avec 2 arc entrants")
            print("nodes two : ",nodesTwo)
            listIngoingNodesNodes = []
            listIngoingNodesNodes = listIngoingNodes(nodesTwo[0], marks, levels, index_level, originalMarks, eleveDejaGroupe) #On récupère les noeuds qui pointent vers lui

            listPossibleCombinations = possibleCombinations(nodesTwo[0], listIngoingNodesNodes)
            print("possibilités : ")
            for i in  listPossibleCombinations:
                print(i)
            mediansTrees = []
            trees = []

            for group in listPossibleCombinations:
                tempMark = copy.deepcopy(marks)
                if studentAvailable(marks, eleveDejaGroupe):
                    newMarks = createGroup(group, tempMark)
                    #newMarks = upgrade(levels[index_level], newMarks)
                    if studentAvailable(marks, eleveDejaGroupe):
                        if (len(eleveDejaGroupe+group)!=len(originalMarks)-1):
                            tree = []
                            tree.append(group)
                            groupToAdd = groupRepartition(newMarks, levels, index_level, eleveDejaGroupe+group, originalMarks)
                            print("group to add : ",groupToAdd)
                            if(groupToAdd!=[]):
                                for i in groupToAdd:
                                    if(i!=[]):
                                        tree.append(i)
                            print(tree,"AJOUTE A TREES")
                            trees.append(tree)
                        else:
                            print("PAS D AJOUT a")
                            tree=[]
                            tree.append([-1,-1])
                            trees.append(tree)

            if studentAvailable(marks, eleveDejaGroupe):
                groupe = bestGroup(trees, originalMarks)
                print("GROUPE : ",groupe)
                return groupe


#=================================     MAIN      ======================================

file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences
data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
marks = extractMarks(data_raw)
marks = initialize(marks)
originalMarks = extractMarks(data_raw)
originalMarks = initialize(originalMarks)

levels = ['AR','I','P','AB','B','TB']
index_level = 0
print("Main, debut du programme ----------------------------------------------------------")
groupsTest = groupRepartition(marks, levels, index_level, [], originalMarks)
print("La répartition est : ")
print(groupsTest)
