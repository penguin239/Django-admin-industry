from django.contrib import admin
from django.template.response import TemplateResponse


class CustomAdminSite(admin.AdminSite):
    def __init__(self):
        super().__init__()

    def site_manage(self, request):
        return TemplateResponse(
            request, 'admin/site-manage.html'
        )

    def category(self, request):
        return TemplateResponse(
            request, 'admin/category.html'
        )


custom_admin_site = CustomAdminSite()
