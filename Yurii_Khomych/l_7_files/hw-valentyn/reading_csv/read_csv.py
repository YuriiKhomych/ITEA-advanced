import csv


def read_csv(name):
    with open(name, 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        line_count = 0
        poDate = 1
        qtyOrdered = 1
        buyers = 1
        parsed_by_date = {}
        # PO Date
        # Qty Ordered
        # Buyers Catalog or Stock Keeping #

        for row in rows:
            if line_count == 0:
                for index in range(len(row)):
                    if row[index] == "PO Date":
                        poDate = index
                    elif row[index] == "Qty Ordered":
                        qtyOrdered = index
                    elif row[index] == "Buyers Catalog or Stock Keeping #":
                        buyers = index
                line_count += 1

            elif line_count > 0:
                l1 = ()
                if parsed_by_date.get(row[poDate]) is None:
                    l1 = ([(row[qtyOrdered], row[buyers])])
                else:
                    l1 = parsed_by_date.get(row[poDate])
                    l1.append((row[qtyOrdered], row[buyers]))

                parsed_by_date[row[poDate]] = l1
                line_count += 1

    return parsed_by_date

