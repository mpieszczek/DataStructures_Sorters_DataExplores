class StackSizeReached(Exception):
    pass


class StackEmpty(Exception):
    pass


MAX_SIZE = 1000


class _StackNode:
    def __init__(self, item):
        self.dane = item
        self.next = None


class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def push(self, element):
        if self._size >= MAX_SIZE:
            raise StackSizeReached
        new_node = _StackNode(element)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
        return

    def pop(self):
        if self.is_empty():
            raise StackEmpty
        self._head = self._head.next
        self._size -= 1
        return

    def top(self):
        if self.is_empty():
            raise StackEmpty
        return self._head.dane


class _QueueNode:

    def __init__(self, dane=None, next_node=None):
        self.dane = dane
        self.next_node = next_node

    def __str__(self):
        return str(self.dane)


class Queue:
    # Implementacja kolejki FIFO za pomoca listy dowiazanej. Zobacz do podrecznika Cormen et al.
    def __init__(self):
        # konstruktor - domyslnie zmienne _head (glowa) oraz _tail (ogon) maja specjalna wartosc None
        # rozmiar moze byc przydatny do obslugi bledow oraz sprawdzenia czy kolejka nie jest pusta
        self.size = 0
        self._head = None
        self._tail = None

    def is_empty(self):
        # sprawdzenie czy kolejka FIFO jest pusta
        return self.size == 0

    def enqueue(self, dane):
        # wstawianie do kolejki FIFO - brak obslugi bledow (nadmiar)
        # zapamietujemy poprzdni ogon
        t = self._tail
        # ogonem staje sie nowo wstawiany wezel
        self._tail = _QueueNode(dane)
        # sa dwie mozliwosci
        if self.is_empty():
            # Jesli lista jest pusta, dany wezel staje sie tez pierwszym
            self._head = self._tail
        else:
            # Jesli lista nie jest pusta, nowy wezel ktory jest teraz ogonem podwiazujemy pod poprzedni ogon
            t.next_node = self._tail
        # zwiekszamy liczbe danych w kolejce FIFO
        self.size += 1

    def dequeue(self):
        # usuwanie z kolejki FIFO
        if self.is_empty():
            raise ValueError("Kolejka FIFO jest pusta!")
        # glowa staje sie nastepnik glowy
        self._head = self._head.next_node
        # zmniejszamy liczbe danych w kolejce FIFO
        self.size -= 1
        # to ponizej naprawde nie jest potrzebne, ale jest to dodane dla celow dydaktycznych i przejrzystosci kodu
        if self.is_empty():
            self._tail = None

    def first(self):
        # zwracanie elementu z kolejki FIFO
        if self.is_empty():
            raise ValueError("Kolejka FIFO jest pusta!")
        return self._head.dane


class _BinaryTreeNode:
    def __init__(self, dane=None, left=None, right=None):
        self.dane = dane
        self.left_node = left
        self.right_node = right


