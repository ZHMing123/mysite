# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/4/14 10:40
# 文件名称：views.py
# 开发工具：PyCharm

from django.shortcuts import HttpResponse, render, redirect

from app01 import models

def zhming(request):
    # request参数保存了所有和浏览器请求相关是数据
    return HttpResponse('hello zhming!')


def hello(request):
    # request参数保存了所有和浏览器请求相关是数据
    # 手动找HTML文件
    # with open("templates/zhming.html", "r", encoding="utf-8") as f:
    #     data = f.read()
    # return HttpResponse(data)

    # Django找html文件
    return render(request, "zhming.html")

# 登录函数
def login(request):
    error_msg = ""
    # 如果是GET请求，返回html页面
    if request.method == "POST":
        # 如果是POST请求，取出提交的数据，做登录判断
        # print(request.POST) # 取到所有post的数据
        email = request.POST.get("email", None) # 没有"email"返回None
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        # 判断是否登录成功
        if email == "1424116457@qq.com" and pwd == "root":
            # 登录成功
            # return HttpResponse("登录成功！")
            return redirect("https://zhming123.github.io/")

        else:
            error_msg = "邮箱或者密码错误！"

    # GET请求或者登录失败后执行
    return render(request, "login_demo.html", {"error": error_msg})

def login_validate(request):
    # request参数保存了所有和浏览器请求相关是数据
    # 获取用户提交的数据
    print(request.POST) # 取到所有post的数据
    email = request.POST.get("email", None) # 没有"email"返回None
    pwd = request.POST.get("pwd", None)
    print(email, pwd)
    # 判断是否登录成功
    if email == "1424116457@qq.com" and pwd == "root":
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("登录失败!")

# 查询函数(展示所有用户）
def user_list(request):
    # 去数据库中查询所有用户
    # 用ORM工具
    ret = models.Student.objects.all()  # 返回一个对象列表[Student Object, Student Object)
    # print(ret)
    # print(ret[0].id, ret[0].name)
    return render(request, "user_list.html", {"user_list": ret})
    # return HttpResponse("ok!")

# 添加用户
def add_user(request):
    # 第一次请求页面时，就返回一个页面，页面上有两个框让用户输入
    error_msg = ""
    if request.method == "POST":
        # 获取POST的数据
        new_name = request.POST.get("username", None)
        if new_name:
            # 去数据库中创建一条新记录
            models.Student.objects.create(name=new_name)
            # return HttpResponse("添加成功！")
            # 添加成功后直接跳转到用户列表页
            return redirect("/user_list/")  # 跳转路径
        else:
            error_msg = "名字不能为空！"

    return render(request, "add_user.html", {"error": error_msg})


# 删除用户
def delete_user(request):
    print(request.GET)
    print("=================================")
    # 取到删除指定的数据（a标签是get请求）
    # 从get请求的参数中获取到要删除的数据的id值
    del_id = request.GET.get("id", None)
    # print(del_id)
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找数据
        del_obj = models.Student.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面
        return redirect("/user_list/")
    else:
        return HttpResponse("要删除的数据不存在！")


# 编辑用户
def edit_user(request):
    # 修改后POST的数据
    if request.method == "POST":
        # 获取新的名字
        edit_id = request.POST.get("id", None)
        new_name = request.POST.get("username", None)
        # 更新
        # 根据id取到编辑的是哪用户
        edit_obj = models.Student.objects.get(id=edit_id)
        edit_obj.name = new_name
        edit_obj.save() # 把修改提交

        # 跳转
        return redirect("/user_list/")


    # 从GET请求中获取到当前编辑的用户对象的id
    edit_id = request.GET.get("id", None)
    if edit_id:
        # 查找到当前编辑的用户对象
        user_obj = models.Student.objects.get(id=edit_id)
        return render(request, "edit_user.html", {"user": user_obj})
    else:
        return HttpResponse("编辑的用户不存在！")


# 出版社视图

