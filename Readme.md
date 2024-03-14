# URL Shortner
## Introduction
This is the web-based application for making the short URL. It is developed using Python (Django Framework) as well as SQLite database(default) as a database.

#### Home Page 
![Home Page](/img.png)

## Features
The URL Shortner has the following features.
 - It will Short the Given Long and Complex URL.
 - User can Copy the send the Shorted URL to other.
 - The Link won't Expire.

## Usages
You System must have the following things to use this Blog App.
 - Installation of `python` and  `pip`

    Python is available for every platform. Download it according to you os. You can download it from [Here.](https://www.python.org/downloads/)


Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
    git https://github.com/santoshvandari/LinkShortenerWebsite
    cd LinkShortenerWebsite
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and MAC User
     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Migrate the Model
```bash
    python3 manage.py makemigrations 
    python3 manage.py migrate
```
 - Run the Server
```bash
    python3 manage.py runserver #FOr Linux User
```
 - Open the url in Browser
 ```bash
    http://127.0.0.1:8000/  
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this Blog app, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this app.

## License
This project is licensed under the [License](LICENSE).