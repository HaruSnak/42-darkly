<div align="center">

# HTTP Header Manipulation - Copyright
### Spoofing the Referer and User-Agent headers with curl to bypass an access check

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**HTTP Header Manipulation** involves modifying the headers sent in an HTTP request. Web applications sometimes rely on these headers (like `User-Agent`, `Referer`, or `X-Forwarded-For`) for security checks, tracking, or logic. Since these headers are completely controlled by the client, relying on them for sensitive operations is a vulnerability — and `curl` makes them trivial to spoof, in particular the `Referer` header which cannot easily be forged from a plain browser navigation.

### ⚡ Quick Demo

```bash
curl -s -A "ft_bornToSec" --referer "https://www.nsa.gov/" "http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

### 📖 Approach

While exploring the main page, I found a link in the footer leading to a "Copyright" page at:
```
http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```
This page just displays a short description of an albatross with a picture. Inspecting the page's source code revealed two HTML comments giving clues:
1. One suggesting the request should "come from" `https://www.nsa.gov/`.
2. Another suggesting the browser should identify itself as `ft_bornToSec`.

These clues map directly to the `Referer` and `User-Agent` HTTP headers. I used `curl` to forge both:

**Command used:**

```bash
curl -s -A "ft_bornToSec" --referer "https://www.nsa.gov/" "http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag
```

**Explanation:**
- `-A "ft_bornToSec"`: Sets the `User-Agent` header.
- `--referer "https://www.nsa.gov/"`: Sets the `Referer` header.
- `| grep flag`: Filters the response to show the line containing the flag.

**Flag:** `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

> Note: this is the same flag as `[SQLi]Images` — this specific VM protects that particular secret behind two different vulnerabilities (this header check, and the SQL injection). It's not a documentation mistake, both exploits legitimately return it.

### 🎯 Benefit

Bypassing this check with forged headers demonstrates that an attacker can reach content the developer believed was gated behind a plausibility check ("only a specific automated tool from a specific origin should reach this"), without any credentials. In a real system, header-based checks are sometimes (wrongly) used to hide internal/staging pages, admin tooling, or debug endpoints from casual users — spoofing them with a one-line `curl` command defeats that "protection" entirely and grants the same access as a legitimate, trusted caller.

### 🛡️ Remediation

To fix this:
- **Do not trust client headers**: Never use `User-Agent` or `Referer` headers for authentication or authorization decisions, as they are trivially spoofed with tools like `curl`.
- **Use proper authentication**: Implement robust session management and access controls instead of header-based checks.

### 🔗 Resources

- [OWASP - Secure Headers Project](https://owasp.org/www-project-secure-headers/)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

La **manipulation d'en-têtes HTTP** consiste à modifier les champs d'en-tête d'une requête HTTP. Les applications web s'appuient parfois sur ces en-têtes (comme `User-Agent`, `Referer` ou `X-Forwarded-For`) pour des vérifications de sécurité ou de logique. Comme ces en-têtes sont entièrement contrôlés par le client, s'y fier pour des opérations sensibles constitue une vulnérabilité — et `curl` permet de les usurper trivialement, en particulier le `Referer` qui ne peut pas être falsifié facilement depuis une simple navigation au navigateur.

### ⚡ Démo rapide

```bash
curl -s -A "ft_bornToSec" --referer "https://www.nsa.gov/" "http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

### 📖 Approche

En explorant la page principale, j'ai trouvé un lien dans le pied de page menant à une page "Copyright" :
```
http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```
Cette page affiche juste une courte description d'un albatros avec une image. En inspectant le code source de la page, j'ai trouvé deux commentaires HTML donnant des indices :
1. L'un suggérant que la requête doit "venir de" `https://www.nsa.gov/`.
2. L'autre suggérant que le navigateur doit s'identifier comme `ft_bornToSec`.

Ces indices font directement référence aux en-têtes HTTP `Referer` et `User-Agent`. J'ai utilisé `curl` pour forger les deux :

**Commande utilisée :**

```bash
curl -s -A "ft_bornToSec" --referer "https://www.nsa.gov/" "http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag
```

**Explication :**
- `-A "ft_bornToSec"` : Modifie le `User-Agent`.
- `--referer "https://www.nsa.gov/"` : Modifie le `Referer`.
- `| grep flag` : Filtre la réponse pour afficher la ligne contenant le flag.

**Flag :** `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

> Remarque : c'est le même flag que `[SQLi]Images` — sur ce VM précis, ce secret est protégé derrière deux failles différentes (cette vérification d'en-têtes, et l'injection SQL). Ce n'est pas une erreur de documentation, les deux exploits renvoient légitimement ce flag.

### 🎯 Bénéfice

Contourner cette vérification avec des en-têtes falsifiés démontre qu'un attaquant peut atteindre un contenu que le développeur pensait protéger par un contrôle de plausibilité ("seul un outil automatisé précis, depuis une origine précise, doit atteindre ceci"), sans aucun identifiant. Sur un système réel, des vérifications basées sur les en-têtes sont parfois (à tort) utilisées pour cacher des pages internes/de staging, des outils d'administration, ou des endpoints de debug aux utilisateurs occasionnels — les usurper avec une simple commande `curl` défait entièrement cette "protection" et donne le même accès qu'un appelant légitime et de confiance.

### 🛡️ Remédiation

Pour corriger cela :
- **Ne pas faire confiance aux en-têtes clients** : Ne jamais utiliser `User-Agent` ou `Referer` pour l'authentification ou l'autorisation, car ils sont trivialement falsifiables avec des outils comme `curl`.
- **Authentification robuste** : Utiliser une gestion de session et des contrôles d'accès solides plutôt que des vérifications basées sur les en-têtes.

### 🔗 Sources

- [OWASP - Secure Headers Project](https://owasp.org/www-project-secure-headers/)

</details>
