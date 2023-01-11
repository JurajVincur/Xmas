from abc import ABCMeta, abstractmethod

class IDecorable(object):
    __metaclass__ = ABCMeta

    """
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """

    @abstractmethod
    def decorate(self):
        pass

class ChristmasTree(IDecorable):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def decorate(self):
        print "Christmas tree",
