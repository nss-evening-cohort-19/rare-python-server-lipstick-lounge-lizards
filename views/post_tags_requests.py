import sqlite3
import json
from models import PostTags

def get_posts_by_tag(tag_id):
    '''gets all posts featuring a specific tag'''
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id
            pt.post_id,
            pt.tag_id,
        FROM PostTags pt

        """, ( tag_id, ))

        post_tag = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tags = PostTags(row['id'], row['post_id'], row['tag_id'])
            post_tag.append(PostTags.__dict__)

    return json.dumps(post_tags)
