-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 27 juin 2024 à 15:18
-- Version du serveur : 8.3.0
-- Version de PHP : 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `workshop-web-s2`
--

-- --------------------------------------------------------

--
-- Structure de la table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id_category` int NOT NULL AUTO_INCREMENT,
  `label` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `category`
--

INSERT INTO `category` (`id_category`, `label`) VALUES
(1, 'any%'),
(2, '100%'),
(3, 'low%'),
(4, 'glitchless'),
(5, 'any% glitchless'),
(6, 'all bosses'),
(7, 'no major glitches'),
(8, 'true ending'),
(9, 'ng+ 100%');

-- --------------------------------------------------------

--
-- Structure de la table `game`
--

DROP TABLE IF EXISTS `game`;
CREATE TABLE IF NOT EXISTS `game` (
  `id_game` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `released_date` date NOT NULL,
  `description` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_game`),
  UNIQUE KEY `unique name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `game`
--

INSERT INTO `game` (`id_game`, `name`, `released_date`, `description`, `image`) VALUES
(1, 'Elden Ring', '2022-02-22', 'Elden Ring est un jeu d\'action-RPG où le joueur explore l\'Entre-Terre, un vaste monde ouvert rempli de dangers et de secrets. Le joueur incarne un Sans-éclat, cherchant à restaurer l\'Elden Ring pour devenir le Seigneur d\'Elden. Il doit affronter des créatures redoutables et des boss puissants, tout en découvrant des traditions profondes et des histoires cachées. Le jeu combine exploration, combat intense, et personnalisation de personnage pour offrir une expérience immersive et engageante.', ''),
(2, 'Portal', '2007-10-17', 'Portal est un jeu de réflexion à la première personne où le joueur incarne Chell, une testeur dans les laboratoires d\'Aperture Science. Armé du Portal Gun, capable de créer des portails de téléportation, le joueur doit résoudre une série de puzzles complexes. GLaDOS, l\'intelligence artificielle de l\'installation, guide et manipule Chell tout au long des tests. Le jeu se distingue par son humour noir, son gameplay innovant et son intrigue captivante.', ''),
(3, 'Hollow Knight', '2017-02-24', 'Hollow Knight est un jeu d\'action-aventure en 2D où le joueur incarne un chevalier insectoïde explorant le royaume souterrain d\'Hallownest. Le joueur doit affronter des créatures redoutables et des boss puissants tout en découvrant des secrets cachés. Le jeu se distingue par son style artistique dessiné à la main, sa bande sonore immersive et son gameplay exigeant. À mesure que le joueur progresse, il débloque de nouvelles capacités et zones, rendant l\'exploration encore plus riche et captivante.', ''),
(4, 'Ori and the Blind Forest', '2015-03-10', 'Ori and the Blind Forest est un jeu de plateforme et d\'aventure en 2D où le joueur incarne Ori, un esprit gardien, et Sein, une \"lumière et des yeux\" de l\'Arbre des Esprits. Ensemble, ils doivent restaurer la forêt de Nibel, qui a été ravagée par une catastrophe. Le jeu se distingue par ses graphismes magnifiques dessinés à la main, sa bande sonore émotive et son gameplay fluide. Les joueurs doivent résoudre des puzzles, débloquer de nouvelles capacités et surmonter des obstacles difficiles pour progresser dans l\'histoire poignante du jeu.', ''),
(5, 'Celeste', '2018-01-25', 'Celeste est un jeu de plateforme en 2D où le joueur incarne Madeline, une jeune femme déterminée à escalader la montagne Celeste tout en affrontant ses propres démons intérieurs. Le jeu est connu pour ses niveaux exigeants, son contrôle précis du personnage, et ses mécaniques de jeu centrées sur le saut et le dash en l\'air. En plus de son gameplay stimulant, Celeste offre une narration émotive et des thèmes sur la santé mentale et la persévérance. Le jeu a été acclamé pour son design, sa musique et son histoire touchante.', ''),
(6, 'LEGO Star Wars', '2005-03-29', 'LEGO Star Wars est un jeu d\'action-aventure où les joueurs revivent les événements des films Star Wars dans un univers recréé avec des briques LEGO. Le jeu propose des niveaux basés sur les différents épisodes de la saga, combinant combat, résolution de puzzles et exploration. Les joueurs peuvent contrôler une variété de personnages emblématiques de Star Wars, chacun ayant des capacités uniques. Le jeu se distingue par son humour léger, son style graphique distinctif et son gameplay coopératif accessible à tous les âges.', ''),
(7, 'Grand Theft Auto III', '2001-01-22', 'Grand Theft Auto (GTA) est une série de jeux d\'action-aventure en monde ouvert où les joueurs peuvent explorer librement des villes fictives inspirées de lieux réels. Chaque jeu suit des protagonistes engagés dans des activités criminelles, incluant braquages, poursuites en voiture, et missions variées. Le gameplay combine conduite, tir, et éléments de simulation de vie urbaine. La série est connue pour son scénario riche, ses personnages mémorables, et sa capacité à offrir une expérience immersive dans un environnement détaillé et dynamique.', ''),
(8, 'God of War', '2018-04-20', 'God of War (2018), souvent appelé God of War 4, est un jeu d\'action-aventure où Kratos, ayant quitté la Grèce antique, vit maintenant dans le monde de la mythologie nordique. Il part en voyage avec son jeune fils Atreus pour accomplir la dernière volonté de sa défunte épouse : répandre ses cendres au sommet de la plus haute montagne des royaumes. Le jeu se distingue par ses combats intenses à la troisième personne, sa narration émotive et ses graphismes impressionnants. Les relations père-fils et la croissance personnelle de Kratos sont au cœur de l\'intrigue.', ''),
(9, 'Marvel\'s Spider-Man', '2018-09-07', 'Marvel\'s Spider-Man: Miles Morales est un jeu d\'action-aventure en monde ouvert où le joueur incarne Miles Morales, le nouveau Spider-Man, dans une New York hivernale. Le jeu suit Miles alors qu\'il apprend à maîtriser ses nouveaux pouvoirs et protège la ville en l\'absence de Peter Parker. Il combine combat dynamique, furtivité, et exploration, avec des pouvoirs uniques comme l\'invisibilité et les attaques bioélectriques. Le jeu est salué pour ses graphismes époustouflants, son gameplay amélioré, et sa narration émotive.', ''),
(10, 'The Witcher 3: Wild Hunt', '2015-05-19', 'The Witcher 3: Wild Hunt est un jeu de rôle en monde ouvert où le joueur incarne Geralt de Riv, un chasseur de monstres professionnel. Le jeu suit Geralt alors qu\'il recherche Ciri, une jeune femme dotée de pouvoirs extraordinaires, tout en naviguant dans un monde riche en quêtes secondaires, créatures fantastiques, et intrigues politiques. Le jeu est acclamé pour son univers immersif, sa narration profonde, et ses graphismes superbes. Il combine combat tactique, exploration et prise de décisions affectant le cours de l\'histoire.', ''),
(11, 'Broforce', '2015-10-15', 'Broforce est un jeu d\'action-plateforme en 2D où les joueurs contrôlent des personnages parodiant des héros d\'action des années 80 et 90, chacun avec des capacités uniques. Le jeu se déroule à travers des niveaux destructibles remplis d\'ennemis, de pièges, et de boss, avec un style rétro pixel art. Les joueurs doivent sauver leurs coéquipiers captifs et détruire les forces ennemies pour progresser. Le jeu est connu pour son gameplay frénétique, son humour irrévérencieux, et son mode coopératif local et en ligne.', ''),
(12, 'SUPERHOT', '2016-02-25', 'SUPERHOT est un jeu de tir à la première personne avec une mécanique unique où le temps ne s\'écoule que lorsque le joueur se déplace. Cela crée une expérience de jeu stratégique où chaque mouvement doit être calculé avec précision pour éviter les balles ennemies et éliminer les adversaires. Le style visuel minimaliste, combiné à des environnements blancs et des ennemis rouges, crée une atmosphère distinctive et immersive. Le jeu propose des niveaux courts et intenses, avec des séquences de combat qui se déroulent comme des puzzles tactiques.', ''),
(13, 'Super Meat Boy', '2010-10-20', 'Super Meat Boy est un jeu de plateforme hardcore où le joueur contrôle Meat Boy, un petit personnage rouge vif, à travers des niveaux remplis d\'obstacles mortels et de pièges vicieux. Le jeu se distingue par son gameplay rapide et exigeant, nécessitant des réflexes rapides et une précision millimétrée pour éviter les dangers et atteindre la sortie. Chaque niveau est conçu pour défier les compétences du joueur, avec des centaines de niveaux à travers différents mondes thématiques. Le style visuel pixel art et la bande sonore dynamique ajoutent à l\'expérience immersive et rétro.', ''),
(14, 'We Were Here', '2017-02-03', 'We Were Here est un jeu d\'aventure coopératif en ligne où deux joueurs incarnent des explorateurs piégés dans un château abandonné. Chacun des joueurs se trouve dans des pièces différentes du château et doit communiquer efficacement avec l\'autre pour résoudre des énigmes complexes et avancer dans le jeu. La communication et la coopération sont essentielles, car chaque joueur possède des informations et des perspectives uniques nécessaires pour résoudre les énigmes et progresser. Le jeu se distingue par son gameplay basé sur la communication, son atmosphère mystérieuse et ses énigmes innovantes.', ''),
(15, 'It Takes Two', '2021-03-26', 'It Takes Two est un jeu d\'aventure coopératif où deux joueurs incarnent Cody et May, un couple sur le point de divorcer, transformés en poupées par leur fille. Ensemble, ils doivent travailler en coopération pour traverser des mondes fantastiques et résoudre des puzzles pour trouver un moyen de revenir à leur forme humaine et de sauver leur relation. Chaque joueur possède des capacités uniques qui complètent celles de l\'autre, encourageant la communication et la coopération étroite tout au long du jeu. It Takes Two est acclamé pour son gameplay innovant, son histoire captivante sur les relations, et ses visuels colorés.', ''),
(16, 'Hades', '2020-09-17', 'Hades est un jeu d\'action-rogue-like où le joueur incarne Zagreus, le fils d\'Hades, se frayant un chemin à travers les Enfers pour s\'échapper vers la surface. Le jeu combine des éléments de combat dynamique, de progression de personnage et de narration interactive. Chaque tentative de sortie est différente grâce à des niveaux générés de manière procédurale, des ennemis variés et des power-ups aléatoires. Hades se distingue par son gameplay fluide et réactif, ses graphismes stylisés et son histoire mythologique captivante. Le jeu a été salué pour son design innovant et sa jouabilité addictive.', ''),
(17, 'Undertale', '2015-09-15', 'Undertale est un jeu de rôle indépendant où le joueur contrôle un enfant qui tombe dans un monde souterrain rempli de monstres. Le jeu offre une expérience narrative unique où les joueurs peuvent choisir de combattre les ennemis de manière traditionnelle ou de les épargner et de résoudre les conflits pacifiquement. Les choix du joueur affectent directement l\'histoire et influencent les interactions avec les personnages. Undertale se distingue par son humour, ses dialogues riches, ses mécaniques de combat originales et sa bande sonore mémorable composée par Toby Fox. Le jeu encourage l\'exploration, la réflexion et la découverte de multiples fins.', ''),
(18, 'Doom Eternal', '2020-03-20', 'Doom Eternal est un jeu de tir à la première personne qui met les joueurs dans la peau du Doom Slayer, un guerrier implacable contre les forces démoniaques de l\'Enfer. Le jeu se distingue par son action effrénée, ses combats brutaux et ses déplacements rapides à travers des environnements infernaux et futuristes. Les joueurs doivent combattre une variété d\'ennemis démoniaques en utilisant un arsenal impressionnant d\'armes et de capacités, tout en explorant des niveaux complexes et en résolvant des énigmes pour progresser.', ''),
(19, 'Ghostrunner', '2020-10-27', 'Ghostrunner est un jeu d\'action à la première personne se déroulant dans un monde cyberpunk dystopique. Le joueur incarne un cyborg agile et puissant, capable de se déplacer à grande vitesse, de sauter entre les structures urbaines vertigineuses et de combattre des ennemis avec une précision mortelle. Le jeu se distingue par son gameplay rapide et fluide, où chaque mouvement compte pour esquiver les attaques ennemies et riposter avec des attaques tranchantes au katana. L\'accent est mis sur l\'agilité, la réactivité et la maîtrise des compétences pour surmonter les défis de niveaux conçus de manière complexe.', ''),
(20, 'Cyberpunk 2077', '2020-12-10', 'Cyberpunk 2077 est un jeu de rôle en monde ouvert se déroulant dans Night City, une mégalopole dystopique du futur où la technologie et la société sont intimement entrelacées. Le joueur incarne V, un mercenaire personnalisable, qui explore cette ville remplie de factions rivales, de cybernétique avancée et de conspirations politiques. Le jeu se distingue par son immersion dans un univers cyberpunk riche en détails, ses choix moraux impactants, et ses missions variées qui peuvent être abordées de multiples façons. Malgré des problèmes techniques lors de sa sortie, Cyberpunk 2077 offre une expérience de jeu ambitieuse avec une histoire profonde et des personnages captivants.', ''),
(21, 'Ghost of Tsushima', '2020-07-17', 'Ghost of Tsushima est un jeu d\'action-aventure développé par Sucker Punch Productions, exclusif à la console PlayStation. Le joueur incarne Jin Sakai, un samouraï en quête de vengeance lors de l\'invasion mongole de l\'île de Tsushima au Japon médiéval. Le jeu se distingue par ses paysages magnifiques, sa direction artistique immersive et son gameplay mélangeant combat au sabre, furtivité et exploration. L\'exploration de l\'île de Tsushima est libre et le joueur peut choisir d\'aborder les missions de manière directe ou discrète, influençant ainsi l\'histoire et les relations de Jin avec les habitants et les factions locales. Le jeu est également salué pour son ambiance et son respect de la culture japonaise, avec des éléments historiques et culturels intégrés dans l\'expérience de jeu.', ''),
(22, 'Baldur\'s Gate 3', '2020-10-06', 'Baldur\'s Gate 3 est un jeu de rôle développé par Larian Studios, basé sur l\'univers de Donjons et Dragons et situé dans les Royaumes Oubliés. Le joueur incarne un personnage personnalisable, affecté par une force sinistre connue sous le nom de Nautiloid, et doit naviguer dans un monde de fantasy riche en dangers et en opportunités. Le jeu combine exploration en vue isométrique, combats tactiques au tour par tour, et interactions avec des personnages non-joueurs variés, chacun ayant des motivations et des histoires uniques. Comme dans les précédents jeux de la série, les choix moraux du joueur ont un impact significatif sur le déroulement de l\'histoire et sur le monde qui l\'entoure.', ''),
(23, 'Grand Theft Auto V', '2013-09-17', 'Grand Theft Auto V (GTA V) est un jeu d\'action-aventure en monde ouvert développé par Rockstar North. Le jeu se déroule dans la ville fictive de Los Santos (inspirée de Los Angeles) et suit les histoires entrecroisées de trois personnages principaux : Michael, un ancien braqueur de banques, Trevor, un psychopathe imprévisible, et Franklin, un jeune escroc ambitieux. Les joueurs peuvent librement alterner entre ces trois protagonistes pour accomplir des missions variées, allant des braquages spectaculaires aux activités quotidiennes. GTA V est acclamé pour son vaste monde ouvert, sa narration complexe, et ses nombreux contenus additionnels en ligne.', ''),
(24, 'Grand Theft Auto IV', '2008-04-29', 'Grand Theft Auto IV (GTA IV) est un jeu d\'action-aventure en monde ouvert développé par Rockstar North. Le joueur incarne Niko Bellic, un vétéran de guerre d\'Europe de l\'Est qui vient à Liberty City (inspirée de New York) en quête du rêve américain, mais se retrouve rapidement plongé dans un monde de crime et de corruption. Le jeu offre une vaste liberté d\'exploration et de nombreuses activités, des missions principales aux quêtes secondaires, dans un environnement urbain vivant et détaillé. GTA IV est salué pour son histoire immersive, ses personnages bien développés, et ses graphismes impressionnants.', ''),
(25, 'Ori and the Will of the Wisps', '2020-03-11', 'Ori and the Will of the Wisps est un jeu de plateforme et de metroidvania développé par Moon Studios. Les joueurs contrôlent Ori, un esprit gardien, dans une quête émotive à travers un monde magnifique et dangereux pour découvrir sa véritable destinée et sauver ses amis. Le jeu se distingue par ses graphismes époustouflants, sa bande sonore envoûtante, et son gameplay fluide qui combine exploration, résolution d\'énigmes et combats dynamiques. Ori and the Will of the Wisps est acclamé pour son atmosphère immersive, sa narration touchante, et ses améliorations par rapport à son prédécesseur.', ''),
(26, 'Sekiro: Shadows Die Twice', '2019-03-22', 'Sekiro: Shadows Die Twice est un jeu d\'action-aventure développé par FromSoftware, où le joueur incarne un shinobi nommé Wolf en quête de vengeance contre un clan samouraï qui l\'a trahi et kidnappé son seigneur. Le jeu se distingue par son système de combat exigeant qui repose sur la parade et la posture, ainsi que par son exploration de niveaux interconnectés remplis de dangers. Sekiro offre également des éléments de furtivité, permettant aux joueurs de planifier leurs attaques. Le jeu est salué pour sa difficulté élevée, ses combats de boss intenses et son immersion dans l\'ère Sengoku du Japon.', ''),
(27, 'Portal 2', '2012-04-19', 'Portal 2 est un jeu de réflexion en vue à la première personne développé par Valve, où le joueur incarne Chell, une testeur humaine dans les installations d\'Aperture Science. En utilisant le \"Portal Gun\", les joueurs résolvent des énigmes en créant des portails pour se déplacer à travers les niveaux et manipuler des objets. Le jeu introduit de nouveaux éléments de gameplay, tels que des gels modifiant les propriétés de surfaces et des lasers, et intègre une campagne coopérative unique où deux joueurs doivent collaborer pour résoudre des puzzles. Portal 2 est acclamé pour son écriture humoristique, ses personnages mémorables, et ses défis de réflexion inventifs.', '');

-- --------------------------------------------------------

--
-- Structure de la table `game_category`
--

DROP TABLE IF EXISTS `game_category`;
CREATE TABLE IF NOT EXISTS `game_category` (
  `_id_game` int NOT NULL,
  `_id_category` int NOT NULL,
  PRIMARY KEY (`_id_game`,`_id_category`),
  KEY `id_category` (`_id_category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `game_category`
