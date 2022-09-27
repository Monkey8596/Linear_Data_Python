from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.tamaño = 0


    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node
            self.tamaño +=1


    def insert_value_from_list(self, data_list):
        """Agrega los datos de una lista al LinkedList"""
        for data in data_list:
            self.append(data)
        current = datos.tail

        while current:
            print(current.data)
            current = current.next


    def size(self):
        print("The size of the LinkedList is:")
        return str(self.tamaño)


    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val


    def delete(self, data):
        current = self.tail
        prev =current

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                    self.tamaño -= 1
                return  print(f"The {current.data} was delete")
            else:
                prev = current
                current = current.next
        print(f"The {data} was not found to delete")


    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"The {data} was found!")


    def display_list(self):
        """Muestra los datos del LinkedList"""
        for node in self.iter():
            print(node)


    def clear(self):
        self.tail = None
        self.head = None
        self.tamaño = 0


if __name__ == "__main__":

    zoo = ["oso","gato","perro","lion"]
    datos = SinglyLinkedList()

    print("LinkedList...")
    datos.insert_value_from_list(zoo)
    print("\n")
    print("Borrando elemento de la LinkedList (perro)")
    datos.delete("perro")
    print("Mostrando lo que queda de la LinkedList...\n")
    datos.display_list()