def task3():
    b=input("Sex: ")
    a=float(input("Hemoglobin: "))
    if b == "female":
        if a < 117:
            print("low hemoglobin")
        elif a <= 155:
            print("normal hemoglobin")
        else:
            print("high hemoglobin")
    if b == "male":
        if a < 134:
            print("low hemoglobin")
        elif a <= 167:
            print("normal hemoglobin")
        else:
            print("high hemoglobin")

task3() 


        