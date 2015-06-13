from django.conf.urls import patterns, include, url
from django.contrib import admin
# import view functions from trips app
from trips.views import hello_world
from trips.views import home
from trips.views import post_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^$', home),
    url(r'^post/(?P<id>\d+)/$', post_detail, name='post_detail'),
)


# \d 代表一個阿拉伯數字。
# + 代表「一個以上」。
# 所以 \d+ 代表一個以上的阿拉伯數字，例如「0」、「99」、「12345」。可是像「8a」就不符合，因為「a」不是數字。
# (?P<id>) 代表「把這一串東西抓出來，命名為 id。
# 所以 (?P<id>\d+) 代表：抓出一個以上阿拉伯數字，並把抓出來的東西取名為 id。