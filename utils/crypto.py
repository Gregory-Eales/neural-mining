import hashlib
from hashlib import sha256


# SHA256(SHA256(previous block hash + merkle root + nonce)) -> block hash

def double_sha(block, phash, merkle, nonce):
	
	s = merkle+phash#+nonce #block+
	hash1 = sha256()
	hash1.update(s)
	hash2 = sha256()
	hash2.update(hash1.digest())
	
	return hash2.hexdigest()
