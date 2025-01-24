from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path('write/', views.write_example, name='write_example'),
    path('read/', views.read_example, name='read_example'),
    path('listen/', views.listen_to_data, name='listen_to_data'),
    path('services/', views.services, name = 'services' ),
    path('contact/',  views.contact, name = 'contact'),
    path('submit-service-request/', views.submit_service_request, name='submit_service_request'),
    path('admin/', admin.site.urls),
    path('graph/', views.GraphChartView, name='graph_chart'),


    # path("templates/", views.templates, name='templates'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

