from . import views
from django.urls import path



urlpatterns = [
    path('us/', views.LIST_User.as_view()),
    path('us/<int:id>/', views.LIST_User.as_view()),

    path('ch/', views.LIST_Chenel.as_view()),
    path('ch/sb', views.LIST_Subs.as_view()),
    path('ch/<int:id>/sb', views.LIST_Subs.as_view()),
    path('ch/<int:id>/bl/<slug:page>', views.CH_BLOG_PAGE),

    path('blm/', views.LIST_Blog.as_view()),
    path('blm/<int:id>/', views.LIST_Blog.as_view()),
    path('bl/lds/', views.LIST_Blog_LDS.as_view()),
    path('bl/<int:id>/lds/', views.LIST_Blog_LDS.as_view()),
    path('bl/<int:id>/', views.BLOG_DETAIL),
    path('bl/', views.ALL_BLOGS),
    path('bl/<slug:page>', views.BLOG_PAGE),

    path('cm/', views.LIST_Chenel.as_view()),
    path('cm/<int:id>', views.LIST_Chenel.as_view()),
    path('cm/lds/', views.LIST_Comm_LDS.as_view()),
    path('cm/<int:id>/lds/', views.LIST_Comm_LDS.as_view()),

    path('ch/<int:id>/', views.LIST_Chenel.as_view()),
    path('ch/<int:id>/bl', views.CHENELL_DETAIL),

    path('mn/', views.LIST_Manager.as_view()),
    path('mn/<int:id>', views.LIST_Manager.as_view()),
    path('mn/ch/<int:id>', views.CHENELL_MANGAER)
]
