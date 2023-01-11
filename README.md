# Merry Christmas & Happy New Year

[![XDE Xmas Video](https://img.youtube.com/vi/bpf1S_3FHOM/0.jpg)](https://www.youtube.com/watch?v=bpf1S_3FHOM)

Decorator pattern visualized using XDE & [Project North Star](https://developer.leapmotion.com/northstar).

Play button represents call of *decorate* method while selected decorators were applied (see attached video & code).

```python
from Christmas.Props import ChristmasTree
from Christmas.TreeDecorators import Bubbles, Lights, TreeTopper

def main():
    christmasTree = Bubbles(Lights(TreeTopper(ChristmasTree())))
    christmasTree.decorate()

if __name__ == "__main__":
    main()
```
