import base64
import os

print(os.stat('D:/code_triger.jpg').st_size)
with open('D:/code_triger.jpg','rb') as file:
    file_bytes = file.read(30*1024*1024)
    print(len(file_bytes))
    base64_bytes = base64.b64encode(file_bytes)
    print(len(base64_bytes),base64_bytes)
    print(b'data:image/jpeg;base64,'+base64_bytes)