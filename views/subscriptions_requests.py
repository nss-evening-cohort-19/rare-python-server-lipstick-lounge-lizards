"""module docstring"""
import sqlite3
import json
from models import Subscriptions

def get_all_subscriptions():
    """_summary_
    Returns:
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.follower_id,
            a.author_id,
            a.created_on
        FROM Subscriptions a           
        """)
        subscriptions = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            subscription = Subscriptions(row['id'], row['follower_id'], row['author_id'], row['created_on'])
            subscriptions.append(subscription.__dict__)
    return json.dumps(subscriptions)

def get_single_subscription(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.follower_id,
            a.author_id,
            a.created_on
        FROM Subscriptions a
        WHERE a.id = ?
        """, ( id, ))


        data = db_cursor.fetchone()

        subscription = Subscriptions(data['id'], data['follower_id'], data['author_id'], data['created_on'])
        return json.dumps(subscription.__dict__)

def create_subscription(new_subscription):
    """_summary_

    Args:
        subscription (_type_): _description_

    Returns:
        _type_: _description_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions
            ( follower_id, author_id, created_on )
        VALUES
            ( ?, ?, ? );
        """, (new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_on'], ))

        id = db_cursor.lastrowid
        new_subscription['id'] = id


    return json.dumps(new_subscription)

def update_subscription(id, new_subscription):
    """_summary_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Subscriptions
            SET
                follower_id = ?,
                author_id = ?,
                created_on = ?
        WHERE id = ?
        """, (new_subscription['follower_id'], new_subscription['author_id'],
              new_subscription['created_on'], id, ))
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def delete_subscription(id):
    """_summary_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Subscriptions
        WHERE id = ?
        """, (id, ))
