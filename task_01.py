#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week12 syn module"""


class BaseError(Exception):
    """ base error class, caught base errors"""


class StringError(BaseError, TypeError):
    """ String error class subclass of BaseError"""
    pass


class NumberError(BaseError, TypeError):
    """number error class subclass of BaseError"""
    pass


class NonZeroError(NumberError):
    """non number error class subclass of BaseError"""
    pass
