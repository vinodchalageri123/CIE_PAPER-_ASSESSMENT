import imp
from django.urls import path
from .import views
from .models import Faculty



urlpatterns = [
    path('', views.home , name="home"),
    path('add_faculty', views.add_faculty, name="add-faculty"),
    path('all_faculty',views.all_faculty, name="list-faculty"),
    path('sem_list', views.sem_list, name="sem-list"),
    path('sem_listc', views.sem_listc, name="sem-listc"),
    path('subject6_list', views.subject6_list, name="sem-6"),
    path('subject6c_list', views.subject6c_list, name="sem-6c"),
    path('add_emf', views.add_emf, name="add-emf"),
    path('add_cn', views.add_cn, name="add-cn"),
    path('add_ml', views.add_ml, name="add-ml"),
    path('add_ws', views.add_ws, name="add-ws"),
    path('add_iot', views.add_iot, name="add-iot"),
    path('emf_disp',views.emfd,name="emf-disp"),
    path('iot_disp',views.iotd,name="iot-disp"),
    path('ws_disp',views.wsd,name="ws-disp"),
    path('ml_disp',views.mld,name="ml-disp"),
    path('cn_disp',views.cnd,name="cn-disp"),
    path('comment_emf', views.commentemf,name="comment-emf"),
    path('comment_iot', views.commentiot,name="comment-iot"),
    path('comment_ws', views.commentws,name="comment-ws"),
    path('comment_ml', views.commentml,name="comment-ml"),
    path('comment_cn', views.commentcn,name="comment-cn"),
    path('comment_dis_emf', views.comment_dis_emf, name="comment-dis-emf"),
    path('comment_dis_iot', views.comment_dis_iot, name="comment-dis-iot"),
    path('comment_dis_ws', views.comment_dis_ws, name="comment-dis-ws"),
    path('comment_dis_ml', views.comment_dis_ml, name="comment-dis-ml"),
    path('comment_dis_cn', views.comment_dis_cn, name="comment-dis-cn"),
    # path('add_committee', views.add_committee, name="add-committee"),
    path('enterc', views.enterc, name="enter"),
    

]

