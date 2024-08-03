import buy
import sell

print("\n")
print("---------------------------------------------------------")
print("Sargat electronics")
print("Hattiban,Lalitpur")
print("---------------------------------------------------------")





print("name      brand      price       quantity     CPU    graphics")
file = open("laptop.txt",'r')
inside_file = file.read()
print(inside_file)
file.close()



program_loop = True

while program_loop == True:
    print("Press 1 to buy")
    print("Press 2 to sell")
    print("Press 3 to exit")

    user_input = int(input("Enter: "))

    if user_input != 3:

        
                

        

        if user_input == 1:
            buy.buy_laptop()
        if user_input == 2:
            sell.sell_laptop()
    else:
        program_loop = False