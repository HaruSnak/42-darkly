<div align="center">

# XSS Stored - Feedback
### Bypassing a client-side length limit to store a persistent XSS payload

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Stored (Persistent) Cross-Site Scripting** occurs when malicious input submitted by a user is saved server-side (in a database, a file, etc.) and later rendered to other visitors without proper sanitization. Unlike reflected XSS, the payload doesn't need to be in the URL — every visitor who views the affected page executes the attacker's script.

### ⚡ Quick Demo

Go to `?page=feedback`, open the DevTools console (F12), run:
```js
document.querySelector('textarea[name="mtxtMessage"]').removeAttribute('maxlength')
```
Then type `<img src=x onload="alert('XSS')">` in the Message field and submit.

### 📖 Approach

The `feedback` page (`?page=feedback`) has a form with a `Name` and a `Message` field; submissions are stored and displayed below the form for everyone to see.

I first tried injecting a raw `<script>alert(1)</script>` tag directly into the message field, but the browser did not execute it — feedback simply stopped rendering, suggesting the tag was stripped or broken by an escaping mechanism that doesn't apply to all HTML tags.

Both fields also enforced a client-side character limit (`maxlength="50"`), too short for a working payload. Using Developer Tools, I edited the `maxlength` attribute directly on the `<textarea>` element:

```html
<!-- before -->
<textarea name="mtxtMessage" cols="50" rows="3" maxlength="50"></textarea>
<!-- after -->
<textarea name="mtxtMessage" cols="50" rows="3" maxlength="42424242"></textarea>
```

With the length restriction removed, I switched from a `<script>` tag (filtered) to an event-handler based payload using an `<img>` tag with a broken `src`, so the `onload`/`onerror`-style handler still fires:

```html
<img src="fakeimage.jpg" onload="alert('Vous avez été piraté !')" />
```

I submitted this payload as the `Message` with any value in `Name`. As soon as the feedback list re-rendered the stored entry, the injected handler executed and the flag appeared.

**Payload used:**
`<img src="fakeimage.jpg" onload="alert('Vous avez été piraté !')" />` (submitted in the `Message` field, after removing the `maxlength` client-side restriction)

**Flag:** `0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e`

### 💥 Impact

A stored XSS on a public feedback wall means **every visitor** who loads the page — not just the attacker — executes the injected script. This can be used to steal session cookies, perform actions on behalf of any user who views the page (including an admin moderating feedback), redirect visitors to phishing pages, or silently deface/deliver malware through the site. It's more severe than a reflected XSS because no crafted link needs to be clicked — simply visiting the page is enough.

### 🛡️ Remediation

To prevent Stored XSS:
- **Server-side validation**: Never rely on a client-side `maxlength` — enforce length and character limits on the server as well.
- **Output Encoding**: HTML-encode all user-submitted content before rendering it back (convert `<`, `>`, `"`, `'` to their HTML entities), for every tag and attribute, not just `<script>`.
- **Sanitize / strip dangerous attributes**: If any HTML is allowed at all, use an allowlist-based sanitizer that strips event-handler attributes (`onload`, `onerror`, `onclick`, ...) rather than trying to blocklist specific tags.
- **Content Security Policy (CSP)**: Restrict inline script/event-handler execution to reduce impact even if a payload slips through.

### 🔗 Resources

- [OWASP - Stored XSS](https://owasp.org/www-community/attacks/xss/)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Cross-Site Scripting stocké (persistant)** survient lorsqu'une entrée malveillante soumise par un utilisateur est enregistrée côté serveur (base de données, fichier, etc.) puis réaffichée à d'autres visiteurs sans être correctement nettoyée. Contrairement à la XSS réfléchie, le payload n'a pas besoin d'être dans l'URL — chaque visiteur qui consulte la page affectée exécute le script de l'attaquant.

### ⚡ Démo rapide

Aller sur `?page=feedback`, ouvrir la console DevTools (F12), lancer :
```js
document.querySelector('textarea[name="mtxtMessage"]').removeAttribute('maxlength')
```
Puis taper `<img src=x onload="alert('XSS')">` dans le champ Message et soumettre.

### 📖 Approche

La page `feedback` (`?page=feedback`) contient un formulaire avec les champs `Name` et `Message` ; les soumissions sont stockées et affichées sous le formulaire pour tout le monde.

J'ai d'abord essayé d'injecter directement une balise `<script>alert(1)</script>` dans le champ message, mais le navigateur ne l'a pas exécutée — la liste des feedbacks ne s'affichait plus, ce qui suggère que la balise était filtrée ou cassait un mécanisme d'échappement qui ne s'applique pas à toutes les balises HTML.

Les deux champs imposaient aussi une limite de caractères côté client (`maxlength="50"`), trop courte pour un payload fonctionnel. Avec les outils de développement, j'ai modifié directement l'attribut `maxlength` de la balise `<textarea>` :

```html
<!-- avant -->
<textarea name="mtxtMessage" cols="50" rows="3" maxlength="50"></textarea>
<!-- après -->
<textarea name="mtxtMessage" cols="50" rows="3" maxlength="42424242"></textarea>
```

Une fois la limite de longueur supprimée, j'ai remplacé la balise `<script>` (filtrée) par un payload basé sur un gestionnaire d'évènement, via une balise `<img>` avec un `src` invalide pour déclencher le handler :

```html
<img src="fakeimage.jpg" onload="alert('Vous avez été piraté !')" />
```

J'ai soumis ce payload comme `Message` avec une valeur quelconque dans `Name`. Dès que la liste des feedbacks a réaffiché l'entrée stockée, le handler injecté s'est exécuté et le flag est apparu.

**Payload utilisé :**
`<img src="fakeimage.jpg" onload="alert('Vous avez été piraté !')" />` (soumis dans le champ `Message`, après suppression de la restriction `maxlength` côté client)

**Flag :** `0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e`

### 💥 Impact

Une XSS stockée sur un mur de feedback public signifie que **chaque visiteur** qui charge la page — pas seulement l'attaquant — exécute le script injecté. Cela peut être utilisé pour voler des cookies de session, effectuer des actions au nom de n'importe quel utilisateur consultant la page (y compris un admin qui modère les feedbacks), rediriger les visiteurs vers des pages de phishing, ou défigurer/diffuser silencieusement un malware via le site. C'est plus grave qu'une XSS réfléchie car aucun lien piégé n'a besoin d'être cliqué — visiter la page suffit.

### 🛡️ Remédiation

Pour corriger cela :
- **Validation côté serveur** : Ne jamais se fier à un `maxlength` côté client — appliquer aussi les limites de longueur et de caractères côté serveur.
- **Encodage de sortie** : Encoder en HTML tout contenu soumis par l'utilisateur avant de le réafficher (convertir `<`, `>`, `"`, `'` en entités HTML), pour toutes les balises et attributs, pas seulement `<script>`.
- **Sanitizer / retirer les attributs dangereux** : Si du HTML doit être autorisé, utiliser un sanitizer basé sur une liste blanche qui retire les attributs de gestion d'évènements (`onload`, `onerror`, `onclick`, ...) plutôt que de bloquer seulement certaines balises.
- **Content Security Policy (CSP)** : Restreindre l'exécution de scripts/handlers inline pour réduire l'impact même si un payload passe au travers.

### 🔗 Sources

- [OWASP - Stored XSS](https://owasp.org/www-community/attacks/xss/)

</details>
