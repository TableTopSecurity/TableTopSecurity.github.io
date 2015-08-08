# TableTopSecurity
===

### Install virtualenv
    pip install virtualenv

### Clone repository and work with `source` branch
    git clone https://github.com/TableTopSecurity/TableTopSecurity.github.io.git
    cd TableTopSecurity.github.io
    git fetch origin
    git checkout -b gh-pages origin/master
    git checkout -b source origin/source

### Setup virtualenv
    mkdir ENV
    virtualenv ENV
    source ENV/bin/activate

### Install dependencies
    pip install pelican
    pip install Markdown
    pip install ghp-import

## Running Pelican for development
    # start local server
    make serve
    # site is viewable at http://localhost:8000/

## Commit content
    pelican content -o output -s publishconf.py
    ghp-import output
    git push origin gh-pages:master
