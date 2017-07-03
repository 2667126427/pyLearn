fw = open('sample.txt', 'w')
fw.write('I want to write something in text\n')
fw.write('No new line?')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
