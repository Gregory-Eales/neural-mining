import hashlib
from hashlib import sha256
import requests


# SHA256(SHA256(previous block hash + merkle root + nonce)) -> block hash


url = "https://blockchain.info/rawblock/${}"


def scrape_data():
	pass

def double_sha(block, phash, merkle, nonce):
	
	s = merkle+phash#+nonce #block+
	hash1 = sha256()
	hash1.update(s)
	hash2 = sha256()
	hash2.update(hash1.digest())
	
	return hash2.hexdigest()

print(double_sha(0, prev_hash, merkle_root, nonce))


def main():
	pass

if __name__ == "__main__":
	main()