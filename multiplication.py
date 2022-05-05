### AKKAMA CODE

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


### YOGI CODE
def yogi_code():
    import time
    from datetime import date
    import os

    def getTables(factor, times) -> list:
        tables = []
        mtables = []
        n = 1
        while n <= times:
            multiple = n * factor
            tables.append(f"{factor} x {n} = " + str(multiple))
            mtables.append(multiple)
            n = n + 1
        return (tables, mtables)
    def writeTxtFile(tables, fileName, folder):
        if (not os.path.exists(folder)):
            os.mkdir(folder)
        no_comma = 1
        file = open(fileName, 'w')
        for num in tables:
            if (no_comma != len(tables)):
                file.write(str(num) + ", \n")
            else:
                file.write(str(num))
            no_comma = no_comma + 1
        file.close()
    def createFileName(folder) -> str:
        werid_time = time.localtime()
        current_time = time.strftime("%H-%M-%S", werid_time)
        today = date.today()
        current_date = today.strftime("%d-%m-%y")
        fileName = folder + "/" +current_date + "-" + current_time + ".txt"
        return fileName

    def yogi_main():
        factor = int(input("Enter the number to get its tables: "))
        times = int(input(f"Enter the times to get the {factor}'s tables: "))
        fileName = str(createFileName("mul"))
        tables = getTables(factor, times)[0]
        mtables = getTables(factor, times)[1]
        print(f"Writing to {fileName}...")
        time.sleep(2)
        writeTxtFile(tables, fileName, "mul")
        print(f"Succesfully Wrote to {fileName}!")
        print(f"\nTables: {mtables}")

    yogi_main()


# Hi, If you want to see Akkama's Code un-comment the below line
    # and type mul in the below terminal or use python3 multiplication.py
akkama_code()

# Hi, If you want to see Yogi's Code un-comment the below line
    # and type mul in the below terminal or use python3 multiplication.py
# yogi_code()