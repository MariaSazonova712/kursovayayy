from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='blog-home'),
    path('rasp', rasp, name='rasp'),
    path('create', create, name='create'),
    # path('news', news, name='news'),
    path('news', TaskListView.as_view(), name='news'),
    path('<int:pk>/delete', Del.as_view(), name='task-delete'),
    path('<int:pk>/update', Upd.as_view(), name='task-update'),
    path('booking', booking, name='booking'),
    path('kontakt', kontakt, name='kontakt'),
    path('orders/new/<int:pk>/', OrderCreateView.as_view(), name='orders-create'),
    path('orders/<str:username>', UserOrdersListView.as_view(), name='orders-list'),
]
