<div align="center">

# Client-Side Security Bypass - Recover Password
### Bypassing frontend restrictions by manipulating HTML

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Client-Side Security Bypass** is a vulnerability where security controls are implemented only on the client side (front-end), such as in HTML, JavaScript, or hidden form fields. Since the client-side code is fully controllable by the user, these controls can be trivially bypassed by modifying the page source or intercepting the request.

### ⚡ Quick Demo

Go to `?page=recover`, open the DevTools console (F12), run:
```js
document.querySelector('input[type=hidden]').type = 'text'
```
Type anything in the now-visible field and submit.

### 📖 Approach

For this vulnerability, the password recovery page seemed suspicious with just an image and a button. I inspected the HTML code (Inspect Element) and noticed a form containing a hidden input field alongside the button.

By modifying the HTML to remove the `type="hidden"` attribute (or simply editing the request), I exposed the input field. I entered a random value and submitted the form, which successfully bypassed the check and revealed the flag.

**Method:**
1. Open Developer Tools (F12 or Ctrl+Shift+I).
2. Inspect the form element.
3. Locate `<input type="hidden" ...>`.
4. Change `type="hidden"` to `type="text"` or remove the attribute.
5. Enter any value and submit.

**Flag:** `1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0`

### 🛡️ Remediation

To fix this:
- **Server-Side Validation**: Never rely solely on client-side checks for security. Always validate and sanitize all inputs on the server.
- **Avoid Hidden Inputs for Logic**: Do not use hidden fields to control critical business logic or security decisions, as they can be easily modified by the user.

### 🔗 Resources

- [OWASP - Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **contournement de sécurité client** (Client-Side Security Bypass) est une vulnérabilité où les contrôles de sécurité sont implémentés uniquement côté client (front-end), par exemple en HTML ou JavaScript. Comme le code côté client est entièrement contrôlable par l'utilisateur, ces contrôles peuvent être contournés trivialement en modifiant la source de la page ou en interceptant la requête.

### ⚡ Démo rapide

Aller sur `?page=recover`, ouvrir la console DevTools (F12), lancer :
```js
document.querySelector('input[type=hidden]').type = 'text'
```
Taper n'importe quelle valeur dans le champ devenu visible et soumettre.

### 📖 Approche

Pour cette faille, la page de récupération de mot de passe me semblait suspecte, avec seulement une image et un bouton. J'ai inspecté le code HTML de la page et j'ai remarqué que le formulaire contenait un champ `input` caché (`type="hidden"`).

En modifiant le code HTML pour enlever l'attribut `hidden` (CTRL + U ou Inspecter l'élément), j'ai rendu le champ visible. J'ai entré une valeur au hasard et j'ai soumis le formulaire. Cela a permis de valider la requête et de récupérer le flag.

**Méthode :**
1. Ouvrir les outils de développement (F12 ou Ctrl+Maj+I).
2. Inspecter l'élément formulaire.
3. Trouver `<input type="hidden" ...>`.
4. Changer `type="hidden"` en `type="text"` ou supprimer l'attribut.
5. Entrer une valeur et soumettre.

**Flag :** `1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0`

### 🛡️ Remédiation

Pour corriger cela :
- **Validation côté serveur** : Ne jamais faire confiance aux vérifications côté client. Toujours valider toutes les données reçues sur le serveur.
- **Éviter les inputs cachés pour la logique critique** : Ne pas utiliser de champs cachés pour contrôler la sécurité ou la logique métier, car ils sont modifiables par l'utilisateur.

### 🔗 Sources

- [OWASP - Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)

</details>
