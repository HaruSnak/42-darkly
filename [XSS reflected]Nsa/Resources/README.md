<div align="center">

# XSS Reflected - Nsa
### Bypassing src filtering with a data: URI to trigger a reflected XSS

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Reflected Cross-Site Scripting (Reflected XSS)** arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way. Here the flaw is reachable through the `data:` URI scheme: the browser can render `data:text/html;base64,...` as a full HTML document, so if a page reflects a user-controlled `src` parameter directly into a tag the browser dereferences (`<iframe>`, `<object>`, etc.), an attacker can smuggle an entire HTML/JS payload past filters that only check for file extensions or classic `<script>` tags.

Note: since 2018, modern browsers (Chrome, Firefox) **block top-level navigation** to a `data:` URI typed or clicked directly in the address bar, specifically to prevent this kind of abuse for phishing. That protection does not apply here, because the browser's top-level request is a normal `http://` URL (`?page=media&src=...`); the server embeds the attacker-controlled value as a *sub-resource* (e.g. inside an `<iframe src="...">`), which is a different, still-unrestricted code path.

### ⚡ Quick Demo

Open directly in the browser:
```
http://X.X.X.X/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

### 📖 Approach

I visited `/index.php?page=media&src=nsa`, a page that loads a resource based on the `src` GET parameter. I tried to control this parameter directly  passing values like `media.php` or other local paths did not work, suggesting some filtering or that the parameter isn't used as a simple file path.

I then suspected the value might be reflected raw into an HTML tag capable of rendering arbitrary content (e.g. an `<iframe src="...">`). To test this without triggering naive `<script>` filters, I encoded a payload as a `data:` URI. I base64-encoded `<script>alert(42)</script>`:

```bash
echo -n '<script>alert(42)</script>' | base64
# PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

I then requested the page with this data URI as the `src` value:

```
http://X.X.X.X/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

The browser rendered the decoded HTML document, executed the injected `<script>` tag, and the flag appeared on the page.

**Payload used:**
`data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=` (decodes to `<script>alert(42)</script>`)

**Flag:** `928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d`

### 🛡️ Remediation

To prevent this vulnerability:
- **Avoid reflecting user input**: Do not echo user-controlled parameters directly into the page whenever it can be avoided.
- **Sanitize / Filter input**: When reflection can't be avoided, sanitize and filter the input against dangerous patterns (e.g. reject or strip the `data:` scheme, `javascript:`, and other non-http(s) URI schemes), and use an allowlist of accepted schemes/values.
- **Escape output**: Use context-aware escaping functions before inserting any value into HTML attributes or tag content.
- **Content Security Policy (CSP)**: Restrict allowed sources for frames/scripts to reduce the impact of any remaining injection point.

### 🔗 Resources

- [OWASP - Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [MDN - data: URIs](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Cross-Site Scripting réfléchi (Reflected XSS)** survient lorsqu'une application reçoit des données dans une requête HTTP et les inclut dans la réponse immédiate de manière non sécurisée. Ici la faille passe par le schéma d'URI `data:` : le navigateur peut interpréter `data:text/html;base64,...` comme un document HTML complet. Si une page réinjecte un paramètre `src` contrôlé par l'utilisateur directement dans une balise que le navigateur va charger (`<iframe>`, `<object>`, etc.), un attaquant peut faire passer tout un payload HTML/JS en contournant des filtres qui ne vérifient que l'extension du fichier ou la présence littérale de `<script>`.

Remarque : depuis 2018, les navigateurs modernes (Chrome, Firefox) **bloquent la navigation de premier niveau** vers une URI `data:` tapée ou cliquée directement dans la barre d'adresse, spécifiquement pour empêcher ce genre d'abus à des fins de phishing. Cette protection ne s'applique pas ici, car la requête de premier niveau du navigateur est une URL `http://` normale (`?page=media&src=...`) ; le serveur intègre la valeur contrôlée par l'attaquant comme *sous-ressource* (par exemple dans un `<iframe src="...">`), ce qui emprunte un chemin de code différent et non restreint.

### ⚡ Démo rapide

Ouvrir directement dans le navigateur :
```
http://X.X.X.X/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

### 📖 Approche

J'ai visité `/index.php?page=media&src=nsa`, une page qui charge une ressource en fonction du paramètre GET `src`. J'ai essayé de contrôler ce paramètre directement des valeurs comme `media.php` ou d'autres chemins locaux ne fonctionnaient pas, ce qui suggère un filtrage ou que le paramètre n'est pas utilisé comme un simple chemin de fichier.

J'ai alors supposé que la valeur pouvait être réinjectée brute dans une balise HTML capable d'afficher du contenu arbitraire (par exemple un `<iframe src="...">`). Pour tester cela sans déclencher un filtre naïf sur `<script>`, j'ai encodé un payload sous forme d'URI `data:`. J'ai encodé `<script>alert(42)</script>` en base64 :

```bash
echo -n '<script>alert(42)</script>' | base64
# PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

J'ai ensuite requêté la page avec cette URI data comme valeur de `src` :

```
http://X.X.X.X/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

Le navigateur a interprété le document HTML décodé, exécuté la balise `<script>` injectée, et le flag est apparu sur la page.

**Payload utilisé :**
`data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=` (décodé : `<script>alert(42)</script>`)

**Flag :** `928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d`

### 🛡️ Remédiation

Pour corriger cela :
- **Éviter de réafficher les entrées utilisateur** : Ne pas réinjecter un paramètre contrôlé par l'utilisateur directement dans la page quand ça peut être évité.
- **Sanitizer / Filtrer les entrées** : Quand la réinjection est nécessaire, filtrer les entrées contre les motifs dangereux (par exemple rejeter ou supprimer le schéma `data:`, `javascript:`, et tout schéma d'URI non http(s)), et utiliser une liste blanche de schémas/valeurs acceptés.
- **Encoder la sortie** : Utiliser des fonctions d'échappement adaptées au contexte avant d'insérer une valeur dans un attribut HTML ou le contenu d'une balise.
- **Content Security Policy (CSP)** : Restreindre les sources autorisées pour les frames/scripts afin de réduire l'impact d'un point d'injection restant.

### 🔗 Sources

- [OWASP - Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [MDN - data: URIs](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data)

</details>
