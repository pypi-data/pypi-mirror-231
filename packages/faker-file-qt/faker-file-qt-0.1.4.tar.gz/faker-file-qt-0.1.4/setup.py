import os

from setuptools import setup

version = "0.1.4"

try:
    readme = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
except OSError:
    readme = ""

install_requires = [
    "Faker",
    "faker-file[common]>=0.17.8",
    "QDarkStyle",
    "PyQt5",
    "Pillow<10.0.0",
]

extras_require = {
    "dev": [
        "black",
        "detect-secrets",
        "doc8",
        "ipython",
        "isort",
        "ruff",
        "twine",
    ]
}

tests_require = [
    "pytest",
    "pytest-cov",
    "tox",
]

setup(
    name="faker-file-qt",
    version=version,
    description="PyQT UI for faker-file.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Environment :: X11 Applications",
        "Environment :: X11 Applications :: Qt",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    project_urls={
        "Bug Tracker": (
            "https://github.com/barseghyanartur/faker-file-qt/issues"
        ),
        "Documentation": "https://faker-file-qt.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/faker-file-qt/",
        "Changelog": "https://faker-file-qt.readthedocs.io/"
        "en/latest/changelog.html",
    },
    entry_points={"console_scripts": ["faker-file-qt = faker_file_qt:main"]},
    keywords="faker-file faker-file-qt",
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    url="https://github.com/barseghyanartur/faker-file-qt/",
    py_modules=["faker_file_qt"],
    license="MIT",
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    include_package_data=True,
)
