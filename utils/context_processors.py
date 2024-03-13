def site_settings(request):
    prefix = ''
    if hasattr(request, 'prefix'):
        prefix = request.prefix
    utils_s = {
        'site_title': '%s邢台丰迪机械有限公司' % prefix,
    }

    return {'site_settings': utils_s}
