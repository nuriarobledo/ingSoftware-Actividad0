from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/specifics/5/
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    path("specifics/<int:question_id>/results/", views.results, name="results"),
    path("specifics/<int:question_id>/vote/", views.vote, name="vote")]