# If you define a docstring and hover over the function name, you can see this as description of the function
# Docstring has to go at the first line after function definition
def format_name(f_name, l_name):
    """Take a first and last name and format it to 
    return the title case version of the name."""
    
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))