"""Installer for the collective.bluesky package."""
from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="collective.bluesky",
    version="1.0.0a3",
    description="Bluesky integration for Plone.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone Bluesky ContentRules SocialNetwork",
    author="Érico Andrei",
    author_email="ericof@plone.org",
    url="https://pypi.python.org/pypi/collective.bluesky",
    license="GPL version 2",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.bluesky",
        "Source": "https://github.com/collective/collective.bluesky",
        "Tracker": "https://github.com/collective/collective.bluesky/issues",
        "Documentation": "https://collective.github.io/collective.bluesky",
    },
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8.0",
    install_requires=[
        "prettyconf",
        "Plone",
        "setuptools",
        "requests",
        "plone.restapi>=8.34.0",
    ],
    extras_require={
        "test": [
            "gocept.pytestlayer",
            "plone.app.testing",
            "plone.restapi[test]",
            "pytest-cov",
            "pytest-plone>=0.2.0",
            "pytest-docker",
            "pytest-mock",
            "pytest",
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "pytest-mock",
            "requests-mock",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.bluesky.locales.update:update_locale
    """,
)
