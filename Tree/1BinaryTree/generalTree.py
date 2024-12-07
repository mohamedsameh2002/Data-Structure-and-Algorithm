class TreeNode:
    def __init__(self,data,childern=[]) -> None:
        self.data=data
        self.childern=childern
    
    def add_child(self,tree_node):
        self.childern.append(tree_node)

    def __str__(self,level=0) -> str:
        ret="-" * level + str(self.data) + "\n"
        for child in self.childern:
            ret +=child.__str__(level+1)
        return ret
    


cold=TreeNode('Cold',[])
drinks=TreeNode('Drinks',[cold])
hot=TreeNode('Hot',[])
drinks.add_child(hot)
tea=TreeNode('tea')
coffee=TreeNode('tea')
cola=TreeNode('cola')
fanta=TreeNode('fanta')

hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(cola)
cold.add_child(fanta)


print(drinks)