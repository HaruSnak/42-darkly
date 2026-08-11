<div align="center">

# Brute Force - Login
### Testing for weak passwords using automated tools

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Brute Force** is an attack method that involves systematic checking of all possible keys or passwords until the correct one is found. In a web context, it typically means attempting to guess a user's password by automating login attempts with a large list of common passwords or random combinations.

### ⚡ Quick Demo

```bash
echo -n admin > user.txt && echo -n shadow > pass.txt
hydra -f -L user.txt -P pass.txt X.X.X.X http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=WrongAnswer"
```
> Tip: `rockyou.txt` has 14M+ entries — running it live can take a long time depending on where the password sits. For a fast on-stage demo, use a 1-line wordlist containing the already-known password (`shadow`) as above; keep the full `rockyou.txt` run as evidence in a terminal recording/screenshot instead.

### 📖 Approach

For this vulnerability, I first manually checked for clues on the site but found nothing. I then decided to test if a brute force attack was possible. Using **Hydra**, a popular password cracking tool, and a password list from Kaggle (thank you community!), I attempted to crack the login form.

I encountered a challenge realizing that the form used a GET request instead of POST, and the parameters were slightly tricky. After correcting my syntax to use `http-get-form` and specifying the correct failure string, I successfully found the password.

**Command used:**

```bash
hydra -f -l admin -P /home/haru/dev/rockyou.txt X.X.X.X http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=WrongAnswer"
```

**Explanation:**
- `-f`: Stop as soon as a valid pair is found.
- `-l admin`: Target the user 'admin'.
- `-P ...`: Path to the password list (rockyou.txt).
- `http-get-form`: The method used by the login form.
- `"...:F=WrongAnswer"`: The parameters and the string determining a failed login attempt.

**Flag:** `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`

### 🎯 Benefit

Successfully brute-forcing the `admin` account grants **full administrative access** to the application, bypassing authentication entirely — no need to find any other flaw once valid credentials are obtained. It also demonstrates the real-world risk of **password reuse**: since `admin` is a common account name across services, a cracked password here could be tried again on other internal tools, email, or infrastructure the same person manages, widening the attacker's foothold far beyond this single site.

### 🛡️ Remediation

To prevent Brute Force attacks:
- **Rate Limiting**: Limit the number of login attempts from a single IP address (e.g., using Fail2Ban or Nginx limit_req).
- **Account Lockout**: Lock the account after a certain number of failed attempts.
- **CAPTCHA**: Implement CAPTCHA to prevent automated bots from submitting the form.

### 🔗 Resources

- [THC-Hydra GitHub](https://github.com/vanhauser-thc/thc-hydra)
- [Rockyou.txt (Kaggle)](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Brute Force** (ou attaque par force brute) est une méthode d'attaque qui consiste à vérifier systématiquement toutes les combinaisons possibles de mots de passe ou de clés jusqu'à trouver la bonne. Dans un contexte web, cela signifie souvent tenter de deviner le mot de passe d'un utilisateur en automatisant les essais avec une liste de mots de passe courants.

### ⚡ Démo rapide

```bash
echo -n admin > user.txt && echo -n shadow > pass.txt
hydra -f -L user.txt -P pass.txt X.X.X.X http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=WrongAnswer"
```
> Astuce : `rockyou.txt` fait 14M+ entrées — le lancer en direct peut prendre longtemps selon où se trouve le mot de passe dans le fichier. Pour une démo rapide devant l'évaluateur, utiliser une wordlist d'une ligne contenant le mot de passe déjà trouvé (`shadow`) comme ci-dessus ; garder le run complet sur `rockyou.txt` comme preuve dans un enregistrement de terminal/capture d'écran.

### 📖 Approche

Pour cette faille, j'ai d'abord cherché des indices sur le site manuellement, sans succès. J'ai alors décidé de tester une attaque par force brute. J'ai utilisé **Hydra**, un outil populaire pour le cassage de mots de passe, avec une liste de mots de passe provenant de la communauté Kaggle (merci à eux !).

J'ai rencontré quelques difficultés en réalisant que je devais utiliser une requête GET au lieu de POST, et en configurant correctement les paramètres de l'attaque. Après avoir corrigé ma commande pour utiliser `http-get-form` et spécifié le bon message d'erreur pour identifier les échecs, j'ai réussi à trouver le mot de passe.

**Commande utilisée :**

```bash
hydra -f -l admin -P /home/haru/dev/rockyou.txt X.X.X.X http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=WrongAnswer"
```

**Explication :**
- `-f`: S'arrête dès qu'un résultat est trouvé.
- `-l admin`: Cible l'utilisateur 'admin'.
- `-P ...`: Chemin vers la liste de mots de passe (rockyou.txt).
- `http-get-form`: La méthode utilisée par le formulaire.
- `"...:F=WrongAnswer"`: Les paramètres et la chaîne de caractères indiquant un échec de connexion.

**Flag :** `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`

### 🎯 Bénéfice

Réussir à casser le compte `admin` par force brute donne un **accès administrateur complet** à l'application, en contournant entièrement l'authentification — plus besoin de trouver une autre faille une fois les identifiants valides obtenus. Cela illustre aussi le risque bien réel de la **réutilisation de mots de passe** : comme `admin` est un nom de compte courant sur de nombreux services, un mot de passe cassé ici pourrait être retesté sur d'autres outils internes, la messagerie, ou l'infrastructure gérée par la même personne, élargissant considérablement la portée de l'attaque au-delà de ce seul site.

### 🛡️ Remédiation

Pour se prémunir des attaques Brute Force :
- **Limitation de débit (Rate Limiting)** : Limiter le nombre de tentatives de connexion depuis une même IP (via Fail2Ban ou Nginx).
- **Verrouillage de compte** : Bloquer le compte après un certain nombre d'échecs.
- **CAPTCHA** : Mettre en place un CAPTCHA pour empêcher les robots de soumettre le formulaire.

### 🔗 Sources

- [THC-Hydra GitHub](https://github.com/vanhauser-thc/thc-hydra)
- [Rockyou.txt (Kaggle)](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)

</details>