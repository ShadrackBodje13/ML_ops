# ML_ops

<!-- Add mes librairies -->
pip freeze > requirements.txt
<!-- Importer mes librairies dans votre code -->
pip install -r requirements.txt


<!-- Creation du projet -->
creation des dossiers src et data
dans src creation des fichier load_data.py, train.py et features.py

<!--  src/Load data -->
Nous permet d'importer nos données et nous les transformer en fichier de données csv
Maintenant lancer 
> python .\src\load_data.py

<!--  src/features.py-->
Faire un travail sur nos features. 
Run notre feature > python .\src\features.py


<!-- Installer black pour reformatter nos codes -->
pip install black 
<!-- Reformatter tous nos code dans src -->
black -l 100 ./src*.py
<!-- Analyse notre code avec pylint -->
pip install pylint
analyser le code avec > pylint .\src*.py

<!-- Install MLFLOW -->
pip install mlflow

<!-- En dehors de notre dossier github, on peut lancer notre projet -->
mlflow server --host 0.0.0.0 --port 8088
ou 
mlflow server --host localhost --port 9090

<!-- Lancer le mlflow -->
python .\src\demo_mlflow.py

<!-- Lancer le train -->
python .\src\train.py   

<!-- NEW -->
<!-- Execution du curl pour aller prendre les données (attention changer l'adresse ip si possible) -->

Sur linux : curl --request GET \
     --url 'https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-tertiaire-2/lines?size=100&sort=Date_visite_diagnostiqueur&format=json'

Sur Windows avec powershell : Invoke-WebRequest -Uri 'https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-tertiaire-2/lines?size=100&sort=Date_visite_diagnostiqueur&format=json' -Method GET


<!-- Recuperer les données -->
Créer un dossier api dans lequel on crée un fichier url.json
Rcuprer et stocker les données dans notre dossier (regarder build_dataset_01.py)



<!-- AIR FLOW pour le CI/CD, il est un orchestrateur -->
https://airflow.apache.org/

Le créer aillerus de notre projet (à la racine de preference)
creer la variable d'environnement sur windows
> set AIRFLOW_HOME=~/airflow (vous pouvez changer le dossier, C:\MASTER\Master2\MachineLearningOPS\MLOps_github\airflow)
Savoir si la variable est declarée
> echo %AIRFLOW_HOME% 


Prendre docker yaml
-> curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.3/docker-compose.yaml'
> windows : Invoke-WebRequest -Uri 'https://airflow.apache.org/docs/apache-airflow/2.8.3/docker-compose.yaml' -OutFile 'docker-compose.yaml'

Lancer docker compose
docker compose up airflow-init
puis docker compose up  

> Lancer le site qui nous parvient 
Identifiant airflow|airflow

<!-- Ensuite choisir un workflow qui nous convient sinon le coder -->

> http://0.0.0.0:8080/dags/tutorial/grid?tab=code

Se diriger dans le repertoire Airflow
puis logs (pour voir les dag qu'on a activé)

<!-- Install Airflow dans notre -->
> pip install apache-airflow

<!-- Creation de notre workflow avec airflow -->
> Creation du dossier dags 
> creation du fichier de notre dags flow puis code


<!-- Container azure -->
Creer compte de stockage sur azure
Ensuite regarder dans container
Creer container azure
Account name = Nom du compte de stockage
Container = nom du container azure qu'on a créé

#Installer  pip install azure-storage-blob

Créer la variable d'environnement sur windows > set STORAGE_BLOB_ADEME_MLOPS=YOUR_STORAGE_KEY_HERE

Puis relancer le fichier qui crée les dags. Live_ademe_data.py

<!-- ---------------------------------Reprise -->
A chaque reprise faire tourner mlflow et airflow en local
Relancer docker. 



<!-- Creer serveur Postgre sur azure -->
D'abord créer le cluster 
Serveurs Azure Database pour PostgreSQL
Puis créer la base de données

Rentrer les informations necessaires. 
shadis
France@2018



<!-- Se connecter àa la base sur azure. -->
Ouvrir le bash après
Se connecter 
Créer la table 

CREATE TABLE dpe_tertiaire (
    id SERIAL PRIMARY KEY,
    adresse_ban TEXT DEFAULT '',
    adresse_brute TEXT DEFAULT '',
    annee_construction TEXT DEFAULT '',
    annee_releve_conso_energie_n_1 TEXT DEFAULT '',
    annee_releve_conso_energie_n_2 TEXT DEFAULT '',
    annee_releve_conso_energie_n_3 TEXT DEFAULT '',
    categorie_erp TEXT DEFAULT '',
    code_insee_ban TEXT DEFAULT '',
    code_postal_ban TEXT DEFAULT '',
    code_postal_brut TEXT DEFAULT '',
    complement_d_adresse_batiment TEXT DEFAULT '',
    complement_d_adresse_logement TEXT DEFAULT '',
    conso_e_finale_energie_n_1 TEXT DEFAULT '',
    conso_e_finale_energie_n_2 TEXT DEFAULT '',
    conso_e_finale_energie_n_3 TEXT DEFAULT '',
    conso_e_primaire_energie_n_1 TEXT DEFAULT '',
    conso_e_primaire_energie_n_2 TEXT DEFAULT '',
    conso_e_primaire_energie_n_3 TEXT DEFAULT '',
    conso_kwhep_m2_an TEXT DEFAULT '',
    coordonnee_cartographique_x_ban TEXT DEFAULT '',
    coordonnee_cartographique_y_ban TEXT DEFAULT '',
    date_etablissement_dpe TEXT DEFAULT '',
    date_fin_validite_dpe TEXT DEFAULT '',
    date_reception_dpe TEXT DEFAULT '',
    date_visite_diagnostiqueur TEXT DEFAULT '',
    dpe_geopoint TEXT DEFAULT '',
    dpe_i TEXT DEFAULT '',
    dpe_id TEXT DEFAULT '',
    dpe_rand TEXT DEFAULT '',
    dpe_score TEXT DEFAULT '',
    emission_ges_kgco2_m2_an TEXT DEFAULT '',
    etiquette_dpe TEXT DEFAULT '',
    etiquette_ges TEXT DEFAULT '',
    frais_annuel_energie_n_1 TEXT DEFAULT '',
    frais_annuel_energie_n_2 TEXT DEFAULT '',
    frais_annuel_energie_n_3 TEXT DEFAULT '',
    identifiant_ban TEXT DEFAULT '',
    invariant_fiscal_logement TEXT DEFAULT '',
    methode_du_dpe TEXT DEFAULT '',
    modele_dpe TEXT DEFAULT '',
    n_departement_ban TEXT DEFAULT '',
    n_dpe TEXT DEFAULT '',
    n_dpe_remplace TEXT DEFAULT '',
    n_etage_appartement TEXT DEFAULT '',
    n_immatriculation_copropriete TEXT DEFAULT '',
    n_region_ban TEXT DEFAULT '',
    n_voie_ban TEXT DEFAULT '',
    nom_commune_ban TEXT DEFAULT '',
    nom_commune_brut TEXT DEFAULT '',
    nom_residence TEXT DEFAULT '',
    nom_rue_ban TEXT DEFAULT '',
    nombre_occupant TEXT DEFAULT '',
    periode_construction TEXT DEFAULT '',
    score_ban TEXT DEFAULT '',
    secteur_activite TEXT DEFAULT '',
    statut_geocodage TEXT DEFAULT '',
    surface_shon TEXT DEFAULT '',
    surface_utile TEXT DEFAULT '',
    type_energie_n_1 TEXT DEFAULT '',
    type_energie_n_2 TEXT DEFAULT '',
    type_energie_n_3 TEXT DEFAULT '',
    type_energie_principale_chauffage TEXT DEFAULT '',
    type_usage_energie_n_1 TEXT DEFAULT '',
    type_usage_energie_n_2 TEXT DEFAULT '',
    type_usage_energie_n_3 TEXT DEFAULT '',
    version_dpe TEXT DEFAULT ''
);

ALTER TABLE dpe_tertiaire  ADD COLUMN created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now();
ALTER TABLE dpe_tertiaire  ADD COLUMN modified_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now();


<!-- Ajouter les variables d'environnement dans admin airflow  -->