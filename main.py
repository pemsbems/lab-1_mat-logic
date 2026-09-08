from logic import read_data
from plot import plot_datasets

FILE = "data.txt"
CHOICE = [1, 2]  

datasets = read_data(FILE)
if not datasets:
    print("Нет подходящих наборов.")
    exit()

indices = []
for n in CHOICE:
    if 1 <= n <= len(datasets):
        indices.append(n - 1)

plot_datasets(datasets, indices)