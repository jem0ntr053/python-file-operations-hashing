from typing import Any


# for number 2:
def hash_10(key): return key // 10 % 10


# for number 3:
def hash_20(key): return key % 20


# for number 5:
def hash_1(key): return key // 11 % 23


if __name__ == '__main__':
    # Problem 2: Write a hash function that returns the 10's digit of a 4-digit
    # key
    user_key = int(input("Enter a 4-digit key: "))
    print(hash_10(user_key))

    my_list = [66, 7, 87, 90, 126, 140, 145, 153, 177, 285, 393, 395, 467, 566,
               620,
               735]

    # Problem # 3: store the values into a hash table with 20 positions using
    # the division method of hashing and the linear probing method of collision
    # resolution.
    hash_table_3 = [None] * 20
    for table_key in my_list:
        idx = hash_20(table_key)
        while hash_table_3[idx] is not None:
            if idx == 19:
                idx = 0
            else:
                idx += 1
        hash_table_3[idx] = table_key
    print(hash_table_3)
    print('\n')

    # write a program to store and retrieve student records from a file using
    # hashing

    # create a list of student records
    student_list = [
        {'name': 'John', 'ID': 1234, 'GPA': 3.0},
        {'name': 'Mary', 'ID': 2345, 'GPA': 3.8},
        {'name': 'Joe', 'ID': 3456, 'GPA': 2.5},
        {'name': 'Sue', 'ID': 4567, 'GPA': 3.5},
        {'name': 'Bob', 'ID': 5678, 'GPA': 3.2},
        {'name': 'Jill', 'ID': 6789, 'GPA': 2.8}
    ]
    # create a hash table with 20 positions
    hash_table_5 = [None] * 25

    # write the student records to a file
    with open('student_records.txt', 'w') as student_records:
        for student in student_list:
            student_records.write(
                f"{student['name']}, {student['ID']}, {student['GPA']}\n")

    # read the student records from the file
    with open('student_records.txt', 'r') as student_records:
        for line in student_records:
            name = line.strip().split(',')[0]
            ID = int(line.strip().split(',')[1])
            GPA = line.strip().split(',')[2]
            idx: int | Any = hash_1(int(ID))

            # store the student records in the hash table
            hash_table_5[idx] = {'name': name, 'ID': ID, 'GPA': GPA}

    # print the hash table
    print(f"Hash table for #5:")
    for items in hash_table_5:
        print(items)
