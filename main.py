# Un = an ** 2 + bn + c

U1 = int(input("1st term:   "))
first_diff = int(input("1st difference:   "))
second_diff = int(input("2nd difference:   "))

u1 = U1
b = first_diff # keeps original value of first_diff
seq1 = [U1]
seq2 = []

pos = 0
while pos < 6: # creating the sequences
    U1 += first_diff
    seq1.append(U1)

    seq2.append(first_diff)
    first_diff += second_diff
    pos += 1

print(f"Sequence: \n{seq1}\n")
print(f"difference for each term: \n{seq2}\n")


# calculating the variables for the equation

a = second_diff/2
three_a = 3*a
b -= three_a
c = u1 - a - b

# display

my_dict = {"a": a, "b": b, "c": c}
for key, value in my_dict.items():
    print(f"{key}:")
    print(value, '\n')

print ('Un = an ^ 2 + bn + c')

equation = f'Un = {a}n ^ 2 + {b}n + {c}'
print (equation)