# 查询函数(展示所有出版社）
def publisher_list(request):
    # 去数据库中查询所有出版社
    # 用ORM工具
    ret = models.Publisher.objects.all()  # 返回一个对象列表[Publisher Object, Publisher Object)
    # print(ret)
    # print(ret[0].id, ret[0].name)
    return render(request, "publisher_list.html", {"publisher_list": ret})
    # return HttpResponse("ok!")


# 添加出版社
def add_publisher(request):
    # 第一次请求页面时，就返回一个页面，页面上有两个框让用户输入
    error_msg = ""
    if request.method == "POST":
        # 获取POST的数据
        new_name = request.POST.get("publisher_name", None)
        if new_name:
            # 去数据库中创建一条新记录
            models.Publisher.objects.create(name=new_name)
            # return HttpResponse("添加成功！")
            # 添加成功后直接跳转到用户列表页
            return redirect("/publisher_list/")  # 跳转路径
        else:
            error_msg = "名字不能为空！"

    return render(request, "add_publisher.html", {"error": error_msg})


# 删除出版社
def delete_publisher(request):
    print(request.GET)
    print("=================================")
    # 取到删除指定的数据（a标签是get请求）
    # 从get请求的参数中获取到要删除的数据的id值
    del_id = request.GET.get("id", None)
    # print(del_id)
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在！")


