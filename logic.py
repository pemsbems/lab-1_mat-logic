def parse_line(line):
    parts = line.replace(',', ' ').split()
    if len(parts) < 2:
        return None
    try:
        return float(parts[0]), float(parts[1])
    except ValueError:
        return None


def read_data(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    blocks = content.split('\n\n')

    datasets = []

    for block in blocks:
        if not block.strip():
            continue  

        name = "Набор"
        x_vals = []
        y_vals = []

        for line in block.strip().splitlines():
            line = line.strip()
            if line.startswith('#'):
                name = line[1:].strip()
                continue

            pair = parse_line(line)
            if pair is None:
                continue

            x_vals.append(pair[0])
            y_vals.append(pair[1])

        if len(x_vals) < 5:
            continue

        pairs = sorted(zip(x_vals, y_vals))

        x_sorted = []
        y_sorted = []
        for x, y in pairs:
            x_sorted.append(x)
            y_sorted.append(y)

        datasets.append({
            'name': name,
            'x': x_sorted,
            'y': y_sorted
        })

    return datasets
