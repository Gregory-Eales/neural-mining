from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import sys



# SHA256(SHA256(previous block hash + merkle root + nonce)) -> block hash


hashes_url = "https://www.blockchain.com/btc/blocks?page={}"

block_url = "https://blockchain.info/rawblock/${}"


def get_block_hashes():

	hashes = []
	
	for i in tqdm(range(1, 13395+1)):
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
	