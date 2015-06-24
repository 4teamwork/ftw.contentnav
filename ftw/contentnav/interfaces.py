from zope.interface import Interface


class ICategorizable(Interface):
    """Marker interface for categorizable content"""


class IFtwContentNavLayer(Interface):
    """Request marker for ftw.contentnav"""
