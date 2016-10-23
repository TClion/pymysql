"""pymysql练习，主要练习对mysql表的增删改查等操作"""
import pymysql

#创建表
def CreateTable(db,cursor):
    sql = """create table test(
              id int not null auto_increment primary key,
              name char(20) not null,
              sex char(4) not null,
              age char(10) not null)
              """           #创建表
    try:
        cursor.execute(sql)     #执行sql语句
    except Exception as e:
        print(e)                #输出错误
        db.rollback()           #出现错误回滚

#插入
def Insert(db,cursor):
    sql = """insert into test(name,sex,age) values (%s,%s,%s)"""    #插入数据
    data = ('张','女','26')
    try:
        cursor.execute(sql,data)
    except Exception as e:
        print(e)
        db.rollback()

#更新表
def Update(db,cursor):
    sql = """update test set age=22 where name='张楠'"""      #更新表
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
        db.rollback()

#删除表
def Delete(db,cursor):
    sql = """delete from test"""    #删除表所有数据
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
        db.rollback()


#查询表
def Select(db,cursor):
    sql = """select * from test"""          #查询表所有数据
    try:
        cursor.execute(sql)
        result = cursor.fetchall()              #导出sql语句返回的数据
        for row in result:
            print('id=%d name=%s sex=%s age=%s' % (row[0],row[1],row[2],row[3]))
    except Exception as e:
        print(e)
        db.rollback()


#对于列的操作
def Alert(db,cursor):
    sqladd = """alter table test add tel char(20) not null"""       #添加列
    sqlchange = """alter table test change tel phonenumber char(15) not null"""     #更改列
    sqldrop = """alter table test drop phonenumber"""   #删除列
    sqlre = """alter table test rename stu"""       #重命名表
    try:
        cursor.execute(sqlre)
    except Exception as e:
        print(e)
        db.rollback()


if __name__ == "__main__":
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="topcoder",
                         port=3306,
                         db="p1_db",
                         charset="utf8")    #连接数据库
    cursor = db.cursor()
    db.autocommit(True)         #保持持续提交
    #CreateTable(db,cursor)
    #Insert(db,cursor)
    #Update(db,cursor)
    #Delete(db,cursor)
    #Select(db,cursor)
    #Alert(db,cursor)
    db.close()
