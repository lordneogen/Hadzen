from . import views_cbf,views_dbf
from django.urls import path, include

from .views_cbf import RegisterView

urlpatterns = [
    path('us/', views_cbf.LIST_User.as_view()),
    path('us/<int:id>/', views_cbf.LIST_User.as_view()),
    path('us/<slug:email>/', views_dbf.get_user_email),
    path('ch/', views_cbf.LIST_Chenel.as_view()),
    path('ch/sb', views_cbf.LIST_Subs.as_view()),
    path('ch/<int:id>/sb', views_cbf.LIST_Subs.as_view()),
    path('ch/<int:id>/bl/<slug:page>', views_dbf.CH_BLOG_PAGE),

    path('blm/', views_cbf.LIST_Blog.as_view()),
    path('blm/<int:id>/', views_cbf.LIST_Blog.as_view()),
    path('bl/lds/', views_cbf.LIST_Blog_LDS.as_view()),
    path('bl/lds/<int:id>/<int:us_id>/', views_dbf.LDS_GET),
    path('bl/<int:id>/lds/', views_cbf.LIST_Blog_LDS.as_view()),
    path('bl/<int:id>/', views_dbf.BLOG_DETAIL),
    path('bl/', views_dbf.ALL_BLOGS),
    path('bl/<slug:page>', views_dbf.BLOG_PAGE),

    path('cm/', views_cbf.LIST_Comm.as_view()),
    path('cm/<int:id>', views_cbf.LIST_Comm.as_view()),
    path('cm/lds/', views_cbf.LIST_Comm_LDS.as_view()),
    path('cm/<int:id>/lds/', views_cbf.LIST_Comm_LDS.as_view()),

    path('ch/<int:id>/', views_cbf.LIST_Chenel.as_view()),
    path('ch/<int:id>/bl', views_dbf.CHENELL_DETAIL),

    path('mn/', views_cbf.LIST_Manager.as_view()),
    path('mn/<int:id>', views_cbf.LIST_Manager.as_view()),
    path('mn/ch/<int:id>', views_dbf.CHENELL_MANGAER),

    path('register/', RegisterView.as_view(), name='auth_register'),

]
