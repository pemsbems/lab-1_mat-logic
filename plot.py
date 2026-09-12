import matplotlib.pyplot as plt

def plot_datasets(datasets, indices):
    if not indices:
        print("Нет наборов для отображения.")
        return

    colors = ['yellow', 'red']  # цвета по порядку

    plt.figure()
    for i, idx in enumerate(indices):
        ds = datasets[idx]
        plt.scatter(ds['x'], ds['y'],
                    s=8,                          
                    color=colors[i % len(colors)],
                    edgecolors='black',           
                    linewidths=0.5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('plot.png')
    print("График сохранён в plot.png")