<div align="center">

# Robots.txt - htpasswd
### Recovering credentials from exposed system files

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Sensitive File Exposure** occurs when an application inadvertently exposes sensitive files, such as configuration files, credential dumps (`.htpasswd`), or backup files. **.htpasswd** is an Apache file used to store usernames and passwords (hashed) for basic authentication. Protecting this file is critical as it allows attackers to attempt cracking the hashes.

### ⚡ Quick Demo

```bash
dirb http://X.X.X.X
# fetch the .htpasswd path it finds, crack the MD5 hash on crackstation.net,
# then log in at /admin with root:<cracked password>
```

### 📖 Approach

I ran `dirb`, a web content scanner, against the site to look for files and directories not linked from any page. It found an exposed `.htpasswd` file directly accessible over HTTP:

```bash
dirb http://X.X.X.X -o dirb.log
```

Fetching that file revealed its content: `root:437394baff5aa33daa618be47b75cb49`. The password was hashed using MD5 — a **weak, reversible-in-practice** algorithm (no salt, fast to brute-force with lookup tables).

I used an online hash cracker (CrackStation) to reverse the MD5 hash `437394baff5aa33daa618be47b75cb49`, which yielded the password `qwerty123@`.

The same `dirb` scan also found an administrative login page at `/admin`. Using the credentials `root` : `qwerty123@`, I successfully logged in and retrieved the flag.

**The potential problem:** the `.htpasswd` file — meant to be read only by the web server for HTTP Basic Auth — was placed inside the web root and served like any other static file, and its password was hashed with plain unsalted MD5 instead of a slow, salted algorithm. Either mistake alone defeats the purpose of the credential file; combined, they let an attacker go from "no access" to "valid admin session" using only public tools.

**Flag:** `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

### 🛡️ Remediation

To prevent this:
- **Restrict Access**: Ensure `.htpasswd` files are not accessible via web browser. Configure the web server (Apache/Nginx) to deny access to files starting with `.ht`.
- **Strong Hashing**: Do not use weak hashing algorithms like MD5. Use bcrypt, Argon2, or PBKDF2.

### 🔗 Resources

- [CrackStation](https://crackstation.net/)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

L'**exposition de fichiers sensibles** se produit lorsqu'une application expose par inadvertance des fichiers confidentiels, tels que des fichiers de configuration ou des fichiers de mots de passe (`.htpasswd`). **.htpasswd** est un fichier Apache utilisé pour stocker les noms d'utilisateurs et mots de passe (hachés). Protéger ce fichier est critique.

### ⚡ Démo rapide

```bash
dirb http://X.X.X.X
# récupérer le chemin .htpasswd trouvé, casser le hash MD5 sur crackstation.net,
# puis se connecter sur /admin avec root:<mot de passe cassé>
```

### 📖 Approche

J'ai lancé `dirb`, un scanner de contenu web, contre le site pour chercher des fichiers et répertoires non liés depuis les pages. Il a trouvé un fichier `.htpasswd` directement accessible en HTTP :

```bash
dirb http://X.X.X.X -o dirb.log
```

En récupérant ce fichier, j'ai obtenu son contenu : `root:437394baff5aa33daa618be47b75cb49`. Le mot de passe était haché en MD5 — un algorithme **faible et cassable en pratique** (pas de sel, cassable rapidement via des tables de correspondance).

J'ai utilisé un casseur de hash en ligne (CrackStation) pour inverser le hash MD5 `437394baff5aa33daa618be47b75cb49`, ce qui a donné le mot de passe `qwerty123@`.

Le même scan `dirb` a aussi trouvé une page de connexion administrative sur `/admin`. En utilisant les identifiants `root` : `qwerty123@`, je me suis connecté et j'ai récupéré le flag.

**Le problème potentiel :** le fichier `.htpasswd` — censé n'être lu que par le serveur web pour l'authentification HTTP Basic — était placé dans la racine web et servi comme n'importe quel fichier statique, et son mot de passe était haché en MD5 non salé au lieu d'un algorithme lent et salé. Chacune de ces deux erreurs suffit à elle seule à annuler l'intérêt du fichier de credentials ; combinées, elles permettent à un attaquant de passer de "aucun accès" à "session admin valide" avec uniquement des outils publics.

**Flag :** `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

### 🛡️ Remédiation

Pour corriger cela :
- **Restreindre l'accès** : S'assurer que les fichiers `.htpasswd` ne sont pas accessibles via le navigateur.
- **Hachage fort** : Ne pas utiliser d'algorithmes faibles comme MD5.

### 🔗 Sources

- [CrackStation](https://crackstation.net/)

</details>