matrix = [
    ["7", "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

decoded_message = ""
columns = len(matrix[0])
rows = len(matrix)

for col in range(columns):
    for row in range(rows):
        char = matrix[row][col]
        if char.isalpha():
            decoded_message += char
        elif decoded_message and decoded_message[-1] != " ":
            decoded_message += " "

print(decoded_message.strip())
