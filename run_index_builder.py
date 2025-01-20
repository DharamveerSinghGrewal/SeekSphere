from indexing.indexer import build_index

# Path to your data folder
DATA_FOLDER = 'data/'

print("Building the index...")
build_index(DATA_FOLDER)
print("Index built successfully!")
