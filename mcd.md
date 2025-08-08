BAR => Cocktails => Clients

stock_cocktails         
_______________      
id primary key   
name_create     
ingredients           
story_describe
sound_ambiance
picture_prompt


 # Arrêter tous les conteneurs
docker-compose down

# Supprimer les conteneurs corrompus
docker container prune -f

# Supprimer les images corrompues
docker image prune -a -f

# Supprimer les volumes
docker volume prune -f

# Supprimer les réseaux
docker network prune -f

# Nettoyage système complet
docker system prune -a --volumes -f

# Lancer
docker-compose up --build

