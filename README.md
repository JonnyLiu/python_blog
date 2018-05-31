# python_blog
python用django模块写的个人bolg

#数据库的配置MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名字',
        'USER': '名字',
        'PASSWORD': '密码',
        'HOST': '',本地使用不用填写
        'PORT': '',
    }
}

在INSTALLED_APPS = []添加APP名

配置静态变量的地址
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),//文件夹名
)

models.py 数据模型的写入
settings.py 全局设置
urls.py 路由配置
admin.py Diango自带的后台管理器

