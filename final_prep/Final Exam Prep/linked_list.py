class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_in_order(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        # add at the beginning of the list
        if data < itr.data:
            self.head = Node(data, itr)
            return
        # remove if matching at the beginning of the list
        if data == itr.data:
            # if there is more than one element in the list
            if itr.next is not None:
                self.head = itr.next
                return
            # if there is only one element in the list
            if itr.next is None:
                self.head = None
                return

        while itr:
            # add at the end of the list
            if itr.data < data and itr.next is None:
                itr.next = Node(data, None)
                return

            # add if in the middle of the list
            if itr.data < data < itr.next.data:
                itr.next = Node(data, itr.next)
                return

            # remove if equal
            if itr.next is not None:
                if data == itr.next.data:
                    if itr.next.next is None:
                        itr.next = None
                        return
                    itr.next = itr.next.next
                    return

            itr = itr.next

    def find(self, data):
        if self.head is None:
            return False
        itr = self.head
        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        return False

    def remove(self, data):
        if self.head is None:
            return False  # data does not exists

        # If the node to be deleted is the head node
        if self.head.data == data:
            self.head = self.head.next
            return

        # Find the node to be removed
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                break
            current_node = current_node.next

        # If the node is found, update the link of the previous node
        if current_node.next is not None:
            current_node.next = current_node.next.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ', '
            itr = itr.next
        print(llstr)
