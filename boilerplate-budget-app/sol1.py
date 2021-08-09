class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
        self.spent = 0

    def deposit(self, amount, description=""):
        self.ledger.append(
            {"amount": amount, "description": description or ""})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if(amount > self.balance):
            return False
        else:
            self.spent += amount
            self.balance -= amount
            self.ledger.append(
                {"amount": -amount, "description": description or ""})
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if(amount > self.balance):
            return False
        else:
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        s = 0
        out = ''
        out += self.name.center(30, "*")+'\n'
        for i in self.ledger:
            out += '{0: <23}'.format(i['description'][:23]) + \
                "{:.2f}".format(i["amount"]).rjust(7) + '\n'
            s += i['amount']
        out += "Total: {:.2f}".format(s)

        return out


def create_spend_chart(categories):
    s = ''
    s += "Percentage spent by category"+'\n'
    total_spent = sum(i.spent for i in categories)
    max_len_name = max(len(i.name) for i in categories)
    # print("Total: ",total_spent)
    percentage_spent = [int(i.spent/total_spent*100) //
                        10*10 for i in categories]

    number_of_category = len(categories)

    for i in range(100, -10, -10):
        s += str(i).rjust(3)+'|'
        for c in range(number_of_category):
            if(percentage_spent[c] >= i):
                s += ' o '
            else:
                s += '   '
        s += ' \n'
    s += ('    '+'---'*number_of_category+'-'+'\n')

    for i in range(int(max_len_name)):
        s += '    '
        for c in categories:
            if(len(c.name) > i):
                s += f' {c.name[i]} '
            else:
                s += '   '
        s += ' '
        if(i < max_len_name-1):
            s += '\n'
    return s
