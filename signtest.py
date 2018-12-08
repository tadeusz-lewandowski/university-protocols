import rsa
import base64
import pickle
(pubkey, privkey) = rsa.newkeys(512)
print(pubkey)
message = 'Go left at the blue tree'
signature = rsa.sign(message.encode(), privkey, 'SHA-1')

print(rsa.verify(message.encode(), signature, pubkey))
print(type(pubkey))
print(pickle.dumps(pubkey))