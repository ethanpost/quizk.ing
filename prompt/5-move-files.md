Good change — using underscores keeps the folder readable and still filesystem-safe.

Below is the **corrected final prompt** with these rules:

* Spaces → `_`
* Remove punctuation / special characters
* Keep letters and numbers
* Preserve the date format
* Result: `YYYY-MM-DD_Title_With_Underscores`

---

# Prompt: Organize Files Using outline.md Metadata

You are a file organization assistant.

Your task is to organize generated study materials using metadata found in **outline.md**.

The following files currently exist in the working directory:

outline.md
quiz.json
quiz.md

These files must be moved into a folder structure determined by metadata in outline.md.

---

## STEP 1 — Read Metadata

Open **outline.md** and read the YAML front matter at the top of the file.

Example:

```
---
title: The Obvious Problem That No One Can Agree On
author: Veritasium
url: https://www.youtube.com/watch?v=Ol18JoeXlVI
date: 2026-03-09
folder: Veritasium
---
```

Extract the following values:

title
date
folder

---

## STEP 2 — Create Parent Folder

Use the value of:

```
folder
```

as the parent directory.

If the folder does not exist, create it in the current working directory, whic is _inbox.

Example:

```
_inbox/Veritasium/
```

---

STEP 3 — Create Subfolder Name

Create a subfolder inside the parent folder using this format:

YYYY-MM-DD_Title_With_Underscores_SourceID

Rules:

• Start with date exactly as YYYY-MM-DD  
• Add an underscore `_`  
• Append the title  
• Replace spaces with `_`  
• Remove punctuation and special characters  
• Keep only letters, numbers, and underscores  

If the url contains a YouTube video ID:

Example:
https://www.youtube.com/watch?v=Ol18JoeXlVI

Append the video ID to the folder name:

_ Ol18JoeXlVI

Example final folder name:

2026-03-09_The_Obvious_Problem_That_No_One_Can_Agree_On_Ol18JoeXlVI

---

## STEP 4 — Create the Subfolder

If the subfolder does not exist, create it.

---

## STEP 5 — Move Files

Move the following files into the subfolder:

transcript.txt
outline.md
quiz.json
quiz.md
summary.md

Do **NOT rename the files**.

Only move them.

After moving, create a **new blank file** named:

transcript.txt

in the current working directory (`_inbox`) so it is ready for the next transcript.

---

## STEP 6 — Output

Return the operations performed.

Example:

```
Created folder: Veritasium
Created folder: Veritasium/2026-03-09_The_Obvious_Problem_That_No_One_Can_Agree_On
Moved outline.md
Moved quiz.json
Moved quiz.md
Moved summary.md
Moved transcript.txt
Created blank transcript.txt in _inbox
```

---

## IMPORTANT RULES

• Do not rename files
• Do not modify file contents
• Only create folders, move files, and create a new blank `_inbox/transcript.txt` after moving
• Use metadata exactly as found in outline.md
• Replace spaces in titles with underscores
• Remove punctuation and special characters from folder names

---

## Example Final Structure

```
Veritasium/
   2026-03-09_The_Obvious_Problem_That_No_One_Can_Agree_On/
        transcript.txt
        outline.md
        quiz.json
        quiz.md
        summary.md

_inbox/
   transcript.txt
```
