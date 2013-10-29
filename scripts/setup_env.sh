#!/usr/bin/env bash
# Setup environment overrides for foreman(local) or heroku app environments
# Usage: ./setup_env.sh -e local

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DOT_ENV="$SCRIPT_DIR/../.ENV"
source $SCRIPT_DIR/overrides

usage() 
{
  cat <<EOF
$1
Usage: $0 -e <env> [-h]

  OPTIONS:
    -h Show this Help page
    -e Environment: local|heroku environment

  ENVIRONMENT:
    local: reserved for foreman local development
    *: your heroku application name
EOF
  exit 1
}

error()
{
  echo "ERROR: $1"
  exit 1
}

checkHerokuApp()
{
  checkApp=`heroku apps|grep $1$`

  if [ "$?" -ne "0" ]; then
    error "Specified Heroku app does not exist"
  fi

}

checkEnv()
{
  if [[ "$ENV" != "local" ]]; then
    checkHerokuApp $ENV
  fi
}

resetLocalEnv()
{

  # DELETE EXISTING DOT ENV FILE
  rm -f $DOT_ENV

}

set_prompt()
{
  read -p "SET $1 :" myresult
  set_env $1 $myresult

}

set_env()
{
  if [ "$2" != "" ]; then
    env="$1=$2"
    ENV_STR="$ENV_STR $env"
  fi
}

save_env()
{
  if [ "$ENV" == "local" ]; then
    resetLocalEnv
    for item in $ENV_STR
    do
      echo $item >> $DOT_ENV
    done
  else
    echo "Setting $ENV_STR"
    heroku config:set $ENV_STR -a $ENV
  fi
}

setupEnv()
{
  # Iterate the overirdes array
  for item in "${OVERRIDES[@]}"
  do
    set_prompt $item
  done
  save_env

}

echo "Press [Enter] to skip any option"

while getopts "e:h:" opt; do
  case $opt in
    e)
      ENV=$OPTARG
      echo "Set ENV: $ENV"
      checkEnv

      #Set this so json config find the base template
      set_env NODE_ENV heroku

      setupEnv
      ;;
    h)
      usage
      ;;
    \?)
      usage "Invalid Option: $OPTARG"
      ;;
  esac
done

# Fail Safe
if [ -z "$ENV" ]
then
  usage
  exit
fi
