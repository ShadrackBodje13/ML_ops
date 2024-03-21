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