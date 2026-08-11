<div align="center">

# Privilege Escalation - Cookie
### Elevating privileges by modifying insecure cookies

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Privilege Escalation** is the act of exploiting a bug, design flaw, or configuration oversight in an operating system or software application to gain elevated access to resources that are normally protected from an application or user.  Specifically using **Cookies**, if an application trusts client-side cookies for role assignment (e.g., `admin=true`) without verifying them on the server, an attacker can simply modify the cookie to gain admin privileges.

### ⚡ Quick Demo

Open the DevTools console (F12) on any page of the site, run:
```js
document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09; path=/"
location.reload()
```

### 📖 Approach

While inspecting the network traffic (Developer Tools > Network), I noticed a cookie named `I_am_admin`. Its value was an MD5 hash: `68934a3e9455fa72420237eb05902327`.

I decoded this hash using an online tool (CrackStation) and found it corresponded to the string `false`. I deduced that to become admin, I needed the hash for `true`.
MD5("true") = `b326b5062b2f0e69046810717534cb09`.

I modified the cookie value in my browser to this new hash and refreshed the page. The application read the cookie, saw "true" (hashed), and granted me admin rights, revealing the flag.

**Method:**
1. Inspect cookies in Developer Tools.
2. Identify `I_am_admin` and decode its MD5 value (`false`).
3. Generate MD5 for `true`.
4. Replace the cookie value and refresh.

**Flag:** `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

### 💥 Impact

Since the privilege level is entirely determined by a client-controlled value that is never verified server-side, **any visitor can self-promote to administrator** in seconds, without knowing any password. This grants access to admin-only pages, data, or actions, and completely defeats the authentication/authorization model of the application. On a real system this could mean full account takeover, access to every user's private data, or the ability to modify site content.

### 🛡️ Remediation

To prevent this:
- **Server-Side Sessions**: Store session data on the server, not in client-side cookies.
- **Sign or Encrypt Cookies**: If cookies must store data, ensure they are cryptographically signed or encrypted so users cannot tamper with them.
- **Avoid Obvious Names**: Avoid using predictable logic like "I_am_admin=true".

### 🔗 Resources

- [CrackStation](https://crackstation.net/)
- [MD5 Hash Generator](https://www.md5hashgenerator.com/)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

L'**escalade de privilèges** est l'acte d'exploiter un bug ou une faille de conception pour obtenir un accès élevé à des ressources normalement protégées. En ce qui concerne les **cookies**, si une application fait confiance aux cookies stockés côté client pour définir les rôles (ex: `admin=true`) sans les vérifier côté serveur, un attaquant peut simplement modifier le cookie pour obtenir les privilèges d'administrateur.

### ⚡ Démo rapide

Ouvrir la console DevTools (F12) sur n'importe quelle page du site, lancer :
```js
document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09; path=/"
location.reload()
```

### 📖 Approche

En inspectant le trafic réseau, j'ai remarqué un cookie nommé `I_am_admin`. Sa valeur était un hash MD5: `68934a3e9455fa72420237eb05902327`.

J'ai décodé ce hash via un outil en ligne et j'ai trouvé qu'il correspondait à la chaîne `false`. J'ai déduit que pour devenir admin, il me fallait le hash de `true`.
MD5("true") = `b326b5062b2f0e69046810717534cb09`.

J'ai modifié la valeur du cookie dans mon navigateur par ce nouveau hash et j'ai rafraîchi la page. L'application a lu le cookie, a vu "true" (hashé), et m'a donné les droits d'admin et le flag.

**Méthode :**
1. Inspecter les cookies.
2. Identifier `I_am_admin` et décoder son MD5 (`false`).
3. Générer le MD5 de `true`.
4. Remplacer la valeur du cookie et rafraîchir.

**Flag :** `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

### 💥 Impact

Comme le niveau de privilège est entièrement déterminé par une valeur contrôlée côté client et jamais vérifiée côté serveur, **n'importe quel visiteur peut s'auto-promouvoir administrateur** en quelques secondes, sans connaître le moindre mot de passe. Cela donne accès aux pages, données ou actions réservées à l'admin, et casse complètement le modèle d'authentification/autorisation de l'application. Sur un système réel, cela peut signifier une prise de contrôle totale de compte, l'accès aux données privées de tous les utilisateurs, ou la modification du contenu du site.

### 🛡️ Remédiation

Pour corriger cela :
- **Sessions côté serveur** : Stocker les données de session sur le serveur, pas dans des cookies manipulables.
- **Signer/Chiffrer les cookies** : Si des données doivent être dans les cookies, les signer cryptographiquement pour empêcher leur modification.
- **Éviter la logique prévisible** : Ne pas utiliser de noms ou de valeurs évidents comme "I_am_admin".

### 🔗 Sources

- [CrackStation](https://crackstation.net/)
- [MD5 Hash Generator](https://www.md5hashgenerator.com/)

</details>