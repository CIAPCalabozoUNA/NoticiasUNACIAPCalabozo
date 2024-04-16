#!/bin/bash

# Check if the production parameter is set to "true"
echo $1
if [[ "$1" == "production" ]]; then
  # Use custom docker-compose file for production
  echo "Running in production mode."
  docker-compose -f docker-compose-prod.yml up
else
  # Use default docker-compose file for development
  echo "Running in development mode."
  docker-compose up
fi
