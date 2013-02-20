import os
from setuptools import setup, find_packages

thisdir = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-notification",
    version=__import__("notification").__version__,
    description="User notification management for the Django web framework",
    long_description=open(os.path.join(thisdir, "docs/usage.txt")).read(),
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    url="https://github.com/jtauber/django-notification",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    zip_safe=False,
)
