import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI

import logging

async def postgre_start():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    if base:
        logging.info(f"data base connect success!")
    cur.execute('''CREATE TABLE IF NOT EXISTS (
        
        )''')
    
    
    base.commit()
    cur.close()
    base.close()