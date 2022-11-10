import sqlite3
import json
from models import Comments, Posts, User

def get_all_comments():
    """
    []
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content
        FROM Comments c
        """)
        comments = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            comment = Comments(row['id'], row['author_id'], row['post_id'], row['content'])
            comments.append(comment.__dict__)

    return json.dumps(comments)

def get_single_comment(id):
    """
    []
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content
        FROM Comments c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        comment = Comments(data['id'], data['author_id'], data['post_id'],
                            data['content'])

    return json.dumps(comment.__dict__)


def create_comment(new_comment):
    """
    []
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( author_id, post_id, content )
        VALUES
            ( ?, ?, ? );
        """, (new_comment['author_id'],
              new_comment['post_id'], new_comment['content']))

        id = db_cursor.lastrowid
        new_comment['id'] = id


    return json.dumps(new_comment)

def delete_comment(id):
    """
    []
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

def update_comment(id, new_comment):
    """
    []
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                author_id = ?,
                post_id = ?,
                content = ?
        WHERE id = ?
        """, (new_comment['author_id'],
              new_comment['post_id'], new_comment['content'],
              id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_comments_by_post(post_id):
    """
    []
    """

    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content,
            p.title,
            u.first_name,
            u.last_name,
            u.profile_image_url,
            u.username
        FROM Comments c
        JOIN Posts p
        ON p.id = c.post_id
        JOIN Users u
        ON u.id = c.author_id
        WHERE c.post_id = ?
        """, ( post_id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comments(row['id'], row['author_id'],
                            row['post_id'], row['content'])
            comments.append(comment.__dict__)
            post = Posts(row['id'],"", "", row['title'],
                         "", "", "", "")
            user = User(row['id'], row['first_name'], row['last_name'], "", "",
                        row['username'], "",row['profile_image_url'], "", "")
            comment.post = post.__dict__
            comment.user = user.__dict__
        return json.dumps(comments)
