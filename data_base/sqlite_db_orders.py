import sqlite3 as sq

def sql_start_orders():
    global base, cur
    base = sq.connect('orders.db')
    cur = base.cursor()
    if base:
        print('data base orders connect Ok!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS orders(id TEXT, pizza TEXT, amount TEXT, status TEXT)')
    base.commit()


async def sql_add_order(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO orders VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()