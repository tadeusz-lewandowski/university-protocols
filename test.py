from DiffieHellman import DiffieHellman

Alice = DiffieHellman()
Bob = DiffieHellman()

Alice.generate_secret()
Bob.generate_secret()

print('Alice secret', Alice.get_secret())
print('Bob secret', Bob.get_secret())

A = Alice.get_public()
B = Bob.get_public()

print('Alice public', A)
print('Bob public', B)

Alice.set_other_public(B)
Bob.set_other_public(A)

Alice.generate_shared_private_key()
Bob.generate_shared_private_key()

print('shared1', Alice.get_shared_private_key())
print('shared2',Bob.get_shared_private_key())