import sqlite3
import json
from models import PostTags

def get_all_post_tags():
    '''gets all of the post tags'''
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                pt.id,
                pt.post_id,
                pt.tag_id
            FROM PostTags pt
        """)

        post_tag_array = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = PostTags(row['id'], row['post_id'], row['tag_id'])

            post_tag_array.append(post_tag.__dict__)

    return json.dumps(post_tag_array)

def create_post_tags(new_post_tag):
    '''creates a new tag on a post'''
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            (post_id, tag_id)
        VALUES
            (?, ?);
        """, (new_post_tag['post_id'], new_post_tag['tag_id']))

        id = db_cursor.lastrowid

        new_post_tag['id'] = id

    return json.dumps(new_post_tag)

def update_post_tags(id, new_post_tag):
    '''updates a tag on a post'''
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE PostTags
            SET
                post_id = ?,
                tag_id =?
        WHERE id = ?
        """, (new_post_tag['post_id'], new_post_tag['tag_id'], id, ))
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
