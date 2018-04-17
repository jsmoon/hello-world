# hello-world
Test activities in GitHub

## The way to git clone

git protocol used for git clone, git fetch and git pull in general.
  - git clone git://github.com/bidtt4/hello-world && cd hello-world

https protocol should used for git push. ssh protocol may not work.
  - git remote set-url --push origin https://github.com/bidtt4/hello-world && git config --local -l

## Syncing a fork

configure a remote for the fork
  - git remote add upstream https://github.com/jsmoon/hello-world

syncing the fork
  - git fetch upstream && git checkout master && git merge upstream/master
  - git push origin master

## 
## Udate test
## Test direct pull request
