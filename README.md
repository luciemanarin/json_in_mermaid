# Outil de Conversion de Mappage Elasticsearch en Diagramme Mermaid

Ce projet contient un script Python qui convertit les définitions de mappage Elasticsearch (fichiers JSON) en diagrammes de classes Mermaid. Ces diagrammes peuvent ensuite être visualisés dans un navigateur web.

## Fichiers Inclus

- `es_mapping_to_mermaid.py`: Le script Python principal qui génère le code Mermaid.
- `run_diagram.bat`: Un script batch pour simplifier l'exécution sur Windows.
- `index.html`: Le fichier HTML qui sert de modèle pour le diagramme et sera mis à jour avec le code Mermaid généré.

## Utilisation

Pour utiliser l'outil, suivez ces étapes :

1.  **Prérequis :** Assurez-vous d'avoir Python 3 installé sur votre machine.

2.  **Exécuter le script (Méthode recommandée sur Windows) :**

    - **Glisser-déposer :** Vous pouvez simplement **glisser-déposer votre fichier JSON de mappage Elasticsearch** sur le fichier `run_diagram.bat`. Le script s'exécutera automatiquement et ouvrira le diagramme dans votre navigateur par défaut.

    - **Ligne de commande (Windows) :** Ouvrez l'Explorateur de fichiers, naviguez jusqu'à l'emplacement des fichiers, tapez `cmd` dans la barre d'adresse et appuyez sur Entrée pour ouvrir une invite de commande dans ce répertoire. Ensuite, exécutez la commande suivante :
      ```bash
      run_diagram.bat votre_fichier_de_mapping.json
      ```
      Remplacez `votre_fichier_de_mapping.json` par le nom de votre fichier JSON.

3.  **Visualisation du Diagramme :**

    - Le script mettra à jour le fichier `index.html` avec le diagramme Mermaid et tentera de l'ouvrir automatiquement dans votre navigateur web par défaut.
    - **Si l'ouverture automatique échoue** (par exemple, "Impossible d'accéder à votre fichier" sur Windows, souvent lié aux permissions), vous pouvez simplement ouvrir le fichier `index.html` manuellement avec votre navigateur web préféré. Le diagramme y sera présent.

---

**Note :** Pour un exemple de fichier JSON de mappage Elasticsearch à utiliser, vous pouvez en créer un manuellement ou utiliser l'un de vos propres fichiers existants. Le script ne contient plus de fichiers d'exemple pré-inclus pour un environnement plus propre.
