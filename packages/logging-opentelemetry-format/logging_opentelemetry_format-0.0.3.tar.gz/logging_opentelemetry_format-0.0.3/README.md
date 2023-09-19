# logging-opentelemetry-format

a simple logging formatter which can be used to format logs to opentelemetry specification coming out from a system.
it also provides some additional size control over log body and log attributes


#### Installation

- from pypi
```
pip install logging_opentelemetry_format
```

#### Usage
- check [example](tests/test_logging.py) for a complete example
- the formatter is available as
```
from logging_opentelemetry_format.utils import OpentelemetryLogFormatter
```
- on a basic level this formatter can be added to a logging handler
- it takes following optional keyword arguments
- `use_traces`: use the traces information to enrich logs or not(trace_id and span_id)
- `restrict_attributes_to`: list of attributes to which log's attributes should be restricted, any extra attributes passed inside extra keywords in logs will be added against `_meta` inside attributes.
- `meta_character_limit`: the max length of value for `_meta` in output logs' attributes, if the length of log's meta exceeds this limit the value of log's meta will be trimmed to specified length. also an attribute `_meta_original_length` is added with value as the length of original log meta and `_meta_too_large` with value `true` for debugging purpose.
- `body_character_limit`: the max length of value for log body, if the length of log body exceeds this limit the value of log body will be trimmed to specified value. also an attribute `_body_original_length` is added with value as the length of original log body and `_body_too_large` with value `true` for debugging purpose.
- `discard_attributes_from`: an array of attributes which needs to be skipped when exporting logs

#### Local development and testing

- build the docker-image of the package `docker-compose build --no-cache`
- run the image `docker-compose up`
- go to the container `docker exec -it loggingoplttester sh`
- to run tests  `pytest tests/` to run the actual tests.


#### License

- this project is licensed under [MIT License](LICENSE)