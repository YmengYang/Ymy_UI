#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: mysqlhelper.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 2月 26, 2021
# ---


#
import pymysql
import re
from utilities.logger import Logger

log = Logger(__name__).getlog()


class MysqlHelper:
    '''
    '''

    def __init__(self, host, db, user, passwd, port=3306, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

        try:
            self.con = pymysql.connect(host=self.host,
                                       port=self.port,
                                       db=self.db,
                                       user=self.user,
                                       passwd=self.passwd,
                                       charset=self.charset)
            self.con.autocommit(1)
            # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
            self.cur = self.con.cursor()
        except:
            log.error("DataBase connect error,please check the db config.")

    # 关闭数据库连接
    def close(self):
        if self.con:
            self.con.close()
        else:
            log.error("DataBase doesn't connect,close connectiong error;please check the db config.")

    # 创建数据库
    def createDataBase(self, DB_NAME):
        # 创建数据库
        self.cur.execute(
            'CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci' % DB_NAME)
        self.con.select_db(DB_NAME)
        log.info('creatDatabase:' + DB_NAME)

    # 选择数据库
    def selectDataBase(self, DB_NAME):
        self.con.select_db(DB_NAME)

    # 获取数据库版本号
    def getVersion(self):
        self.cur.execute("SELECT VERSION()")
        return self.getOneData()

    # 获取上个查询的结果
    def getOneData(self):
        # 取得上个查询的结果，是单个结果
        data = self.cur.fetchone()
        return data

    # 创建数据库表
    def creatTable(self, tablename, attrdict, constraint):
        """创建数据库表

            args：
                tablename  ：表名字
                attrdict   ：属性键值对,{'book_name':'varchar(200) NOT NULL'...}
                constraint ：主外键约束,PRIMARY KEY(`id`)
        """
        if self.isExistTable(tablename):
            log.info('%s is exit' % tablename)
            return
        sql = ''
        sql_mid = '`id` bigint(11) NOT NULL AUTO_INCREMENT,'
        for attr, value in attrdict.items():
            sql_mid = sql_mid + '`' + attr + '`' + ' ' + value + ','
        sql = sql + 'CREATE TABLE IF NOT EXISTS %s (' % tablename
        sql = sql + sql_mid
        sql = sql + constraint
        sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
        log.info('creatTable:' + sql)
        self.executeCommit(sql)

    def executeSql(self, sql=''):
        """执行sql语句，针对读操作返回结果集
            args：
                sql  ：sql语句
        """
        try:
            self.cur.execute(sql)
            records = self.cur.fetchall()
            return records
        except pymysql.Error as e:
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            log.error(error)

    def executeSqlstr(self, sql=''):
        """执行sql语句，针对读操作返回结果集
            args：
                sql  ：sql语句
        """
        try:
            self.cur.execute(sql)
            records = self.cur.fetchone()
            return records
        except pymysql.Error as e:
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            log.error(error)

    def executeCommit(self, sql=''):
        """执行数据库sql语句，针对更新,删除,事务等操作失败时回滚

        """
        try:
            self.cur.execute(sql)
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            log.error("error:%s" % error)
            return error

    def insert(self, tablename, params):
        """创建数据库表

            args：
                tablename  ：表名字
                key        ：属性键
                value      ：属性值
        """
        key = []
        value = []
        for tmpkey, tmpvalue in params.items():
            key.append(tmpkey)
            if isinstance(tmpvalue, str):
                value.append("\'" + tmpvalue + "\'")
            else:
                value.append(tmpvalue)
        attrs_sql = '(' + ','.join(key) + ')'
        values_sql = ' values(' + ','.join(value) + ')'
        sql = 'insert into %s' % tablename
        sql = sql + attrs_sql + values_sql
        log.info('_insert:' + sql)
        self.executeCommit(sql)

    def select(self, tablename, fields='*', cond_dict='', order=''):
        """查询数据

            args：
                tablename  ：表名字
                cond_dict  ：查询条件
                order      ：排序条件

            example：
                print mydb.select(table)
                print mydb.select(table, fields=["name"])
                print mydb.select(table, fields=["name", "age"])
                print mydb.select(table, fields=["age", "name"],cond_dict={"score":"60"})
        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                consql = consql + '`' + k + '`' + '=' + '"' + v + '"' + ' and '
        consql = consql + ' 1=1 '
        if fields == "*":
            sql = 'select * from %s where ' % tablename
        else:
            if isinstance(fields, list):
                fields = ",".join(fields)
                sql = 'select %s from %s where ' % (fields, tablename)
            else:
                log.error("fields input error, please input list fields.")
        sql = sql + consql + order
        log.info('select:' + sql)
        return self.executeSql(sql)

    def selectone(self, tablename, fields='*', cond_dict='', order='order by id desc'):
        """查询数据

            args：
                tablename  ：表名字
                cond_dict  ：查询条件
                order      ：排序条件

            example：
                print mydb.select(table)
                print mydb.select(table, fields=["name"])
                print mydb.select(table, fields=["name", "age"])
                print mydb.select(table, fields=["age", "name"],cond_dict={"score":"60"})
        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                consql = consql + '`' + k + '`' + '=' + '"' + v + '"' + ' and '
        consql = consql + ' 1=1 '
        if fields == "*":
            sql = 'select * from %s where ' % tablename
        else:
            if isinstance(fields, list):
                fields = ",".join(fields)
                sql = 'select %s from %s where ' % (fields, tablename)
            else:
                log.error("fields input error, please input list fields.")
        sql = sql + consql + order
        log.info('select:' + sql)
        return self.executeSqlstr(sql)

    def insertOne(self, table, attrs, values):
        """插入多条数据

            args：
                tablename  ：表名字
                attrs        ：属性键
                values      ：属性值

            example：
                table='test_mysqldb'
                key = ["id" ,"name", "age"]
                value = [101, "liuqiao", "25"]
                mydb.insertOne(table, key, value)
        """
        values_sql = ['%s' for v in attrs]
        attrs_sql = '(' + ','.join(attrs) + ')'
        values_sql = ' values(' + ','.join(values_sql) + ')'
        sql = 'insert into %s' % table
        sql = sql + attrs_sql + values_sql
        try:
            log.info("插入数据库数据：%s " % values)
            self.cur.execute(sql, values)
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            error = 'insertMany executemany failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            log.error(error)

    def insertMany(self, table, attrs, values):
        """插入多条数据

            args：
                tablename  ：表名字
                attrs        ：属性键
                values      ：属性值

            example：
                table='test_mysqldb'
                key = ["id" ,"name", "age"]
                value = [(101, "liuqiao", "25"), (102,"liuqiao1", "26")] or [(101, "liuqiao", "25")]
                mydb.insertMany(table, key, value)
        """
        values_sql = ['%s' for v in attrs]
        attrs_sql = '(' + ','.join(attrs) + ')'
        values_sql = ' values(' + ','.join(values_sql) + ')'
        sql = 'insert into %s' % table
        sql = sql + attrs_sql + values_sql
        log.info('insertMany:' + sql)
        try:
            log.info(sql)
            for i in range(0, len(values), 20000):
                log.info(values[i:i + 20000])
                self.cur.executemany(sql, values[i:i + 20000])
                self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            error = 'insertMany executemany failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            log.error(error)

    def delete(self, tablename, cond_dict):
        """删除数据

            args：
                tablename  ：表名字
                cond_dict  ：删除条件字典

            example：
                params = {"name" : "caixinglong", "age" : "38"}
                mydb.delete(table, params)

        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    _v = "\'" + v + "\'"
                else:
                    _v = str(v)
                consql = consql + tablename + "." + k + '=' + _v + ' and '
        consql = consql + ' 1=1 '
        sql = "DELETE FROM %s where%s" % (tablename, consql)
        log.info(sql)
        return self.executeCommit(sql)

    def update(self, tablename, attrs_dict, cond_dict):
        """更新数据

            args：
                tablename  ：表名字
                attrs_dict  ：更新属性键值对字典
                cond_dict  ：更新条件字典

            example：
                params = {"name" : "caixinglong", "age" : "38"}
                cond_dict = {"name" : "liuqiao", "age" : "18"}
                mydb.update(table, params, cond_dict)

        """
        attrs_list = []
        consql = ' '
        for tmpkey, tmpvalue in attrs_dict.items():
            attrs_list.append("`" + tmpkey + "`" + "=" + "\'" + tmpvalue + "\'")
        attrs_sql = ",".join(attrs_list)
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    _v = "\'" + v + "\'"
                else:
                    _v = str(v)
                consql = consql + "`" + tablename + "`." + "`" + k + "`" + '=' + _v + ' and '
        consql = consql + ' 1=1 '
        sql = "UPDATE %s SET %s where%s" % (tablename, attrs_sql, consql)
        log.info(sql)
        return self.executeCommit(sql)

    def dropTable(self, tablename):
        """删除数据库表

            args：
                tablename  ：表名字
        """
        sql = "DROP TABLE  %s" % tablename
        self.executeCommit(sql)

    def deleteTable(self, tablename):
        """清空数据库表

            args：
                tablename  ：表名字
        """
        sql = "DELETE FROM %s" % tablename
        log.info("sql=%s" % sql)
        self.executeCommit(sql)

    def isExistTable(self, tablename):
        """判断数据表是否存在

            args：
                tablename  ：表名字

            Return:
                存在返回True，不存在返回False
        """
        sql = "select * from %s" % tablename
        result = self.executeCommit(sql)
        if result is None:
            return True
        else:
            if re.search("doesn't exist", result):
                return False
            else:
                return True
