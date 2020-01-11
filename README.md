# car-spec
Simple website to add, edit and show car specifications

## Permanent Website Link

:warning: **Free-tier track user browsing time and will shutdown when we hit monthly limit of 550 hours**: Be very careful and close the browser after you view it!

https://car-spec-dev.herokuapp.com/

## First Time - Install dependency

```cmd
python -m virtualenv venv
.\venv\Scripts\activate

pip install requirements.txt
.\local_deploy.bat
```

## Afterward - Run web server in localhost, window

```cmd
.\local_deploy.bat
```

## Git remote detail

Three set of git remote should be set up for staging and prod deployment

* dev     https://git.heroku.com/car-spec-dev.git (fetch)
* dev     https://git.heroku.com/car-spec-dev.git (push)
* prod    https://git.heroku.com/car-spec-prod.git (fetch)
* prod    https://git.heroku.com/car-spec-prod.git (push)
* origin  https://github.com/Jimsparkle/car-spec.git (fetch)
* origin  https://github.com/Jimsparkle/car-spec.git (push)

*Rules of thumb*: Develop app in origin, deploy app to dev, never deploy app to prod until we are ready to go public

## Web server detail

https://dashboard.heroku.com/apps/car-spec-dev

https://dashboard.heroku.com/apps/car-spec-prod/

## Postgre SQL detail

[to be added]