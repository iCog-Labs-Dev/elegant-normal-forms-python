class BinaryExpressionTreeNode:
    def __init__(self, value: str):
        self.left : BinaryExpressionTreeNode | None = None
        self.right : BinaryExpressionTreeNode | None = None
        self.value:str = value


class BinaryContraintTreeNode:
    def __init__(self, value: str, contraint: bool = False):
        self.left : BinaryContraintTreeNode | None = None
        self.right : BinaryContraintTreeNode | None = None
        self.value : str = value
        self.contraint : bool = contraint