# 编辑出版社
def edit_publisher(request):
    # 修改后POST的数据
    if request.method == "POST":
        # 获取新的名字
        edit_publisher_id = request.POST.get("id", None)
        new_publisher_name = request.POST.get("publisher_name", None)
        # 更新
        # 根据id取到编辑的是哪用户
        edit_obj = models.Publisher.objects.get(id=edit_publisher_id)
        edit_obj.name = new_publisher_name
        edit_obj.save() # 把修改提交到数据库

        # 跳转
        return redirect("/publisher_list/")


    # 从GET请求中获取到当前编辑的用户对象的id
    edit_publisher_id = request.GET.get("id", None)
    if edit_publisher_id:
        # 查找到当前编辑的用户对象
        publisher_obj = models.Publisher.objects.get(id=edit_publisher_id)
        return render(request, "edit_publisher.html", {"publisher": publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在！")


# 书的视图

# 查询函数(展示所有出版社）
def book_list(request):
    # 去数据库中查询所有出版社
    # 用ORM工具
    all_book = models.Book.objects.all()  # 返回一个对象列表[Publisher Object, Publisher Object)
    # print(ret)
    # print(ret[0].id, ret[0].name)
    return render(request, "book_list.html", {"all_book": all_book})



# 添加书籍
def add_book(request):
    # 取到所有出版社
    publisher_list = models.Publisher.objects.all()
    # 第一次请求页面时，就返回一个页面，页面上有两个框让用户输入
    error_msg = ""
    if request.method == "POST":
        # 获取POST的数据 {"book_title": "电子工业出版社" ,  "publisher_id": id}
        new_book_title = request.POST.get("book_title", None)
        new_publisher_id = request.POST.get("publisher", None)
        if new_book_title:
            # 去数据库中创建一条新记录,自动提交
            models.Book.objects.create(title=new_book_title, publisher_id=new_publisher_id)
            # return HttpResponse("添加成功！")
            # 添加成功后直接跳转到书籍列表页
            return redirect("/book_list/")  # 跳转路径
        else:
            error_msg = "书名不能为空！"

    return render(request, "add_book.html", {"error": error_msg, "publisher_list": publisher_list})


# 删除书籍
def delete_book(request):
    # print(request.GET)
    # print("=================================")
    # 取到删除指定的数据（a标签是get请求）
    # 从get请求的参数中获取到要删除的数据的id值
    del_id = request.GET.get("id", None)
    # print(del_id)
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找数据
        del_obj = models.Book.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面
        return redirect("/book_list/")
    else:
        return HttpResponse("要删除的数据不存在！")


# 编辑书籍
def edit_book(request):
    # 取到所有出版社
    publisher_list = models.Publisher.objects.all()
    # 修改后POST的数据
    if request.method == "POST":
        # 获取新的名字
        edit_id = request.POST.get("book_id", None)
        print(edit_id)
        new_book_title = request.POST.get("book_title", None)
        new_book_publisher_id = request.POST.get("publisher", None)
        # 更新
        # 根据id取到编辑的是哪本书籍
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_book_title
        edit_book_obj.publisher_id = new_book_publisher_id   # 当前书籍关联的出版社id值
        edit_book_obj.save() # 把修改提交到数据库

        # 跳转
        return redirect("/book_list/")


    # 从GET请求中获取到当前编辑的用户对象的id
    edit_id = request.GET.get("id", None)
    # print(edit_id)
    if edit_id:
        # 查找到当前编辑的用户对象
        edit_book_obj = models.Book.objects.get(id=edit_id)
        return render(request,
                      "edit_book.html",
                      {"book": edit_book_obj, "publisher_list": publisher_list}
                )
    else:
        return HttpResponse("编辑的书籍不存在！")


# 作者视图

# 作者列表
def author_list(request):
    all_author = models.Author.objects.all().order_by("id")
    # print(all_author[0].book.all()) # 当前所有作者的书籍
    return render(request, "author_list.html", {"author_list": all_author})


# 增加作者
def add_author(request):
    # 获取所有是书籍
    all_book = models.Book.objects.all()
    # 第一次请求页面时，就返回一个页面，页面上有两个框让用户输入
    error_msg = ""
    if request.method == "POST":
        # 获取POST的数据
        new_author_name = request.POST.get("author_name", None)
        # post提交的数据是多个值时,用getlist,如多选的select或者checkbox
        books = request.POST.getlist("books", None)
        # print(new_author_name, books)
        if new_author_name:
            # 去数据库中创建一条新记录,自动提交
            # 创建作者
            new_author_obj = models.Author.objects.create(name=new_author_name)
            # 把新作者和书籍建立对应关系
            new_author_obj.book.set(books)
            # return HttpResponse("添加成功！")

            # 添加成功后直接跳转到书籍列表页
            return redirect("/author_list/")  # 跳转路径
        else:
            error_msg = "作者不能为空！"

    return render(request, "add_author.html", {"all_book": all_book, "error": error_msg})


# 删除作者
def delete_author(request):
    # print(request.GET)
    # print("=================================")
    # 取到删除指定的数据（a标签是get请求）
    # 从get请求的参数中获取到要删除的数据的作者id值
    del_id = request.GET.get("id", None)
    # print(del_id)
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找数据
        del_obj = models.Author.objects.get(id=del_id)
        # 删除
        # 1、去作者表把作者删除
        # 2、去作者和书籍的关联表,把对应关联记录删除
        del_obj.delete()
        # 返回删除后的页面
        return redirect("/author_list/")
    else:
        return HttpResponse("要删除的数据不存在！")


# 编辑作者
def edit_author(request):
    # 取到所有书籍对象
    book_list = models.Book.objects.all()
    # 修改后POST的数据
    if request.method == "POST":
        # 获取新的名字
        edit_author_id = request.POST.get("author_id", None)
        # print(edit_id)
        new_author_name = request.POST.get("author_name", None)
        # 拿到编辑后作者关联的书籍
        new_books = request.POST.getlist("books", None)
        # 更新
        # 根据id取到当前编辑的作者
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)   # 当前作者关联是书
        edit_author_obj.save() # 把修改提交到数据库

        # 跳转
        return redirect("/author_list/")


    # 从GET请求中获取到当前编辑的作者对象的id
    edit_id = request.GET.get("id", None)
    # print(edit_id)
    if edit_id:
        # 查找到当前编辑的用户对象
        edit_author_obj = models.Author.objects.get(id=edit_id)
        return render(request,
                      "edit_author.html",
                      {"author": edit_author_obj, "book_list": book_list}
                )
    else:
        return HttpResponse("编辑的作者不存在！")