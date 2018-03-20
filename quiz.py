"""
Question 1:
Given two int values, return their sum. Unless the two values
are the same, then return double their sum.
"""

def sum_double(a, b):
    if a != b:
        return(a+b)
    else:
        return(2*(a+b))


# When you've completed your function, uncomment the
# following lines and run this file to test!


print(sum_double(1, 2))

print(sum_double(2, 2))




"""
-----------------------------------------------------------------------
Question 2:
In a small town the population is p0 = 1500 at the beginning of a year.
The population regularly increases by 5 percent per year and moreover 100
new inhabitants per year come to live in the town. How many years does
the town need to see its population greater or equal to p = 5000
inhabitants?
Answer: 15 years
Create a function that takes four parameters to return the number of
years needed.
"""
def number_of_years(p0, percent, aug, p):
    year = 1
    while year >= 0:
        p0 = (p0*(1+percent/100))+(aug)
        if p0 < p:
            year = year + 1
        elif p0>=p:
            return year
            break



# When you've completed your function, uncomment the
# following lines and run this file to test!

print(number_of_years(1500, 5, 100, 5000))

print(number_of_years(1500000, 2.5, 10000, 2000000))


"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
"""

def sum_squares(n):
    i =0
    ss = 0
    while i <= n:
        ss = ss + i**2
        i = i + 1
    return ss

# When you've completed your function, uncomment the
# following lines and run this file to test!

print(sum_squares(2))
print(sum_squares(100))
