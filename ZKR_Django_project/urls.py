"""ZKR_Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/page/yun/
    path('page/yun', views.page_yun_view),

    path('', views.index_view),
    # http://127.0.0.1:8000/page/1
    path('page/1', views.page1_view),
    # http://127.0.0.1:8000/page/2
    path('page/2', views.page2_view),
    # http://127.0.0.1:8000/page/3-100
    path('page/<int:pg>', views.pagen_view),
    # http://127.0.0.1:8000/birthday/年4/月2/日2
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$', views.birthday_view),

    path('test_request', views.test_request),

    path('get_or_post', views.get_or_post),

    path('test_html', views.test_html),

    path('test_html_param', views.test_html_param),

    path('test_if_for', views.test_if_for),

    path('test_calculator', views.test_calculator),
    # 三个路由对应三个视图
    path('base_html', views.base_view),
    path('music', views.music_view),
    path('sports', views.sports_view),

    path('url', views.test_url),
    path('urls_result/<int:age>', views.test_url_result, name='us')# 使用了一个path转换器

]
