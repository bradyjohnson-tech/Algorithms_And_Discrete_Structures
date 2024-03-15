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


    def swapNodes(self, key_1, key_2):
        if key_1 == key_2:   # if the keys are same then there's nothing to swap
            return -1

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:  # search for the key_1 in the linked list
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:  # search for the key_2 in the linked list
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:    # if either `key_1` or `key_2` were not there in the linked list.
            return -1

        if prev_1:
            prev_1.next = curr_2
        else:    # make `curr_2` the new head
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:    # make `curr_1` the new head
            self.head = curr_1

        # Swap next pointers
        temp = curr_1.next
        curr_1.next = curr_2.next
        curr_2.next = temp


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

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(20)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.insert_at_end(60)
    ll.insert_at_end(70)
    ll.print()

    print(ll.swapNodes(50,60))
    print(ll.swapNodes(70, 80))

    ll.print()

