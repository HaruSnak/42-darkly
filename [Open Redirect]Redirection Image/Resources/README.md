<div align="center">

# Open Redirect - Redirection Image
### Bypassing an unvalidated redirect parameter

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

An **Open Redirect** occurs when an application accepts a user-controlled parameter to build a redirect target without validating that the destination belongs to a trusted, expected set of values. The application blindly trusts whatever value is supplied and redirects the browser to it — no injection or script execution is required, just an unvalidated destination.

### ⚡ Quick Demo

Open directly in the browser:
```
http://X.X.X.X/index.php?page=redirect&site=abc
```

### 📖 Approach

The bottom of the page has social media icons (Facebook, Twitter, Instagram) built as anchor tags pointing to `index.php?page=redirect&site=<name>`, e.g.:

```html
<a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>
```

I tried replacing the `site` value with something the application never expected — not a script, just any arbitrary string (a full external URL, an empty value, or a random word):

```
http://X.X.X.X/index.php?page=redirect&site=https://youtube.com
http://X.X.X.X/index.php?page=redirect&site=
http://X.X.X.X/index.php?page=redirect&site=abc
```

In every case the server accepted the value without validating it against a whitelist of known destinations, and the page revealed the flag — confirming the redirect target isn't checked server-side.

**Payload used:**
Any arbitrary value for `site=` (e.g. `site=abc`) on `?page=redirect&site=...`

**Flag:** `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3`

### 🛡️ Remediation

To prevent this vulnerability:
- **Whitelist destinations**: Only allow redirects to a fixed, server-side list of known-safe values/URLs (e.g. map `facebook` → the real Facebook URL server-side, never trust a raw URL from the client).
- **Avoid passing full URLs as parameters**: Use internal identifiers instead of letting the client supply the destination directly.
- **Warn on external redirect**: If redirecting to arbitrary external content is required, show an interstitial warning page instead of redirecting silently.

### 🔗 Resources

- [OWASP - Unvalidated Redirects and Forwards](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Un **Open Redirect** survient lorsqu'une application accepte un paramètre contrôlé par l'utilisateur pour construire une redirection sans vérifier que la destination appartient à un ensemble de valeurs de confiance attendues. L'application fait aveuglément confiance à la valeur fournie et redirige le navigateur vers celle-ci — aucune injection ni exécution de script n'est nécessaire, juste une destination non validée.

### ⚡ Démo rapide

Ouvrir directement dans le navigateur :
```
http://X.X.X.X/index.php?page=redirect&site=abc
```

### 📖 Approche

En bas de page se trouvent des icônes de réseaux sociaux (Facebook, Twitter, Instagram) construites comme des balises `<a>` pointant vers `index.php?page=redirect&site=<nom>`, par exemple :

```html
<a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>
```

J'ai essayé de remplacer la valeur de `site` par quelque chose que l'application n'attendait pas — pas un script, simplement une chaîne arbitraire quelconque (une URL externe complète, une valeur vide, ou un mot au hasard) :

```
http://X.X.X.X/index.php?page=redirect&site=https://youtube.com
http://X.X.X.X/index.php?page=redirect&site=
http://X.X.X.X/index.php?page=redirect&site=abc
```

Dans tous les cas, le serveur a accepté la valeur sans la valider contre une liste blanche de destinations connues, et la page a révélé le flag — confirmant que la destination de la redirection n'est pas vérifiée côté serveur.

**Payload utilisé :**
N'importe quelle valeur arbitraire pour `site=` (ex : `site=abc`) sur `?page=redirect&site=...`

**Flag :** `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3`

### 🛡️ Remédiation

Pour corriger cela :
- **Liste blanche de destinations** : N'autoriser les redirections que vers une liste fixe et connue côté serveur (par exemple faire correspondre `facebook` à la vraie URL Facebook côté serveur, sans jamais faire confiance à une URL brute venant du client).
- **Éviter de passer des URLs complètes en paramètre** : Utiliser des identifiants internes plutôt que de laisser le client fournir directement la destination.
- **Avertir en cas de redirection externe** : Si une redirection vers un contenu externe arbitraire est nécessaire, afficher une page d'avertissement intermédiaire plutôt que de rediriger silencieusement.

### 🔗 Sources

- [OWASP - Unvalidated Redirects and Forwards](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)

</details>
