from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
   url(r'^login/$', 'login_view', name='login'),
   url(r'^logout/$', 'logout_view', name='logout'),
   url(r'^profile/$', 'profile_view', name='profile'),
   url(r'^register/$', 'register_view', name='register'),
   url(r'^hello/$', 'hello_view', name='hello'),
)
