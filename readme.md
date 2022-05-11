# NFE Verifier

Take a brazilian NFe - Nota Fiscal Eletrônica Brasileira - and verify if its integrity through XML-signature digest checking

## Running setup

It's a docker-compose/Fast-API project.
Check the docker-compose.yaml file to get more environmental customizations

```
docker-compose up --build
```
### Docs

Auto-generated documentation is activated for this Fast-API project, and it can be accessed at /docs (when the project is running)


## Example

```
    curl -X POST -F file=@/path/to/file.xml "localhost:8080/verify"
```
