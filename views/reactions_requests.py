"""module docstring"""
import sqlite3
import json
from models import Reactions

REACTIONS = [
        {
        "id": 7,
        "label": [
            "kiss"
        ],
        "image_url": "https://pngtree.com/freepng/kiss-emoji-vector-icon_3719375.html"
    },
    ]
def get_all_reactions():
    """_summary_
    Returns:
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.label,
            a.image_url
        FROM Reactions a           
        """)
        reactions = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            reaction = Reactions(row['id'], row['label'], row['image_url'])
            reactions.append(reaction.__dict__)
    return json.dumps(reactions)

def get_single_reaction(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.label,
            a.image_url
        FROM Reactions a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        reaction = Reactions(data['id'], data['label'], data['image_url'])
        return json.dumps(reaction.__dict__)

def create_reaction(new_reaction):
    """_summary_

    Args:
        reaction (_type_): _description_

    Returns:
        _type_: _description_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO reactions
            ( label, image_url )
        VALUES
            ( ?, ? );
        """, (new_reaction['label'],new_reaction['image_url']))

        id = db_cursor.lastrowid
        new_reaction['id'] = id


    return json.dumps(new_reaction)

# def update_animal(id, new_animal):
#     """_summary_
#     """
#     with sqlite3.connect("./db.sqlite3") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         UPDATE Animal
#             SET
#                 name = ?,
#                 breed = ?,
#                 status = ?,
#                 location_id = ?,
#                 customer_id = ?
#         WHERE id = ?
#         """, (new_animal['name'], new_animal['breed'],
#               new_animal['status'], new_animal['locationId'],
#               new_animal['customerId'], id, ))

#         # Were any rows affected?
#         # Did the client send an `id` that exists?
#         rows_affected = db_cursor.rowcount

#     if rows_affected == 0:
#         # Forces 404 response by main module
#         return False
#     else:
#         # Forces 204 response by main module
#         return True
