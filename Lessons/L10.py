cats = {
    'red': "The red cat is very angry. This breed...",
    'blue cat': "sdkgfosdngsgdo vfgijd ofigjdofigd oifg d5hyftnfntjhftnj " +
                "fntufytfnytfyfntybftyft ftyft5tbftbjftnujuftjftjn d",
    'yellow cat': "rgdnhdrnhdnrhrbd"
}
print(cats["red"])

employees_salary = {
    'tom john': '3000 per month',
    'sarah smith': '2000 per month',
}

employees_monthly_salary = {
    'tom john': 3000,
    'sarah smith': 2000,
}

animals = {
    'dogs': ["Heeler", "Bulldog"],
    'cats2': {
        'red': "The red cat is very angry. This breed...",
        'blue cat': "sdkgfosdngsgdo vfgijd ofigjdofigd oifg d5hyftnfntjhftnj " +
        "fntufytfnytfyfntybftyft ftyft5tbftbjftnujuftjftjn d",
        'yellow cat': "rgdnhdrnhdnrhrbd",
        'favorites': ["Tommy", "Jimmy", [2342, 234234, 99999, [345435435, 345345, 0]]]
    }
}


nested_dict = {
    'dictA': {'key_1': 'value_1'},
    'dictB': {'key_2': 'value_2'}
}

print(employees_monthly_salary['tom john']*2)

print(animals['cats2']['favorites'][2][3][2])
