import csv
import random

def nomes_reader():
    with open('nomes.csv') as csvfile:
        nomesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1,100)
        auxs = str(aux)
        for x in nomesCSV:
            if auxs == x[0]:
                return x[1]

def random_city():
    with open('cidades.csv') as csvfile:
        cidadesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1, 20)
        for x in cidadesCSV:
            if str(aux) == x[0]:
                return x[1]

def random_cpf():
    cpf1 = random.randint(100, 999)
    cpf2 = random.randint(100, 999)
    cpf3 = random.randint(100, 999)
    cpf4 = random.randint(0,99)

    cpf = str(cpf1) + "." + str(cpf2) + "." + str(cpf3) + "-" + str(cpf4)
    return cpf

def random_date():
    random_date.year = random.randint(1960, 2001)
    random_date.date = random.randint(1, 31)
    random_date.month = random.randint(1, 12)
    
    date = str(random_date.date) + "/" + str(random_date.month) + "/" + str(random_date.year)
    return date

def random_tel():
    tel1 = random.randint(100, 999)
    tel2 = random.randint(1000, 9999)

    tel = str((3000 + tel1)) + "-" + str(tel2)
    return tel

person = []
date = []
cpf = []
age = []
tel = []
city = []
year = []

for k in range(51):
    person.append(nomes_reader())
    date.append(random_date())
    cpf.append(random_cpf())
    year.append(date[k][-4:])
    print(year[k])
    age.append(2019 - int(year[k]))
    tel.append(random_tel())
    city.append(random_city())
