# read a file
with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/reading_file_example.txt', 'r+') as file:
    content = file.read()
    print(content)

# read a file line by line
with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/reading_file_example.txt', 'r+') as file2:
    for line in file2: 
        print(line)
        # print(line.strip()) for when you want to strip out the spaces.

# readline
with open ('python_30_day_challenge/30-Days-Of-Python-JCM/files/reading_file_example.txt') as file3:
    firstline = file3.readline()
    print(firstline)

with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/reading_file_example.txt') as file4:
    lines = file4.readlines()
    print(lines)
    print(f'The third line is: {lines[2]}')

with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/reading_file_example.txt') as file5:
    character_no = file5.read(10)
    print(character_no)

# tell and seek -- think of the file pointer like a cursor
with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/reading_file_example.txt') as file6:
    print(file6.tell())
    print(file6.read(15))
    print(file6.tell())
    print(file6.seek(0))

# write to a file;
with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/try2.txt', 'w') as file7:
    file7.write('Hello world!')
    file7.write('\nWelcome!')
with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/try2.txt') as file7:
    print(file7.read())

with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/try2.txt', 'a') as file8:
    file8.write('\nThis line is appending.')

with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/try2.txt') as file8:
    print(file8.read())

# error handling
# try:
#     a = b
# except: 
#     print('\nThis is not assigned')
# print('Hello') 

try:
    a=b
except NameError as ex:
    print(ex)

try:
    1/0
except ZeroDivisionError as ex:
    print(ex)

try:
    num = int(input('Enter a number: '))
    result = 10/num
except ValueError:
    print('This is not a valid number.')
except ZeroDivisionError:
    print('You cannot divide a number by zero. Number cannot be zero')
except Exception as ex:
    print(ex)
# else:
#     print(result)
finally:
    print(f'Finally statement. {result}')

try:
    with open('python_30_day_challenge/30-Days-Of-Python-JCM/files/try3.txt') as file9:
        content = file9.read()
except FileNotFoundError:
    print("File doesn't exist")
except Exception as ex:
    print(ex)
else: 
    print('file read from else')
    print(content)
finally:
    print('execute everytime.')