alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  new_text = ""
  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      if direction == "e":
        new_index = (index + shift) % len(alphabet)
      elif direction == "d":
        new_index = (index - shift) % len(alphabet)
      new_char = alphabet[new_index]
      new_text += new_char
    else:
      new_text += char
  return new_text

print("Hey there! I'm Caesar. Try my cipher out!")
go_again = True
while go_again:
  direction = input("\nType 'e' to encrypt, type 'd' to decrypt:\n").lower()
  if direction == "e" or direction == "d":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  
    new_text = caesar(direction, text, shift)
    if direction == "e":
      print(f"The encrypted message is: {new_text}")
    elif direction == "d":
      print(f"The decrypted message is: {new_text}")

    again = input("Type 'yes' if you want to try again. Otherwise, type 'no'.\n").lower()
    if again == "no":
      print("Good Bye!")
      go_again = False
  else:
    print("Please enter a valid option.")