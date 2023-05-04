import sys

def encode(message, shift):
  message = message.upper()
  encoded = ''
  
  for c in message:
    if c.isalpha():
      code = ord(c) - 65
      code = code + (shift % 26)
      encoded += chr(code + 65)
            
    # Break encoded message into blocks of 5 letters
  blocks = [encoded[i:i+5] for i in range(0, len(encoded), 5)]
  
  # Print encoded message in blocks of 5 letters
  with open("crypted.txt", "w") as file:
    for i, block in enumerate(blocks):
      if i % 10 == 9:
        file.write(block + "\n")
      else:
        file.write(block + " ")
    
    
if __name__ == '__main__':
    # Get shift amount from command line argument
    shift = int(sys.argv[1])
    
    # Open the file and read the encoded message
    with open('encoded.txt', 'r') as f:
        message = f.read()
    
    # Encode the message and print it
    encode(message, shift)