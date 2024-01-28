from django.urls import path
from . import views
from .views import HomeView,LikeView,DeleteServicePostView,UpdateServicePostView,ServiceDetailView,DeleteContactUsPostView, AddContactUsPostView,UpdateContactUsPostView, ContacttUsView, ArticleDetailView,DeleteAboutUsPostView,UpdateAboutUsPostView, AddPostView,UpdatePostView, DeletePostView, AddServiceView, CategoryView, ServiceView, AboutUsView,AddAboutUsPostView

urlpatterns = [
  
    #path('',views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('contact_us/', ContacttUsView.as_view(), name='contact_us'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post' ),
    path('add_about_us_post/', AddAboutUsPostView.as_view(), name='add_about_us_post' ),
    path('add_contact_us_post/', AddContactUsPostView.as_view(), name='add_contact_us_post' ),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post' ),
    path('service/edit/<int:pk>', UpdateServicePostView.as_view(), name='update_service_post' ),
    path('about_us/edit/<int:pk>', UpdateAboutUsPostView.as_view(), name='update_about_us_post' ),
    path('contact_us/edit/<int:pk>', UpdateContactUsPostView.as_view(), name='update_contact_us_post' ),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post' ),
    path('about_us/<int:pk>/remove', DeleteAboutUsPostView.as_view(), name='delete_about_us_post' ),
    path('contact_us/<int:pk>/remove', DeleteContactUsPostView.as_view(), name='delete_contact_us_post' ),
    path('add_service/', AddServiceView.as_view(), name='add_service' ),
    path('category/<str:cats>', CategoryView, name='category' ),
    path('our_services/', ServiceView.as_view(), name='our_services'),
    path('service/<int:pk>/remove', DeleteServicePostView.as_view(), name='delete_service_post' ),
    path('like/<int:pk>', LikeView, name='like_service_post' ),

]
