from django.db import models

# Create your models here.
# ORM相关的类只能写在这个文件里，否则Django找不到


class Student(models.Model):
   id = models.AutoField(primary_key=True)  # 自增的主键字段
   name = models.CharField(null=False, max_length=20)  # 创建一个varchar(20)类型的不能为空的字段

   def __str__(self):
       return "<{}-{}>".format(self.id, self.name)



# 图书管理系统示例： 书， 作者， 出版社

# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True) # 自增主键ID
    name = models.CharField(max_length=64, null=False, unique=True)
    address = models.CharField(max_length=128, default="广东省茂名市")

    def __str__(self):
        return "<Publisher Object: {}-{}>".format(self.id, self.name)


# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    # 很出版社关联的外键字段(ForeignKey会自动在字段后面加上_id)
    # publisher指向的是一个book对应的具体的Publisher对象
    publisher = models.ForeignKey(to="Publisher")

    def __str__(self):
        return "<Book Object: {}-{}-{}>".format(self.id, self.title, self.publisher.name)


# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True) # 自增主键ID
    name = models.CharField(max_length=16, null=False, unique=True)
    # 建立多对多的关系(通过第三张表author_book关联)
    # 告诉ORM 这张表和book表是多对多关联关系，ORM自动生成第三张表author_book
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author Object: {}-{}>".format(self.id, self.name)