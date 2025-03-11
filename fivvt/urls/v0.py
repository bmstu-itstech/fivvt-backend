from django.urls import include, path

urlpatterns = [
    path('board/', include('board.urls'), name='board'),
]
