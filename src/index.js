import { marked } from "marked";
import "./index.css";

const content = await (await fetch("/README.md")).text();

document.body.innerHTML = marked.parse(content);
