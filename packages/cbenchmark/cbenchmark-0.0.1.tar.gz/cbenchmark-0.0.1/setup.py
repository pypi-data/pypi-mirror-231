import os
import re

from setuptools import setup

# Get version
current_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_path, "cbenchmark", "__init__.py"), encoding="utf-8") as f:
    output = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not output:
        raise ValueError("Error: can't find version in cbenchmark/__init__.py")

    version = output.group(1)


############################################################
# Add all directories in "automations" to the distribution

root = 'cbenchmark'

setup(
    name="cbenchmark",

    author="",
    author_email="",

    version=version,

    description="cBenchmark",

    license="",

    long_description=open('./README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url="",

    python_requires="", 

    packages=['cbenchmark'],

    include_package_data=False,

    package_data={'cbenchmark':['']},

    entry_points={"console_scripts": [
                      "cb = cbenchmark.cli:run"
                  ]},

    zip_safe=False,

    keywords=""
)
