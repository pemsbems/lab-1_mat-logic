import matplotlib.pyplot as plt

def plot_datasets(datasets, indices):
    if not indices:
        print("Нет наборов для отображения.")
        return

    plt.figure()
    for idx in indices:
        ds = datasets[idx]
        plt.scatter(ds['x'], ds['y'])


    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('plot.png')
    print("График сохранён в plot.png")