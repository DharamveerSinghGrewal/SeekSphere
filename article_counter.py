import os

data_dir = "./data"
article_count = len([f for f in os.listdir(data_dir) if f.endswith('.txt')])

print(f"Total articles downloaded: {article_count}")