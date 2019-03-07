
#Method which permits to return the sub-matrix of marks of the group given in parameters
def marksGroup(listGroup, marks):
    print("LISTGROUP : ",listGroup)
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))] 
    for i in range(0, len(listGroup) ):
        for j in range(0, len(listGroup) ):
            groupMarks[i][j] = marks[ listGroup[i] ][ listGroup[j] ]
    return groupMarks


#Methods which permits to return medians 2 by 2 of a group of students
#Exemple : 1 -(AR)-> 2, 2-(B)->1, 1-(TB)->3, 3-(I)-> 1
#Return [B, TB]
def groupMedians(groupMarks):
    print("GROUP MARK : ", groupMarks)
    medians = []
    levels = ['AR','I','P','AB','B','TB']
    for i in range(len(groupMarks)):
        for j in range(len(groupMarks[i])):
            if i != j: #condition to eliminate the "-1" value

                #as we have 2 values (mark of the student A on B and reciprocally) , the median is the largest
                print("J : ", j)
                print("I : ", i)
                #we use the table level to do the correspondence
                if levels.index(groupMarks[i][j]) > levels.index(groupMarks[j][i]):
                    median = groupMarks[i][j]
                else:
                    median = groupMarks[j][i]

                medians.append(median)
    return medians


def newGroupMedian(group, marks):
    levels = ['AR','I','P','AB','B','TB']
    print("Calcule mediane du groupe : ", group)
    
    if(group[0]!=-1):
        if(len(group)==2):
            mid = min( levels.index(marks[group[0]][group[1]]) , levels.index(marks[group[1]][group[0]]) )
            print("median groupe : ", levels[mid])
            return levels[mid]
        
        if(len(group)==3):
            result = []
            print("test : ",levels.index(marks[group[0]][group[1]]))
            print("test 2 : ",levels.index(marks[group[1]][group[0]]))
            result.append(min( levels.index(marks[group[0]][group[1]]) , levels.index(marks[group[1]][group[0]]) ) )
            result.append(min( levels.index(marks[group[0]][group[2]]) , levels.index(marks[group[2]][group[0]]) ) )
            result.append(min( levels.index(marks[group[2]][group[1]]) , levels.index(marks[group[1]][group[2]]) ) )
            
            result.sort()
            print("median groupe : ", levels [ result[ round(len(result) / 2) ] ])
            #we get the median (we round up if we have an even number) which corresponds to the value in the middle of our table "medians" (since it is sorted) and we retransform this value into the corresponding level
            return levels [ result[ round(len(result) / 2) ] ]
    else:
        return "N"    

#Method which permits to return the median of the group given in parameters
#Median of groupMedians
def median(listGroup, marks):
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))]
    medians = []
    levels = ['AR','I','P','AB','B','TB']
    print("LIST GROUP : ", listGroup)
    
    for i in listGroup:
        #groupMarks = marksGroup(i, marks)
        #medians.append(groupMedians(groupMarks)) #get medians of each relation in the group 2 by 2
        medians.append(newGroupMedian(i, marks))

    #the matrix of medians is transformed using the matrix of levels in order to be able to sort and calculate the mathematical median
    for i in range(len(medians)):
        if(medians[i]!="N"):
            medians[i] = levels.index(medians[i])
        else:
            return "N"
    medians.sort()

    #we get the median (we round up if we have an even number) which corresponds to the value in the middle of our table "medians" (since it is sorted) and we retransform this value into the corresponding level
    print("MEDIANE repartition : ", levels [ medians[ round(len(medians) / 2) ] ])
    return levels [ medians[ round(len(medians) / 2) ] ]


#Method which returns which group of the list is the best (by using the median)
#To change : we can implement the fact that bestGroup returns more than 1 group
def bestGroup(groups, marks):
    print("GROUPS in BESTGROUP : ", groups)
    levels = ['AR','I','P','AB','B','TB']
    medians = []
    
    for i in range(len(groups)):
        print("AHAH")
        if(median(groups[i], marks)!="N"):
            medians.append(levels.index(median(groups[i], marks)))

    #medians contient les indices de levels

    if(medians!=[]):
        maxi = max(medians) #contient l'indice max de levels
        #maxValue = levels[maxi] #je recupère la valeur qui correspond à l'indice max ex : AB
        indexGroups = medians.index(maxi)
        #grp = []
        #for i in range(len(groups)):
        #    grp.append(median(groups[i], marks))
        #indexGroups = grp.index(maxValue)
        return groups[indexGroups]
    else:
        return[[-1,-1]]

