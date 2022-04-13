from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from api.views import list,DateManageViewSet,DateFormView,TodayView


router =routers.DefaultRouter()
router.register(r'dates',DateManageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('',list),
    path('create/',DateFormView.as_view(),name="create"),
    path('today/', TodayView.as_view()),
]

admin.site.site_header='日付管理'
