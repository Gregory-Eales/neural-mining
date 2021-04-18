from multiprocessing import Pool
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import json
import sys
import threading
import time

# SHA256(SHA256(previous block hash + merkle root + nonce)) -> block hash

hashes_url = "https://www.blockchain.com/btc/blocks?page={}"
block_url = "https://blockstream.info/api/block/{}"


def get_block_hashes():

	hashes = []
	
	for i in tqdm(range(1, 13395+1)):
		r = requests.get(hashes_url.format(i))
		soup = BeautifulSoup(r.text, 'html.parser')
		links = soup.findAll('a')
		links = [l.get('href') for l in links]
		for l in links:
			url = '/btc/block/'
			if l[0:len(url)] == url:
				hashes.append(l[11:])

	return hashes

def get_block_hash(i):

	print(i)

	hashes = []

	try:

		r = requests.get(hashes_url.format(i))
		soup = BeautifulSoup(r.text, 'html.parser')
		links = soup.findAll('a')
		links = [l.get('href') for l in links]
		for l in links:
			url = '/btc/block/'
			if l[0:len(url)] == url:
				hashes.append(l[11:])

	except:
		pass

	return hashes


def threaded_get_block_hashes(n, n_threads=20):
	p = Pool(processes=n_threads)
	data = p.map(get_block_hash,[i for i in range(1, n)])
	p.close()
	l = []
	for d in data:
		l += d

	return l


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




def get_block(h):
	r = requests.get(block_url.format(h))
	return r.json()
	

def get_block_data(hashes, n=5):

	data = {}
	data['data'] = []

	for i in tqdm(range(len(hashes))):
		data['data'].append(get_block(hashes[i]))

	return data


def save_block_data(data, path='./data/data.txt'):
	with open(path, 'w') as file:
		json.dump(data, file)


def load_block_data(path='./data/data.txt'):

	with open(path, 'r') as file:
		data = json.load(file)

	return data



def generate_dataset(data):
	pass


	