class BinaryTree:
    def __init__(self):
        self.korzen = None

    def _inorder(self, drzewo):
        if drzewo is not None:
            self._inorder(drzewo.left_node)
            print(drzewo.dane)
            self._inorder(drzewo.right_node)

    def inorder(self):
        self._inorder(self.korzen)

    def preorder_stack_alt(self):
        stos = Stack()
        stos.push(self.korzen)
        while not stos.is_empty():
            temp_node = stos.top()
            stos.pop()
            if temp_node is not None:
                stos.push(temp_node.right_node)
                stos.push(temp_node.left_node)
                print(temp_node.dane)

    def preorder_stack(self):
        # Wypisujemy tylko liście,
        # ale podczas przeglądania sztucznie
        # dodajemy korzeń do stosu jako liść
        # (wstawiamy bez dzieci), aby w poprawnym momencie się wyświetlił
        stos = Stack()
        stos.push(self.korzen)
        while not stos.is_empty():
            temp_node = stos.top()
            stos.pop()
            if temp_node is not None:
                if temp_node.left_node is None and temp_node.right_node is None:
                    print(temp_node.dane)
                else:
                    temp_dane = temp_node.dane
                    stos.push(temp_node.right_node)
                    stos.push(temp_node.left_node)
                    stos.push(_BinaryTreeNode(temp_dane))

    def postorder_stack(self):

        stos = Stack()
        stos.push(self.korzen)
        while not stos.is_empty():
            temp_node = stos.top()
            stos.pop()
            if temp_node is not None:
                if temp_node.left_node is None and temp_node.right_node is None:
                    print(temp_node.dane)
                else:
                    temp_dane = temp_node.dane
                    stos.push(_BinaryTreeNode(temp_dane))
                    stos.push(temp_node.right_node)
                    stos.push(temp_node.left_node)

    def inorder_stack(self):
        stos = Stack()
        stos.push(self.korzen)
        while not stos.is_empty():
            temp_node = stos.top()
            stos.pop()
            if temp_node is not None:
                if temp_node.left_node is None and temp_node.right_node is None:
                    print(temp_node.dane)
                else:
                    temp_dane = temp_node.dane
                    stos.push(temp_node.right_node)
                    stos.push(_BinaryTreeNode(temp_dane))
                    stos.push(temp_node.left_node)

    def _postorder(self, drzewo):
        # Wypisywanie w porzadku postorder dla korzenia - procedura wewnetrzna
        if drzewo is not None:
            self._postorder(drzewo.left_node)
            self._postorder(drzewo.right_node)
            print(drzewo.dane)

    def preorder(self):
        # Wypisywanie w porzadku postorder dla korzenia - procedura zeewnetrzna
        self._preorder(self.korzen)

    def _preorder(self, drzewo):
        # Wypisywanie w porzadku postorder dla korzenia - procedura wewnetrzna
        if drzewo is not None:
            print(drzewo.dane)
            self._preorder(drzewo.left_node)
            self._preorder(drzewo.right_node)

    def postorder(self):
        # Wypisywanie w porzadku postorder dla korzenia - procedura zeewnetrzna
        self._postorder(self.korzen)

    @staticmethod
    def _breadth_first(drzewo):
        # Wypisywanie metoda przeszukiwania wszerz - procedura wewnetrzna
        # korzystamy z kolejki FIFO (nieistotne jak zaimplementowanej!)
        q = Queue()
        # wkladamy do naszej kolejki FIFO korzen
        q.enqueue(drzewo)

        # odwiedzamy kazdy wezel w drzewie
        while not q.is_empty():
            # wypisujemy i usuwamy to co jest na poczatku kolejki
            node = q.first()
            q.dequeue()
            print(node.dane)
            # i dodajemy dzieci tego wezla do kolejki o ile nie sa puste (czyli "Nonami")
            if node.left_node is not None:
                q.enqueue(node.left_node)
            if node.right_node is not None:
                q.enqueue(node.right_node)

    def breadth_first(self):
        # Wypisywanie metoda przeszukiwania wszerz - procedura zewnetrzna
        self._breadth_first(self.korzen)

    def _w(self, drzewo):
        # wysokosc drzewa
        if drzewo is None:
            return -1
        return max(self._w(drzewo.left_node), self._w(drzewo.right_node)) + 1

    def w(self):
        return self._w(self.korzen)

    def _weight(self, drzewo):
        if drzewo is None:
            return 0
        return 1 + self._weight(drzewo.left_node) + self._weight(drzewo.right_node)

    def weight(self):
        return self._weight(self.korzen)

    def _level0(self, drzewo):
        if drzewo is None:
            return 0
        if drzewo.left_node is None and drzewo.right_node is None:
            return 1
        return self._level0(drzewo.left_node) + self._level0(drzewo.right_node)

    def level0(self):
        return self._level0(self.korzen)

    def _depth(self, drzewo, key):
        non_str = "brak"
        if drzewo is None:
            return non_str
        elif drzewo.dane == key:
            return 0
        right = self._depth(drzewo.right_node, key)
        left = self._depth(drzewo.left_node, key)

        if right != non_str and left != non_str:
            return min([right, left]) + 1
        elif right != non_str:
            return right + 1
        elif left != non_str:
            return left + 1
        else:
            return non_str

    def depth(self, key):
        return self._depth(self.korzen, key)

    def _level2(self, drzewo):
        if drzewo is None:
            return 0
        if drzewo.left_node is None or drzewo.right_node is None:
            return self._level2(drzewo.left_node) + self._level2(drzewo.right_node)
        return 1 + self._level2(drzewo.left_node) + self._level2(drzewo.right_node)

    def level2(self):
        return self._level2(self.korzen)

    def _is_balanced(self, drzewo):
        if abs(drzewo.left_node.depth() - drzewo.right_node.depth())<=1:
            if self._is_balanced(drzewo.left_node) and self._is_balanced(drzewo.right_node):
                return True
        return False
    def is_balanced(self):
        return self._is_balanced(self.korzen)


class _PriorityNode:
    def __init__(self,key = None, dane=None, left=None, right=None):
        self.key = key
        self.dane = dane
        self.left = left
        self.right = right


class PriorityQueue:
    def __init__(self):
        self.korzen = None
    def is_empty(self):
        if self.korzen == None:
            return True
        else:
            return False

    def _insert(self, korzen, key,dane):
        if korzen == None:
            self.korzen = _PriorityNode(key,dane)
        elif key > self.korzen.key:
            if self.korzen.right == None:
                self.korzen.right = _PriorityNode(key, dane)
            else:
                self._insert(korzen.right,key,dane)
        else:
            if self.korzen.left == None:
                self.korzen.left = _PriorityNode(key, dane)
            else:
                self._insert(korzen.left, key, dane)
    def insert(self, key, dane):
        self._insert(self.korzen, key, dane)

    def _maximum(self,korzen):
        if korzen == None:
            return None
        if korzen.right == None:
            return korzen.dane
        else:
            return self._maximum(korzen.right)
    def maximum(self):
        return self._maximum(self.korzen)
    def _delete_max(self,korzen):
        if korzen == None:
            return 0
        if korzen.right == None:
            return 1
        else:
            if self._delete_max(korzen.right) == 1:
                korzen.right = korzen.right.left
        return 0
    def delete_max(self):
        if self._delete_max(self.korzen) == 1:
            self.korzen = self.korzen.left