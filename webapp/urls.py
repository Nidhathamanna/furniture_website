from.import views
from django.urls import path
urlpatterns=[
path('web',views.web,name='web'),
path('pg_1',views.pg_1,name='pg_1'),
path('pg_2',views.pg_2,name='pg_2'),
path('pg_3',views.pg_3,name='pg_3'),
path('pg_4',views.pg_4,name='pg_4'),
path('pg_5',views.pg_5,name='pg_5')

]