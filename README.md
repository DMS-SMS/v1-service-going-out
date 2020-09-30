# v1-outing-service
하 다 갈아 엎고 싶다 코드가 이게 뭘까요 ? <br/>
날 잡고 다 갈아 엎을게요 
## Run
```bash
$ python3 run.py
```
## Test
```bash
$ pytest
```
## Components
### Presentation
- servicers (gRPC)
### Application
- services
- mapper
- decorator (Error handling)
### Domain
- entity (DTO)
- repository (interface) 
- domain service (interface)

### Infrastructure
- domain service (implements)
- repository (implements)
- model
- mapper
- extension 
- exception
- util
