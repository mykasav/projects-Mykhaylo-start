import random
class guessNR:
    def gerarnr(self):
        nr=random.randint(1,100)
        return nr
    
    def comparar(self,nr,guess):
        if nr==guess:
            return "Acertou"
        elif nr<guess:
            return "Mais baixo"
        elif nr>guess:
            return "Mais  alto"
 
    
    def iniciar(self):
        
        nr=self.gerarnr()
        while True:
            try:
                escolha = int(input("Adivinhe o número (1-100): "))
                resultado = self.comparar(nr,escolha)
                print(resultado)
                
                if resultado == "Acertou":
                    break
            except ValueError:
                print("Por favor, digite um número válido.")
jogo=guessNR()

jogo.iniciar()

        
    