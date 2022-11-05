"""module docstring"""
import sqlite3
import json
from models import Reactions

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

        db_cursor.execute("""
        SELECT
            a.id,
            a.label,
            a.image_url
        FROM Reactions a
        WHERE a.id = ?
        """, ( id, ))


        data = db_cursor.fetchone()

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

def update_reaction(id, new_reaction):
    """_summary_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Reactions
            SET
                label = ?,
                image_url = ?
        WHERE id = ?
        """, (new_reaction['label'], new_reaction['image_url'], id, ))
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def delete_reaction(id):
    """_summary_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Reactions
        WHERE id = ?
        """, (id, ))
