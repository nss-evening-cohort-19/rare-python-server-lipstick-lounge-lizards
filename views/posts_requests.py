import sqlite3
import json
from models import Posts, Categories, User, Subscriptions

def get_all_posts():
    '''gets all of the posts'''
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved
            FROM Posts p
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Posts(row['id'], row['user_id'], row['category_id'], row['title'],
                         row['publication_date'], row['image_url'], row['content'], row['approved'])

            posts.append(post.__dict__)

    return json.dumps(posts)

def get_single_post(id):
    '''get a single post by id'''
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post = Posts(data['id'], data['user_id'], data['category_id'], data['title'],
                    data['publication_date'], data['image_url'], data['content'], data['approved'])

        return json.dumps(post.__dict__)

def create_post(new_post):
    '''creates a new entry to the post table'''
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            (user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            (?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'],
              new_post['category_id'], new_post['title'],
              new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved']))

        id = db_cursor.lastrowid

        new_post['id'] = id

    return json.dumps(new_post)

def update_post(id, new_post):
    '''updates a single post'''
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (new_post['user_id'], new_post['category_id'],
              new_post['title'], new_post['publication_date'],
              new_post['image_url'], new_post['content'], new_post['approved'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def delete_post(id):
    '''deletes a single post'''
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))

def get_post_by_title(title):
    '''get a single post by title'''
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.title = ?
        """, ( title, ))

        data = db_cursor.fetchone()

        post = Posts(data['id'], data['user_id'], data['category_id'], data['title'],
                    data['publication_date'], data['image_url'], data['content'], data['approved'])

        return json.dumps(post.__dict__)

def get_posts_by_user(user_id):
    """_summary_

    Args:
        author_id (_type_): _description_
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor =conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label,
            u.first_name,
            u.last_name,
            u.username,
            u.profile_image_url
        FROM Posts p
        JOIN Users u
        ON u.id = p.user_id
        JOIN Categories c
        ON c.id = p.category_id
        WHERE p.user_id = ?
        """, ( user_id, ))
        posts = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            post = Posts(row['id'], row['user_id'], row['category_id'], row['title'],
                         row['publication_date'], row['image_url'], row['content'],
                         row['approved'])
            category = Categories(row['id'], row['label'])
            user = User(row['id'], row['first_name'], row['last_name'], "", "",
                        row['username'], "",row['profile_image_url'], "", "")
            post.category = category.__dict__
            post.user = user.__dict__
            posts.append(post.__dict__)
        return json.dumps(posts)

def get_posts_by_category(category_id):
    """_summary_

    Args:
        category_id (_type_): _description_
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label category_name,
            u.username,
            u.first_name,
            u.last_name
        FROM Posts p
        JOIN Categories c on c.id = p.category_id
        JOIN Users u on u.id = p.user_id
        WHERE p.category_id = ?
        """, ( category_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Posts(row['id'], row['user_id'], row['category_id'],
                         row['title'], row['publication_date'], row['image_url'],
                         row['content'], row['approved'])
            posts.append(post.__dict__)

            category = Categories(row['id'], row['category_name'])
            user = User(row['id'], row['first_name'], row['last_name'],
                        "", "", row['username'], "",
                        "", "", "")
            post.category = category.__dict__
            post.user = user.__dict__

    return json.dumps(posts)

def get_posts_by_subscription(follower_id):
    """_summary_

    Args:
        follower_id (_type_): _description_
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor =conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label,
            u.first_name,
            u.last_name,
            u.username,
            u.profile_image_url,
            a.id,
            a.author_id,
            a.follower_id,
            a.created_on
        FROM Posts p
        JOIN Subscriptions a
        JOIN Users u
        ON a.author_id = p.user_id
          AND a.follower_id = u.id
        JOIN Categories c
        ON c.id = p.category_id
        WHERE follower_id = ?
        """, ( follower_id ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Posts(row['id'], row['user_id'], row['category_id'],
                         row['title'], row['publication_date'], row['image_url'],
                         row['content'], row['approved'])
            posts.append(post.__dict__)

            category = Categories(row['id'], row['label'])
            subscription = Subscriptions(row['id'], row['follower_id'], row['author_id'],
                                         row['created_on'])
            user = User(row['id'], row['first_name'], row['last_name'],
                        "", "", row['username'], "",
                        "", "", "")
            post.category = category.__dict__
            post.subscription = subscription.__dict__
            post.user = user.__dict__

    return json.dumps(posts)
