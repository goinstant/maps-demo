# GoInstant Google Maps Demo

This repository demonstrates binding the [Google Maps API](https://developers.google.com/maps/) to the [GoInstant API](https://developers.goinstant.com/v1/).

[View live demo here](https://maps.goinstant.com/).

## Running the Demo Yourself

### Locally

If you'd like to work on the maps demo on your local machine, you'll need to do some setup.

#### Prerequisites

You must have node js v0.10+ install and a redis 2.6+ server running.

#### Setup

##### 1. Install + Config Heroku toolbelt; [quick link](https://toolbelt.heroku.com)
##### 2. execute `npm install` from the repo root
##### 3. copy the example configuration and fill out platform object with your own application information
```
cp config/example.json config/local.json
```
##### 4. execute `foreman start` from repo root to start the application

### Heroku

We host the demo on Heroku. These are instructions for setting up and deploying the maps demo to Heroku.

#### Prerequisites

##### Setup Heroku App + Services

##### 1. Create a heroku app 

```
heroku apps:create yourmapsapp
```

##### 2. Enable Redis Cloud 

```
heroku addons:add rediscloud:20
```

##### 3. Setup Heroku Environment

To make setting up your Heroku environment simple, we've provided a script to guide you throught the process.

Before running the script, please have the following information:

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

##### Running the Script

```
./scripts/setup_env.sh -e yourmapsapp
```

*Note about Skipping Variables*

If you hit enter without entering anything, the value on Heroku will be retained.

*Note about Configuring Locally:*

This script can be used to set your local environment as well, by passing `-e local` in order to keep configurations consistent between local and Heroku.

##### Verifying the Script Ran Correctly

You should see the information you entered above, when you run the following command

```
heroku config
```

#### Using Heroku

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



#### adding heroku repos

```
heroku git:remote -a <prod repo name>
heroku git:remote -a <stg repo name>
```


