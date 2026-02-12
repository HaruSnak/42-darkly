<div align="center">

# Insecure Logic Handling - Feedback
### Input Validation Bypass / Logic Flaw

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Insecure Logic Handling** vulnerabilities occur when an application's internal logic is flawed, allowing an attacker to manipulate the workflow or data processing in unintended ways. This can occur when the application fails to properly validate input constraints or handle specific edge cases, leading to information disclosure or other security breaches.

### 📖 Approach

This vulnerability was found in the "Feedback" or "Guestbook" form. I initially attempted to perform a Stored XSS attack, but by repeatedly experimenting with the feedback forms, I realized that submitting the form with only a single letter in the "Name" field revealed the flag.

The application seemingly checks for the existence of the feedback or performs a specific check on the name length but fails to handle the single-character case securely, defaulting to a debug or success state that outputs the flag.

**Payload used:**
A single letter in the `Name` field (e.g., `a`).

**Flag:** `0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e`

### 🛡️ Remediation

To prevent Insecure Logic Handling flaws:
- **Input Validation**: Enforce strict input validation rules (e.g., minimum and maximum length for names, allowed characters).
- **Secure Error Handling/Logic**: Ensure that edge cases (like short inputs) are handled gracefully and do not fail open or reveal sensitive information.
- **Code Review**: Audit the business logic to ensure that no specific input combinations trigger unintended debug paths or privileged information disclosure.

### 🔗 Resources

- [OWASP - Business Logic Vulnerabilities](https://owasp.org/www-community/vulnerabilities/Business_logic_vulnerability)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Les failles de **gestion logique non sécurisée** (Insecure Logic Handling) surviennent lorsque la logique interne d'une application est défaillante, permettant à un attaquant de manipuler le flux de travail ou le traitement des données de manière inattendue. Cela peut se produire lorsque l'application ne valide pas correctement les contraintes d'entrée ou gère mal des cas limites spécifiques, entraînant une divulgation d'informations.

### 📖 Approche

Cette faille se trouvait dans le formulaire "Feedback". J'ai tenté au début de faire une stored XSS, puis en bidouillant en boucle dans les formulaires du feedback, je me suis rendu compte qu'en mettant uniquement une seule lettre dans le champ "Name", le flag apparait.

L'application semble échouer à gérer correctement ce cas limite, déclenchant l'affichage du flag au lieu d'un message d'erreur ou d'un comportement standard.

**Payload utilisé :**
Une seule lettre dans le champ `Name` (ex: `a`).

**Flag :** `0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e`

### 🛡️ Remédiation

Pour corriger cela :
- **Validation des entrées** : Appliquer des règles strictes de validation (longueur minimale et maximale, caractères autorisés).
- **Gestion sécurisée des erreurs** : S'assurer que les cas limites (comme les entrées très courtes) ne révèlent pas d'informations sensibles.
- **Revue de code** : Vérifier la logique métier pour s'assurer qu'aucune combinaison d'entrées spécifique ne déclenche des chemins de débogage ou des fuites d'informations.

### 🔗 Sources

- [OWASP - Business Logic Vulnerabilities](https://owasp.org/www-community/vulnerabilities/Business_logic_vulnerability)

</details>
