FROM photoprism/develop:260814-resolute

ENV NPM_CONFIG_IGNORE_SCRIPTS=true

ARG WORKING_DIR=/go/src/github.com/photoprism/photoprism
WORKDIR "${WORKING_DIR}"

COPY . .
COPY --chown=root:root ./scripts/dist/ /scripts/
