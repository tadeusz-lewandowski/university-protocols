import rsa


message = "I want this stream signed"

(priv, pub) = rsa.newkeys(512)

print(priv)
print(pub)

signature = rsa.sign(message.encode(), priv, 'SHA-1')

print(signature)