def includeme(config):
    # # config.add_static_view('assets', 'static/assets', cache_max_age=3600)
    config.add_static_view('static', 'static')
    config.add_static_view('templates', 'templates')
    config.add_route('index', '/')
