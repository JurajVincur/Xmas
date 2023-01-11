from Christmas.Props import ChristmasTree
from Christmas.TreeDecorators import Bubbles, Lights, TreeTopper

def main():
    christmasTree = Bubbles(Lights(TreeTopper(ChristmasTree())))
    christmasTree.decorate()

if __name__ == "__main__":
    main()