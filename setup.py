from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

project_name = "django-floc-disable"

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="django-floc-disable",
    version="1.0.0",
    description="Django middleware to disable Google FLoC tracking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nhymxu/django-floc-disable",
    author="Dung Nguyen",
    project_urls={
        "Bug Tracker": "https://github.com/nhymxu/django-floc-disable/issues",
        "Funding": "https://dungnt.net/donate.html",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={project_name: project_name},
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=['Django'],
)
