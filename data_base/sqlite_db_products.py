import sqlite3 as sq

def sql_start_products():
    global base, cur
    base = sq.connect('products.db')
    cur = base.cursor()
    if base:
        print('data base products connect Ok!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS products(name TEXT PRIMARY KEY, description TEXT, category TEXT,img)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO products VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

