def generate_truth(n):
    rows = 2 ** n
    table = []

    for i in range(n):
        repeat = 2 ** (n - i - 1)
        pattern = []

        val = 'T'
        count = 0

        for _ in range(rows):
            pattern.append(val)
            count += 1

            if count == repeat:
                val = 'F' if val == 'T' else 'T'
                count = 0

        table.append(pattern)

    return table

vars = generate_truth(2)

p, q, = vars

for i in range(len(p)):
    print(p[i], q[i])