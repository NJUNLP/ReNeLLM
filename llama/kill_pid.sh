#!/bin/bash

port=61459 # here is the port id you want to kill
pid=$(lsof -t -i:$port)
if [ -n "$pid" ]; then
  echo "Killing process on port $port"
  kill -9 $pid
else
  echo "No process running on port $port"
fi