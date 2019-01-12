import os

BASE_DIRS = os.path.dirname(__file__)


options = {
    'port': 8000,

    'static_path': os.path.join(BASE_DIRS, 'static'),

    # 配置模板路径
    'template_path': os.path.join(BASE_DIRS, 'templates'),

    # 开启xsrf保护，当我们把修改cookie次数的改变放在post方法中时
    # 在模板中需要添加 {% module xsrf_form_html() %}
    'xsrf-cookies': True,

    'login_url': '/login',
}