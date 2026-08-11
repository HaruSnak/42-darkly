<div align="center">

# Robots.txt - Hidden
### Crawling hidden directories discovered via robots.txt

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

The **robots.txt** file is a standard used by websites to communicate with web crawlers and other web robots. It specifies which areas of the website should not be processed or scanned. However, since this file is publicly accessible and its directives are voluntary, it can inadvertently reveal the location of sensitive or hidden directories to attackers.

**Sensitive Information Disclosure** via `robots.txt` occurs when an administrator lists private or hidden directories in the `robots.txt` file to prevent search engines from indexing them. While this stops honest bots, it serves as a roadmap for attackers to find hidden content that might not be properly secured.

### ⚡ Quick Demo

```bash
sed -i 's/X.X.X.X/<VM_IP>/' spider_darkly.py   # edit the target IP first
pip install scrapy
scrapy runspider spider_darkly.py -o output.json
cat output.json
```

### 📖 Approach

I checked `http://X.X.X.X/robots.txt` and found a disallowed entry: `/.hidden`. Accessing this directory revealed a massive structure of nested subdirectories and files, making manual exploration impossible.

To automate the search, I used **Scrapy**, a Python framework for web crawling. I wrote a spider to recursively traverse the directory structure and read the contents of all `README` files found, until it discovered the flag.

**Command used:**

```bash
scrapy runspider spider_darkly.py -o output.json
```

**Content of `spider_darkly.py` (concept):**
A script that follows links recursively and checks for the flag pattern in file contents.

[
{"flag": "Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466", "url": "http://X.X.X.X/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README"}
]

**Flag:** `d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466`

### 🎯 Benefit

Beyond the single flag, mapping the whole `.hidden` tree gives the attacker full visibility over content the administrator only tried to hide "by obscurity" instead of actually protecting it. This kind of reconnaissance regularly uncovers backup files, leftover debug scripts, or old versions of the application that were never meant to be public but are just as accessible as the flag once you know the path — turning a small crawl into a much wider information-disclosure surface.

### 🛡️ Remediation

To prevent this:
- **Security by Obscurity is not Security**: Do not rely on hidden folder names or `robots.txt` to secure sensitive content.
- **Access Control**: Use proper authentication (.htaccess, permissions) to restrict access to internal directories.
- **Do not list sensitive paths**: Avoid listing sensitive hidden paths in `robots.txt`.

### 🔗 Resources

- [Scrapy Documentation](https://docs.scrapy.org/en/latest/topics/spiders.html)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le fichier **robots.txt** est un standard utilisé par les sites web pour communiquer avec les robots d'indexation (crawlers). Il spécifie quelles zones du site ne doivent pas être traitées ou scannées. Cependant, comme ce fichier est accessible publiquement et que ses directives sont volontaires, il peut involontairement révéler l'emplacement de répertoires sensibles ou cachés aux attaquants.

La **divulgation d'informations sensibles** via `robots.txt` se produit lorsqu'un administrateur liste des répertoires privés ou cachés dans le fichier `robots.txt` pour empêcher les moteurs de recherche de les indexer. Bien que cela arrête les robots honnêtes, cela sert de carte pour les attaquants afin de trouver du contenu caché qui pourrait ne pas être correctement sécurisé.

### ⚡ Démo rapide

```bash
sed -i 's/X.X.X.X/<IP_VM>/' spider_darkly.py   # renseigner l'IP cible d'abord
pip install scrapy
scrapy runspider spider_darkly.py -o output.json
cat output.json
```

### 📖 Approche

J'ai vérifié `http://X.X.X.X/robots.txt` et j'ai trouvé une entrée interdite : `/.hidden`. L'accès à ce répertoire a révélé une structure massive de sous-répertoires et de fichiers imbriqués, rendant l'exploration manuelle impossible.

Pour automatiser la recherche, j'ai utilisé **Scrapy**, un framework Python pour le web crawling. J'ai écrit un spider pour parcourir récursivement la structure des répertoires et lire le contenu de tous les fichiers `README` trouvés, jusqu'à découvrir le flag.

**Commande utilisée :**

```bash
scrapy runspider spider_darkly.py -o output.json
```

**Concept de `spider_darkly.py` :**
Un script qui suit les liens récursivement et vérifie la présence du flag dans le contenu des fichiers.

[
{"flag": "Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466", "url": "http://X.X.X.X/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README"}
]

**Flag :** `d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466`

### 🎯 Bénéfice

Au-delà du simple flag, cartographier toute l'arborescence `.hidden` donne à l'attaquant une visibilité complète sur du contenu que l'administrateur a seulement tenté de cacher "par obscurité" plutôt que de réellement protéger. Ce type de reconnaissance révèle régulièrement des fichiers de sauvegarde, des scripts de debug oubliés, ou d'anciennes versions de l'application qui n'étaient pas censées être publiques mais restent tout aussi accessibles que le flag une fois le chemin connu — transformant un simple crawl en une surface bien plus large de divulgation d'informations.

### 🛡️ Remédiation

Pour corriger cela :
- **La sécurité par l'obscurité n'est pas de la sécurité** : Ne pas compter sur des noms de dossiers cachés ou `robots.txt` pour sécuriser le contenu.
- **Contrôle d'accès** : Utiliser une authentification appropriée (.htaccess, permissions) pour restreindre l'accès aux répertoires internes.
- **Ne pas lister les chemins sensibles** : Éviter de lister des chemins sensibles dans `robots.txt`.

### 🔗 Sources

- [Documentation Scrapy](https://docs.scrapy.org/en/latest/topics/spiders.html)

</details>