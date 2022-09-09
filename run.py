
import re 
from collections import Counter


f = open('blast.txt', 'r')
print(f.read())


def reader(blast):
    with open('blast.txt') as f:
        log = f.read()

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        ips_list = re.findall(regexp, log)

        return ips_list


def count(ips_list):
    return Counter(ips_list)


def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['ip', 'frequency']

        writer.writeow(header)

        for item in counter:
            writer.writerow((item, counter[item]))




if __name__ == '__main__':
    write_csv(count(reader('log')))
 