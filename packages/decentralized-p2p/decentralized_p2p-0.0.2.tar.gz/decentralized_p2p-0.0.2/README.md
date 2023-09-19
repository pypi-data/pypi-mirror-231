
# CS50P peer to peer network

A simple system to handle networking through python sockets, in a p2p style

## Installation

Download PyPI library

```bash
  pip install decentralized-p2p
```

Import the peer class in your main file

```py
  from peer import Peer
```
## Usage/Examples

Declare a peer object with:

```py
my_peer = Peer()
```

To create a new network, use the Peer.create_network method.
You will need to specify your username, password, ip and eventual signature and encryption keys

```py
my_peer.create_network("Username", "Password", "192.168.1.2", "None", "None")
```

In another file, call the sign up method to connect to the newly created network:

```py
my_peer_2.signup("SecondUsername", "SecondPassword", "192.168.1.2")
```

Now you can send and receive messages respectivly with the .send() and .read() methods.

## Features

- Asyncronous message send and receive
- Totally decentralized system, allows for wide horizontal expansion
- Asymmetrix signature implemented through ecdsa
- Asymmetric encryption implemented using fernet


## Running Tests

To run tests, run the following command

```bash
  pytest test_project.py
```


## Authors

- [@NeekoKun](https://www.github.com/NeekoKun)
- [@NeekoKun02](https://www.github.com/NeekoKun02)