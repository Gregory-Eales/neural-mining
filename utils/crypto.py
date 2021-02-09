import hashlib
from hashlib import sha256
from bitstring import BitArray
from tqdm import tqdm
#import torch


def get_header(block):

	version = block['version'].to_bytes(4, 'little').hex()

	p_hash = bytearray.fromhex(block['previousblockhash'])
	p_hash.reverse()
	p_hash = p_hash.hex()

	merkle = bytearray.fromhex(block['merkle_root'])
	merkle.reverse()
	merkle = merkle.hex()

	time = block['timestamp'].to_bytes(4, 'little').hex()
	bits = block['bits'].to_bytes(4, 'little').hex()
	nonce = block['nonce'].to_bytes(4, 'little').hex()

	return version, p_hash, merkle, time, bits, nonce
	

def double_sha(version, p_hash, merkle, time, bits, nonce):
	
	s = (version + p_hash + merkle + time + bits + nonce)

	c = BitArray(hex=s)
	print(c.bin[2:])

	s = bytes.fromhex(s)
	s = sha256(s).digest()
	s = sha256(s).digest()

	return s.hex()[::-1]


def get_binary(block):
	
	version, p_hash, merkle, time, bits, nonce = get_header(block)
	
	x = (version + p_hash + merkle + time + bits)
	x = BitArray(hex=x).bin[2:]
	x = list(map(int,list(x)))
	
	y = (nonce)
	y = BitArray(hex=y).bin[2:]
	y = list(map(int,list(y)))
		
	return x, y


def generate_data(blocks):
	
	for i in tqdm(range(len(blocks))):

		x, y = get_binary(blocks[i])

