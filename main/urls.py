from django.urls import path
from . import views

urlpatterns = [

    # ── AUTH ──
    path("login/",    views.login_view,    name="login"),
    path("logout/",   views.logout_view,   name="logout"),
    path("register/", views.register_view, name="register"),

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

    # ── ADMIN UI ──
    path("pickups/",                    views.pickups_view),
    path("pickup/update/<int:id>/",     views.update_pickup),
    path("dashboard/",                  views.city_dashboard,   name="dashboard"),
    path("admin-dashboard/",            views.admin_dashboard,  name="admin_dashboard"),
    path("admin-dashboard/pickups/",    views.pickups_view,     name="admin_pickups"),
    path("admin-dashboard/bins/",       views.admin_bins,       name="admin_bins"),
    path("admin-dashboard/reports/",    views.admin_reports,    name="admin_reports"),
    path("admin-dashboard/feedback/",   views.admin_feedback,   name="admin_feedback"),
    path("admin-dashboard/notifications/", views.admin_notifications, name="admin_notifications"),
]
