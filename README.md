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
| javascript-alt   | ![JavaScript](https://badgelab.dev/api/badge/javascript-alt)   | <https://badgelab.dev/api/badge/javascript-alt>   |
| javascript-color | ![JavaScript](https://badgelab.dev/api/badge/javascript-color) | <https://badgelab.dev/api/badge/javascript-color> |
| python           | ![Python](https://badgelab.dev/api/badge/python)               | <https://badgelab.dev/api/badge/python>           |
| python-alt       | ![Python](https://badgelab.dev/api/badge/python-alt)           | <https://badgelab.dev/api/badge/python-alt>       |
| python-color       | ![Python](https://badgelab.dev/api/badge/python-color)           | <https://badgelab.dev/api/badge/python-color>       |
| swift            | ![Swift](https://badgelab.dev/api/badge/swift)                 | <https://badgelab.dev/api/badge/swift>            |
| java             | ![Java](https://badgelab.dev/api/badge/java)                   | <https://badgelab.dev/api/badge/java>             |
| markdown         | ![Markdown](https://badgelab.dev/api/badge/markdown)           | <https://badgelab.dev/api/badge/markdown>         |
| json             | ![JSON](https://badgelab.dev/api/badge/json)                   | <https://badgelab.dev/api/badge/json>             |

### Frameworks
| ID          | Rendered                                                   | Route                                        |
| ----------- | ---------------------------------------------------------- | -------------------------------------------- |
| react       | ![React](https://badgelab.dev/api/badge/react)             | <https://badgelab.dev/api/badge/react>       |
| jquery      | ![jQuery](https://badgelab.dev/api/badge/jquery)           | <https://badgelab.dev/api/badge/jquery>      |
| tailwindcss | ![TailwindCSS](https://badgelab.dev/api/badge/tailwindcss) | <https://badgelab.dev/api/badge/tailwindcss> |

### Learning Platforms

| ID            | Rendered                                                       | Route                                          |
| ------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| w3schools     | ![W3Schools](https://badgelab.dev/api/badge/w3schools)         | <https://badgelab.dev/api/badge/w3schools>     |
| khan-academy  | ![Khan Academy](https://badgelab.dev/api/badge/khan-academy)   | <https://badgelab.dev/api/badge/khan-academy>  |
| codecademy    | ![Codecademy](https://badgelab.dev/api/badge/codecademy)       | <https://badgelab.dev/api/badge/codecademy>    |
| mdn           | ![MDN Web Docs](https://badgelab.dev/api/badge/mdn)            | <https://badgelab.dev/api/badge/mdn>           |
| geeksforgeeks | ![GeeksForGeeks](https://badgelab.dev/api/badge/geeksforgeeks) | <https://badgelab.dev/api/badge/geeksforgeeks> |

### Hosting

| ID           | Rendered                                                     | Route                                         |
| ------------ | ------------------------------------------------------------ | --------------------------------------------- |
| firebase     | ![Firebase](https://badgelab.dev/api/badge/firebase)         | <https://badgelab.dev/api/badge/firebase>     |
| netlify      | ![Netlify](https://badgelab.dev/api/badge/netlify)           | <https://badgelab.dev/api/badge/netlify>      |
| github-pages | ![Github Pages](https://badgelab.dev/api/badge/github-pages) | <https://badgelab.dev/api/badge/github-pages> |

### Tools

| ID     | Rendered                                                     | Route                                   |
| ------ | ------------------------------------------------------------ | --------------------------------------- |
| github | ![Github](https://badgelab.dev/api/badge/github)             | <https://badgelab.dev/api/badge/github> |
| vscode | ![Visual Studio Code](https://badgelab.dev/api/badge/vscode) | <https://badgelab.dev/api/badge/vscode> |

### Browsers
| ID      | Rendered                                           | Route                                    |
| ------- | -------------------------------------------------- | ---------------------------------------- |
| firefox | ![Firefox](https://badgelab.dev/api/badge/firefox) | <https://badgelab.dev/api/badge/firefox> |
| chrome  | ![Chrome](https://badgelab.dev/api/badge/chrome)   | <https://badgelab.dev/api/badge/chrome>  |
| safari  | ![Safari](https://badgelab.dev/api/badge/safari)   | <https://badgelab.dev/api/badge/safari>  |
| edge    | ![Edge](https://badgelab.dev/api/badge/edge)       | <https://badgelab.dev/api/badge/edge>    |
| opera   | ![Opera](https://badgelab.dev/api/badge/opera)     | <https://badgelab.dev/api/badge/opera>   |
| brave   | ![Brave](https://badgelab.dev/api/badge/brave)     | <https://badgelab.dev/api/badge/brave>   |
| tor     | ![Tor](https://badgelab.dev/api/badge/tor)         | <https://badgelab.dev/api/badge/tor>     |


### Systems
| ID      | Rendered                                           | Route                                    |
| ------- | -------------------------------------------------- | ---------------------------------------- |
| debian  | ![Debian](https://badgelab.dev/api/badge/debian)   | <https://badgelab.dev/api/badge/debian>  |
| ubuntu  | ![Ubuntu](https://badgelab.dev/api/badge/ubuntu)   | <https://badgelab.dev/api/badge/ubuntu>  |
| windows | ![Windows](https://badgelab.dev/api/badge/windows) | <https://badgelab.dev/api/badge/windows> |

