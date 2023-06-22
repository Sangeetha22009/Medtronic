
# CDS Services

A sample python basic script to reprsent cds Services of FHIR 



## NGROK Installation

download package from - https://dashboard.ngrok.com/get-started/setup 

and install as per documentation


## Install dependencies

Install requirements

```bash
 pip install flask
 pip install flask_cors

```
    
    
## Run CDS Services

Navigate to the folder which contain main.py

```bash
  python3 main.py
```


## Run NGROK

Run NGROK with specific port number mentioned in the main.py

```bash
  ngrok http <port_no> # in main.py its 8080
```

run ngrok for our project

```bash
  ngrok http 8080
```


