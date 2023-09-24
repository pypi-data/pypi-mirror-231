import importlib.resources as pkg_resources

def get_template(template_name):
    with pkg_resources.path('dashboard_builder.templates', template_name) as template_path:
        with open(template_path, 'r') as file:
            return file.read()