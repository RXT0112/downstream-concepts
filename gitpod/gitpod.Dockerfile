FROM gitpod/workspace-full:latest

RUN true \
  && apt update \
  && apt install -y shellcheck