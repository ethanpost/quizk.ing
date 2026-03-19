# quizk.ing

https://ethanpost.github.io/quizk.ing/

This repository hosts the **Quiz King** quiz runner (`index.html`).

Open `index.html` in your browser, then load a quiz from a public `quiz.json` URL, paste raw JSON, or upload a `.json` file.

You can also prefill the loader with a query parameter:
`index.html?url=https://example.com/quiz.json`

Quiz JSON format (minimum):
- a top-level array of questions, or `{ "questions": [...] }`
- each question has `question` (string), `options` (array of strings), and either `answer` (exact option text) or `correct` (index or string)

Quiz content/data is expected to live elsewhere; this repo is just the UI runner.

