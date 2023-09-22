from django.urls import path
from .views import ImageProcessingView

urlpatterns = [
    path('/remove-bg/', ImageProcessingView.as_view(), name='remove-bg'),
]
