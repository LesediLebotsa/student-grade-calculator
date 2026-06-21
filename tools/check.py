from database import get_connection, create_users_table, create_user

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    SELECT username, role
    FROM users
""")

print(cursor.fetchall())
# create_user("lecturer1","lecturer123", "lecturer")