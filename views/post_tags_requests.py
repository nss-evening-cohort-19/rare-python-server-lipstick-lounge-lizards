import sqlite3
import json

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
