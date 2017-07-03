try:
    count = 0.0
    sum = 0
    while True:
        line = input("enter a number or Enter to finish:")
        if line is not "":
            sum += int(line)
            count += 1
        else:
            print(sum / count)
            break;
except ValueError as err:
    print(err)
