from django.urls import path, include
from .views import  PodsView, MachinesView

urlpatterns = [
    path('machines/', MachinesView.as_view(), name='view_machines'), 
    path('pods/', PodsView.as_view(), name='view_cached_books'), 

]
