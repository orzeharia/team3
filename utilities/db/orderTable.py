from datetime import datetime

from utilities.db.db_manager import dbManager


class Order:

    def __init__(self):
        super().__init__()
        self.cursor = None

    def add_order(self, email, time_wanted, address, phone_number, pizza, amount, total_price, cc_number, cc_exp, cvv):
        query = "INSERT INTO orders(email, order_time, time_wanted, address, phone_number, pizza, amount," \
                " total_price, cc_number, cc_exp, cvv) VALUES ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s')" % (
            email, datetime.today(), time_wanted, address, phone_number, pizza, amount,
            total_price, cc_number, cc_exp, cvv)
        query_result = dbManager.commit(query)
        print(query_result)

    def search_order(self, email):
        query = f"select * from orders where email='%s'" % email
        query_result = dbManager.fetch(query)
        return query_result


    # def update_order(self):
    #     query = f"UPDATE orders set  where
    #     query_result = dbManager.commit(query)
    #     return query_result