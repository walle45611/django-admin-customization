def breadcrumbs(request):
    crumbs = []
    path = request.path.strip('/').split('/')
    url = ''
    for part in path:
        url += '/' + part
        crumbs.append({'name': part.capitalize(), 'url': url})
    return {'breadcrumbs': crumbs}