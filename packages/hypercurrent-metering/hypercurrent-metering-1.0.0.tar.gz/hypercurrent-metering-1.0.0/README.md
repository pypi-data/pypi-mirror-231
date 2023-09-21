# hypercurrent-metering
HyperCurrent Metering SDK

- API version: 1.11.0-SNAPSHOT
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://hypercurrent.io](https://hypercurrent.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/hypercurrentio/hypercurrent-python-metering.git  --break-system-packages
```
(you may need to run `pip` with root permission: `sudo pip install git@github.com:hypercurrentio/hypercurrent-python-metering.git`)

Then import the package:
```python
import hypercurrent_metering 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and consult the following example:

```python
import hypercurrent_metering
from hypercurrent_metering.rest import ApiException
from hypercurrent_metering import Configuration, ApiClient

hypercurrent = hypercurrent_metering.MeteringControllerApi(hypercurrent_metering.ApiClient())
hypercurrent.api_client.default_headers["x-api-key"] = "HYPERCURRENT_API_KEY"
body = hypercurrent_metering.MeteringRequestDTO(
        application = "77273cd5-02be-46da-8022-87e237f25393", # REQUIRED, this is generally the clientId
        method="GET", # REQUIRED
        url="/api/1", # REQUIRED
        request_headers=[], # REQUIRED (but can be empty)
        response_headers=[], # REQUIRED (but can be empty)
        metadata = "5", # OPTIONAL 
        backend_latency = 100, # OPTIONAL 
        gateway_latency = 14, # OPTIONAL 
        response_code = 200, # OPTIONAL 
        timed_out = False, # OPTIONAL 
        request_message_size = 1024, # OPTIONAL 
        response_message_size = 4096, # OPTIONAL 
        remote_user = "gabe@acmesoft.com", # OPTIONAL 
        remote_host = "10.0.2.12", # OPTIONAL 
        http_protocol = "https", # OPTIONAL 
        content_type = "application/json", # OPTIONAL 
        correlation_id = "3b3e9685-99e9-4f2d-9cd7-6c8de3cff2ae" # OPTIONAL 
        )
try:
        hypercurrent.meter(body)
except ApiException as e:
        print("Exception when metering API request: %s\n" % e)


```

## Documentation for API Endpoints

All URIs are relative to *https://api.hypercurrent.io/meter/v1/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiEventsControllerApi* | [**event**](docs/ApiEventsControllerApi.md#event) | **POST** /event | Log API event
*MeteringControllerApi* | [**meter**](docs/MeteringControllerApi.md#meter) | **POST** /meter | Insert API metering data
*MeteringControllerApi* | [**valid**](docs/MeteringControllerApi.md#valid) | **GET** /meter/product-key | Determine if a ProductKey is valid or not

## Documentation For Models

 - [ApiEventDTO](docs/ApiEventDTO.md)
 - [MeteringRequestDTO](docs/MeteringRequestDTO.md)

## Documentation For Authorization


## x-api-key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

## Author
info@hypercurrent.io
