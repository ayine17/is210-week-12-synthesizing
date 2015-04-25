#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 12 syn module"""


class CustomError(Exception):
    """ custom exception class
    attributes:
        None
    """

    def __init__(self, message, cause):
        """ CustomError constructor
        args:
            Message(string): an args that hold the error msg
            cuase(string): stores its value as self.cause
        return:
            return custom
        example:
            >>> myerr = CustomError('Whoah!', cause='Messed up!')
            >>> print myerr.cause
            Messed up!

        """
        self.cause = cause
        self.message = message
