#!/usr/bin/python
# -*- coding: utf-8 -*

class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        """
        Retorna o primeiro nó se existir, caso contrário retorna None
        """
        return self._head.value if self._head is not None else None

    @property
    def tail(self):
        """
        Retorna o último nó se existir, caso contrátio retorna None
        """
        return self._tail.value if self._tail is not None else None

    def append(self, value):
        """
        Adiciona um nó ao FINAL da lista ligada. 
        Atualiza os apontadores _head, _tail e o contador _len. 

        Args:
            value: Valor do nó a ser adicionado na lista ligada
        """

        # Cria o nó:
        new_last_node = LinkedListNode(value)

        # Caso a lista esteja vazia, o nó adicionado será o primeiro e último
        if self._tail is None:
            self._head = new_last_node
            self._tail = new_last_node

        # Caso contrário, adicione o novo nó como próximo item depois do ponteiro final e 
        # atualize o ponteiro _tail
        else:
            self._tail.next = new_last_node
            self._tail = new_last_node
        
        # Ao fim, a lista ligada terá um elemento a mais
        self._len += 1
        

    def insert(self, value):
        """
        Adiciona um nó ao INÍCIO da lista ligada. 
        Atualiza os apontadores _head, _tail e o contador _len. 

        Args:
            value: Valor do nó a ser adicionado na lista ligada
        """

        # Cria o nó:
        new_first_node = LinkedListNode(value) 

        # Caso a lista esteja vazia, o nó adicionado será o primeiro e último
        if self._head is None:
            self._head = new_first_node
            self._tail = new_first_node
        
        # Caso contrário, adicione o nó do ponteiro _head como próximo item do novo nó e 
        # atualize o ponteiro _head com o valor do novo nó
        else:
            new_first_node.next = self._head
            self._head = new_first_node

        # Ao fim, a lista ligada terá um elemento a mais
        self._len +=1

    def removeFirst(self):
        """
        Remove o primeiro elemento da lista ligada.

        Retorna:
            O valor do primeiro elemento a ser removido
        """
        first_node = None
        
        # Caso exista um primeiro nó, pegue seu valor e use o seu próximo
        # como novo ponteiro _head
        if self._head is not None:
            first_node = self._head.value
            self._head = self._head.next

            # Caso a lista seja de um único elemento, o novo ponteiro
            # _head e _head serão vazio e
            if self._head is None:
                self._tail = None
            
            # Ao fim, a lista ligada terá um elemento a menos
            self._len -= 1

        return first_node               

    def getValueAt(self, index):
        """
        Pega o valor de um nó na posiçao definida pelo index.
        
        Args:
            index: Índice do nó a ser retornado
        
        Retorna:
            O valor do nó na posição do index.
        """

        # Caso o index seja maior ou igual ao tamanho da lista ligada 
        # ou ainda caso seja negativo, retorne OutOfBoundsException
        if index >= self._len or index < 0:
            raise OutOfBoundsException("Index out of bounds!")
        
        # Caso contrátio, defina o nó do ponteiro inicial:
        node = self._head

        # Avança nos itens da lista ligada até chegar ao índice desejado
        for i in range(index):
            node = node.next
            
        # Ao final, retorne o valor do nó na posição do index
        return node.value


    def toList(self):
        """
        Cria uma lista a partir de uma lista ligada.

        Retorna:
            Lista criada
        """
        list = []
        
        # Seta o ponteiro inicial como atual nó
        node = self._head

        # Enquando o nó atual não for vazio, adiciona ele a lista 
        # e atualiza o nó atual como o próximo elemento.
        while node is not None:
            list.append(node.value)
            node = node.next
        
        # Ao fim retorne a lista baseada na lista ligada.
        return list



if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert(ll.head is None)
    assert(ll.tail is None)
    assert(ll.toList() == [])
    ll.append(1)
    assert(ll.head == 1)
    assert(ll.tail == 1)
    assert(len(ll) == 1)
    assert(ll.toList() == [1])
    ll.append(2)
    assert(ll.head == 1)
    assert(ll.tail == 2)
    assert(len(ll) == 2)
    assert(ll.toList() == [1, 2])
    ll.append(3)
    assert(ll.head == 1)
    assert(ll.tail == 3)
    assert(len(ll) == 3)
    assert(ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert(ll.head == 0)
    assert(ll.tail == 3)
    assert(len(ll) == 4)
    assert(ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert(ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == -1)
    assert(ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == 0)
    assert(ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert(v == 1)
    assert(ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert(v == 2)
    assert(ll.toList() == [3])
    v = ll.removeFirst()
    assert(v == 3)
    assert(ll.toList() == [])
    assert(len(ll) == 0)
    print("100%")