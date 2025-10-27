# BadgeLab

A collection of API endpoints to simplify GitHub README badges. With predefined badges for standard technologies and platforms, along with custom badges you can make yourself.

## Routes

Here is a list of all the routes you can find under `https://badgelab.dev/api/*`. Along with their params and a brief description.

### customBadge

Route:
`https://badgelab.dev/api/customBadge`

This route can be used to create your own badge, customizing the color, text, etc.

Params:

| Name      | Description                                  | Example                       | Required | Default |
| --------- | -------------------------------------------- | ----------------------------- | -------- | ------- |
| name      | Text shown on badge                          | Hello World                   | true     | NA      |
| textColor | Color of text show on badge                  | FFFFFF                        | false    | white   |
| bgColor   | Color of background show on badge            | 000000                        | false    | black   |
| image     | Display an icon with the badge (must be svg) | <https://sample.com/some.svg> | false    | "null"  |
| noLogo    | Force logo to not be shown                   | true                          | false    | false   |

### badge

Route:
`https://badgelab.dev/api/badge/:name`

This route can be used to get predefined badges that live in the `badgeList.json` file.

Params:

| Name   | Description                   | Example    | Required | Default |
| ------ | ----------------------------- | ---------- | -------- | ------- |
| :name  | Id of badge you want to fetch | javascript | true     | NA      |
| noLogo | Force logo to not be shown    | true       | false    | false   |

## Predefined Badges

