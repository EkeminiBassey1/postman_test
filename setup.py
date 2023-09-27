from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent


# Declare packages that your project has to install whenever somebody (or script)
# installs it. This specifies an interface.
#
# For an analysis of "install_requires" vs pip's requirements files see:
# see also: https://caremad.io/posts/2013/07/setup-vs-requirement/
#
# THIS is the minimal set of requirements that the model needs to serve/predict
install_requires = [
    "loguru>=0.6.0",
    "click>=8.1.3",
    "pytest>=7.1.3",
    "uvicorn[standard]>=0.18.3",
    "fastapi>=0.85.0",
    "termcolor>=2.0.1",
    "google-cloud-storage==1.44.0",
    "protobuf==3.20.3",
    "locust==2.13.2",
    "structlog",
    "python-dotenv",
    "google-cloud-bigquery>=2.34.4",
    "google-cloud-logging>=2.6.0",
    "db-dtypes", 
    "aiohttp",
    "aiohttp_retry",
    "pytest", 
    "pytest-asyncio",
    "pandas",
    "gspread",
    "requests",
    "fire",
    "kfp",
    "geoutils@git+https://github.com/WALTER-GROUP/geoutils.git@v2.6.2-logging-empty",
    "pipesql @ git+https://github.com/WALTER-GROUP/pipesql@main",
]
# to install your package for development, you run `pip install -e '.[dev]'`.
# This installs all the regular required packages and those listed in the dev
# section of extras_require.
extras_require = {
    #
    # what is needed for training, e.g. vertex and BQ access
    "train": [
        "kfp==1.8.17",
        "google-cloud-aiplatform==1.19.1",
        "google-cloud-pipeline-components==1.0.29",
        "cloudevents==1.8.0",
        "google-cloud-pubsub==2.13.11",
    ],
    #
    #
}

# auto-generate all dependencies
extras_require["all"] = list(sum([], extras_require.values()))


#

# This is THE standard way to share packages in Python world
# see https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install ml-platform
    #
    # If published on PyPI: https://pypi.org/project/mlmplatform/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    # also see this for package vs folder vs pip naming conventions:
    # https://oep.readthedocs.io/en/latest/oep-0003.html
    name="postman_collab",
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version="1.0.0",
    # This should be the name of the organization which owns the
    # project.
    author="Ekemini Bassey",
    # This should be a valid email address corresponding to the author listed
    # above, within the LKWW domain
    author_email="bassey@walter-group.com",
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": "src"},
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"),
    # scripts=['bin/script1','bin/script2'],
    # TODO: link to the LKWW Confluence
    url="https://github.com/WALTER-GROUP/emissions_pipeline",
    # TODO: link to the license
    license="LICENSE.txt",
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="TODO: fill me in",
    # Optional full description, that is usually matches README
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=(this_directory / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",  # Optional (see note above)
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will run_check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=">=3.7, <4",
    # read more about above
    install_requires=install_requires,
    # read more above
    extras_require=extras_require,
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        "Bug Reports": "https://github.com/WALTER-GROUP/mlp-experiment-blueprint/issues",
        "Source": "https://github.com/WALTER-GROUP/ml-experiment-blueprint",
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `mycli` which
    # executes the cli entrypoint within the cli.py. It is built with click
    entry_points={  # Optional
        "console_scripts": [
            "mypipeline=emissions_pipeline.pipeline.cli:cli",
            #
            "myupdate=emissions_pipeline.model.update_coors:main"
        ],
    },
    zip_safe=False,
    # to include additional files from MANIFEST.in
    include_package_data=True,
    package_data={'emissions_pipeline': ['util/sql/*', 'tools/mytest/*']},
)
