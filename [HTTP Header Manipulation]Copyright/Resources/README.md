<div align="center">

# HTTP Header Manipulation - Copyright
### Altering HTTP headers to bypass access controls

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**HTTP Header Injection** or **Manipulation** involves modifying the headers sent in an HTTP request. Web applications sometimes rely on these headers (like `User-Agent`, `Referer`, or `X-Forwarded-For`) for security checks, tracking, or logic. Since these headers are completely controlled by the client, relying on them for sensitive operations is a vulnerability.

### 📖 Approach

For this challenge, I found clues on the "Copyright" page suggesting that to access the flag, I needed to "come from" `https://www.nsa.gov/` and use a specific browser `ft_bornToSec`. These requirements directly point to the `Referer` and `User-Agent` HTTP headers.

I used `curl` to send a request to the feedback page (or the page indicated by the challenge) with these specific headers modified. 

**Command used:**

```bash
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://192.168.56.102/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

**Explanation:**
- `-A "ft_bornToSec"`: Sets the `User-Agent` header.
- `-e "https://www.nsa.gov"`: Sets the `Referer` header.

**Flag:** `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

### 🛡️ Remediation

To fix this:
- **Do not trust client headers**: Never use `User-Agent` or `Referer` headers for authentication or authorization decisions, as they are easily spoofed.
- **Use proper authentication**: Implement robust session management and access controls instead.

### 🔗 Resources

- [OWASP - HTTP Headers](https://owasp.org/www-project-secure-headers/)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

L'**injection ou manipulation d'en-têtes HTTP** consiste à modifier les champs d'en-tête d'une requête HTTP. Les applications web s'appuient parfois sur ces en-têtes (comme `User-Agent`, `Referer` ou `X-Forwarded-For`) pour des vérifications de sécurité ou de logique. Comme ces en-têtes sont entièrement contrôlés par le client, s'y fier pour des opérations sensibles constitue une vulnérabilité.

### 📖 Approche

Pour ce défi, j'ai trouvé des indices sur la page "Copyright" indiquant que pour obtenir le flag, je devais "venir de" `https://www.nsa.gov/` et utiliser le navigateur `ft_bornToSec`. Ces indices font référence aux en-têtes HTTP `Referer` et `User-Agent`.

J'ai utilisé `curl` pour envoyer une requête avec ces en-têtes modifiés.

**Commande utilisée :**

```bash
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://192.168.56.102/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

**Explication :**
- `-A "ft_bornToSec"` : Modifie le `User-Agent`.
- `-e "https://www.nsa.gov"` : Modifie le `Referer` (l'URL de provenance).

**Flag :** `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

### 🛡️ Remédiation

Pour corriger cela :
- **Ne pas faire confiance aux en-têtes clients** : Ne jamais utiliser `User-Agent` ou `Referer` pour l'authentification ou l'autorisation, car ils sont falsifiables.
- **Authentification robuste** : Utiliser des méthodes fiables comme les sessions sécurisées.

### 🔗 Sources

- [OWASP - HTTP Headers](https://owasp.org/www-project-secure-headers/)

</details>