Badges are defined within each section below and can be accessed with the [badge route](#badge)

### Languages

| ID               | Rendered                                                       | Route                                             |
| ---------------- | -------------------------------------------------------------- | ------------------------------------------------- |
| html5            | ![HTML5](https://badgelab.dev/api/badge/html5)                 | <https://badgelab.dev/api/badge/html5>            |
| css3             | ![CSS3](https://badgelab.dev/api/badge/css3)                   | <https://badgelab.dev/api/badge/css3>             |
| javascript       | ![JavaScript](https://badgelab.dev/api/badge/javascript)       | <https://badgelab.dev/api/badge/javascript>       |
| javascript-white | ![JavaScript](https://badgelab.dev/api/badge/javascript-white) | <https://badgelab.dev/api/badge/javascript-white> |
| javascript-black | ![JavaScript](https://badgelab.dev/api/badge/javascript-black) | <https://badgelab.dev/api/badge/javascript-black> |
| python           | ![Python](https://badgelab.dev/api/badge/python)               | <https://badgelab.dev/api/badge/python>           |
| python-white     | ![Python](https://badgelab.dev/api/badge/python-white)         | <https://badgelab.dev/api/badge/python-white>     |
| python-black     | ![Python](https://badgelab.dev/api/badge/python-black)         | <https://badgelab.dev/api/badge/python-black>     |
| swift            | ![Swift](https://badgelab.dev/api/badge/swift)                 | <https://badgelab.dev/api/badge/swift>            |
| swift-white      | ![Swift](https://badgelab.dev/api/badge/swift-white)           | <https://badgelab.dev/api/badge/swift-white>      |
| java             | ![Java](https://badgelab.dev/api/badge/java)                   | <https://badgelab.dev/api/badge/java>             |
| java-white       | ![Java](https://badgelab.dev/api/badge/java-white)             | <https://badgelab.dev/api/badge/java-white>       |
| markdown         | ![Markdown](https://badgelab.dev/api/badge/markdown)           | <https://badgelab.dev/api/badge/markdown>         |
| json             | ![JSON](https://badgelab.dev/api/badge/json)                   | <https://badgelab.dev/api/badge/json>             |

### Frameworks
| ID                | Rendered                                                         | Route                                              |
| ----------------- | ---------------------------------------------------------------- | -------------------------------------------------- |
| react             | ![React](https://badgelab.dev/api/badge/react)                   | <https://badgelab.dev/api/badge/react>             |
| jquery            | ![jQuery](https://badgelab.dev/api/badge/jquery)                 | <https://badgelab.dev/api/badge/jquery>            |
| jquery-white      | ![jQuery](https://badgelab.dev/api/badge/jquery-white)           | <https://badgelab.dev/api/badge/jquery-white>      |
| tailwindcss       | ![TailwindCSS](https://badgelab.dev/api/badge/tailwindcss)       | <https://badgelab.dev/api/badge/tailwindcss>       |
| tailwindcss-white | ![TailwindCSS](https://badgelab.dev/api/badge/tailwindcss-white) | <https://badgelab.dev/api/badge/tailwindcss-white> |


### Learning Platforms

| ID                 | Rendered                                                           | Route                                               |
| ------------------ | ------------------------------------------------------------------ | --------------------------------------------------- |
| w3schools          | ![W3Schools](https://badgelab.dev/api/badge/w3schools)             | <https://badgelab.dev/api/badge/w3schools>          |
| w3schools-white    | ![W3Schools](https://badgelab.dev/api/badge/w3schools-white)       | <https://badgelab.dev/api/badge/w3schools-white>    |
| khan-academy       | ![Khan Academy](https://badgelab.dev/api/badge/khan-academy)       | <https://badgelab.dev/api/badge/khan-academy>       |
| khan-academy-white | ![Khan Academy](https://badgelab.dev/api/badge/khan-academy-white) | <https://badgelab.dev/api/badge/khan-academy-white> |
| codecademy         | ![Codecademy](https://badgelab.dev/api/badge/codecademy)           | <https://badgelab.dev/api/badge/codecademy>         |
| mdn                | ![MDN Web Docs](https://badgelab.dev/api/badge/mdn)                | <https://badgelab.dev/api/badge/mdn>                |
| geeksforgeeks      | ![GeeksForGeeks](https://badgelab.dev/api/badge/geeksforgeeks)     | <https://badgelab.dev/api/badge/geeksforgeeks>      |

### Hosting

| ID             | Rendered                                                     | Route                                           |
| -------------- | ------------------------------------------------------------ | ----------------------------------------------- |
| firebase       | ![Firebase](https://badgelab.dev/api/badge/firebase)         | <https://badgelab.dev/api/badge/firebase>       |
| firebase-white | ![Firebase](https://badgelab.dev/api/badge/firebase-white)   | <https://badgelab.dev/api/badge/firebase-white> |
| netlify        | ![Netlify](https://badgelab.dev/api/badge/netlify)           | <https://badgelab.dev/api/badge/netlify>        |
| github-pages   | ![Github Pages](https://badgelab.dev/api/badge/github-pages) | <https://badgelab.dev/api/badge/github-pages>   |

### Tools

| ID           | Rendered                                                           | Route                                         |
| ------------ | ------------------------------------------------------------------ | --------------------------------------------- |
| github       | ![Github](https://badgelab.dev/api/badge/github)                   | <https://badgelab.dev/api/badge/github>       |
| vscode       | ![Visual Studio Code](https://badgelab.dev/api/badge/vscode)       | <https://badgelab.dev/api/badge/vscode>       |
| vscode-white | ![Visual Studio Code](https://badgelab.dev/api/badge/vscode-white) | <https://badgelab.dev/api/badge/vscode-white> |


### Browsers
| ID            | Rendered                                                 | Route                                          |
| ------------- | -------------------------------------------------------- | ---------------------------------------------- |
| firefox       | ![Firefox](https://badgelab.dev/api/badge/firefox)       | <https://badgelab.dev/api/badge/firefox>       |
| firefox-white | ![Firefox](https://badgelab.dev/api/badge/firefox-white) | <https://badgelab.dev/api/badge/firefox-white> |
| chrome        | ![Chrome](https://badgelab.dev/api/badge/chrome)         | <https://badgelab.dev/api/badge/chrome>        |
| chrome-white  | ![Chrome](https://badgelab.dev/api/badge/chrome-white)   | <https://badgelab.dev/api/badge/chrome-white>  |
| safari        | ![Safari](https://badgelab.dev/api/badge/safari)         | <https://badgelab.dev/api/badge/safari>        |
| safari-white  | ![Safari](https://badgelab.dev/api/badge/safari-white)   | <https://badgelab.dev/api/badge/safari-white>  |
| edge          | ![Edge](https://badgelab.dev/api/badge/edge)             | <https://badgelab.dev/api/badge/edge>          |
| edge-white    | ![Edge](https://badgelab.dev/api/badge/edge-white)       | <https://badgelab.dev/api/badge/edge-white>    |
| opera         | ![Opera](https://badgelab.dev/api/badge/opera)           | <https://badgelab.dev/api/badge/opera>         |
| opera-white   | ![Opera](https://badgelab.dev/api/badge/opera-white)     | <https://badgelab.dev/api/badge/opera-white>   |
| brave         | ![Brave](https://badgelab.dev/api/badge/brave)           | <https://badgelab.dev/api/badge/brave>         |
| brave-white   | ![Brave](https://badgelab.dev/api/badge/brave-white)     | <https://badgelab.dev/api/badge/brave-white>   |
| tor           | ![Tor](https://badgelab.dev/api/badge/tor)               | <https://badgelab.dev/api/badge/tor>           |
| tor-white     | ![Tor](https://badgelab.dev/api/badge/tor-white)         | <https://badgelab.dev/api/badge/tor-white>     |


### Systems
| ID            | Rendered                                                 | Route                                          |
| ------------- | -------------------------------------------------------- | ---------------------------------------------- |
| debian        | ![Debian](https://badgelab.dev/api/badge/debian)         | <https://badgelab.dev/api/badge/debian>        |
| debian-white  | ![Debian](https://badgelab.dev/api/badge/debian-white)   | <https://badgelab.dev/api/badge/debian-white>  |
| ubuntu        | ![Ubuntu](https://badgelab.dev/api/badge/ubuntu)         | <https://badgelab.dev/api/badge/ubuntu>        |
| ubuntu-white  | ![Ubuntu](https://badgelab.dev/api/badge/ubuntu-white)   | <https://badgelab.dev/api/badge/ubuntu-white>  |
| windows       | ![Windows](https://badgelab.dev/api/badge/windows)       | <https://badgelab.dev/api/badge/windows>       |
| windows-white | ![Windows](https://badgelab.dev/api/badge/windows-white) | <https://badgelab.dev/api/badge/windows-white> |

