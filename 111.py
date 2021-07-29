# AUTHOR : ACHILLE SAGANG TANWOUO
# QUESTION2 :

class Node:

    def __init__(self, data):
        # this one is the data
        self.data = data

# next pointer
        self.next = None
# precedent pointer :
        self.prec = None




class doublelist:

    def __init__(self):
        ## Here I create the head of my list
        self.head = None

    def insertion(self, new_node):
        ## I create the node we know that on my def init i give None o my head
        ##  so the last node is None because is egal at head
        if self.head:
            ## getting the last node
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

            new_node.prec=last_node
            ## assigning the new node to the next pointer of last node
            last_node.next = new_node

        else:

            self.head = new_node

    def next_movement (self):

        ## this method is no move to normal movement
        print("Normal movement: ", end='-->')

        Mov_node = self.head
        # It's like when the pointer detect the None is move to the next r precedent movement
        while Mov_node != None:
            print(Mov_node.data, end='---> ')
            Mov_node = Mov_node.next
        print()

        ## Is print the reverse movement
        print("Reverse mouvement: ", end='<---')

        ## getting the last node
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        Mov_node = last_node
        while Mov_node != None:
            print(Mov_node.data, end=' <-----')
            Mov_node = Mov_node.prec
        print()

# i test my code
if __name__ == '__main__':

    list = doublelist()

    ## inserting the data into the doublelist
    list.insertion(Node(1))
    list.insertion(Node(2))
    list.insertion(Node(3))
    list.insertion(Node(4))
    list.insertion(Node(5))
    list.insertion(Node(6))
    list.insertion(Node(7))
    list.insertion(Node(8))
    list.insertion(Node(9))

    ## printing the  list
    list.next_movement()
