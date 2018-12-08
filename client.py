import socket as _s
from config import SERVER_IP, PORT
from Messanger import Messanger
from diffie_hellman.DiffieHellman import DiffieHellman
from AES import AESCipher
import rsa
import pickle

socket = _s.socket(_s.AF_INET, _s.SOCK_STREAM)
print('Waiting for connection...')
socket.connect((SERVER_IP, PORT))
print('Connected!')
messanger = Messanger(socket)

#start diffie hellman key exchange
diffie_hellman = DiffieHellman()
diffie_hellman.generate_secret()

messanger.send_message(str(diffie_hellman.get_public()).encode())

server_public_key = int(messanger.get_message().decode())

diffie_hellman.set_other_public(server_public_key)
diffie_hellman.generate_shared_private_key()
SECRET = diffie_hellman.get_shared_private_key()

print('shared secret', SECRET)

#signature procedure
(pubkey, privkey) = rsa.newkeys(512)
messanger.send_message(pickle.dumps(pubkey))

aes = AESCipher(str(SECRET))
message = 'Hello!'
encrypted_message = aes.encrypt(message)

signature = rsa.sign(encrypted_message, privkey, 'SHA-1')

final_message = (encrypted_message, signature)
messanger.send_message(pickle.dumps(final_message))
