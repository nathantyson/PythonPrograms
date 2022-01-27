#Pgm11_Salesperson
#Name: Nathan Tyson

#This program will utilize a Class that gives information on a sales person

#Specifications:
                #This program is intended to read a txt file full of information on salesmen, including their ID
                # number, their full name, and a sample of their sales.
                #Class Salesperson encapsulates this data and forms it together for each salesman in the file.
                #Class Salesforce actually reads the file and uses the Salesperson methods in order to complete
                # its own methods.
                #Then this data is imported into the test driver, where the information will be displayed.

#Design:
        #First comes the Salesperson class, with the __init__ initializing the ID, name, and list of sales.
        #Then methods to get the ID and the name.
        #Then a method to add sales to the list, as well as one to add all of the sales together, and a method that
        #returns a copy of that list.
        #then there is a method to determine whether or not the salesperson met the quota or not,
        # as well asa a method to compare a certain salesman against another salesman.
        #finally there is a string method to display information on the salesman.

        #Then comes the Salesforce class, with the __init__ establishing the Salesperson methods.
        #Then a method that actually reads the file and splits it up into it's respective identifiers.
        #Then there is a method to display whether or not a salesman met the quota report.
        #A method to display the top seller, as well as a method to display an individual salesman and all their sales.

class SalesPerson:
    def __init__(self, idnumber, name, sales):
        self.idnumber = idnumber
        self.name = name
        self.sales = []

    def get_id(self, idnumber):
        return idnumber

    def get_name(self, name):
        return name

    def enter_sale(self, a_sale):
        new_entry = self.sales.append(a_sale)
        return new_entry

    def total_sales(self):
        total = sum(self.sales)
        return total

    def get_sales(self):
        copy = self.sales.copy()
        return copy

    def met_quota(self, quota):
        total = SalesPerson.total_sales(self)
        if total >= quota:
            return True
        else:
            return False

    def compare_to(self, other_person):
        this_total = SalesPerson.total_sales(self)
        if this_total == other_person:
            return "Their total sales are equal."
        elif this_total > other_person:
            return "This Salesman has greater total sales than the other salesman."
        elif this_total < other_person:
            return "This Salesman has lesser total sales than the other salesman."

    def __str__(self):
        return "This Salesman's ID number: {self.idnumber}. Their name is: {self.name}. " \
               "Their total sales are {self.sales}.".format(self=self)




class SalesForce:
    def __init__(self):
        self.list = []
        self.totalsales = SalesPerson.total_sales
        self.quota = SalesPerson.met_quota
        self.idnumber = SalesPerson.get_id
        self.name = SalesPerson.get_name
        self.sales = SalesPerson.get_sales


    def add_data(self, filename):
        infile = open(filename, "r")
        for line in infile:
            list = line.split()
            idnumber = int(list[0])
            name = list[1:3]
            name = " ".join(name)
            sales = list[3:-1]

            self.idnumber = idnumber
            self.name = name
            self.sales = sales
            return idnumber, name, sales

    def quota_report(self, quota):
        print("ID: ", self.idnumber , "Name: ", self.name, "Total Sales: ", self.totalsales,
              "Did they meet the quota? ", self.quota)

    def top_sales_person(self):
        sales = self.sales
        top_seller = max(sales)
        return top_seller

    def individual_sale(self, id):
        return self.sales
