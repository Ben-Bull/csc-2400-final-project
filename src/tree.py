'''
    Author - Ben Bull
    Date of Creation - Nov 20 2026
    Purpose - Serve as tree for the algorithms
'''


class Node:
    def __init__(self, data, level, maxlevel):
        self.data = data
        self.children = []
        self.level = level
        self.maxlevel = maxlevel

#creating all nodes
root = Node("Start", 1, 1)
node_b = Node("Drone Speed", 0, 5)
node_c = Node("Grass Yield", 0, 10)
node_d = Node("Expand Farm Size", 0, 9)
node_e = Node("Plant", 0, 1)
node_f = Node("Carrots", 0, 10)
node_g = Node("Water", 0, 9)
node_h = Node("Trees", 0, 10)
node_i = Node("Fertilizer", 0, 4)
node_j = Node("Sunflowers", 0, 1)
node_k = Node("Pumpkins", 0, 10)
node_l = Node("Mazes", 0, 6)
node_m = Node("Cactus", 0, 6)
node_n = Node("PolyCulture", 0, 5)
node_o = Node("Megafarm", 0, 5)
node_p = Node("Dinosaurs", 0, 6)

#forming the tree
root.children.append(node_b)
root.children.append(node_c)
node_b.children.append(node_d)
node_b.children.append(node_e)
node_e.children.append(node_f)
node_f.children.append(node_g)
node_f.children.append(node_h)
node_g.children.append(node_i)
node_g.children.append(node_j)
node_h.children.append(node_k)
node_i.children.append(node_l)
node_k.children.append(node_m)
node_k.children.append(node_n)
node_l.children.append(node_o)
node_m.children.append(node_p)

# THIS IS TO TEST THAT THE TREE PRINTED CORRECTLY

# print("Tree Data: ")

# print("\nLayer 1: ")
# print(root.data)

# print("\nLayer 2: ")
# for i in root.children:
#     print(i.data)

# print("\nLayer 3: ")
# for i in node_b.children:
#     print(i.data)

# print("\nLayer 4: ")
# for i in node_e.children:
#     print(i.data)

# print("\nLayer 5: ")
# for i in node_f.children:
#     print(i.data)

# print("\nLayer 6: ")
# print("\nChildren of Water: ")
# for i in node_g.children:
#     print(i.data)

# print("\nChildren of Trees: ")
# for i in node_h.children:
#     print(i.data)

# print("\nLayer 7: ")
# print("\nChildren of Fertilizer: ")
# for i in node_i.children:
#     print(i.data)

# print("\nChildren of Pumpkins: ")
# for i in node_k.children:
#     print(i.data)

# print("\nLayer 8: ")
# print("\nChildren of Mazes: ")
# for i in node_l.children:
#     print(i.data)

# print("\nChildren of Cactus: ")
# for i in node_m.children:
#     print(i.data)