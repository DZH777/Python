import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "CREATE TABLE words (word TEXT PRIMARY KEY NOT NULL,usage_count INT DEFAULT 1 NOT NULL);"
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cur.execute(ddl)
    conn.close()


def save_words_to_database(database_path: str, words_list: list):
    # TODO: save the words to the database
    pass
