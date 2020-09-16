
# eCoffee


# Django + MongoDB + DRF

eCoffee is an API tool for two lines of coffee products which returns the data for two screens of a mobile app .


## GET STARTED
Run the following commands to get started:


### 1- Database Installation
MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database
```json
$ sudo apt update
$ sudo apt install -y mongodb
```

### 2- Database creation
The mongo shell is an interactive JavaScript interface to MongoDB
```json
$ mongo
> use YOUR_DATABASE
```

### 3- Environment setup
Use the package manager pip to install foobar.

```json
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### 4- GO LIVE
```json
$cd .\ecoffee\
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)