def akkama_code():
    factor = int(input("Enter the number to get its tables: "))
    times = int(input(f"Enter the times to get the {factor}'s tables: "))
    tables = []

    n = 1

    while n <= times:
        multiple = n * factor
        tables.append(multiple)
        n = n + 1

    for x in tables:
        print(x)