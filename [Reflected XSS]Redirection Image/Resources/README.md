<div align="center">

# Reflected XSS - Redirection Image
### Injecting malicious scripts via URL parameters

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Reflected Cross-Site Scripting (Reflected XSS)** arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way. The attacker can use this to inject malicious scripts (JavaScript) that are executed in the browser of any user who clicks on a crafted link.

### 📖 Approach

For this vulnerability, I noticed redirection links at the bottom of the page (Twitter, Facebook, Instagram). These links used a `site=` parameter in the URL. I suspected this parameter might be vulnerable to XSS.

I modified the URL to inject a JavaScript payload instead of a valid site URL. By setting the `site` parameter to `<script>alert(1)</script>`, the application reflected this input directly into the page without sanitization, executing the script and revealing the flag.

**Payload used:**
`http://X.X.X.X/?page=redirect&site=<script>alert(1)</script>`

**Flag:** `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3`

### 🛡️ Remediation

To prevent Reflected XSS:
- **Input Validation**: Validate all input against a strict allowlist.
- **Output Encoding**: Encode user input before rendering it in the browser (e.g., convert `<` to `&lt;`).
- **Content Security Policy (CSP)**: Implement CSP to restrict where scripts can be loaded from.

### 🔗 Resources

- [OWASP - Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Cross-Site Scripting réfléchi (Reflected XSS)** survient lorsqu'une application reçoit des données dans une requête HTTP et inclut ces données dans la réponse immédiate de manière non sécurisée. L'attaquant peut utiliser ces données pour injecter des scripts malveillants (JavaScript) qui sont exécutés dans le navigateur de tout utilisateur cliquant sur un lien piégé.

### 📖 Approche

Pour cette faille, j'ai remarqué des liens de redirection au bas de la page utilisant un paramètre `site=` dans l'URL. J'ai soupçonné que ce paramètre pouvait être vulnérable aux XSS.

J'ai modifié l'URL pour injecter une charge utile JavaScript au lieu d'une URL de site valide. En définissant le paramètre `site` sur `<script>alert(1)</script>`, l'application a renvoyé cette entrée directement dans la page sans la nettoyer, exécutant le script et révélant le flag.

**Payload utilisé :**
`http://X.X.X.X/?page=redirect&site=<script>alert(1)</script>`

**Flag :** `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3`

### 🛡️ Remédiation

Pour corriger cela :
- **Validation des entrées** : Valider toutes les entrées par rapport à une liste blanche stricte.
- **Encodage de sortie** : Encoder les entrées utilisateur avant de les afficher dans le navigateur.
- **Content Security Policy (CSP)** : Mettre en œuvre CSP pour restreindre les sources de scripts.

### 🔗 Sources

- [OWASP - Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)

</details>