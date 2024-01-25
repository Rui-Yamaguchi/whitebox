from django.urls import path
from . import views

urlpatterns = [
    path('',views.WhiteboxView,name='index'),
    path('Howaito',views.Howaito,name='Howaito'),
    path('Rio',views.Rio,name='Rio'),
    path('Aka',views.Aka,name='ToudaiAka'),
    path('Tedhi',views.Tedhi,name='Teddy'),
    path('Coco',views.Coco,name='Coco'),
    path('Wiru',views.Wiru,name='Will'),
    path('Communication',views.Communication,name='Communication'),
    


]