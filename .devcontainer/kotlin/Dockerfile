FROM eclipse-temurin:21-jdk-alpine

LABEL author="G30v4" \
      version="1.0" \
      description="Customized contanier to test Java & Kotlin codes"

## Install Kotlin compiler
RUN apk add --no-cache bash git && \
    cd /usr/lib && \
    wget https://github.com/JetBrains/kotlin/releases/download/v2.1.21/kotlin-compiler-2.1.21.zip && \
    unzip kotlin-compiler-*.zip && \
    rm kotlin-compiler-*.zip && \
    rm kotlinc/bin/*.bat
    
ENV PATH $PATH:/usr/lib/kotlinc/bin
