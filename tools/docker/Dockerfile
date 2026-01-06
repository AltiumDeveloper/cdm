
FROM eclipse-temurin:21-jre

ENV ROBOT_VERSION=1.9.5     WIDOCO_VERSION=1.4.25     JENA_VERSION=5.5.0

ADD https://github.com/ontodev/robot/releases/download/v${ROBOT_VERSION}/robot.jar /opt/robot.jar
ADD https://github.com/dgarijo/Widoco/releases/download/v${WIDOCO_VERSION}/widoco-${WIDOCO_VERSION}-jar-with-dependencies_JDK-17.jar /opt/widoco.jar
ADD https://downloads.apache.org/jena/binaries/apache-jena-${JENA_VERSION}.tar.gz /tmp/
RUN tar -xzf /tmp/apache-jena-${JENA_VERSION}.tar.gz -C /opt && ln -s /opt/apache-jena-${JENA_VERSION} /opt/jena

RUN apt-get update && apt-get install -y python3 python3-pip make bash jq
RUN pip3 install --no-cache-dir pyshacl==0.30.1 rdflib==7.1.4 PyYAML==6.0.2 --break-system-packages   
RUN ln -s /opt/jena/bin/riot /usr/local/bin/riot && ln -s /opt/jena/bin/arq  /usr/local/bin/arq

ENV PATH="/opt/jena/bin:${PATH}"
WORKDIR /workspace
ENTRYPOINT ["/bin/bash"]
