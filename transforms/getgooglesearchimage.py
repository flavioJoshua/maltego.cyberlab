"""Compatibility shim so maltego_trx can discover getgooglesearchimage as local transform.

maltego_trx.register_transform_classes expects each module to expose a class
named exactly like the module filename.
"""

from .GetGoogleSearch import GetGoogleSearchImage as getgooglesearchimage
