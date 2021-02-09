from utils import *



def main():
	
	# get block hashes
	#hashes = get_block_hashes()

	# save hashes
	#save_block_hashes(hashes)
	#hashes = load_block_hashes()

	# use hashes to get block data
	#data = get_block_data(hashes)

	# save block data as torch dataset
	#save_block_data(data)

	# load block data
	data = load_block_data()

	x, y = generate_data(data['data'])
	save_tensors(x, y)

	"""
	for d in data['data']:
		print(get_hash(d))
	"""

if __name__ == "__main__":
	main()