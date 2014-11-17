from modelbicycleclass import *

#Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
bike_1 = Bicycle('Ant', '110', 150)
bike_2 = Bicycle('Bee', '120', 170)
bike_3 = Bicycle('Cat', '130', 250)
bike_4 = Bicycle('Dog', '140', 550)
bike_5 = Bicycle('Eagle', '150', 750)
bike_6 = Bicycle('Flamingo', '160', 1200)
currentinventory = [bike_1, bike_2, bike_3, bike_4, bike_5, bike_6]

#Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
cust_1 = Customers('Paul', 200)
cust_2 = Customers('Mary', 500)
cust_3 = Customers('Jim', 1000)
cust = [cust_1, cust_2, cust_3]

bikeshop_1 = Bikeshops('SFbikeshop', currentinventory)

custbikelist = []

print 'The current inventory is '

for bike in currentinventory:
 print (bike.modelname)
 
for customer in cust:
    for bike in bikeshop_1.currentinventory:
        if customer.fund >= bikeshop_1.sellprice(bike):
           custbikelist.append(bike)
    print (customer.custname) + " has enough fund to buy "
    for bike in custbikelist:
        print bike.modelname
    del custbikelist[:]
# each customer purchases a bike. print a model, cost and how much money they have left
print cust_1.custname + ' has purchased ' + currentinventory[0].modelname + ' and paid ' + str(bikeshop_1.sellprice(bike_1)) + ' . The fund this customer has left is ' + str((cust_1.fund)-(bikeshop_1.sellprice(bike_1)))
print cust_2.custname + ' has purchased ' + currentinventory[1].modelname + ' and paid ' + str(bikeshop_1.sellprice(bike_2)) + ' . The fund this customer has left is ' + str((cust_2.fund)-(bikeshop_1.sellprice(bike_2)))
print cust_3.custname + ' has purchased ' + currentinventory[2].modelname + ' and paid ' + str(bikeshop_1.sellprice(bike_3)) + ' . The fund this customer has left is ' + str((cust_3.fund)-(bikeshop_1.sellprice(bike_3)))

purchased_list = [0,1,2]

for purchased in purchased_list:
	currentinventory[purchased] = 'removed'
for purchased in range(0,currentinventory.count('removed')):
	currentinventory.remove('removed')

# print the remaining inventory and the profit the shop makes

print 'the remaining inventory is '
for bike in currentinventory:
    print (bike.modelname)


profit_perbike_1 = ((bikeshop_1.sellprice(bike_1)) - (bike_1.cost))
profit_perbike_2 = ((bikeshop_1.sellprice(bike_2)) - (bike_2.cost))
profit_perbike_3 = ((bikeshop_1.sellprice(bike_3)) - (bike_3.cost))
total_profit = [profit_perbike_1, profit_perbike_2, profit_perbike_3]
sum_total = sum(total_profit)
print 'SFbikeshop has made a profit of ' + str(sum_total)
