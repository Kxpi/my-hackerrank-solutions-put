jump = int(input())
jump*=-1
message = input()
cipher = ""

for letter in message:
    if letter.isupper():
        letter_index = ord(letter) - ord('A')
        changed_letter = (letter_index + jump) % 26 + ord('A')
        new_letter = chr(changed_letter)
        cipher += new_letter

    else:
        letter_index = ord(letter) - ord('a')
        changed_letter = (letter_index + jump) % 26 + ord('a')
        new_letter = chr(changed_letter)
        cipher += new_letter

print(cipher)
