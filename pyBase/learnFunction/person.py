def person(name, age, *args, city = 'Beijing', job):
    print(name, age, city, job)


if __name__ == '__main__':
    person('Bob', 27, city='Beijing', job='Engineer')
