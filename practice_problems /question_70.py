# Please write a program to compress and decompress the string “hello world!hello world!hello world!hello world!”.
# Hints: Use zlib.compress() and zlib.decompress() to compress and decompress a string.

import zlib


a= b"hello  nikhil i love you "
b=zlib.compress(a)
print(zlib.compress(a))

print(zlib.decompress(b))