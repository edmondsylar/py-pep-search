
def create_pep_table():
    create_table = """ CREATE TABLE peps(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    pep_name TEXT NOT NULL,
    link TEXT NOT NULL,
    description INTEGER NOT NULL
    )
    """

    con = get_database_connection()
    con.execute(create_table)
    con.close()

    return False