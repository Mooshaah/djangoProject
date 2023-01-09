from django.urls import path, include
from api.views import Article_View_Set, User_View_Set
from rest_framework.routers import DefaultRouter
# article_list,article_details

router = DefaultRouter() # ROUTER OBJECT
router.register('articles', Article_View_Set, basename='articles')
router.register('users', User_View_Set)


urlpatterns = [
    path('api/', include(router.urls)),
    
]
