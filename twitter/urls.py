from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forbidden/', views.forbidden, name='forbidden'),
    path('streamer/', views.streamers, name='streamers'),
    path('streamer/<int:id>/', views.streamer, name='streamer'),
    path('streamer/<int:id>/<slug:action>/', views.streamer_action, name='streamer_action'),
    path('list/', views.lists, name='lists'),
    path('list/<int:id>/', views.list_detail, name='list_detail'),
    path('entity/', views.entities, name='entities'),
    path('tag/', views.tags, name='tags'),
    path('tag/<int:tagid>', views.tag, name='tag'),
    path('entity/<slug:slug>/', views.entity, name='entity'),
    path('campaign/', views.campaigns, name='campaigns'),
    path('campaign/<slug:campaign_slug>/', views.campaign, name='campaign'),
    path('campaign/<slug:campaign_slug>/datacenter/<int:data_center>/', views.campaign_datacenter, name='campaign_datacenter'),
    path('manage/', views.manage_index, name='manage_index'),
    path('manage/twitter_accounts/', views.manage_twitter_accounts, name='manage_twitter_accounts'),
    path('manage/streamers/', views.manage_streamers, name='manage_streamers'),
    path('manage/streamers/<slug:campaign_slug>', views.manage_streamers, name='manage_streamers'),
    path('manage/entities/', views.manage_entities, name='manage_entities'),
    path('manage/entities/<slug:campaign_slug>', views.manage_entities, name='manage_entities'),
    path('manage/campaign/', views.manage_campaign, name='manage_campaign'),
    path('manage/campaign/<slug:campaign_slug>/', views.manage_campaign, name='manage_campaign'),
    path('metric/<int:metric_id>/', views.metric_detail, name='metric_detail'),
    path('twitter_user/', views.twitter_users, name='twitter_users'),
    path('twitter_user/<int:id_str>/', views.twitter_user, name='twitter_user'),
    path('tweet/<int:id_str>/', views.tweet, name='tweet'),
    path('source/<slug:slug>/', views.source, name='source'),
    path('hashtag/<str:text>/', views.hashtag, name='hashtag'),
    path('location/<int:id>/', views.location, name='location'),
    path('url/<int:id>/', views.url, name='url'),
    path('domain/<str:hostname>/', views.domain, name='domain'),
    path('graph/<int:id>/', views.graph, name='graph'),
    path('community/<int:community_id>/', views.community, name='community'),
    path('ajax/metric/', views.metric_compute, name='metric_compute'),
    path('ajax/user_graph/', views.twitter_user_graph_detail, name='twitter_user_graph_detail'),
    path('ajax/user/', views.twitter_user_detail, name='twitter_user_detail'),
    path('ajax/tweet/', views.tweet_detail, name='tweet_detail'),
    path('ajax/selection/', views.selection_add, name='add_to_selection'),
    path('search/<slug:campaign_slug>/', views.search, name='search'),
    path('selection/', views.selection_detail, name='view_selection'),
    path('ajax/selection/clear', views.clear_selection, name='clear_selection'),
    path('selection/<str:limit_target>', views.selection_detail, name='view_selection'),
    path('selection/dashboard/<str:limit_target>', views.selection_dashboard, name='selection_dashboard'),
    path('ajax/note/add/', views.note_add, name='note_add'),
    path('ajax/list/create/', views.list_create, name='list_create'),
    path('ajax/list/add/', views.list_add, name='list_add'),
    path('ajax/tag/add/', views.tag_add, name='tag_add'),
    path('ajax/tag/list/', views.tag_list, name='tag_list'),
    path('ajax/tag/remove/', views.tag_remove, name='tag_remove'),
    path('ajax/metric_form/', views.ajax_metric_form, name='ajax_metric_form'),
    path('ajax/validate_regex/', views.validate_regex, name='validate_regex'),
    path('ajax/count/', views.count, name='count'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)