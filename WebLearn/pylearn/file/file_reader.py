file = 'text_files/pi_digits.txt'

with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file) as file_object:
    lines = file_object.readlines()

for l in lines:
    print(l.rstrip())

pi = ''
for l in lines:
    pi += l.strip()

print(len(pi), pi)
print(float(pi))