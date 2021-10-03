

# Generation des fichiers de configuration

## Configuration de l'accès à l'API
``` bash
export VAPORMAP_BACKEND=localhost
export VAPORMAP_BACKEND_PORT=8001
envsubst '${VAPORMAP_BACKEND},${VAPORMAP_BACKEND_PORT}' < config.json.template > config.json
```

## Génération du fichier de configuration du serveur Nginx
``` bash
export VAPORMAP_URL_SERVERNAME=localhost
export VAPORMAP_URL_PORT=8000
export VAPORMAP_FRONTEND_ROOT=${PWD}
envsubst '${VAPORMAP_URL_SERVERNAME},${VAPORMAP_URL_PORT},${VAPORMAP_FRONTEND_ROOT}' < nginx.conf.template > nginx.conf
```
