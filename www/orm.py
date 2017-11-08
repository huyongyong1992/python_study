__author__ = 'Young Hu'

import asyncio, logging
import aiomysql

# 创建连接池:由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务：
async def create_pool(loop, **kw):
    logging.info('create database connection pool')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop

    )

# SELECT语句，我们用select函数执行，需要传入SQL语句和SQL参数：
async def select(sql, args, size=None):
    logging.info(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            # 传入size参数，就通过fetchmany()获取最多指定数量的记录，否则，通过fetchall()获取所有记录。
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await  cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

# 要执行INSERT、UPDATE、DELETE语句，可以定义一个通用的execute()函数，因为这3种SQL的执行都需要相同的参数，以及返回一个整数表示影响的行数：
async def excute(sql, args, autocommit=True):
    logging.info(sql)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.excute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected


# 定义一个User对象，然后把数据库表users和它关联起来。
from orm import Model, StringField, IntegerField
class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()
