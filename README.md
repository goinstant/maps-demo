# Goinstant maps-demo

## Environment Setup
### Local
#### Prerequisites
You must have node js v0.10+ install and a redis 2.6+ server running.

#### Setup

1. Install + Config Heroku toolbelt; [quick link](https://toolbelt.heroku.com)
2. execute `npm install` from the repo root
3. copy the example configuration and fill out platform object with your own application information, you can leave out any private data  from the config see [here](#environment-overrides) for environment overrides `cp config/example.json config/local.json`
4. execute `foreman start` from repo root to start the application

### Heroku
#### Prerequisites
##### Setup Heroku App + Services
1. Create a heroku app `heroku apps:create yourmapsapp`
2. Enable Redis Cloud `heroku addons:add rediscloud:20`
3. Run Environment Setup script see [here](#heroku-setup-environment)

#### Install + Start Services

You simply have to push to the heroku git master to launch the app, below are a few different ways

##### Push Master
Normal or First Push

`git push heroku master`

##### Push Branch
To push your branch your working on

`git push heroku branchname:master`

#### Push Tag
To push a existing tag, note that this will not work unless you have already initialized the remote repo.

`git push heroku v1.0.0^{}:master`



### Setup Environment Script
#### local environment overrides
Overrides are not required for the local environment but you are welcome to use `./scripts/setup_env.sh -e local` in the spirit of consistency if you have a live heroku environment. This lets your keep out any of your private keys and user names if you want to redistribute your local.json.

Press Enter to skip any variables you set in the config.

#### heroku setup environment
Execute the setup_env.sh script to set all environment variables required to run on heroku. Have the following available before you start:

- FORCE_SSL (Set to anything but "true" makes the most sense :-D )
- REDISCLOUD_URL *Press enter to skip this, rediscloud addon automatically sets this
- SENDGRID_USER +
- SENDGRID_PASSWORD +
- TWILIO_AUTH_TOKEN +
- TWILIO_ACCOUNT_SID +
- TWILIO_NUMBER +
- PLATFORM_ACCOUNT ++
- PLATFORM_APP ++
- PLATFORM_SECRET ++


\+ Recommend entering valid accounts if you have them, if not available fake them out but will error the invite feature
++ These are all required and available in the goinstant dashboard [here](https://goinstant.com/dashboard)

1. Execute setup_env script `./scripts/setup_env.sh -e yourmapsapp`
2. Execute `heroku config` to verify config was set properly


#### adding heroku repos

```
heroku git:remote -a <prod repo name>
heroku git:remote -a <stg repo name>
```


