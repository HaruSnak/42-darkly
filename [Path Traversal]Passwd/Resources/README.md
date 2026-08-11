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

### ⚡ Quick Demo

Open directly in the browser:
```
http://X.X.X.X/?page=../../../../../../../etc/passwd
```

### 📖 Approach

The site uses the `?page=` parameter to load content. I suspected a traversal vulnerability and attempted to access `/etc/passwd`, a standard Linux file containing user information.

I repeatedly added `../` to move up the directory tree until I reached the root, and then navigated to `etc/passwd`.

**Payload used:**
`http://X.X.X.X/?page=../../../../../../../etc/passwd`

**Flag:** `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

### 💥 Impact

Reading `/etc/passwd` is mostly a proof-of-concept here, but the same unvalidated `page` parameter can reach **any file readable by the web server user** — application source code (exposing further vulnerabilities or hardcoded secrets), configuration files, private keys, or log files. If the target also runs other services on the same host, this can leak credentials for those services too. Combined with a way to write attacker-controlled content to disk (log poisoning, an upload feature, session files), this class of bug commonly escalates into full **Remote Code Execution**.

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

### ⚡ Démo rapide

Ouvrir directement dans le navigateur :
```
http://X.X.X.X/?page=../../../../../../../etc/passwd
```

### 📖 Approche

Le site utilise le paramètre `?page=` pour charger du contenu. J'ai suspecté une vulnérabilité de ce type et j'ai tenté d'accéder à `/etc/passwd`, un fichier standard sous Linux contenant les informations des utilisateurs.

J'ai ajouté plusieurs fois `../` pour remonter jusqu'à la racine du système, puis j'ai navigué vers `etc/passwd`.

**Payload utilisé :**
`http://X.X.X.X/?page=../../../../../../../etc/passwd`

**Flag :** `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

### 💥 Impact

Lire `/etc/passwd` n'est ici surtout qu'une preuve de concept, mais le même paramètre `page` non validé peut atteindre **n'importe quel fichier accessible par l'utilisateur du serveur web** : code source de l'application (exposant d'autres failles ou des secrets en dur), fichiers de configuration, clés privées, ou fichiers de logs. Si la cible héberge d'autres services sur la même machine, cela peut aussi divulguer leurs identifiants. Combinée à un moyen d'écrire du contenu contrôlé par l'attaquant sur le disque (log poisoning, fonctionnalité d'upload, fichiers de session), ce type de faille dégénère fréquemment en **exécution de code à distance (RCE)** complète.

### 🛡️ Remédiation

Pour corriger cela :
- **Nettoyer les entrées** : Supprimer les caractères `..`, `/` et `\` des entrées utilisateur.
- **Utiliser `basename()`** : Si l'entrée est utilisée pour un nom de fichier, utiliser `basename()` pour ne récupérer que le nom sans le chemin.
- **Environnement restreint (Chroot)** : Exécuter le serveur web dans un environnement "chrooté" pour limiter son accès au système de fichiers.

### 🔗 Sources

- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

</details>
