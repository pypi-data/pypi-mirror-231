def create(name):
    """
    create template via name
    """
    import os

    prefix = os.getenv("TC_URL", "git@github.com:svtter")

    template_dict = {
        "django": "{prefix}/cookiecutter-django.git".format(prefix=prefix),
        "package": "{prefix}/cookiecutter-pypackage.git".format(prefix=prefix),
        "compose": "{prefix}/cookiecutter-compose.git".format(prefix=prefix),
    }
    template = template_dict[name]
    os.system(f"cookiecutter {template}")
