from django.urls import path

from .views import (
    CreateProfile,
    DiarioListView,
    DiarioDetailView,
    DiarioUpdateView,
    DiarioDeleteView
)

urlpatterns = [
    path("crear-perfil/", CreateProfile.as_view(), name="profile_createuser"),

    path("diario/lista/", DiarioListView.as_view(), name="diario_list"),
    path("diario/detalle/<int:pk>/", DiarioDetailView.as_view(), name="diario_detail"),
    path("diario/editar/<int:pk>/", DiarioUpdateView.as_view(), name="diario_update"),
    path("diario/eliminar/<int:pk>/", DiarioDeleteView.as_view(), name="diario_delete"),
]