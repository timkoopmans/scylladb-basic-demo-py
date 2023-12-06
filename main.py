from cassandra.cluster import Cluster
import uuid


class User:
    def __init__(self, first_name, last_name, age):
        self.user_id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def create_user(session, user):
    query = "INSERT INTO demo.users (user_id, first_name, last_name, age) VALUES (%s, %s, %s, %s)"
    session.execute(query, (user.user_id, user.first_name, user.last_name, user.age))


def read_user_data(session, user_id):
    query = "SELECT * FROM demo.users WHERE user_id = %s LIMIT 1"
    result = session.execute(query, (user_id,))
    for row in result:
        print(row)


def update_user(session, user_id, new_age):
    query = "UPDATE demo.users SET age = %s WHERE user_id = %s"
    session.execute(query, (new_age, user_id))


def delete_user(session, user_id):
    query = "DELETE FROM demo.users WHERE user_id = %s"
    session.execute(query, (user_id,))


def main():
    cluster = Cluster(['0.0.0.0'])
    session = cluster.connect()

    # Example: Creating a new user
    new_user = User("Dolly", "Partition", 77)
    create_user(session, new_user)

    # Example: Reading user data
    read_user_data(session, new_user.user_id)

    # Example: Updating a user's age
    update_user(session, new_user.user_id, 78)

    # Example: Deleting a user
    delete_user(session, new_user.user_id)


if __name__ == "__main__":
    main()
