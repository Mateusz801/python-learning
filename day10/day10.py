# Functions with outputs
def my_function():
    return 3 * 2


output = my_function()


# Multiple return values
# Code after return is not executed
# Docstrings - three quotation marks under function definition
def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case of the name"""
    # String starting with capital letter, later small
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("MaTeUSZ", "ZYGMUNT")
print(formatted_string)


# Ex1
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(p_year, p_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(p_year) and p_month == 2:
        return 29
    else:
        return month_days[p_month - 1]


year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
