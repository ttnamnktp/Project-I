class Transaction:
    def __init__(self, from_account, to_account, money, time_point, atm):
        self.from_account = from_account
        self.to_account = to_account
        self.money = money
        self.time_point = time_point
        self.atm = atm

def executer(transactions, queries):
    number_of_transactions = len(transactions)

    #number_transactions
    def number_transactions():
        return number_of_transactions

    #total_money_transaction
    def total_money_transaction():
        return sum(int(transaction.money) for transaction in transactions)

    #list_sorted_accounts
    sorted_accounts_list = set()
    for transaction in transactions:
        sorted_accounts_list.add(transaction.to_account)
        sorted_accounts_list.add(transaction.from_account)
    sorted_accounts_list = sorted(sorted_accounts_list)
    def list_sorted_accounts():
        sorted_accounts_list_string = ""
        for _ in sorted_accounts_list:
            sorted_accounts_list_string = sorted_accounts_list_string + _ + " "
        return sorted_accounts_list_string

    #total_money_transaction_from
    money_transaction_dict = {}
    for transaction in transactions:
        if transaction.from_account not in money_transaction_dict:
            money_transaction_dict[transaction.from_account] = int(transaction.money)
        else:
            money_transaction_dict[transaction.from_account] += int(transaction.money)
    def total_money_transaction_from(account):
        if account not in money_transaction_dict:
            return 0
        return money_transaction_dict[account]

    #inspect_cycle = using backtrack
    def inspect_cycle(started_account, visited, k, count_cycle, final_account):
        if k == count_cycle:
            return final_account == started_account
        for transaction in transactions:
            if transaction.from_account == started_account and transaction not in visited:
                visited.add(transaction)
                print(transaction)
                if inspect_cycle(transaction.to_account, visited, k, count_cycle + 1, final_account):
                    return True
                visited.remove(transaction)  # backtrack

        return False

    #excecuting queries
    results = []
    for query in queries:
        if query[0] == "?number_transactions":
            results.append(number_transactions())
        elif query[0] == "?total_money_transaction":
            results.append(total_money_transaction())
        elif query[0] == "?list_sorted_accounts":
            results.append(list_sorted_accounts())
        elif query[0] == "?total_money_transaction_from":
            results.append(total_money_transaction_from(query[1]))
        elif query[0] == "?inspect_cycle":
            visited_account = set()
            results.append(1 if inspect_cycle(query[1], visited_account, int(query[2]),0, query[1]) else 0)

    return results

def main():
    transactions = []
    while True:
        read_info = input().split()
        if read_info[0] == "#":
            break
        transaction = Transaction(read_info[0],read_info[1],read_info[2],read_info[3],read_info[4])
        transactions.append(transaction)

    queries = []
    while True:
        query = input().split()
        if query[0] == "#":
            break
        queries.append(query)

    results = executer(transactions,queries)
    for each in results:
        print(each)

if __name__ == "__main__":
    main()



