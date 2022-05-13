# expression
5 + 3

# assignment statement
a = 5 + 3

num = 5
num += 4

print(num += 4)
# produce an error

eval("num += 4")


(another_num := 15)

print(another_num := 15)

eval("(another_num := 15)")

def withdraw_money(account_number):
    if account := locate_account(account_number):
        take_money_from(account)
    else:
        found_no_account()

def withdraw_money(account_number):
    account = locate_account(account_number)
    if account:
        take_money_from(account)
    else:
        found_no_account()


def withdraw_money(account_number):
    if account := locate_account_in_saving(account_number):
        take_money_from_saving(account)
    elif account := locate_account_in_checking(account_number):
        take_money_from_checking(account)
    elif account := locate_account_in_retirement(account_number):
        take_money_from_retirement(account)
    else:
        pass
