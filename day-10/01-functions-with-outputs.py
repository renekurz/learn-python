# Convert to Title Case
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

name1 = format_name("anglea", "LOPEZ")
print(name1)

name2 = format_name("aNGeLa", "LOpeZ")
print(name2)