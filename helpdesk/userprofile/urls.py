from django.conf.urls import url
from userprofile.views import login,update_profile,logout


urlpatterns = [
    url(r'^login/$','userprofile.views.login',name="login"),  
    url(r'^logout/$',logout,name="logout"), 
    url(r'^profile/update/$',update_profile,name="update_profile"),  
    
]