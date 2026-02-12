<div align="center">

# Local File Inclusion - Code Source
### Exploiting insecure file handling to view local files

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Local File Inclusion (LFI)** is a vulnerability where an application allows a user to include files present on the server through the web browser. This usually happens when an application uses user input to construct a file path for inclusion without proper validation.

### 📖 Approach

For this specific challenge, I examined the source code of the page and noticed a link that passed a file location or identifier as a parameter. By manipulating this parameter or simply following the link provided in the source code (which seemed to point to an internal file), I was able to access the flag.

The link in the source code was: `<a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f">`. Following this `?page=` parameter revealed the file content.

**Flag:** Found in the source code link or by accessing the page.

### 🛡️ Remediation

To prevent LFI:
- **Input Sanitization**: Strictly validate and sanitize all user inputs used in file paths.
- **Whitelist**: Use a whitelist of allowed files or IDs instead of directly using user input to construct file paths.
- **Disable `allow_url_include`**: in PHP configuration if not needed.

### 🔗 Resources

- [OWASP - Local File Inclusion](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

La **Local File Inclusion (LFI)** est une vulnérabilité permettant à un utilisateur d'inclure des fichiers présents sur le serveur via le navigateur. Cela se produit généralement lorsqu'une application utilise des entrées utilisateur pour construire un chemin de fichier sans validation appropriée.

### 📖 Approche

Pour ce challenge, j'ai examiné le code source de la page et j'ai remarqué un lien qui passait un identifiant de fichier en paramètre. Le lien semblait pointer vers une ressource interne.

Le lien dans le code source était : `<a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f">`. En suivant ce paramètre `?page=`, j'ai pu accéder au contenu caché.

**Flag :** Trouvé via le lien dans le code source.

### 🛡️ Remédiation

Pour corriger cela :
- **Validation des entrées** : Valider et nettoyer strictement toutes les entrées utilisateur utilisées dans les chemins de fichiers.
- **Liste blanche** : Utiliser une liste blanche de fichiers autorisés plutôt que d'utiliser directement l'entrée utilisateur.
- **Désactiver `allow_url_include`** : dans la configuration PHP si non nécessaire.

### 🔗 Sources

- [OWASP - Local File Inclusion](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)

</details>
