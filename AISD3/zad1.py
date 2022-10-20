from typing import Any

class Node:
    value: Any  #atrybut ten przechowuje wartość z danego węzła "element"
    next: 'Node' #wskaźnik do kolejnego węzła w liście, referencja

    def __init__(self, value: Any) -> None:
        self.value = value


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None #puste

    def push(self, value: Any) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
            selt.tail = node
        else:
            node.next  = self.head #przesuwamy head na kolejna pozycje
            self.head =node
            #tail nie przesuwa sie
#powyzej schemat klasy
