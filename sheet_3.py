
# Exercise 1: Average Run Time
number_of_runs = 0
total_time = 0

while True:
    time_input = input("Enter 10 km run time: ")

    if time_input == "" or time_input == "0":
        break

    run_time = float(time_input)
    total_time += run_time
    number_of_runs += 1

if number_of_runs > 0:
    average = total_time / number_of_runs
    print(f"Average of {average}, over {number_of_runs} runs")
else:
    print("No runs entered.")


# Exercise 2: Number Cropping
fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

str_num = str(fl_num)
before_dot, after_dot = str_num.split(".")
cropped = before_dot[-bef_int_num:] + "." + after_dot[:aft_int_num]
new_float = float(cropped)

print(new_float)


# Exercise 3: String Sorting
s = "Tom Jerry Harry"

words = s.split()
words.sort()
sorted_string = ", ".join(words)

print(sorted_string)


# Exercise 4: Even/Odd Index Sums
sequence = [10, 20, 30, 40, 50, 60]
even_sum = 0
odd_sum = 0

for i in range(len(sequence)):
    if i % 2 == 0:
        even_sum += sequence[i]
    else:
        odd_sum += sequence[i]

print("Even index sum:", even_sum)
print("Odd index sum:", odd_sum)


# Exercise 5: Simple Login System
USERS = {'user1': 'password1', 'user2': 'password2'}

name_input = input("Enter username: ")
pass_input = input("Enter password: ")

if name_input in USERS and USERS[name_input] == pass_input:
    print("Login successful!")
else:
    print("Invalid username or password.")


# Exercise 6: Dictionary Merger
d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}
all_dicts = [d1, d2, d3]
fin_di = {}

for d in all_dicts:
    fin_di.update(d)

print(fin_di)


# Exercise 7: Unique Number Counter
numbers1 = [10, 20, 30]
numbers2 = [10, 20, 30, 10, 20, 30]

unique1 = len(set(numbers1))
unique2 = len(set(numbers2))

print("Unique in numbers1:", unique1)
print("Unique in numbers2:", unique2)
