import csv

def listOfSales():
    sales = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            sale = int(row['sales'])
            sales.append(sale)
    return sales
# print(listOfSales())
def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
            return data

def total_sales():
    list = listOfSales()
    total =sum(list)
    print('Total sales: {}'.format(total))
# total_sales()

def total_sales_return():
    list = listOfSales()
    total = sum(list)
    return total


def average():
    count=0
    total = total_sales_return()
    salesList = listOfSales()
    for row in salesList:
        count+=1
    total = total_sales_return()
    print(total/count)
# average()

def calculate_percentage_change(startPoint,currentPoint):
    return(((currentPoint-startPoint)*100)/startPoint)

# print(calculate_percentage_change(100,50))
def percentage_changes_in_sales():
    sales =listOfSales()
    index = 1
    for each in sales:
        while index < len(sales):
            # print(sales[index])
            # index = index+1
            pc = float(calculate_percentage_change(each,sales[index]))
            index = index + 1
            print("Month {} difference = {}".format(index,pc))


# percentage_changes_in_sales()


def lowestSale():
    saleList = listOfSales()
    saleList.sort()
    print(saleList[0])

def highestSale():
    saleList = listOfSales()
    saleList.sort()
    length = int(len(saleList)-1)
    print(saleList[length])
