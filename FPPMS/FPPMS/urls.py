"""FPPMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views as mainviews
from adminportal import views as adminportal_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     url(r'^admin/', admin.site.urls),
    path('Insertproposal',mainviews.saveproposal,name="saveproposal"),
    path('',mainviews.insertproposal),
    path('displayProposal',adminportal_views.displayProposal,name="displayProposal"),
    path('proposals',adminportal_views.displayProposalList),
    path('addAdmin',adminportal_views.addAdmin),
    path('dashboard',adminportal_views.dashboard,name="dashboard"),
    path('proposal/<int:pk>',adminportal_views.ProposalUpdate.as_view()),
    path('adminlogin/', include('django.contrib.auth.urls')),
    path('adminlogin/', include('adminlogin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)