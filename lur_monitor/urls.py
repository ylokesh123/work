
from django.urls import path,include
from . import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/week/me',views.dash_week_me, name='dash_week_me'),
    path('dashboard/week/all',views.dash_week_all, name='dash_week_all'),
    path('dashboard/month/me',views.dash_month_me, name='dash_month_me'),
    path('dashboard/month/all',views.dash_month_all, name='dash_month_all'),
    path('dashboard/current/me',views.dash_current_me, name='dash_current_me'),
    path('dashboard/current/all',views.dash_current_all, name='dash_current_all'),
    path('screenshot/<int:id>',views.screenshot, name='screenshot'),
    path('apps/<int:id>',views.apps, name='apps'),
    path('urls/<int:id>',views.urls, name='urls'),
    path('view_timesheet/<int:id>',views.Viewtsheet, name='timesheet'),
    path('approve_timesheet',views.approvetsheet, name='approve'),
    path('attendence/<int:id>',views.attendence, name='attendence'),
    path('members',views.members, name='members'),
    path('teams',views.teams, name='teams'),
    path('project/<int:id>',views.project, name='project'),
    path('todo',views.todo, name='todo'),
    path('clients',views.client, name='clients'),
    path('jobsite',views.jobsite, name='jobsite'),
    path('schedule',views.schedules, name='schedules'),
    path('timeoff',views.timeoff, name='timeoff'),
    path('time_act',views.time_act, name='time_act'),
    path('weekly',views.weekly, name='weekly'),
    path('dynamic',views.dynmic_rep, name='dynamic_report'),
    path('allreport',views.all_report, name='all_reports'),
    path('general',views.general, name='general'),
    path('features',views.features, name='features'),
    path('subscription',views.subscription, name='subscription'),
    path('organization',views.organization, name='organization'),
    path('allsettings',views.all_settings, name='all_settings'),
    path('integration',views.integration, name='integration'),
    path('changelog',views.change_log, name='change_log'),
    path('helpdesk',views.help_desk, name='help_desk'),
    path('', views.Login, name="admin_login"),
    path('logout/', views.Alogout, name="logout"),
    path('register',views.register, name='register'),
    path('profile',views.profile,name='profile'),
    path('privacy',views.privacy,name='privacy'),

   path('accounts/', include('django.contrib.auth.urls')),


    path('comp', views.comp,name="comp"),
    path('show', views.show,name="show"),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

    #employee paths
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),

    path('addclients', views.add_client,name="add_clients"),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 