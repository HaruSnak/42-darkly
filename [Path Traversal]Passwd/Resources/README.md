<div align="center">

# Path Traversal - Passwd
### Navigating directory structures to access sensitive system files

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Path Traversal** (or Directory Traversal) is a vulnerability that allows an attacker to access files and directories that are stored outside the web root folder. By using "dot-dot-slash" (`../`) sequences, an attacker can navigate up the directory tree to access arbitrary files on the system, such as application code or sensitive operating system files.

### 📖 Approach

The site uses the `?page=` parameter to load content. I suspected a traversal vulnerability and attempted to access `/etc/passwd`, a standard Linux file containing user information.

I repeatedly added `../` to move up the directory tree until I reached the root, and then navigated to `etc/passwd`.

**Payload used:**
`http://X.X.X.X/?page=../../../../../../../etc/passwd`

**Flag:** `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

### 🛡️ Remediation

To prevent Path Traversal:
- **Sanitize Input**: Remove `..`, `/`, and `\` characters from user input.
- **Use `basename()`**: Logic that uses user input for filenames should filter it through functions like `basename()` to retrieve only the filename part.
- **Chrooted Jail**: Run the web server in a chrooted environment to limit access to the file system.

### 🔗 Resources

- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Path Traversal** (ou traversée de répertoire) est une vulnérabilité qui permet à un attaquant d'accéder à des fichiers et dossiers stockés en dehors de la racine du site web. En utilisant des séquences `../`, il est possible de remonter dans l'arborescence pour accéder à n'importe quel fichier du système.

### 📖 Approche

Le site utilise le paramètre `?page=` pour charger du contenu. J'ai suspecté une vulnérabilité de ce type et j'ai tenté d'accéder à `/etc/passwd`, un fichier standard sous Linux contenant les informations des utilisateurs.

J'ai ajouté plusieurs fois `../` pour remonter jusqu'à la racine du système, puis j'ai navigué vers `etc/passwd`.

**Payload utilisé :**
`http://X.X.X.X/?page=../../../../../../../etc/passwd`

**Flag :** `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

### 🛡️ Remédiation

Pour corriger cela :
- **Nettoyer les entrées** : Supprimer les caractères `..`, `/` et `\` des entrées utilisateur.
- **Utiliser `basename()`** : Si l'entrée est utilisée pour un nom de fichier, utiliser `basename()` pour ne récupérer que le nom sans le chemin.
- **Environnement restreint (Chroot)** : Exécuter le serveur web dans un environnement "chrooté" pour limiter son accès au système de fichiers.

### 🔗 Sources

- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

</details>