--

INSERT INTO `game_category` (`_id_game`, `_id_category`) VALUES
(1, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(17, 1),
(18, 1),
(19, 1),
(20, 1),
(21, 1),
(22, 1),
(23, 1),
(24, 1),
(25, 1),
(27, 1),
(1, 2),
(3, 2),
(4, 2),
(5, 2),
(6, 2),
(7, 2),
(8, 2),
(9, 2),
(10, 2),
(11, 2),
(13, 2),
(14, 2),
(15, 2),
(16, 2),
(18, 2),
(21, 2),
(23, 2),
(24, 2),
(25, 2),
(27, 2),
(3, 3),
(11, 3),
(16, 3),
(18, 3),
(2, 4),
(6, 4),
(8, 4),
(1, 5),
(13, 5),
(14, 5),
(17, 5),
(27, 5),
(1, 6),
(19, 6),
(25, 6),
(26, 6),
(8, 7),
(13, 7),
(17, 7),
(5, 8),
(14, 8),
(23, 8),
(26, 8),
(1, 9),
(8, 9),
(9, 9),
(10, 9),
(12, 9),
(21, 9);

-- --------------------------------------------------------

--
-- Structure de la table `session`
--

DROP TABLE IF EXISTS `session`;
CREATE TABLE IF NOT EXISTS `session` (
  `id_session` int NOT NULL AUTO_INCREMENT,
  `time` time NOT NULL,
  `date` datetime NOT NULL,
  `_id_game` int NOT NULL,
  `_id_user` int NOT NULL,
  `_id_category` int NOT NULL,
  PRIMARY KEY (`id_session`),
  KEY `_id_game` (`_id_game`),
  KEY `_id_user` (`_id_user`),
  KEY `_id_category` (`_id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `session`
--

INSERT INTO `session` (`id_session`, `time`, `date`, `_id_game`, `_id_user`, `_id_category`) VALUES
(1, '12:34:56', '2024-06-27 10:15:00', 1, 1, 1),
(2, '08:15:30', '2024-06-26 14:30:00', 3, 2, 1),
(3, '09:45:10', '2024-06-25 16:45:00', 4, 3, 1),
(4, '11:23:45', '2024-06-24 18:00:00', 5, 4, 2),
(5, '07:12:55', '2024-06-23 20:15:00', 6, 5, 4),
(6, '13:14:22', '2024-06-22 09:30:00', 8, 6, 2),
(7, '15:46:33', '2024-06-21 11:45:00', 11, 7, 3),
(8, '10:25:47', '2024-06-20 13:00:00', 14, 8, 5),
(9, '14:34:12', '2024-06-19 15:15:00', 17, 9, 1),
(10, '16:55:59', '2024-06-18 17:30:00', 21, 10, 2),
(11, '14:20:15', '2024-06-17 09:45:00', 1, 11, 1),
(12, '08:10:45', '2024-06-16 11:00:00', 3, 12, 1),
(13, '17:55:30', '2024-06-15 12:15:00', 4, 1, 1),
(14, '13:45:00', '2024-06-14 13:30:00', 5, 2, 2),
(15, '09:30:20', '2024-06-13 14:45:00', 6, 3, 4),
(16, '10:20:10', '2024-06-12 16:00:00', 8, 4, 2),
(17, '07:50:05', '2024-06-11 17:15:00', 11, 5, 3),
(18, '12:10:30', '2024-06-10 18:30:00', 14, 6, 5),
(19, '01:51:54', '2024-06-27 00:00:00', 1, 12, 2),
(20, '05:56:35', '2024-06-27 00:00:00', 1, 12, 6),
(22, '11:30:50', '2024-06-06 13:30:00', 3, 10, 1),
(23, '13:55:10', '2024-06-05 14:45:00', 4, 11, 1),
(24, '14:45:35', '2024-06-04 16:00:00', 5, 12, 2),
(25, '09:20:20', '2024-06-03 17:15:00', 6, 1, 4),
(26, '10:10:15', '2024-06-02 18:30:00', 8, 2, 2),
(27, '07:40:25', '2024-06-01 09:45:00', 11, 3, 3),
(28, '12:30:55', '2024-05-31 11:00:00', 14, 4, 5),
(29, '16:10:45', '2024-05-30 12:15:00', 17, 5, 1),
(30, '15:05:20', '2024-05-29 13:30:00', 21, 6, 2),
(31, '06:25:35', '2024-05-28 14:45:00', 1, 7, 1),
(32, '11:40:10', '2024-05-27 16:00:00', 3, 8, 1),
(33, '13:15:50', '2024-05-26 17:15:00', 4, 9, 1),
(34, '14:05:45', '2024-05-25 18:30:00', 5, 10, 2),
(35, '09:50:15', '2024-05-24 09:45:00', 6, 11, 4),
(36, '10:35:10', '2024-05-23 11:00:00', 8, 12, 2),
(37, '07:55:05', '2024-05-22 12:15:00', 11, 1, 3),
(38, '12:45:35', '2024-05-21 13:30:00', 14, 2, 5),
(39, '16:30:20', '2024-05-20 14:45:00', 17, 3, 1),
(40, '15:25:10', '2024-05-19 16:00:00', 21, 4, 2),
(41, '06:15:25', '2024-05-18 17:15:00', 1, 5, 1),
(42, '11:05:45', '2024-05-17 18:30:00', 3, 6, 1),
(43, '13:25:30', '2024-05-16 09:45:00', 4, 7, 1),
(44, '14:15:10', '2024-05-15 11:00:00', 5, 8, 2),
(45, '09:35:55', '2024-05-14 12:15:00', 6, 9, 4),
(46, '10:45:25', '2024-05-13 13:30:00', 8, 10, 2),
(47, '07:35:50', '2024-05-12 14:45:00', 11, 11, 3),
(48, '12:20:15', '2024-05-11 16:00:00', 14, 12, 5),
(49, '16:55:45', '2024-05-10 17:15:00', 17, 1, 1),
(50, '15:50:20', '2024-05-09 18:30:00', 21, 2, 2),
(51, '06:35:10', '2024-05-08 09:45:00', 1, 3, 1),
(52, '11:15:55', '2024-05-07 11:00:00', 3, 4, 1),
(53, '13:40:25', '2024-05-06 12:15:00', 4, 5, 1),
(54, '14:25:50', '2024-05-05 13:30:00', 5, 6, 2),
(55, '09:15:35', '2024-05-04 14:45:00', 6, 7, 4),
(56, '10:55:10', '2024-05-03 16:00:00', 8, 8, 2),
(57, '07:20:15', '2024-05-02 17:15:00', 11, 9, 3),
(58, '12:50:05', '2024-05-01 18:30:00', 14, 10, 5),
(59, '16:40:25', '2024-04-30 09:45:00', 17, 11, 1),
(60, '15:10:35', '2024-04-29 11:00:00', 21, 12, 2),
(61, '06:10:50', '2024-04-28 12:15:00', 1, 1, 1),
(62, '11:25:35', '2024-04-27 13:30:00', 3, 2, 1),
(63, '13:55:45', '2024-04-26 14:45:00', 4, 3, 1),
(64, '14:35:25', '2024-04-25 16:00:00', 5, 4, 2),
(65, '09:40:20', '2024-04-24 17:15:00', 6, 5, 4),
(66, '10:15:10', '2024-04-23 18:30:00', 8, 6, 2),
(67, '07:25:55', '2024-04-22 09:45:00', 11, 7, 3),
(68, '12:05:35', '2024-04-21 11:00:00', 14, 8, 5),
(69, '16:30:15', '2024-04-20 12:15:00', 17, 9, 1),
(70, '15:55:45', '2024-04-19 13:30:00', 21, 10, 2),
(71, '06:45:20', '2024-04-18 14:45:00', 1, 11, 1),
(72, '11:35:10', '2024-04-17 16:00:00', 3, 12, 1),
(73, '13:25:05', '2024-04-16 17:15:00', 4, 1, 1),
(74, '14:15:30', '2024-04-15 18:30:00', 5, 2, 2),
(75, '09:10:55', '2024-04-14 09:45:00', 6, 3, 4),
(76, '10:35:35', '2024-04-13 11:00:00', 8, 4, 2),
(77, '07:55:45', '2024-04-12 12:15:00', 11, 5, 3),
(78, '12:15:20', '2024-04-11 13:30:00', 14, 6, 5),
(79, '16:45:10', '2024-04-10 14:45:00', 17, 7, 1),
(80, '15:50:55', '2024-04-09 16:00:00', 21, 8, 2),
(81, '06:35:35', '2024-04-08 17:15:00', 1, 9, 1),
(82, '11:15:20', '2024-04-07 18:30:00', 3, 10, 1),
(83, '13:10:25', '2024-04-06 09:45:00', 4, 11, 1),
(84, '14:55:50', '2024-04-05 11:00:00', 5, 12, 2),
(85, '09:05:05', '2024-04-04 12:15:00', 6, 1, 4),
(86, '10:45:35', '2024-04-03 13:30:00', 8, 2, 2),
(87, '07:20:55', '2024-04-02 14:45:00', 11, 3, 3),
(88, '12:55:10', '2024-04-01 16:00:00', 14, 4, 5),
(89, '16:30:35', '2024-03-31 17:15:00', 17, 5, 1),
(90, '15:15:45', '2024-03-30 18:30:00', 21, 6, 2),
(91, '06:25:20', '2024-03-29 09:45:00', 1, 7, 1),
(92, '11:55:50', '2024-03-28 11:00:00', 3, 8, 1),
(93, '13:35:35', '2024-03-27 12:15:00', 4, 9, 1),
(94, '14:25:25', '2024-03-26 13:30:00', 5, 10, 2),
(95, '09:55:45', '2024-03-25 14:45:00', 6, 11, 4),
(96, '10:20:15', '2024-03-24 16:00:00', 8, 12, 2),
(97, '07:30:10', '2024-03-23 17:15:00', 11, 1, 3),
(98, '12:40:05', '2024-03-22 18:30:00', 14, 2, 5),
(99, '16:55:20', '2024-03-21 09:45:00', 17, 3, 1),
(100, '15:05:50', '2024-03-20 11:00:00', 21, 4, 2),
(101, '06:10:35', '2024-03-19 12:15:00', 1, 5, 1),
(102, '11:35:45', '2024-03-18 13:30:00', 3, 6, 1),
(103, '13:45:25', '2024-03-17 14:45:00', 4, 7, 1),
(104, '14:55:10', '2024-03-16 16:00:00', 5, 8, 2),
(105, '09:50:20', '2024-03-15 17:15:00', 6, 9, 4),
(106, '10:40:45', '2024-03-14 18:30:00', 8, 10, 2),
(107, '07:35:55', '2024-03-13 09:45:00', 11, 11, 3),
(108, '12:15:05', '2024-03-12 11:00:00', 14, 12, 5),
(109, '16:30:50', '2024-03-11 12:15:00', 17, 1, 1),
(110, '15:25:35', '2024-03-10 13:30:00', 21, 2, 2);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'John Doe',
  `password` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `profile_picture` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nationality` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id_user`, `email`, `username`, `password`, `profile_picture`, `nationality`, `admin`) VALUES
(1, 'johndupond001@orange.fr', 'John Dupond', 'c940cca4fd8d2d8a618f4537229b44d80826733588ac36c31a160ca564d8dcb1', NULL, 'Francais', 0),
(2, 'lexiewilliams.05@gmail.com', 'Lexie Williams', '4cddbd268f651fc8cd0a8aa7e5537cfa53c89065361a5eb8995720a198ddf450', NULL, 'Americian', 0),
(3, 'aaron.oconnor@gmail.com', 'Aaron O\'Connor', '2261a0afd640867539f41b886e27d8bd34ef651f8a1d6c505ccadcda591038a9', NULL, 'Americian', 0),
(4, 'linda.smith27@yahoo.com', 'Linda Smith', '32c4373c5589a865ce64429af60ff86f32e290f6a08bc305906d1d02ac3e22fa', NULL, 'Americain', 0),
(5, 'mika.j@outlook.com', 'Michael Jones', 'eff120af2c06a240dffe76c93417e20247c976bb5f7dd36fcc234aa9e9785842', NULL, 'Americain', 0),
(6, 'davidgaming@gmail.com', 'David Miller', 'eeea396402ad2f91b26aa5d094efcffcc51f52d06cfda72166823647ef717459', NULL, 'Americain', 0),
(7, 'gabrielaaa99@outlook.com', 'Gabriella Diaz', 'c41a7f66b8d30f18148d587c96b41b6b82bda07655398d6f08daa93c858a7c5b', NULL, 'Espagnole', 0),
(8, 'ppierre@orange.fr', 'Pierre Petit', '303757515c232e58474cc12a45119a16e24836ac42acafd4522e47178dc18cd7', NULL, 'Francais', 0),
(9, 'antoniorusso@gamil.com', 'Antonio Russo', '53d7a5a916657474b9753c6db47135476c09ef6072e39161753c298eb5c6545b', NULL, 'Italien', 0),
(10, 'elvin.kaukau@gmail.com', 'Elvin Kauffmann', '6468279f37421d31c2fa7277b6c351ba3fd56e73a349b51a00e4a32807d8ef55', NULL, 'Francais', 0),
(11, 'anneuuuh@yahoo.com', 'Anne Passelegue', '178e90adefc9317077c7d983341f4e2bc0644334f3d62f74eca35f91e20c5b26', NULL, 'Francais', 0),
(12, 'sarured@gmail.com', 'sakured', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', NULL, 'Francais', 1);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `game_category`
--
ALTER TABLE `game_category`
  ADD CONSTRAINT `id_category` FOREIGN KEY (`_id_category`) REFERENCES `category` (`id_category`),
  ADD CONSTRAINT `id_game` FOREIGN KEY (`_id_game`) REFERENCES `game` (`id_game`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Contraintes pour la table `session`
--
ALTER TABLE `session`
  ADD CONSTRAINT `_id_category` FOREIGN KEY (`_id_category`) REFERENCES `category` (`id_category`),
  ADD CONSTRAINT `_id_game` FOREIGN KEY (`_id_game`) REFERENCES `game` (`id_game`),
  ADD CONSTRAINT `_id_user` FOREIGN KEY (`_id_user`) REFERENCES `user` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
