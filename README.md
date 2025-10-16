# BadgeLab

A collection of API endpoints to simplify GitHub README badges. With predefined badges for standard technologies and platforms, along with custom badges you can make yourself.

## Routes

Here is a list of all the routes you can find under `https://badgelab.dev/api/*`. Along with their params and a brief description.

### customBadge

Route:
`https://badgelab.dev/api/customBadge`

This route can be used to create your own badge, customizing the color, text, etc.

Params:

| Name | Description | Example | Required | Default |
| ---- | ----------- | ------- | -------- | ------- |
| name | Text shown on badge | Hello World | true | NA |
| textColor | Color of text show on badge | FFFFFF | false | white |
| bgColor | Color of background show on badge | 000000 | false | black |
| image | Display an icon with the badge (must be svg) | <https://sample.com/some.svg> | false | "null" |
| noLogo | Force logo to not be shown | true | false | false |

### badge

Route:
`https://badgelab.dev/api/badge/:name`

This route can be used to get predefined badges that live in the `badgeList.json` file.

Params:

| Name | Description | Example | Required | Default |
| ---- | ----------- | ------- | -------- | ------- |
| :name | Id of badge you want to fetch | javascript | true | NA |
| noLogo | Force logo to not be shown | true | false | false |

#### Predefined Badges

| Rendered | Route |
| -------- | ----- |
| ![HTML5](https://badgelab.dev/api/badge/html5) | <https://badgelab.dev/api/badge/html5> |
| ![CSS3](https://badgelab.dev/api/badge/css3) | <https://badgelab.dev/api/badge/css3> |
| ![JavaScript](https://badgelab.dev/api/badge/javascript) | <https://badgelab.dev/api/badge/javascript> |
| ![Python](https://badgelab.dev/api/badge/python) | <https://badgelab.dev/api/badge/python> |
| ![Swift](https://badgelab.dev/api/badge/swift) | <https://badgelab.dev/api/badge/swift> |
| ![Java](https://badgelab.dev/api/badge/java) | <https://badgelab.dev/api/badge/java> |
| ![Markdown](https://badgelab.dev/api/badge/markdown) | <https://badgelab.dev/api/badge/markdown> |
| ![W3Schools](https://badgelab.dev/api/badge/w3schools) | <https://badgelab.dev/api/badge/w3schools> |
| ![Khan Academy](https://badgelab.dev/api/badge/khan-academy) | <https://badgelab.dev/api/badge/khan-academy> |
| ![Codecademy](https://badgelab.dev/api/badge/codecademy) | <https://badgelab.dev/api/badge/codecademy> |
| ![MDN Web Docs](https://badgelab.dev/api/badge/mdn) | <https://badgelab.dev/api/badge/mdn> |
| ![GeeksForGeeks](https://badgelab.dev/api/badge/geeksforgeeks) | <https://badgelab.dev/api/badge/geeksforgeeks> |
| ![Firebase](https://badgelab.dev/api/badge/firebase) | <https://badgelab.dev/api/badge/firebase> |
| ![JSON](https://badgelab.dev/api/badge/json) | <https://badgelab.dev/api/badge/json> |
| ![React](https://badgelab.dev/api/badge/react) | <https://badgelab.dev/api/badge/react> |
| ![jQuery](https://badgelab.dev/api/badge/jquery) | <https://badgelab.dev/api/badge/jquery> |
| ![Netlify](https://badgelab.dev/api/badge/netlify) | <https://badgelab.dev/api/badge/netlify> |
| ![Github](https://badgelab.dev/api/badge/github) | <https://badgelab.dev/api/badge/github> |
| ![Github Pages](https://badgelab.dev/api/badge/github-pages) | <https://badgelab.dev/api/badge/github-pages> |
| ![Debian](https://badgelab.dev/api/badge/debian) | <https://badgelab.dev/api/badge/debian> |
| ![Visual Studio Code](https://badgelab.dev/api/badge/vscode) | <https://badgelab.dev/api/badge/vscode> |
| ![Firefox](https://badgelab.dev/api/badge/firefox) | <https://badgelab.dev/api/badge/firefox> |
| ![TailwindCSS](https://badgelab.dev/api/badge/tailwindcss) | <https://badgelab.dev/api/badge/tailwindcss> |
