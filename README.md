# Simple UDP Rendezvous Server
A general purpose UDP Rendezvous server for implementing peer to peer systems.


### Get client's address
Default Port is `5700`
Payload and Response are in Big Endian format
##### Payload
```
| 1 byte uint8 with value of 200 |
```

##### Responee
- The first four bytes are the ip's components.
- The last two bytes are the port value
```
| 1 byte | 1 byte | 1 byte | 1 byte | 2 byte port |
| uint8  | uint8  | uint8  | uint8  | uint16      |
```

