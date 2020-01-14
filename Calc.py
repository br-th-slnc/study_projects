
# coding: utf-8

# In[5]:


while True:
    result = ''
    option = input(' Если хотите что-то посчитать, напишите "старт".\n Если хотите выйти из программы, напишите "выход": ')
    if option == "выход" or option == "exit":
        print("Выход из программы")
        break

    if option == "старт" or option == "start":
        num1 = input('Введите первое число: ') 
        num2 = input('Введите второе число: ')
        
        num1 = int(num1)
        num2 = int(num2)
       
        operation = input('Выберите арифметическую операцию и введите ниже ее символ  +, -, *, / : \n ')
        while result == '':
            
            if (operation != "*")&(operation != "/")&(operation != "+")&(operation != "-"):
                operation = input("Введите один из символов арифм.операций: +, -, *, /")
                continue
                
            if operation == "*":
                result = num1 * num2
                print("Результат:", result)
            
            elif operation == "/":
                result = num1 / num2
                print("Результат:", result)
            
            elif operation == "+":
                result = num1 + num2
                print("Результат:", result)

            elif operation == "-":
                result = num1 - num2
                print("Результат:", result)

