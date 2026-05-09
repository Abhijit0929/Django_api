from django.urls import path
from . import views

urlpatterns = [

    # ── AUTH ──
    path("login/",       views.login_view,       name="login"),
    path("logout/",      views.logout_view,      name="logout"),
    path("register/",    views.register_view,    name="register"),
    path("admin-login/", views.admin_login_view, name="admin_login"),

    # ── HTML PAGES ──
    path("",               views.home,               name="home"),
    path("bins/",          views.bins_view,           name="bins"),
    path("report/",        views.report_waste,        name="report"),
    path("reports/",       views.reports_view,        name="reports"),
    path("feedback/",      views.feedback_view,       name="feedback"),
    path("profile/",       views.profile_view,        name="profile"),
    path("notifications/", views.notifications_view,  name="notifications"),
    path("notifications/mark-read/", views.mark_notifications_read, name="mark_notifications_read"),

    # ── API ──
    path("api/bins/",             views.bin_list_create),
    path("api/bins/<int:id>/",    views.bin_update),
    path("api/pickups/",          views.pickup_list_create),
    path("api/pickups/<int:id>/", views.update_pickup_status),
    path("api/reports/",          views.report_list_create),

    # ── CITY ──
    path("dashboard/", views.city_dashboard, name="dashboard"),

    # ── ADMIN UI ──
    path("admin-dashboard/",                              views.admin_dashboard,      name="admin_dashboard"),
    path("admin-dashboard/bins/",                         views.admin_bins,           name="admin_bins"),
    path("admin-dashboard/add-bin/",                      views.admin_add_bin,        name="admin_add_bin"),
    path("admin-dashboard/edit-bin/<int:id>/",            views.admin_edit_bin,       name="admin_edit_bin"),
    path("admin-dashboard/delete-bin/<int:id>/",          views.admin_delete_bin,     name="admin_delete_bin"),
    path("admin-dashboard/pickups/",                      views.pickups_view,         name="admin_pickups"),
    path("admin-dashboard/pickup/update/<int:id>/",       views.update_pickup,        name="update_pickup"),
    path("admin-dashboard/reports/",                      views.admin_reports,        name="admin_reports"),
    path("admin-dashboard/report/resolve/<int:id>/",      views.resolve_report,       name="resolve_report"),
    path("admin-dashboard/feedback/",                     views.admin_feedback,       name="admin_feedback"),
    path("admin-dashboard/notifications/",                views.admin_notifications,  name="admin_notifications"),
]
