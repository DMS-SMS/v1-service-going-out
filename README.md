# v1-outing-service
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
