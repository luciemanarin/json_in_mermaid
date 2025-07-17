# json_in_mermaid

Ce projet vise à fournir un script Python pour convertir les fichiers de mapping Elasticsearch au format JSON en diagrammes Mermaid. Ces diagrammes, en particulier les diagrammes de classes, permettent de visualiser de manière claire et structurée la schémas de vos index Elasticsearch, y compris les champs, leurs types et les objets imbriqués.

## Utilisation

Pour utiliser le script, exécutez-le depuis votre terminal en spécifiant le chemin vers votre fichier de mapping Elasticsearch au format JSON comme argument :

```bash
python es_mapping_to_mermaid.py <chemin_vers_votre_fichier_mapping.json>
```

Le script affichera le diagramme Mermaid généré directement dans la console. Vous pouvez ensuite copier cette sortie et l'utiliser dans un outil supportant Mermaid (par exemple, GitHub, GitLab, ou des éditeurs de texte avec prévisualisation Mermaid) pour visualiser le diagramme.
