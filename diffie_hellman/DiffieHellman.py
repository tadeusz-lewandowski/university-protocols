from ssl import RAND_bytes
from .Primes import PRIMES

class DiffieHellman:
	def __init__(self, secret_length=64, secret=None, group=14):
		self.secret_length = secret_length
		self.secret = secret
		self.group = group
		self.generator = PRIMES[group]["generator"]
		self.prime = PRIMES[group]["prime"]
		self.other_public = 0
		self.shared_private_key = 0

	def generate_secret(self):  
		random_bytes = RAND_bytes(self.secret_length)
		self.secret = int.from_bytes(random_bytes, byteorder='big') 

	def get_secret(self):
		return self.secret

	def get_public(self):
    	# A is Alice public
    	# A = g^a mod p
		return pow(self.generator, self.secret, self.prime)

	def set_other_public(self, other_public):
		self.other_public = other_public

	def generate_shared_private_key(self):
		# B is Bob public
		# s = B^a mod p
		self.shared_private_key =  pow(self.other_public, self.secret, self.prime)

	def get_shared_private_key(self):
		return self.shared_private_key