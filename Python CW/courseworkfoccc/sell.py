file = open("laptop.txt","r")
mydict = {}
lap_id= 1


for line in file:
    line = line.replace("\n","")
    mydict[lap_id]=line.split(",")
    lap_id += 1


def sell_laptop():
            print("Enter your name and number for bill: ")
            print("---------------------------------------------------------------------")
            print("\n")
            name = input("Enter your name ")
            phone = input("Enter your phone number ")
            print("----------------------------------------------------------------------")
            print("S.N    Name     Brand           Price       Quantity      CPU     graphics")
            a = 1
            file = open('laptop.txt','r')
            for line in file:
                print(a,"\t"+line.replace(",","\t"))
                a+=1
            file.close()
            print("-------------------------------------------------------------------------")


            valid_id = int(input("Enter laptop ID: "))
            while valid_id <=0 or valid_id > len(mydict):
                print("Error enter again")
                valid_id = int(input("Enter laptop ID: "))

            user_quantity = int(input("Enter quantity of laptop "))

            get_quantity = mydict[valid_id][3]
            while user_quantity <= 0 or user_quantity>int(get_quantity):
                print("Quantity invalid ")
                user_quantity = int(input("Enter quantity of laptop "))
            
            mydict[valid_id][3] = int(mydict[valid_id][3])+ int(user_quantity)
            file = open('laptop.txt','w')

            for values in mydict.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()

            product_name = str(mydict[valid_id][0])
            user_quantity = str(user_quantity)
            per_price = str(mydict[valid_id][2])
            price = str(mydict[valid_id][2].replace("$",""))
            amount = str(int(price)*int(user_quantity))
            tot = str(float(int(amount)+(0.13)*(int(amount))))

            shipping_cost = input("Do you want your laptop to be shipped? (y/n)").lower()
            if shipping_cost == "y":
                tot = str(float(tot)+100)

            dir = [product_name,user_quantity,per_price,amount,tot]                    
     
     
            with open('sell.txt','w') as sell:
                
                sell.write("\n\n\n----------------------------------------------------------------------------------\n")
                sell.write("\t\t\t\tBILL\n")
                sell.write("----------------------------------------------------------------------------------\n")
                sell.write("Sargat electronics\n")
                sell.write("\t \t \t Hattiban,lalitpur\n")
                sell.write("----------------------------------------------------------------------------------\n\n")

                sell.write("\nName of customer: "+name+"\n")
                sell.write("Phone number of customer: "+phone+"\n")
                sell.write("\n")
                sell.write("----------------------------------------------------------------------------------\n")
                sell.write("\t\t\t   Your order:\n")
                sell.write("----------------------------------------------------------------------------------\n")
                sell.write("\nProduct\t quantity\t per Price\t  amount\t Tot\n")
                for i in dir:
                    sell.write(i+"\t")

            f = open('sell.txt','r')
            inside = f.read()
            print(inside)
            f.close()