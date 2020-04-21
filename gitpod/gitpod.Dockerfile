FROM gitpod/workspace-full:latest

USER root

RUN true \
  && apt update \
  && apt install -y shellcheck

# Add ION support
RUN sudo add-apt-repository ppa:mmstick76/ion-shell \
    && sudo apt-get update \
    && sudo apt-get install -yq \
        ion-shell
