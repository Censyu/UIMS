# 后端部署

## 数据库创建

首先确保安装好python包：

```bash
pip install django djangorestframework coreapi mysqlclient django-cors-headers
```

确保安装并启动了MySQL（或者MariaDB），给MySQL创建账户。
默认设置的用户名为`mysql`，密码为`mysql`，可以到`backend/settings.py`中的`DATABASES`修改（也可以在这里换回SQLite）。

确保该用户具有建表权限，手动建立`uims`表：

```
mysql -u mysql -p
...
> create database uims;
> show databases;
```

然后进行迁移（在此之前记得`rm uims/migrations/000*.py`清除以前makemigrations生成的文件，否则会报错，好坑）：

```bash
./manage.py makemigrations
./manage.py migrate
```

通过`show tables;`可以看到各表已经建立。如果需要创建管理员账户也可以用`./manage.py createsuperuser`。

## 运行

```bash
./manage.py runserver
```

此时访问`127.0.0.1:8000/admin`可以进入admin界面操作，访问`127.0.0.1:8000/docs`可以查看接口文档和操作接口，对`127.0.0.1:8000/api/xxx`也可以直接操作接口。

## CORS策略

在`backend/settings.py`中可以设置CORS策略，控制是否接受跨域请求。目前设置为：

```python
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
]
```

如果有需要的话可以相应设置。