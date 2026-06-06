import random 
class dicerollgame:
#Gerar o dado
    def gerar(self):
        nr1=random.randint(1,6)
        nr2=random.randint(1,6)
        return nr1,nr2

    #criar condicao
    def iniciar(self):
        while True:
            escolha=input("Roll the dice: (y/n)?")
            escolhaLista=["y","Y"]
            escolhama=["n","N"]
            
            if escolha in escolhaLista:
                resultado=self.gerar()
                print(resultado)
            
            elif escolha in escolhama:
                print ("thx for playing")
                break 
                
            elif escolha is not escolhaLista:
                print("give me a valid output")
                
jogo=dicerollgame()
jogo.iniciar()
        

    

        
    









