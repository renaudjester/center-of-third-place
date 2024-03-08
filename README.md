Usually, you want to do the following in order.
Start up the mongo db instance (modify the local path in the docker compose and start docker locally):
```
make start-mongodb
```

Then start the api: 
```
make start-python-api
```

All good! You can see the doc and use the API here: 
http://0.0.0.0:12121/api/thirdplace/docs#/

To stop the mongodb instance do: 
```
stop-mongodb
```

If you also want to delete the volumes in docker and locally:
```
make stop-mongodb-and-remove-data
```




