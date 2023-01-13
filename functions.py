

class Functions:
    def __init__(self):
        self.last_semester = []
        self.classes = []
        self.attributed = []

    def file_man(self):
        vector = []
        
        i = 0

        with open("file.txt", "r") as file:
            content = file.read().split('*')

            for x in content:
                vector.append(x.split('?'))

            last_semester = vector[0]
            classes = vector[1]
            attributed = vector[2]

            for x in last_semester:
                self.last_semester.append(x.split('\n'))
            for x in classes:
                self.classes.append(x.split('\n'))
            for x in attributed:
                self.attributed .append(x.split('\n'))
            for x in self.last_semester:
                x.pop()
                x.pop(0)
            self.last_semester.pop()
            for x in self.classes:
                x.pop()
                x.pop(0)
            for x in self.attributed:
                x.pop()
                x.pop(0)
            self.attributed.pop()

            
            


    def graph(self):

        for i in range(len(self.classes)):  # percorre os horarios
            
           
            for j in range(len(self.classes[i])): # percorre as turmas dentro de um horario
                
                
                
                for m in range (len(self.attributed)):#percorre os professores
                
                    bool = True   
                    for w in range (len(self.last_semester[m])):
                        if self.classes[i][j] == self.last_semester[m][w]:
                            bool = False
                            break
                    for k in range(len(self.attributed[m])): #percorre as turmas dos professores
                        if self.classes[i][j] == self.attributed[m][k]:
                           
                            bool = False
                            
                            break
                    
                    for n in self.attributed[m]: #percorre as turmas do professor m
                        
                        if n in self.classes[i]:
                            
                            bool = False
             
                            break
                    
                         
                    if bool == True:
                        self.attributed[m].append(self.classes[i][j])
                        
                        break
        print (self.attributed)


if __name__ == "__main__":
    func = Functions()
    func.file_man()
    func.graph()
