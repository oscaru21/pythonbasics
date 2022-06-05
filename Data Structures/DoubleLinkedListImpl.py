import collections

linked_list = collections.deque([])

#append is going to insert elements at the tail
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print(linked_list)

#appendleft is going to append elements at the head
linked_list.appendleft(0)
print(linked_list)
