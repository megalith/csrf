import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

install_requires = [
    "pyramid"
]

test_requires = [
    "WebTest"
]

setup(
    name="megalith.csrf",
    version="0.0.1",
    description="Helper library for application-level CSRF protection in Pyramid",
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
    ],
    url="http://www.megalithproject.org",
    license="MIT",
    packages=find_packages(),
    namespace_packages=["megalith"],
    test_suite="megalith.csrf.tests",
    install_requires=install_requires,
    tests_require=test_requires
)
