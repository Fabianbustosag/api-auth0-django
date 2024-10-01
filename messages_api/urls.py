from django.urls import path

from .views import PublicMessageApiView, ProtectedMessageApiView, AdminMessageApiView

######################################################################################

from .views import EntityList

urlpatterns = [
    path('public', PublicMessageApiView.as_view(), name='public-message'),
    path(
        'protected', ProtectedMessageApiView.as_view(), name='protected-message'
    ),
    path('admin', AdminMessageApiView.as_view(), name='admin-message'),

    ################################################################################

    path('entities', EntityList.as_view(), name='entity-list'),
]
