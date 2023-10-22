# Contributions

Contributions are welcome and are greatly appreciated! Every little bit helps,
and credit will always be given.


# Report Bugs

Report bugs through [GitHub issues](https://github.com/ShashkovS/tgbotzero/issues).


# Improve Documentation

tgbotzero could always use better documentation, whether as part of the docs, in docstrings, ``docs/*.md`` or even on the web as blog posts or
articles.

# Install the last version from GitHub 

```shell
pip uninstall tgbotzero
pip install --upgrade git+https://github.com/ShashkovS/tgbotzero.git
```

# Configure Your Environment

First you need clone repo, create virtual environment and make an editable install of the package ([ref](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout)):

```shell
# Clone
git clone https://github.com/ShashkovS/tgbotzero.git
# Get into
cd tgbotzero
# Create virtual environment
python -m venv venv

# Activate (bash)
source venv/bin/activate
# Activate (Windows)
. venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
# Install dev-dependencies
pip install -r requirements-dev.txt

# Make an editable install of the package
python -m pip install --editable . --upgrade
```

# Add bot token to TOKEN env'var and it will be used in examples



# Run tests

```shell
python -m pytest -vvs tests/
# or
python -m coverage run -m pytest -vvs tests/
```
