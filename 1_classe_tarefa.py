from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        
    def concluir(self):
        self.feito = True
        
    def __str__(self):
        return f'{self.descricao} (concluida) ' if self.feito else ''
    
    
def main(self):
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
        
    for tarefa in casa:
        print(tarefa)    
    
    
if __name__ == '__main__':
    main()