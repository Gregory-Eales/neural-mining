from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import json
import sys

# SHA256(SHA256(previous block hash + merkle root + nonce)) -> block hash


hashes_url = "https://www.blockchain.com/btc/blocks?page={}"

block_url = "https://blockstream.info/api/block/{}"


def get_block_hashes():

	hashes = []
	
	for i in tqdm(range(1, 100)):#13395+1)):
		r = requests.get(hashes_url.format(1))
		soup = BeautifulSoup(r.text, 'html.parser')
		links = soup.findAll('a')
		links = [l.get('href') for l in links]
		for l in links:
			url = '/btc/block/'
			if l[0:len(url)] == url:
				hashes.append(l[11:])

	
	return hashes


def save_block_hashes(hashes, path="./data/hashes.txt"):

	with open(path, 'w') as file:

		for h in hashes:

			file.write("{}\n".format(h))


def load_block_hashes(path="./data/hashes.txt"):

	hashes = []

	with open(path, 'r') as file:
		for line in file.readlines():
			hashes.append(line.strip('\n'))

	return hashes

def get_block_data(hashes):

	data = {}
	data['data'] = []

	for i in tqdm(range(len(hashes))):
		r = requests.get(block_url.format(hashes[i]))
		data['data'].append(r.json())

	return data

def save_block_data(data):
	with open('data.txt', 'w') as file:
		json.dump(data, file)

	