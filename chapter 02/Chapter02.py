# Logical Operators
# or {atleast one should be True} 
# not {invert the value of boolean}
# and {Both should be True}

#is_running = True
#name = "Mayank"

# if name == "Mayank" and is_running:
#     print("Mayank is running")

# else:
#     print("Mayank is not running")
    
    
# Conditional Statements : X if {condition} else Y

# is_running = True
# print("Mayank is running") if is_running else print("Mayank is not running")

# a = 1
# b = 2 
# max_num = a if a > b else b
# min_num = a if a < b else b

 
# Indexing = accessing elements of a sequence using []
#            [start : stop : step]

credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[0])  # Output: 1
print(credit_card_number[0:4])  # Output: 1234
print(credit_card_number[5:9])  # Output: 5678
print(credit_card_number[10:14])  # Output: 9012
print(credit_card_number[15:19])  # Output: 3456
# First and last digit of this property of string should be excluded

print(credit_card_number[::2]) # every second character starting from index 0
print(credit_card_number[1:19:2]) # every second character from index 1 to 18

last_four_digits = credit_card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_four_digits}") # Output: 3456


print(credit_card_number[::-1]) # for reversing the string





# ****************************************************************************************************

# format specifiers = {value:flags} format a value based on what flags are inserted

price = 19.99
price1 = 34332.3423423
print(f"${price:+,.1f}") # {, & + & .1f} is used where , is used for thousand separator and .1f is used for rounding the number to 1 decimal place and + is used for showing the sign of the number if it is positive or negative

print(f"${price1:+,.2f}")





