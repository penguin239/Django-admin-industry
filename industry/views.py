from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse


# 后台用法
@staff_member_required
def site_manage(request):
    return TemplateResponse(
        request, 'admin/site-manage.html'
    )
