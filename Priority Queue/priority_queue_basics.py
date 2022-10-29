class Node:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority


class MaxPQ:
    def __init__(self) -> None:
        self.value_list = ["*"]
        print(self.value_list)

    def swap(self, index_1, index_2):
        temp = self.value_list[index_2]
        self.value_list[index_2] = self.value_list[index_1]
        self.value_list[index_1] = temp

    def add_element(self, node):
        self.value_list.append(node)
        queue_length = len(self.value_list)-1
        while(True):
            if int(queue_length / 2) == 0:
                break
            if self.value_list[int(queue_length/2)].value < self.value_list[queue_length].value:
                self.swap(int(queue_length/2), queue_length)
            else:
                break

    def remove_top_element(self, node):
        pass

    def show(self):
        for index in range(1, len(self.value_list)):
            print(self.value_list[index].value)


node_1 = Node("Samuel", 3)
node_2 = Node("Jackson", 4)
node_3 = Node("Elton", 1)
node_4 = Node("John", 2)
node_5 = Node("Simson", 5)
node_6 = Node("Jaqueline", 6)
node_7 = Node("Eric", 8)
node_8 = Node("Abelle", 7)

max_pq = MaxPQ()
max_pq.add_element(node_1)
max_pq.add_element(node_2)
max_pq.add_element(node_3)
max_pq.add_element(node_4)
max_pq.add_element(node_5)
max_pq.add_element(node_6)
max_pq.add_element(node_7)
max_pq.add_element(node_8)

max_pq.show()
