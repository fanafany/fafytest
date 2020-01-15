import sqlite3,os
#创建表

class Sqlite3():

    #关闭数据库
    def off( self ):
        self.conn.close()
        self.Info("数据库关闭完成...")

    def Info( self , *txt ):
        print(" ".join(txt))

    #条件判断  如果有 就返回 该条记录   没有就返回 false
    def AI(self,table,name):

        have_data = list( self.c.execute("select * from {0} where {1}".format(table,name)) )
        if have_data : return have_data
        else: return False

    #创建数据库  和表  CREATE TABLE
    def create_table( self , db_name = "xin_Voice.db" ,table = "Voice", table_name = "id integer primary key autoincrement ,name TEXT"):

        #链接数据库,如果不存在则创建数据库
        self.conn = sqlite3.connect(db_name)
        self.Info("链接数据库完成...")

        #创建游标
        self.c = self.conn.cursor()

        try:
            #创建表,id integer primary key autoincrement  是自动增加id
            self.c.execute("create table {0}({1})".format(table,table_name))
            #提交修改给数据库
            self.conn.commit()
        except:self.Info("表以存在...")

        self.Info("表以就绪...")


    #写入数据库insert into
    #classs.writes(table = "Voice",name = "name,key", write_ = "'的','看看'",conditions = "name = '{0}'".format('的'))
    def writes(self,table = "Voice",name = "name,key", write_ = "'的','看看'",conditions = "name = '{}'"):
        if self.AI(table,"{0}".format(conditions)):
            self.Info("文件存在,不在写入--->{}".format(conditions))
        else:
            self.c.execute("insert into {0} ({1}) values ({2})"\
            .format(table,name,write_))
            #提交修改给数据库
            self.conn.commit()
            self.Info("写入完成...")


    #删除表内指定的数据 delete from {0} where {1}
    def delete_(self,table = "Voice",name = "id = 1"):

        if name == '':
            #直接清空表内容数据
            self.c.execute("delete from {0}".format(table))

            print("删除了全部")
        #指定要求删除表内容
        else:
            if self.AI(table,"{0}".format(name)):

                self.c.execute("delete from {0} where {1}".format(table,name))
                self.Info("已经删除,--->{}".format(name))
            else:
                self.Info("删除失败文件不存在,--->{}".format(name))
        # 提交修改给数据库
        self.conn.commit()


    #修改数据库表内容updata {} set {} where {}
    def update_(self,table = "Voice",name ="name = '你好'", conditions = "id = 1"):

        if conditions == "":
            self.c.execute("update {0} set {1}".format(table, name))
            self.Info("已修改数据库表全部内容为,--->{}".format(name))

        else:
            if self.AI(table,"{0}".format(conditions)):
                self.c.execute("update {0} set {1} where {2}".format(table, name, conditions))
                self.Info("修改数据库表内容为,--->{}-->完成".format(name))
            else:
                self.Info("修改数据库表内容为,--->{},-->没有".format(conditions))
        # 提交修改给数据库
        self.conn.commit()

    ###########################数据库操作进阶################################
    # HAVING 子句允许指定条件来过滤将出现在最终结果中的分组结果。
    def Having_(self,table = "Voice", tabe_name = 'name' ,name ="'你好'",  conditions = " > 1"):
        if self.AI(table,"{0} = {1}".format(tabe_name,name)):
            have_ = self.c.execute("select * from {0} group by {1} having count ({2}) {3}".format(table , name , name , conditions))
            print( list(have_ ) )
        else:
            self.Info("查询Having数据库表内容为,--->{0},{1}-->没有".format(name,conditions))











if __name__ == '__main__':
    classs=Sqlite3()

    # 创建数据库#创建表
    classs.create_table(db_name = "xin_Voice.db",table = "Voice", table_name = "id integer primary key autoincrement ,name TEXT")
#---------------------------------------------------------------------------------------------------------------------------------------------
    # 写入数据到表
 #   for x in os.listdir("yuyinku"):
 #       classs.writes(table = "Voice",name = "name", write_ = "'{}'".format(x),conditions = "name = '{0}'".format(x))
#---------------------------------------------------------------------------------------------------------------------------------------
    # 数据库查询在修改文件名
#    for x in classs.AI(table ="Voice",name = "id >0"):
#        print(x)
#        os.rename( 'yuyinku/{}'.format(x[1]), "yuyinku/{}Voice.wav".format(x[0]) )              #修改文件名
    # 查找单个数据库查询
#    print("{}Voice.wav".format(classs.AI(table ="Voice",name = "name = '{}.wav'".format("我"))[0][0]))
#---------------------------------------------------------------------------------------------------------------------------------------
    #一次性读取数据库所有文件,转换为字典类型
    def loading():
        all_ = classs.AI(table ="Voice",name = "id >0")
        new_dict = {}
        for x in all_:
            new_dict[x[1]] = x[0]
        print(new_dict["我.wav"])
   # loading()
#-----------------------------------------------------------------------------------------------------------------------------------------
    #清空表内所以内容方法
   # classs.delete_(table = "sqlite_sequence",name = "")
   # classs.delete_(table = "Voice",name = "")
#----------------------------------------------------------------------------------------------------
    #清空表内指定内容方法
   # classs.delete_(table = "Voice",name = "id = 3537")

#--------------------------------------------------------------------------------------------------
    #修改数据库表指定内容
    #classs.update_(table = "Voice",name ="name = '你好'", conditions = "id = 1")

    #修改数据库表全部内容
   # classs.update_(table = "Voice",name ="name = '你好'", conditions = "")
#------------------------------------------------------------------------------

    # HAVING 子句允许指定条件来过滤将出现在最终结果中的分组结果。
 #   classs.Having_(table = "Voice",
#    tabe_name = 'name' ,name ="'你好'", conditions = " > 3031")







#-----------------------------------------------------------------------------
    #关闭数据库
    classs.off()
    input("...")