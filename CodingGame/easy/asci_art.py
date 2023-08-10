L = int(input())
H = int(input())
letters = list(input())

T = []
for i in range(H):
    T.append(list(input()))

for row in range(len(T)):
    row_string = ""
    for letter in letters:
        if letter.isalpha(): letter_idx = ord(letter.capitalize()) - 65
        else: letter_idx = 26
        row_idx_start = letter_idx*L
        row_idx_end   = letter_idx*L + L
        row_string += "".join(T[row][row_idx_start:row_idx_end])
    print(''.join(row_string))