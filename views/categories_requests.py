import sqlite3
import json
from models import Categories

def get_all_categories():
    """Get all categories"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)
      
        categories = []
      
        dataset = db_cursor.fetchall()
      
        for row in dataset:
            category = Categories(row['id'], row['label'])
          
            categories.append(category.__dict__)
  
    return json.dumps(categories)

def create_category(new_category):
    """Creating a new category then adding it to 'Categories' table in db.sqlite3"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Categories
            ( label )
        VALUES
            ( ? );
        """, (new_category['label']))
        
        id = db_cursor.lastrowid
        
        new_category['id'] = id
