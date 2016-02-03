# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from procult.authentication.views import (
    UserViewSet,
    ProposalViewSet,
    LoginView,
    ProposalView,
    ProposalUploadFilesView,
    ProposalUploadFilesDetailView,
    ProposalDetailView,
    ProposalOwnListView
)

router = DefaultRouter()

router.register(r'api/v1/usuarios', UserViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/propostas/$', ProposalView.as_view()),
    url(r'^api/v1/propostas/(?P<number>\d+)/$',
        ProposalDetailView.as_view()),
    url(r'^api/v1/propostas/(?P<number>\d+)/upload/$',
        ProposalUploadFilesView.as_view()),
    url(r'^api/v1/propostas/documentos/(?P<uid>[a-zA-Z0-9\-]+)/$',
        ProposalUploadFilesDetailView.as_view()),
    url(r'^api/v1/propostas/user/(?P<user_pk>\d+)/$',
        ProposalOwnListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
