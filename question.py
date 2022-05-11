import json 
quest=dict()
while(True) :
    quest["level"]=input('donner level')
    quest["theme"]=input('donner theme ')
    quest["question"]=input('donner la question')
    l=[]
    for i in range(4) :
        l.append(input('donner les reponses'))
    quest["answers"]=l
    quest["correct"]=input("donner la correcte reponse")
    a=input("tapez o si vous voulez ajouter une autre question sinon tapez n")
    
    with open('data.json', 'a') as question:
        json.dump(quest,question)
    if (a=="n") :
        break
    




    
