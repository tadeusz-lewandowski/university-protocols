import socket as _s
from  config import SERVER_IP, PORT
from Messanger import Messanger
from diffie_hellman.DiffieHellman import DiffieHellman
from AES import AESCipher

socket = _s.socket(_s.AF_INET, _s.SOCK_STREAM)
socket.bind((SERVER_IP, PORT))
print('Listening for connections...')
socket.listen()
conn, addr = socket.accept()
messanger = Messanger(conn)
print('Connected!')

#start diffie hellman key exchange
diffie_hellman = DiffieHellman()
diffie_hellman.generate_secret()

client_public_key = int(messanger.get_message().decode())

diffie_hellman.set_other_public(client_public_key)

messanger.send_message(str(diffie_hellman.get_public()).encode())

diffie_hellman.generate_shared_private_key()
SECRET = diffie_hellman.get_shared_private_key()

print('shared secret', SECRET)

aes = AESCipher(str(SECRET))

data = aes.decrypt(messanger.get_message())

print('Decrypted: ', data)
messanger.send_message(aes.encrypt(data))