"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.include('cornice')
    config.include('pyramid_mailer')
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.include('.routes')
    config.include('.models')

    config.scan('ngse.views')
    config.route_prefix = 'v1'
    config.scan('ngse.views.api')
    return config.make_wsgi_app()
