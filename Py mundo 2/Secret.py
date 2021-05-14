from time import time, sleep
from tqdm import tqdm

for i in tqdm(range(10),unit=' Peta',bar_format="Secret: {l_bar}{bar}{r_bar}"):
    sleep(0.5)
    