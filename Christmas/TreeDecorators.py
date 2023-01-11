from abc import ABCMeta, abstractmethod
from Props import IDecorable

class TreeDecorator(IDecorable, object):
    __metaclass__ = ABCMeta

    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, tree):
        self._tree = tree

    @abstractmethod
    def decorate(self):
        pass

class TreeTopper(TreeDecorator):
    """
    Add responsibilities to the component.
    """

    def decorate(self):
        self._tree.decorate()
        print "with tree topper",

class Lights(TreeDecorator):
    """
    Add responsibilities to the component.
    """

    def decorate(self):
        self._tree.decorate()
        print "with lights",

class Bubbles(TreeDecorator):
    """
    Add responsibilities to the component.
    """

    def decorate(self):
        self._tree.decorate()
        print "with bubbles",

class Bells(TreeDecorator):
    """
    Add responsibilities to the component.
    """

    def decorate(self):
        self._tree.decorate()
        print "with bubbles",