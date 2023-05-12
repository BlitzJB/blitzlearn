API Documentation
-----------------

This documentation provides details about the endpoints available in the API and the expected request and response formats.

Base URL
--------
The base URL for accessing the API is: `[http://api.example.com](https://blitzlearn.jb2k4.repl.co/)`

Heartbeat Endpoint
------------------
This endpoint is used to check the status of the API.

```
GET /hb
POST /hb
HEAD /hb
```

Response
```
Status: 200 OK
Content-Type: text/plain

"ok"
```

Breakdown Endpoint
------------------
This endpoint provides a breakdown of a given topic.

```
POST /v1/breakdown
```

Request
```json
{
  "topic": "string"
}
```

Response
```json
Status: 200 OK
Content-Type: application/json

{
  "status": "success",
  "result": {
    // breakdown information
  }
}
```

Error Responses
```
Status: 400 Bad Request
Content-Type: application/json

{
  "status": "error",
  "error": "No topic provided."
}
```

Describe Endpoint
-----------------
This endpoint provides a description of a given subtopic within a context.

```
POST /v1/describe
```

Request
```json
{
  "subtopic": "string",
  "context": "string"
}
```

Response
```json
Status: 200 OK
Content-Type: application/json

{
  "status": "success",
  "result": {
    // description information
  }
}
```

Error Responses
```
Status: 400 Bad Request
Content-Type: application/json

{
  "status": "error",
  "error": "No subtopic provided."
}
```
```
Status: 400 Bad Request
Content-Type: application/json

{
  "status": "error",
  "error": "No context provided."
}
```

Bulk Describe Endpoint
----------------------
This endpoint provides descriptions of multiple subtopics within a common context.

```
POST /v1/bulk_describe
```

Request
```json
{
  "subtopics": ["string"],
  "context": "string"
}
```

Response
```json
Status: 200 OK
Content-Type: application/json

{
  "status": "success",
  "result": {
    // bulk description information
  }
}
```

Error Responses
```
Status: 400 Bad Request
Content-Type: application/json

{
  "status": "error",
  "error": "No subtopics provided."
}
```
```
Status: 400 Bad Request
Content-Type: application/json

{
  "status": "error",
  "error": "No context provided."
}
```
