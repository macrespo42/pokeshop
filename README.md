# Pokéshop

## 1. Catalogue

Le Catalogue est le referential des cartes proposees a la vente. Il gère l'identité de chaque carte:  
quel Pokemon, quelle edition, quel stat physique, quelle rareté. C'est la "fiche produit" de la boutique.

***Donnee d'une carte***

Chaque carte du catalogue est décrite par les informations suivantes:

- ***Nom du Pokemon*** -- Ex: "dracaufeu", "Pikachu", "Mewtwo"
- ***Rareté*** — Le niveau de rareté imprime sur la carte
- ***Edition*** — L'extension d'origine avec son code, son nom et son année de sortie
- ***État physique*** — L'état de conservation de la carte
- ***Type de Pokemon*** — Feu, Eau, Plante, Électrique, etc.
- ***Holographique*** — Oui ou Non
- ***Illustration*** -- Image de la carte (optionnel)
- ***Date d'ajout*** — Quand la carte à ete référencée
- ***Status*** -- Disponible, reservee, vendue ou retiree

***Niveau de rareté***

| Rarete             | Description                                    | Symbole       |
|--------------------|------------------------------------------------|---------------|
| Commune            | Carte les plus courantes                       | Cercle        |
| Peu commune        | Cartes intermediaire                           | Losange       |
| Rare               | Carte recherchees                              | Etoile        |
| Rare holographique | Carte rare avec effet brillant                 | Etoile + holo |
| Ultra rare         | Cartes premium (EX,GX,V,VMAX                   | Etoile doree  |
| Secrete            | Cartes dont le numero depasse la taille du set |

***États physiques***

| Etat      | Description                    |
|-----------|--------------------------------|
| Mint      | Carte les plus courantes       |
| Near Mint | Cartes intermediaire           |
| Excellent | Carte recherchees              |
| Played    | Carte rare avec effet brillant |
| Damaged   | Cartes premium (EX,GX,V,VMAX   |

***Status d'une carte***

| Status     | Description                                          |
|------------|------------------------------------------------------|
| Disponible | La carte peut etre achetee                           |
| Reservee   | La carte est dans une commande en cours              |
| Vendue     | la carte a ete achetee                               |
| Retiree    | La carte a ete retiree du catalogue par un operateur |

***Règles metier***

- Toute carte doit obligatoirement avoir un nom, une rareté, une edition et un état physique.
- une carte entre au catalogue avec le status "Disponible".
- Une carte vendue ne peut jamais redevenir disponible.
- Une carte retiree peut être remise en vente (retour au status "Disponible")
- Une carte reservee ne peut devenir que vendue (achat confirme) ou disponible (commande annulée).

***Fonctionnalités***

| Fonction                     | Description                                                             |
|------------------------------|-------------------------------------------------------------------------|
| Referencer une carte         | Ajouter une nouvelle carte au catalogue avec toutes ses caracteristique |
| Consulter une carte          | Afficher le detail complet d'une carte                                  |
| Rechercher des cartes        | Filtrer par nom, rarete, edition, type, etat, status                    |
| Retirer une carte            | Retirer une carte de la vente                                           |
| Lister les cartes disponible | Afficher uniquement les cartes en status "Disponible                    |

***Notifications émises vers les autres domaines***

- ***Nouvelle carte référencée*** — Informe le Stock et la Tarification qu'une nouvelle carte existe
- ***Carte retiree*** — Informe le Stock et la Tarification qu'une carte n'est plus en vente

## TODO

- [ ] Gérer le cas ou l'event publish échoue
- [x] Renommage des tests pour un nom plus précis
- [x] Check du publish implem dans le fake à la place de mock
- [x] remove --> soft remove simplement un changement d'état
- [ ] event concret inmemory pas rabbitmq
- [x] checker les règles métier certaine ne sont pas implémenter
