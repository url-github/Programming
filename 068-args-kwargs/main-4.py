def calculate_paint(efficency_ltr_per_m2, *rooms):

    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint

print(calculate_paint(0.25, 42, 28, 30))

rooms = [42, 28, 30]
print(calculate_paint(0.25,*rooms))

print('-'*30)


def log_it(*args):

    path = r'/Users/p/Documents/Scripts/Programming/068-args-kwargs/log-2.txt'
    with open(path, "a") as f:

        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')