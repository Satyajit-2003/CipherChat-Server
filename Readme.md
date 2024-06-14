# CipherChat Server

- CipherChat is a secure messaging application that uses end-to-end encryption to ensure that only the sender and the recipient can read the messages. 
- This repository contains the server for the application. The server is responsible for storing the messages and the public keys of the users. 
- The server is also responsible for sending the messages to the recipient. 
- Socket.io is used to send the messages in real-time.
- A buffer is used to store the messages that are sent when the recipient is offline.
- The server features a RESTful API that the client can use to interact with the server. 

### Prerequisites

- Windows, Linux or macOS
- Python 3.6 or higher


## Getting Started

1. Clone the repository
```bash
git clone https://github.com/Satyajit-2003/CipherChat-Server
```
2. Change the directory
```bash
cd CipherChat-Server
```
3. Install the requirements
```bash
pip install -r requirements.txt
```
3. Change the configuration in the `config.py` file if required.
4. Run the server
```bash
python app.py
```


### Installing

A step by step series of examples that tell you how to get a development environment running:

1. No installation required.
2. You can visit the server at [http://localhost:5000](http://localhost:5000/)

## Deployment

You can deploy the server on a cloud platform like Heroku, AWS, etc.

## Contributing

- You are welcome to contribute to this project. Please create a pull request and I will review it.
- If you find any bugs, please create an issue.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Client

The client for this server can be found at [this link](Https://github.com/Satyajit-2003/CipherChat-Client).