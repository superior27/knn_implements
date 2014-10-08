#-*- coding:utf-8-*-
from numpy import loadtxt
import numpy as np
from matplotlib import pyplot as plt
import matplotlib



def class2int(s):
    if s == 'Iris-setosa':
        return 0
    elif s == 'Iris-versicolor':
        return 1
    else:
        return 2

def createMyIris():

    n1 = float(raw_input("Digite o primeiro elemento:"))
    my_iris = np.array(n1)

    n1 = float(raw_input("Digite o segundo elemento:"))
    my_iris = np.hstack((my_iris,n1))

    n1 = float(raw_input("Digite o terceiro elemento:"))
    my_iris = np.hstack((my_iris,n1))

    n1 = float(raw_input("Digite o quarto elemento:"))
    my_iris = np.hstack((my_iris,n1))

    print my_iris
    return my_iris

list_iris = loadtxt('iris.txt',delimiter=',',converters={4: lambda s: class2int(s)})
print list_iris

def simple1nnComparation(my_iris): 
    menor = None
    for element_iris in list_iris:
        result0 = (my_iris[0]-element_iris[0])**2
        result1 = (my_iris[1]-element_iris[1])**2
        result2 = (my_iris[2]-element_iris[2])**2
        result3 = (my_iris[3]-element_iris[3])**2
        result = result0+result1+result2+result3
        if menor == None:
            my_iris = np.hstack((my_iris,element_iris[4]))
            menor = result
           
        elif result < menor:
            my_iris[4] = element_iris[4]
            menor = result            
            
    return my_iris

def orderElement(element_iris):
    return element_iris[5]

def orderList(list_iris):
    new_list_iris = []
    for element_iris in list_iris:
        result0 = (my_iris[0]-element_iris[0])**2
        result1 = (my_iris[1]-element_iris[1])**2
        result2 = (my_iris[2]-element_iris[2])**2
        result3 = (my_iris[3]-element_iris[3])**2
        result = result0+result1+result2+result3
        element_iris = np.hstack((element_iris,result))
        new_list_iris.append(element_iris)
    list_iris = np.array(new_list_iris)
    return list_iris

def orderNeighbor(my_dict):
    return my_dict[1]

def chooseNeighbor(new_list_iris,number):
    i = 0
    my_dict = {"0":0,"1":0,"2":0}
    while(i<number):
        
        if new_list_iris[i][4] == 0:
            my_dict["0"]+=1
        
        elif new_list_iris[i][4] == 1:
            my_dict["1"]+=1
        
        else:
            my_dict["2"]+=1
        
        i+=1    
    most_neighbor = sorted(my_dict.items(),key=orderNeighbor,reverse=True)
    return int(most_neighbor[0][0])

def simpleKnnComparation(my_iris):    
    new_list_iris = orderList(list_iris)
    new_list_iris = sorted(new_list_iris,key=orderElement)
    for element_iris in new_list_iris:
        print element_iris
    number = int(raw_input("Informe o número de 'K' 'Vizinhos':"))
    my_iris = np.append(my_iris,chooseNeighbor(new_list_iris,number))   
    print my_iris        
    return my_iris

def plotGraphBeforeClassification(my_iris):
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    red_axis_x = []
    red_axis_y = []
    blue_axis_x = []
    blue_axis_y = []
    green_axis_x = []
    green_axis_y = []
    for element_iris in list_iris:
        if element_iris[4] == 0:
            red_axis_x.append(element_iris[0])
            red_axis_y.append(element_iris[1])            
        elif element_iris[4] == 1:
            blue_axis_x.append(element_iris[0])
            blue_axis_y.append(element_iris[1])            
        else:
            green_axis_x.append(element_iris[0])
            green_axis_y.append(element_iris[1])            
    ax.set_title('From Patterns Using KNN classification')
    ax.plot(red_axis_x,red_axis_y,'o',color="red",label="Classe 1")
    ax.plot(blue_axis_x,blue_axis_y,'x',color="blue",label="Classe 2")
    ax.plot(green_axis_x,green_axis_y,'>',color="green",label="Classe 3")    
    ax.plot(my_iris[0], my_iris[1], '^', color='pink',label="Elemento Teste - Classe ?")    
    ax.set_title('From Patterns Using KNN classification')
    ax.legend()
    plt.show()

def plotGraphAfterClassification(my_iris):
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    red_axis_x = []
    red_axis_y = []
    blue_axis_x = []
    blue_axis_y = []
    green_axis_x = []
    green_axis_y = []
    for element_iris in list_iris:
        if element_iris[4] == 0:
            red_axis_x.append(element_iris[0])
            red_axis_y.append(element_iris[1])            
        elif element_iris[4] == 1:
            blue_axis_x.append(element_iris[0])
            blue_axis_y.append(element_iris[1])            
        else:
            green_axis_x.append(element_iris[0])
            green_axis_y.append(element_iris[1])            
    ax.set_title('From Patterns Using KNN classification')
    ax.plot(red_axis_x,red_axis_y,'o',color="red",label="Classe 1")
    ax.plot(blue_axis_x,blue_axis_y,'x',color="blue",label="Classe 2")
    ax.plot(green_axis_x,green_axis_y,'>',color="green",label="Classe 3")
    my_color = ['red','blue','green']
    ax.plot(my_iris[0], my_iris[1], '^', color=my_color[int(my_iris[4])],label="Elemento Teste - Classe "+str(my_iris[4]+1))
    ax.legend()
    plt.show()

my_iris = createMyIris()
my_iris = simpleKnnComparation(my_iris)
plotGraphBeforeClassification(my_iris)
plotGraphAfterClassification(my_iris)