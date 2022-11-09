"""module docstring"""
import sqlite3
import json
from models import PostReactions

def get_all_post_reactions():
    """_summary_
    Returns:
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.user_id,
            a.reaction_id,
            a.post_id
        FROM PostReactions a           
        """)
        post_reactions = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            post_reaction = PostReactions(row['id'], row['user_id'],
                                          row['reaction_id'], row['post_id'])
            post_reactions.append(post_reaction.__dict__)
    return json.dumps(post_reactions)

def get_single_post_reaction(id):
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
            a.user_id,
            a.reaction_id,
            a.post_id
        FROM PostReactions a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post_reaction = PostReactions(data['id'], data['user_id'],
                                      data['reaction_id'], data['post_id'])
        return json.dumps(post_reaction.__dict__)

def create_post_reaction(new_post_reaction):
    """_summary_

    Args:
        reaction (_type_): _description_

    Returns:
        _type_: _description_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostReactions
            (user_id, reaction_id, post_id)
        VALUES
            ( ?, ?, ? );
        """, (new_post_reaction['user_id'], new_post_reaction['reaction_id'],
              new_post_reaction['post_id']))

        id = db_cursor.lastrowid
        new_post_reaction['id'] = id


    return json.dumps(new_post_reaction)

def update_post_reaction(id, new_post_reaction):
    """_summary_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE PostReactions
            SET
                user_id = ?,
                reaction_id = ?,
                post_id = ?
        WHERE id = ?
        """, (new_post_reaction['user_id'],new_post_reaction['reaction_id'],
              new_post_reaction['post_id'], id, ))
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
def delete_post_reaction(id):
    """_summary_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostReactions
        WHERE id = ?
        """, (id, ))
