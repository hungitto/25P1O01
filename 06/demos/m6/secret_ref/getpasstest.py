#!/usr/bin/env python

"""
Purpose: Illustrates the usage of getpass for interactive
password collection, then prints the password.
"""

import getpass

secret = getpass.getpass()
print(type(secret), secret)
