from datetime import datetime, date
from utilities.db.db_manager import dbManager


class User:

    def __init__(self):
        super().__init__()
        self.cursor = None


    def add_user(self,email, username, birthday, password):
        query = "INSERT INTO users(email, username, birthday, password, date_added, points) VALUES ('%s', '%s', '%s', '%s','%s', '%s')" % (
            email, username, birthday, password, date.today(), 0)
        query_result = dbManager.commit(query)
        return query_result


    def search_user(self, email):
        query = f"select * from users where email='%s'" % email
        query_result = dbManager.fetch(query)
        return query_result

    def update_user(self, new_email, username, password, prev_email):
        query = f"UPDATE users set email='%s', username='%s', password='%s' where email='%s'" % \
                (new_email, username, password, prev_email)
        query_result = dbManager.commit(query)
        return query_result

    def add_points(self, points, email):
        points_query = f"SELECT points FROM users where email='%s'" % email
        cur_points = dbManager.fetch(points_query)
        point_lst = []
        for point in cur_points:
            point_lst.append(point.points)
        cur_points = point_lst[0]
        new_points = cur_points + points
        query = f"UPDATE users set points= '%s' where email='%s'" % (new_points, email)
        query_result = dbManager.commit(query)
        return query_result


    def get_points(self, email):
        query = f"SELECT points FROM users where email='%s'" % email
        cur_points = dbManager.fetch(query)
        point_lst = []
        for point in cur_points:
            point_lst.append(point.points)
        cur_points = point_lst[0]
        return cur_points

    def get_birthday(self, email):
        query = f"SELECT birthday FROM users where email='%s'" % email
        birthday = dbManager.fetch(query)
        birthday_lst = []
        for date in birthday:
            birthday_lst.append(date.birthday)
        birthday = birthday_lst[0]
        return birthday



    def use_points(self, email, price):
        query = f"SELECT points FROM users where email='%s'" % email
        cur_points = dbManager.fetch(query)
        point_lst = []
        for point in cur_points:
            point_lst.append(point.points)
        cur_points = point_lst[0]
        new_points = cur_points - price
        query = f"UPDATE users set points= '%s' where email='%s'" % (new_points, email)
        query_result = dbManager.commit(query)
        return query_result


    def delete_user(self, email):
        query = f"delete from users where email='%s'" % email
        query_result = dbManager.commit(query)
        return query_result



# Creates an instance for the User class for export.
#user = User()
