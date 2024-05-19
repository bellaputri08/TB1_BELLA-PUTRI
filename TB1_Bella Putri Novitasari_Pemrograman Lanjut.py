import re

def decode_script(matrix, n, m):
  
  decoded = ''.join(''.join(row[col] for row in matrix) for col in range(m))
  decoded = re.sub(r'(?<=\w)(\W+)(?=\w)', ' ', decoded)

  return decoded

n, m = 7, 3
matrix = [
  "Tsi",
  "h%x",
  "i #",
  "sM ",
  "$a ",
  "#t%",
  "ir!"
]

result = decode_script(matrix, n, m)
print(result)