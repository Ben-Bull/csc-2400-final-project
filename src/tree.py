'''
    Author - Ben Bull
    Date of Creation - Nov 20 2026
    Purpose - Serve as tree for the algorithms
'''

#node for tree, with each node having an initial level of 0 and costing an item to upgrade
class Node:
    def __init__(self, data, level, maxlevel, ):
        self.data = data
        self.children = []
        self.level = level
        self.maxlevel = maxlevel
        self.cost = []

#list of items used as currency
class Items:
    def __init__(self):
        self.Hay = 0
        self.Wood = 0
        self.Carrot = 0
        self.Pumpkin = 0
        self.Cactus = 0
        self.Gold = 0
        self.Bone = 0

#creating all nodes
root = Node("Start", 1, 1)
node_b = Node("Drone Speed", 0, 5, [
		{Items.Hay: 20},
		{Items.Wood: 20},
		{Items.Wood: 50, Items.Carrot: 50},
		{Items.Carrot: 500},
		{Items.Carrot: 1000}
	])
node_c = Node("Grass Yield", 0, 10, [
		{Items.Hay: 100},
		{Items.Hay: 300},
		{Items.Wood: 500},
		{Items.Wood: 2500},
		{Items.Wood: 12500},
		{Items.Wood: 62500},
		{Items.Wood: 312000},
		{Items.Wood: 1560000},
		{Items.Wood: 7810000},
		{Items.Wood: 39100000}
	])
node_d = Node("Expand Farm Size", 0, 9, [
		{Items.Hay: 30},
		{Items.Wood: 20},
		{Items.Wood: 30, Items.Carrot: 20},
		{Items.Wood: 100, Items.Carrot: 50},
		{Items.Pumpkin: 1000},
		{Items.Pumpkin: 8000},
		{Items.Pumpkin: 64000},
		{Items.Pumpkin: 512000},
		{Items.Pumpkin: 4100000}
	])
node_e = Node("Plant", 0, 1, [{Items.Hay: 50}])
node_f = Node("Carrots", 0, 10, [
		{Items.Wood: 50},
		{Items.Wood: 250},
		{Items.Wood: 1250},
		{Items.Wood: 6250},
		{Items.Wood: 31200},
		{Items.Wood: 156000},
		{Items.Wood: 781000},
		{Items.Wood: 3910000},
		{Items.Wood: 19500000},
		{Items.Wood: 97700000}
	])
node_g = Node("Water", 0, 9, [
		{Items.Wood: 50},
		{Items.Wood: 200},
		{Items.Wood: 800},
		{Items.Wood: 3200},
		{Items.Wood: 12800},
		{Items.Wood: 51200},
		{Items.Wood: 205000},
		{Items.Wood: 819000},
		{Items.Wood: 3280000}
	])
node_h = Node("Trees", 0, 10, [
		{Items.Wood: 50, Items.Carrot: 70},
		{Items.Hay: 300},
		{Items.Hay: 1200},
		{Items.Hay: 4800},
		{Items.Hay: 19200},
		{Items.Hay: 76800},
		{Items.Hay: 307000},
		{Items.Hay: 1230000},
		{Items.Hay: 4920000},
		{Items.Hay: 19700000}
	])
node_i = Node("Fertilizer", 0, 4, [
		{Items.Wood: 500},
		{Items.Wood: 1500},
		{Items.Wood: 9000},
		{Items.Wood: 54000}
	])
node_j = Node("Sunflowers", 0, 1, [{Items.Carrot: 500}])
node_k = Node("Pumpkins", 0, 10, [
		{Items.Wood: 500, Items.Carrot: 200},
		{Items.Carrot: 1000},
		{Items.Carrot: 4000},
		{Items.Carrot: 16000},
		{Items.Carrot: 64000},
		{Items.Carrot: 256000},
		{Items.Carrot: 1020000},
		{Items.Carrot: 4100000},
		{Items.Carrot: 16400000},
		{Items.Carrot: 65500000}
	])
node_l = Node("Mazes", 0, 6, [
		{Items.Weird_Substance: 1000},
		{Items.Cactus: 12000},
		{Items.Cactus: 72000},
		{Items.Cactus: 432000},
		{Items.Cactus: 2590000},
		{Items.Cactus: 15600000}
	])
node_m = Node("Cactus", 0, 6, [
		{Items.Pumpkin: 5000},
		{Items.Pumpkin: 20000},
		{Items.Pumpkin: 120000},
		{Items.Pumpkin: 720000},
		{Items.Pumpkin: 4320000},
		{Items.Pumpkin: 25900000}
	])
node_n = Node("PolyCulture", 0, 5, [
		{Items.Pumpkin: 3000},
		{Items.Bone: 10000},
		{Items.Bone: 50000},
		{Items.Bone: 250000},
		{Items.Bone: 1250000}
	])
node_o = Node("Megafarm", 0, 5, [
		{Items.Gold: 2000},
		{Items.Gold: 8000},
		{Items.Gold: 32000},
		{Items.Gold: 128000},
		{Items.Gold: 512000}
	])
node_p = Node("Dinosaurs", 0, 6, [
		{Items.Cactus: 2000},
		{Items.Cactus: 12000},
		{Items.Cactus: 72000},
		{Items.Cactus: 432000},
		{Items.Cactus: 2590000},
		{Items.Cactus: 15600000}
	])
# THIS IS THE WINNING NODE; IT IS INDEPENDENT OF THE TREE
node_q = Node("Leaderboard", 0, 1, [{
		Items.Bone: 2000000,
		Items.Gold: 1000000
	}])

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