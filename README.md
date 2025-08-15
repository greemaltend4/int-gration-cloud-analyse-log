# Intégration Cloud pour l'Analyse de Logs

## Description
Ce projet permet d'analyser des fichiers de logs en temps réel en utilisant des services de cloud tels que AWS Lambda et AWS S3. Les logs sont ingérés dans S3, et une fonction Lambda est déclenchée pour effectuer des analyses et générer des rapports.

## Fonctionnalités
- Téléchargement de fichiers de logs dans AWS S3
- Analyse des logs à l'aide de AWS Lambda
- Génération de rapports en temps réel

## Configuration
1. Créez un compartiment S3 nommé `logs-bucket`.
2. Déployez la fonction Lambda avec les permissions nécessaires pour lire et écrire dans S3.
3. Configurez un déclencheur S3 pour invoquer la fonction Lambda à chaque fois qu'un fichier est téléchargé.

## Technologies Utilisées
- AWS S3
- AWS Lambda
- Python

## Contribution
Les contributions sont les bienvenues! Veuillez soumettre un problème ou une demande de tirage pour commencer.
