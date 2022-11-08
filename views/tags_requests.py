import sqlite3
import json

def create_tag(new_tag):
    """Creating a new tag then adding it to 'Tags' table in db.sqlite3"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'], ))
        
        id = db_cursor.lastrowid
        new_tag['id'] = id
    
    return json.dumps(new_tag)
