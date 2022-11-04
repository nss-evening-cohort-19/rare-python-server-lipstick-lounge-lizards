import sqlite3
import json
from models import Reactions

def get_all_reactions():
    """_summary_
    Returns:
    """
    with sqlite3.connect('./db.sqlite3') as conn:
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
