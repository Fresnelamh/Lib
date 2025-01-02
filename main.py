print("Bienvenue dans notre Bibliothèque estudiantine:\n"
      "1:Ajouter un livre\n"
      "2:Afficher la liste des livres disponibles\n"
      "3:Emprunter un livre\n"
      "4:Retourner un livre\n"
      "5:Quitter\n" )




class Book():
    def __init__(self,titre,auteur):
        self.titre=titre
        self.auteur=auteur
        self.statut=True

    def afficher_infos(self):
        print ("Le titre du livre est " + self.titre + " et son auteur se nomme " +self.auteur + ". Le livre est " +self.statut)

    def emprunter(self):
        self.statut=False

    def retourner(self):
        self.statut=True



class Bibliothèque():
    def __init__(self):
        self.livres=[]
   
   
    def  ajouter_livre(self):


        Addbooktitle=str(input("Veuillez saisir le titre du livre à ajouter : "))
        Addbookautor=str(input("Veuillez saisir l'auteur du livre: "))
        
       
        self.livres.append(Book(Addbooktitle,Addbookautor))
    
    def afficher_livres_disponibles(self):
        print("Liste des livres disponibles:")
        for x in self.livres:
           if x.statut==True:
              print(x.titre)


    def emprunter_livre(self):

        E_livre=str(input("Veuillez saisir le titre du livre à emprunter :"))
        for x in self.livres:
            if x.titre==E_livre and x.statut==True:
                x.emprunter()

        print("Le livre a été emprunté avec succès ")
    

    def retourner_livres(self):
        R_livre=str(input("Veuillez saisir le titre du livre à retourner :"))
        for x in self.livres:
            if x.titre==R_livre and x.statut==False:
                x.retourner()
        print("Le livre a été retourné avec succès")

    
my_library=Bibliothèque()



def ourmainfunction():

 OPTION=int(input("Choisissez une option: "))

 if OPTION==1:
    my_library.ajouter_livre()

 elif  OPTION==2:
     my_library.afficher_livres_disponibles()


 elif OPTION==3:
      my_library.emprunter_livre()

 elif OPTION==4:
      my_library.retourner_livres()

 elif OPTION==5:
   print("Vous êtes sur le point de quitter le jeu !")
   confirm=str(input("Répondez par OUI ou NON !"))
   if confirm=="OUI":
       exit()
   
       
   

 else:
   print("Option indisponible")



while True:
    
   ourmainfunction()
    