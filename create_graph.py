import csv
import matplotlib.pyplot as plt


def create_graph(type_req, count):
    fig, ax = plt.subplots()
    ax.set_facecolor('orange')
    plt.xlabel('Запрос')
    plt.ylabel('Кол-во')

    plt.xticks(rotation=90)

    plt.bar(type_req, count)
    plt.show()


def read_csv(path):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        res = {
            'name': [],
            'count': [],
        }

        for row in spamreader:
            row = row[0].split(',')
            if row:
                res['name'].append(row[0])
                res['count'].append(row[1])

        return res


if __name__ == '__main__':
    data = read_csv('/home/berkyt/PycharmProjects/shop-with-postgresql/load-testing/names.csv')
    data_name = ['Postgresql_' + name for name in data['name'][1:]]
    data_count = [int(item) for item in data['count'][1:]]

    data = read_csv('/home/berkyt/PycharmProjects/shop-with-redis/load-testing/names.csv')
    data_name += ['Redis_' + name for name in data['name'][1:]]
    data_count += [int(item) for item in data['count'][1:]]

    create_graph(data_name, data_count)

