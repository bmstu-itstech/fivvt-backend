from django.urls import include, path

urlpatterns = [
    path('board/', include('board.urls'), name='board'),
    path('albums/', include('albums.urls'), name='albums'),
    path('hospitals/', include('hospitals.urls'), name='hospitals'),
]
