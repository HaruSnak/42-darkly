<div align="center">

# Client-Side Security Bypass - Survey
### Manipulating form values to bypass logic restrictions

</div>

---

## 🇬🇧 English

<details>
<summary><b>📖 Click to expand/collapse English version</b></summary>

### 📖 Definition

**Client-Side Parameter Tampering** is a form of bypass where an attacker modifies the parameters sent by the client (browser) to the server. Applications often assume that users can only submit values provided by the visible interface elements (like dropdown menus or checkboxes), but these values can be easily changed using browser development tools.

### ⚡ Quick Demo

Go to `?page=survey`, open the DevTools console (F12), run:
```js
document.querySelector('select').innerHTML += '<option value="999999999999">999999999999</option>'
```
Select the new option and submit.

### 📖 Approach

In this case, the "Survey" page allows users to vote by selecting a grade from a dropdown menu. I wondered what would happen if I sent a value outside expected range. Using the browser's Developer Tools, I located the `<select>` element and modified the `value` attribute of one of the options (originally "10") to a much larger number, "1000000000000000000".

Upon submitting this modified value, the application accepted it and revealed the flag, demonstrating that the server was not validating the range of the input score.

**Method:**
1. Open Developer Tools on the Survey page.
2. Locate the `<select>` element for the vote/grade.
3. Change the `value` of an `<option>` to an arbitrary high number.
4. Select that option and submit the form.

**Flag:** `03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa`

### 💥 Impact

Since the score is never validated server-side, an attacker can inject statistically impossible values (here `10^18`), silently corrupting the integrity of the survey's results. Beyond a single bogus entry, this means the aggregated statistics, averages, or rankings computed from this data become meaningless or attacker-controlled — a real business relying on these numbers (customer satisfaction scores, product ratings, public leaderboards) could have its metrics manipulated at will, with no way to distinguish genuine votes from forged ones.

### 🛡️ Remediation

To fix this:
- **Server-Side Validation**: Ensure the server verifies that the submitted value is within the allowed range (e.g., between 1 and 10) and is of the expected data type.
- **Treat Input as Untrusted**: Never assume constraints defined in HTML (like dropdown options or `max` attributes) will be respected by the client.

### 🔗 Resources

- [OWASP - Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)

</details>

---

## 🇫🇷 Français

<details>
<summary><b>📖 Cliquez pour développer/réduire la version française</b></summary>

### 📖 Définition

Le **Parameter Tampering** côté client est une forme de contournement où un attaquant modifie les paramètres envoyés par le client (navigateur) au serveur. Les applications supposent souvent que les utilisateurs ne peuvent soumettre que les valeurs fournies par l'interface visible (comme les menus déroulants), mais ces valeurs peuvent être facilement modifiées.

### ⚡ Démo rapide

Aller sur `?page=survey`, ouvrir la console DevTools (F12), lancer :
```js
document.querySelector('select').innerHTML += '<option value="999999999999">999999999999</option>'
```
Sélectionner la nouvelle option et soumettre.

### 📖 Approche

La page "Survey" permet de voter en choisissant une note dans une liste déroulante (`select`). Je me suis demandé ce qui se passerait si je modifiais la valeur envoyée. En utilisant les outils de développement (Inspecter), j'ai trouvé l'élément `<option>` correspondant à la note et j'ai modifié sa `value` (initialement "10") par un nombre beaucoup plus grand, "1000000000000000000".

En soumettant ce vote modifié, le site a accepté la valeur et m'a donné le flag, prouvant que le serveur ne vérifiait pas si la note était valide.

**Méthode :**
1. Ouvrir l'inspecteur d'éléments sur la page de sondage.
2. Localiser la balise `<select>` et ses `<option>`.
3. Modifier la valeur (`value`) d'une option pour mettre un grand nombre.
4. Sélectionner cette option et voter.

**Flag :** `03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa`

### 💥 Impact

Comme la note n'est jamais validée côté serveur, un attaquant peut injecter des valeurs statistiquement impossibles (ici `10^18`), corrompant silencieusement l'intégrité des résultats du sondage. Au-delà d'une simple entrée aberrante, cela signifie que les statistiques agrégées, moyennes ou classements calculés à partir de ces données deviennent faussés ou entièrement contrôlables par l'attaquant — une entreprise s'appuyant sur ces chiffres (score de satisfaction client, notes de produits, classements publics) pourrait voir ses métriques manipulées à volonté, sans moyen de distinguer les votes légitimes des votes falsifiés.

### 🛡️ Remédiation

Pour corriger cela :
- **Validation côté serveur** : Le serveur doit impérativement vérifier que la valeur reçue est bien comprise dans la plage autorisée (par exemple, entre 1 et 10).
- **Considérer toute entrée comme non fiable** : Ne jamais supposer que les contraintes HTML (comme les options d'un select) seront respectées par le client.

### 🔗 Sources

- [OWASP - Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)

</details>
