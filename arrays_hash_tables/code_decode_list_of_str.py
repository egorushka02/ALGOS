"""Необходимо разработать алгоритм кодирования списка строк в одну строку. 
Закодированная строка будет отправлена по сети и затем декодирована 
обратно в исходный список строк.

Необходимо реализовать функции `encode` и `decode`."""

def encode(strs):
    result = ""
    for s in strs:
        result += str(len(s)) + s
    return result

def decode(s):
    result = []
    i = 0
    while i < len(s):
        length = int(s[i])
        i += 1
        result.append(s[i:i+length])
        i += length
    return result
my_str = ["hello", "world", "python"]

encoded_str = encode(my_str)
decoded_str = decode(encoded_str)
print(encoded_str)
print(decoded_str)