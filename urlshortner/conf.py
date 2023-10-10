""" Const defs moved here
"""
import string

## used for base62
ALPHABET = string.ascii_letters + string.digits

## length of SHAKE hash lenth
## this will result in a 16^8 number of hash space
## after transforming to base62, this will generate short URLs with max length being 6.
## TODO: is it possible to make this dynamic and adaptive?
HASH_LEN = 4

## database path
#### set to a valid path if enable persistent storage
DBPATH = None

## auth url
AUTH_URL = "http://127.0.0.1:12356/users/auth"
