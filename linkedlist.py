
# Projeto 1VA
# HELDON JOSE OLIVEIRA ALBUQUERQUE
# aluno: JOSÉ JONATHAN PEREIRA LIMA
# •
# 16 de ago.
# 100 pontos
# Data de entrega: 30 de ago.
# Desenvolver a LIsta simples e a lista dupla.
# Completar as funções dos arquivos em anexo. E testar.

# Lista Simplesmente Encadeada


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
# .....................................................................................................................#
class LinkedList:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0
# .....................................................................................................................#
    """adicionar elemento ao final da lista"""
    def adicionar(self, elem):
        if self.inicio: # se self.inicio existi faça!
            perc = self.inicio #perc aponta para self.inicio
            while(perc.proximo): # loop = perc.proximo é igual a none? se sim entre
                perc = perc.proximo #loop procurando perc.proximo = none
            perc.proximo = No(elem) # encontrado perc.proximo = none adiciana novo elemento

        else: # se self.inicio não existir faça!
            self.inicio = No(elem) #self.inicio recebe primeiro elemento da lista
        self._tamanho = self._tamanho + 1 #contador
# .....................................................................................................................#
    """Retorna o tamanho da lista"""
    def __len__(self):
        return self._tamanho
# .....................................................................................................................#
    def _getnode(self, indice):
        perc = self.inicio
        for i in range(indice):
            if perc:
                perc = perc.proximo
            else:
                raise IndexError("list index out of range") #return None
        return perc
# .....................................................................................................................#
    def set(self, indice, elem):
        # lista.set(5, 9)
        pass
# .....................................................................................................................#
    def __getitem__(self, indice):
        # a = lista[6]
        perc = self._getnode(indice)
        if perc:
            return perc.dado
        else:
            raise IndexError("list index out of range")
# .....................................................................................................................#
    def __setitem__(self, indice, elem):
        # lista[5] = 9
        perc = self._getnode(indice)
        if perc:
            perc.dado = elem
        else:
            raise IndexError("list index out of range")
# .....................................................................................................................#
    """Retorna o índice do elem na lista"""
    def indice(self, elem):
        perc = self.inicio #perc aponta para self.inicio
        i = 0 #indice recebe 0
        while(perc): #enquanto perc for perc faça! (loop)
            if perc.dado == elem: #se perc.dado for igual ao elemento escolhido entao faça!
                return i   #retorne o indice do elemento da lsita escolhido
            perc = perc.proximo #movimenta perc para proximo
            i = i+1 #adiciona mais um indice ao contador
        raise ValueError("{} is not in list".format(elem)) #retorna um erro
# .....................................................................................................................#
    """inserir elementos em qualquer posicao da lista"""
    def inserir(self, indice, elem):

        no = No(elem) #no recebe a classe No com o novo elemento inserido
        if indice == 0: #se indice inserido for igual a 0 faça
            no.proximo = self.inicio #proximo recebe o antigo primeiro elemento que agora passa a ser o segundo(proximo)
            self.inicio = no #inicio agora recebe novo elemento que está em "no" que passa a ser o novo primeiro elemento

        else:
            perc = self._getnode(indice-1)
            no.proximo = perc.proximo
            perc.proximo = no
        self._tamanho = self._tamanho + 1
# .....................................................................................................................#
    """Remover elementos na lista"""
    def remover_elem(self, elem):
        if self.inicio == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.inicio.dado == elem:
            self.inicio = self.inicio.proximo
            self._tamanho = self._tamanho - 1
            return True
        else:
            antecessor = self.inicio
            perc = self.inicio.proximo
            while(perc):
                if perc.dado == elem:
                    antecessor.proximo = perc.proximo
                    perc.proximo = None
                    self._tamanho = self._tamanho - 1
                    return True
                antecessor = perc
                perc = perc.proximo
        raise ValueError("{} is not in list".format(elem))
# .....................................................................................................................#
    def __repr__(self):
        r = "["
        perc = self.inicio
        while perc.proximo:
            r += f' {perc.dado}, '
            perc = perc.proximo
        r += f'{perc.dado} ]'
        return r
# .....................................................................................................................#
    def __str__(self):
        return self.__repr__()
# .....................................................................................................................#
    """Remover elementos na lista pelo index"""
    def remover_index(self, index):
        if index == 0:
            aux = self.inicio
            self.inicio = aux.proximo
        else:
            perc = self.inicio
            aux = perc
            for i in range(index):
                perc = perc.proximo
            for i in range(index - 1):
                aux = aux.proximo
            aux.proximo = perc.proximo
            perc.proximo = None
# .....................................................................................................................#
    """Buscar elementos repetidos na lista"""
    def buscar_valores_repetidos(self):
        comeco = self.inicio
        perc = self.inicio

        for c in range(self._tamanho - 1):
            P = False
            cont = 0
            aux = comeco
            num = perc.dado

            for i  in range(self._tamanho - 1):
                if aux.dado == num:
                    cont += 1
                    if cont > 1:
                        print(f'{num}', end='...')
                        P = True

                aux = aux.proximo
            perc = perc.proximo
            if P:
                print()

# .....................................................................................................................#
    """Ordenar lista"""
    def ordernar(self, crescente=True):
        lista = LinkedList()
        fim = self._tamanho
        while fim > 0:
            i = 0
            while i < fim:
                pass
# .....................................................................................................................#
    """Editar item da lista"""
    def editar_item(self,index,novo_valor):
        if index == 0:
            self.inicio.dado = novo_valor

        else:
            perc = self.inicio
            for i in range(index):
                perc = perc.proximo
            perc.dado = novo_valor
# .....................................................................................................................#
if __name__ == '__main__':
    lista = LinkedList()
    lista.adicionar(15)
    print(f'adicionado elemento a lista\n{lista} ')
    lista.adicionar(20)
    print(f'adicionado elemento ao final da lista \n{lista}')
    lista.adicionar(30)
    print(f'adicionado elemento ao final da lista \n{lista}')
    lista.adicionar(40)
    print(f'adicionado elemento ao final da lista \n{lista}')
    lista.inserir(1, 20)
    print(f'inserido elemento \n{lista}')
    lista.editar_item(2, 15)
    print(f'editado elemento da lista \n{lista}')
    lista.inserir(3, 300)
    print(f'inserido elemento \n{lista}')
    lista.remover_index(3)
    print(f'removido um elemento da lista por index \n{lista}')
    lista.remover_elem(30)
    print(f'removido um elemento da lista \n{lista}')
    print("valores repetidos sao:")
    lista.buscar_valores_repetidos()










