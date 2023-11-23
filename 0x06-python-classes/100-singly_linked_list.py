#!/usr/bin/python3

"""class Node that defines a node of a singly linked list"""


class Node:
    """class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize the Node instance.

        Args:
            data (int): data to be stored in a node, it must be an integer.
            next_node (Node type): next node on SLL, it must be a Node,
                and can be None.

        Raises:
            TypeError: if the given next_node is not a Node type or
                it is not a None value.
        """
        self.data = data
        self.next_node = next_node

    # data's getter and setter
    @property
    def data(self):
        """Get the data of the courant node

        Returns:
            int : the courant node's data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """Set the the data of the courant node

        Args:
            value (int): The new data of the courant node
                Must be a integer.

        Raises:
            TypeError: If the given data is not integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    # next_node's getter and setter
    @property
    def next_node(self):
        """Get the next_node of the SLL

        Returns:
            Node : next_node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the the next_node of the SLL
        Args:
            value (Node): The new next_node of the SLL
                Must be a Node type or None.

        Raises:
            TypeError: If the given next_node is not a Node type,
                or not a None value.
        """

        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""SinglyLinkedList that defines a singly linked list"""


class SinglyLinkedList:

    """SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """Initialize the head of the SLL instance

        Args:
            head (SinglyLinkedList): the head of the SLL

        """

        self.__head = None

    def sorted_insert(self, value):
        """Insert a value into the singly linked list in sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new = Node(value)

        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        cur = self.__head
        while cur.next_node and value > cur.next_node.data:
            cur = cur.next_node

        if cur == self.__head:
            if value < cur.data:
                new.next_node = cur
                self.__head = new
            else:
                new.next_node = cur.next_node
                cur.next_node = new
        elif cur.next_node is None:
            cur.next_node = new
            new.next_node = None
        else:
            new.next_node = cur.next_node
            cur.next_node = new

        return

    def __str__(self):
        courant = self.__head
        st = ""
        while courant:
            st += str(courant.data) + "\n"
            courant = courant.next_node
        return st[:-1]
