FROM gitpod/workspace-full:latest

USER root

RUN true \
  && apt update \
  && apt install -y shellcheck
