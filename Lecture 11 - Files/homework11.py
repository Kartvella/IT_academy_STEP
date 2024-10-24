# Exercise N1
with open("first.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"line {i}\n")

with open("first.txt", "r") as file:
    lines = file.readlines()

n_of_lines = [line for line in lines]

print(f"number of lines: {len(n_of_lines)}")

# Exercise N2

with open("second.txt", "w") as file:
    for i in range(1, 18):
        if i == 2:
            file.write("line 2\n")
        elif i == 8:
            file.write("line 8\n")
        elif i == 10:
            file.write("line 10\n")
        elif i == 13:
            file.write("line 13\n")
        elif i == 17:
            file.write("line 17\n")
        else:
            file.write("\n")

#Exercise N3
with open("sample.txt", "w") as sample1, open("sample2.txt", "w") as sample2:
    sample1.write("this line is from sample.txt")
    sample2.write("this line is from sample2.txt")

with open("sample.txt", "r") as sample1, open("sample2.txt", "r") as sample2, open("merged.txt", "w") as merged_file:
    content1 = sample1.read()
    content2 = sample2.read()
    
    merged_file.write(content1 + "\n") 
    merged_file.write(content2)

with open("merged.txt", "r") as merged_file:
    merged_content = merged_file.read()

print(merged_content)

#Exercise N4
def find_palindrome_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    for index, line in enumerate(lines):
        if line == line[::-1]:
            print(f"Palindrome found: {line} (Line {index + 1})")

with open('palindrome.txt', 'w') as pali:

    example_pals = ["madam", "racecar", "hello", "madam", "olleh", "racecar"]
    for elem in example_pals:
        pali.write(elem + '\n')
find_palindrome_lines("palindrome.txt")


# #Exercise N5

def split_file_by_lines(input_filename, max_lines=10):
    
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]


    for i in range(0, len(lines), max_lines):
        part_filename = f"{input_filename[:-4]}_part{i//max_lines + 1}.txt"
        with open(part_filename, 'w') as output_file:
            output_file.write('\n'.join(lines[i:i + max_lines]))
        print(f"Created: {part_filename}")
with open('C://Users//kartv//OneDrive//Desktop//test//Lecture 11 - Files//fifth.txt', 'r') as file:
    split_file_by_lines("C://Users//kartv//OneDrive//Desktop//test//Lecture 11 - Files//fifth.txt")


# #Exercise N6
def remove_empty_lines(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            lines = [line.strip() for line in input_file.readlines()]

        non_empty_lines = [line for line in lines if line]

        with open(output_filename, 'w') as output_file:
            output_file.write('\n'.join(non_empty_lines))

    except FileNotFoundError:
        print(f"the file '{input_filename}' does not exist")
    except IOError as e:
        print(f"an I/O error occurred: {e}")
with open('sample3.txt', 'w+') as file:
    for _ in range(100):
        file.write('\n')
    file.write('this line is not empty and is from sample3.txt(input_filename)')
remove_empty_lines('sample3.txt', 'sample4.txt')
