#Projeto 1VA
#HELDON JOSE OLIVEIRA ALBUQUERQUE
#aluno: JOSÉ JONATHAN PEREIRA LIMA
#•
#16 de ago.
#100 pontos
#Data de entrega: 30 de ago.
#Desenvolver a LIsta simples e a lista dupla.
#Completar as funções dos arquivos em anexo. E testar.

#Lista Duplamente Encadeada


class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
    def __str__(self):
        proximo = f', {self.proximo}'
        if self.proximo is None:
            proximo = ''
        return f'{self.valor}{proximo}'
# .....................................................................................................................#
class DoublyLinkedList:
    def __init__(self, tipo=None):
        self.inicio = None
        self.final = None
        self.tamanho = 0
        self.tipo = tipo
    def __str__(self):
        value_list = '['
        perc = self.inicio
        while perc.proximo:
            value_list += f' {perc.valor}, '
            perc = perc.proximo
        value_list += f'{perc.valor} ]'
        return value_list
        # return f'[{self.inicio}]' if self.inicio else '[]'
    def __len__(self):
        return self.tamanho
# .....................................................................................................................#
    def _percorrer(self, perc, count, proximo):
        for i in range(count):
            if proximo:
                perc = perc.proximo
            else:
                perc = perc.anterior
        return perc
    def _get_perc_index(self, index):
        if index >= self.tamanho or index < 0:
            raise IndexError("não existe essa posição")
        if index == 0:
            return self.inicio
        elif index == self.tamanho -1:
            return self.final
        else:
            metade = int(self.tamanho -1 / 2)
            count = 0
            proximo = True
            perc = self.inicio
            if index <= metade:
                count = index - 0
            else:
                proximo=False
                count = (self.tamanho - 1) - index
                perc = self.final
            return self._percorrer(perc, count, proximo)
    def _get_perc_valor(self, valor):
        perc_inicio = self.inicio
        perc_fim = self.final
        c = 0
        c2 = self.tamanho
        while True:
            if perc_inicio.valor == valor:
                return c
            if perc_fim.valor == valor:
                return c2
            if perc_inicio.valor != valor:
                perc_inicio = perc_inicio.proximo
                c += 1
            if perc_fim.valor != valor:
                perc_fim = perc_fim.anterior
                c2 -= 1
    def get_valor(self, index):
        pass
    def get_index(self, valor):
        perc_inicio = self.inicio
        perc_fim = self.final
        #metade = self.tamanho/2
        while perc_inicio != perc_fim:
            if perc_inicio.valor == valor:
                return perc_inicio
            elif perc_fim.valor == valor:
                return perc_fim
            if perc_inicio == perc_fim:
                break
            perc_inicio = perc_inicio.proximo
            if perc_fim == perc_fim:
                break
            perc_fim = perc_fim.anterior
            if perc_inicio == perc_fim:
                break
# .....................................................................................................................#
    def adicionar(self, valor):
        no = _No(valor)
        if self.tamanho == 0:
            self.inicio = no
            self.final = no
        else:
            self.final.proximo = no
            no.anterior = self.final
            self.final = no
        self.tamanho += 1
# .....................................................................................................................#
    def inserir(self, index, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo Invalido a função só aceita tipo:{self.tipo}')
        if index >= self.tamanho:
            self.adicionar(valor)
            return
        no = _No(valor)
        perc = self._get_perc_index(index)
        if index == 0:
            no.proximo = self.inicio
            self.inicio= no
            self.inicio.proximo.anterior = self.inicio
        else:
            aux = perc.anterior
            no.proximo = aux.proximo
            aux.proximo = no
            no.proximo.anterior = no
            no.anterior = aux
        self.tamanho += 1
# .....................................................................................................................#
    def editar_item(self, index, novo_valor):
        perc = self._get_perc_index(index)
        perc.valor = novo_valor
# .....................................................................................................................#
    def remover_item(self, valor):

        perc_valor = self._get_perc_valor(valor)
        perc = self._get_perc_index(perc_valor - 1)
        aux_ant = perc.anterior
        aux_prox = perc.proximo

        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

        elif self.final.valor == valor:
            self.final = self.final.anterior
            self.final.proximo = None

        else:
             aux_ant.proximo = perc.proximo
             aux_prox.anterior = perc.anterior
             perc = perc.proximo

             self.tamanho -= 1
        return perc
# .....................................................................................................................#
    def remover_index(self, index):
        perc = self._get_perc_index(index)
        aux_ant = perc.anterior
        aux_prox = perc.proximo

        if index == 0:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

        elif index == self.tamanho - 1:
            self.final = self.final.anterior
            self.final.proximo = None

        else:
            aux_ant.proximo = perc.proximo
            aux_prox.anterior = perc.anterior

        self.tamanho -= 1
# .....................................................................................................................#
    def buscar_valor_por_index(self, index):
        perc = self._get_perc_index(index)
        return perc.valor
# .....................................................................................................................#
    def buscar_valores_repetidos(self):
        espelho = self.inicio.valor

# .....................................................................................................................#
    def ordernar(self, crescente=True):
        # insertionSort
        pass
# .....................................................................................................................#
if __name__ == '__main__':

    lista = DoublyLinkedList()
    lista.adicionar(5)
    print(f'adicionar elemento {lista.inicio} a lista\n{lista} ')
    lista.adicionar(20)
    print(f'adicionar elemento {lista.inicio.proximo} ao final da lista \n{lista}')
    lista.adicionar(30)
    print(f'adicionar elemento {lista.inicio.proximo.proximo} ao final da lista \n{lista}')
    lista.adicionar(40)
    print(f'adicionar elemento {lista.inicio.proximo.proximo.proximo} ao final da lista \n{lista}')
    print(f'buscar valor por index \n{lista.buscar_valor_por_index(2)}')
    lista.inserir(1, 10)
    print(f'inserido elemento \n{lista}')
    lista.editar_item(1, 15)
    print(f'editado elemento da lista \n{lista}')
    lista.inserir(3, 300)
    print(f'inserido elemento \n{lista}')
    lista.remover_index(2)
    print(f'remover index \n{lista}')
    lista.remover_item(30)
    print(f'remover item \n{lista}')
