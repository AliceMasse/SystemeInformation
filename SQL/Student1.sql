-- Supprime le type 'type_jeu' s'il existe déjà
DROP TYPE IF EXISTS type_jeu;

-- Crée un nouveau type énuméré 'type_jeu' avec les valeurs spécifiées
CREATE TYPE type_jeu AS ENUM ('puzzle', 'stop ou encore', 'jeu de role', 'title');

-- Supprime les tables 'achat', 'client', 'jeu_de_societe', 'magasin_en_ligne', 'editeur' si elles existent déjà
DROP TABLE IF EXISTS achat, client, jeu_de_societe, magasin_en_ligne, editeur;

-- Crée une nouvelle table 'editeur' avec les colonnes 'code_editeur' et 'nom_editeur'
CREATE TABLE editeur (
    code_editeur SERIAL PRIMARY KEY,  -- 'code_editeur' est la clé primaire et est auto-incrémentée
    nom_editeur TEXT  -- 'nom_editeur' est de type texte et ne peut pas être nul
);

-- Crée une nouvelle table 'magasin_en_ligne' avec les colonnes 'code_magasin', 'nom_magasin'
CREATE TABLE magasin_en_ligne (
    code_magasin INT PRIMARY KEY,  -- 'code_magasin' est la clé primaire
    nom_magasin TEXT  -- 'nom_magasin' est de type texte et ne peut pas être nul
);

-- Crée une nouvelle table 'jeu_de_societe' avec les colonnes 'code_jeu_de_societe', 'nom_jeu_de_societe', 'nb_de_joueurs', 'code_editeur', 'code_magasin'
CREATE TABLE jeu_de_societe (
    code_jeu_de_societe INT PRIMARY KEY,  -- 'code_jeu_de_societe' est la clé primaire
    nom_jeu_de_societe TEXT,  -- 'nom_jeu_de_societe' est de type texte et ne peut pas être nul
    nb_de_joueurs INT,  -- 'nb_de_joueurs' est de type entier
    code_editeur INT,  -- 'code_editeur' est de type entier
    code_magasin INT,  -- 'code_magasin' est de type entier
    FOREIGN KEY (code_editeur) REFERENCES editeur(code_editeur),  -- 'code_editeur' est une clé étrangère qui fait référence à 'code_editeur' dans la table 'editeur'
    FOREIGN KEY (code_magasin) REFERENCES magasin_en_ligne(code_magasin)  -- 'code_magasin' est une clé étrangère qui fait référence à 'code_magasin' dans la table 'magasin_en_ligne'
);

-- Crée une nouvelle table 'client' avec les colonnes 'code_client', 'nom_client', 'age', 'email'
CREATE TABLE client (
    code_client INT PRIMARY KEY,  -- 'code_client' est la clé primaire
    nom_client TEXT,  -- 'nom_client' est de type texte et ne peut pas être nul
    age INT CHECK (age >= 18),  -- 'age' est de type entier et doit être supérieur ou égal à 18
    email text CHECK (email IS NOT NULL AND email LIKE '%@%')  -- 'email' est de type texte et ne peut pas être nul, et doit contenir un caractère '@'
);

-- Crée une nouvelle table 'achat' avec les colonnes 'code_client', 'code_jeu_de_societe', 'quantite', 'date_achat'
CREATE TABLE achat (
    code_client INT,  -- 'code_client' est de type entier
    code_jeu_de_societe INT,  -- 'code_jeu_de_societe' est de type entier
    quantite INT CHECK (quantite > 0),  -- 'quantite' est de type entier et doit être supérieur à 0
    date_achat DATE,  -- 'date_achat' est de type date
    FOREIGN KEY (code_client) REFERENCES client(code_client),  -- 'code_client' est une clé étrangère qui fait référence à 'code_client' dans la table 'client'
    FOREIGN KEY (code_jeu_de_societe) REFERENCES jeu_de_societe(code_jeu_de_societe),  -- 'code_jeu_de_societe' est une clé étrangère qui fait référence à 'code_jeu_de_societe' dans la table 'jeu_de_societe'
    PRIMARY KEY (code_client, code_jeu_de_societe, date_achat)  -- La clé primaire est une combinaison de 'code_client', 'code_jeu_de_societe' et 'date_achat'
);
