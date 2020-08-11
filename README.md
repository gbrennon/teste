# RiskScore

### Description

Microservice that evaluate risk score based on personal information provided.

### Architecture Proposal

<p align="center">
  <img src="https://github.com/maiaPhilippe/teste/blob/master/readme_images/risk_score.png" />
</p>

The proposed architecture assume that the application will be deployed on AWS cloud basis, however, there are several similar cloud tools available on market.

### API flow steps:

- All exposed APIs will be authenticated by AWS Cognito on every request conducted by APIGateway
- Check cache data on Redis layer
- Evaluate Risk
- Generate events over ElasticSearch (kinesis firehose ingestion)

### Installation

#### Docker-compose

```sh
$ cd teste
$ docker-compose up
```

#### MakeFile

```sh
$ cd teste
$ make run
```

### Tests

#### MakeFile

```sh
$ cd teste
$ make test
```

### API

#### Health-Check

url:
```
GET http://0.0.0.0:8080/risk/health-check
```

#### Risk

url:
```
POST http://0.0.0.0:8080/risk/v1
```

headers:
```
Content-Type: application/json
```

body:
```
{
  "age": 35,
  "dependents": 0,
  "house": {"ownership_status": "owned"},
  "income": 10,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2014}
}
```