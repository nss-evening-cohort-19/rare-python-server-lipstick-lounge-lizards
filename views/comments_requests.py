import sqlite3
import json
from models import comments

COMMENTS = [
  {
            "id": 1,
            "author_id": "",
            "post_id": "",
            "content": ""
        },
        {
            "id": 2,
            "author_id": "",
            "post_id": "",
            "content": ""
        }
]

def post_comment():
    """_summary_
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
        FROM Comment c
        """)
