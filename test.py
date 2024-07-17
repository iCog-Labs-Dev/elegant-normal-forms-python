from Utilities.ReduceToElegance import commandSetIterator
from DataStructures.Trees import TreeNode

a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')

c.guardSet.append(b)
b.guardSet.append(a)


children = [a,b,c,d]
print(commandSetIterator(children))

