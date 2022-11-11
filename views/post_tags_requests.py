import sqlite3
import json
from models import PostTags, Posts, Tags

def get_posts_by_tag(tag_id):
    '''gets all posts featuring a specific tag'''
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id,
            p.title,
            p.image_url,
            p.content,
            t.label
        FROM PostTags pt
        JOIN Posts p
            ON p.id = pt.post_id
        JOIN Tags t
            ON t.id = pt.tag_id
        WHERE pt.tag_id = ?
        """, ( tag_id, ))

        post_tag_array = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tags = PostTags(row['id'], row['post_id'], row['tag_id'])
            post_tag_array.append(post_tags.__dict__)

            post = Posts("", "", "", row['title'], "", row['image_url'], row['content'], "")
            post_tags.post = post.__dict__

            tag = Tags("", row['label'])
            post_tags.tag = tag.__dict__

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
