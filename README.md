# TableTopSecurity
===

### Clone repository and work with `source` branch
    git clone https://github.com/TableTopSecurity/TableTopSecurity.github.io.git
    cd TableTopSecurity.github.io
    git fetch origin
    git branch gh-pages origin/master

### Option 1: Setup virtualenv
    pip install virtualenv
    mkdir ENV
    virtualenv ENV
    source ENV/bin/activate

### Option 2: conda environment
	conda create --name TTS python=3
	source activate TTS

### Install dependencies
    pip install pelican
    pip install Markdown
    pip install ghp-import

## Running Pelican for development
    # start local server
    make devserver
    # site is viewable at http://localhost:8000/
    # to stop: make stopserver

## Publish
    # You have some changes to the `source` branch
    #   They should be all committed; check with `git status` and commit if any
    #   Now we are about to re-generate the website in a `gh-pages` branch
    # Prep that by getting it up to date:
    git checkout gh-pages
    git pull origin master

    # now, switch back to the `source` branch
    git checkout source

    # now generate the new `output` and use it to update the `gh-pages` branch
    pelican content -o output -s publishconf.py
    ghp-import output

    # now push the local `gh-pages` branch to the remote `master` branch
    git push origin gh-pages:master

    # if you did this wrong, you'll get some type of merge error when
    #    you push gh-pages to the remote master branch and it will
    #    complain that you shoud have done a pull first
