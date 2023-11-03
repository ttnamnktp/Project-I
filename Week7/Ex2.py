# cau truc tu dien de luu tru price theo shop hoac theo shop va customer
# de tranh time limited exceed

#tao lop ECommerceSystem
#chua list order, tong revunue, tu dien luu tru price theo shop va theo shop and revenue
class ECommerceSystem:
    def __init__(self):
        self.orders = []
        self.total_revenue = 0
        self.shop_revenue = {}
        self.customer_shop_revenue = {}

    # them order vao mang
    def add_order(self, customer_id, product_id, price, shop_id, time_point):
        self.orders.append((customer_id, product_id, price, shop_id, time_point))
        self.total_revenue += price
        if shop_id not in self.shop_revenue:
            self.shop_revenue[shop_id] = price
        else:
            self.shop_revenue[shop_id] += price
        if (customer_id, shop_id) not in self.customer_shop_revenue:
            self.customer_shop_revenue[(customer_id, shop_id)] = price
        else:
            self.customer_shop_revenue[(customer_id, shop_id)] += price


    # tinh revenue theo time
    def calculate_revenue_in_period(self, from_time, to_time):
        revenue = 0
        for order in self.orders:
            _, _, price, _, time_point = order
            if from_time <= time_point <= to_time:
                revenue += price
        return revenue

    def execute_queries(self, queries):
        results = []
        for query in queries:
            if query == "?total_number_orders":
                results.append(len(self.orders))
            elif query == "?total_revenue":
                results.append(self.total_revenue)
            elif query.startswith("?revenue_of_shop "):
                shop_id = query.split()[1]
                results.append(self.shop_revenue.get(shop_id, 0))
            elif query.startswith("?total_consume_of_customer_shop "):
                _, customer_id, shop_id = query.split()
                results.append(self.customer_shop_revenue.get((customer_id, shop_id), 0))
            elif query.startswith("?total_revenue_in_period "):
                _, from_time, to_time = query.split()
                revenue_in_period = self.calculate_revenue_in_period(from_time, to_time)
                results.append(revenue_in_period)
        return results

if __name__ == "__main__":
    ecommerce_system = ECommerceSystem()

    # Parse the operational data
    while True:
        line = input().strip()
        if line == "#":
            break
        customer_id, product_id, price, shop_id, time_point = line.split()
        ecommerce_system.add_order(customer_id, product_id, int(price), shop_id, time_point)

    # Parse and execute queries
    queries = []
    while True:
        query = input().strip()
        if query == "#":
            break
        queries.append(query)

    results = ecommerce_system.execute_queries(queries)
    for result in results:
        print(result)
