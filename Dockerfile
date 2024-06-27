FROM pytorch/torchserve:latest

EXPOSE 8080
EXPOSE 8081

COPY model_store/ model_store/
COPY config.properties config.properties

CMD ["torchserve", "--start", "--model-store", "model_store", "--ts-config", "config.properties"]
