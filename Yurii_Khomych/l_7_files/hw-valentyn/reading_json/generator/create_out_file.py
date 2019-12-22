import csv


def create_output(nodes_list):
    final_dict = {}
    for n in nodes_list:
        if n.get_sourcing():
            final_dict[n.get_sourcing()] = final_dict.get(n.get_sourcing(), 0) + 1

    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'Destination', 'ElementPath', 'SourcePath', 'Occurrences'])

        for d in final_dict:
            d1 = d.replace(':', '|')
            d1 = d1.split('|')
            writer.writerow([d1[0], d1[1], d1[2].replace('//', '/'), d1[3], final_dict[d]])

    print('result.csv was built')
