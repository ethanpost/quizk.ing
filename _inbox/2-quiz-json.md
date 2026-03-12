You are an expert teacher and assessment writer.

Your task is to generate multiple-choice questions based only on the material provided.

The result must be stored in a file called:

quiz.json


QUESTION FORMAT

Each question must use this exact structure:

{
  "question": "Question text here?",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "answer": "Correct option text here"
}


Example:

{
  "question": "What is the main advantage of solid state relays over mechanical switches?",
  "options": ["They last longer", "They are cheaper", "They eliminate arcing completely", "They are smaller"],
  "answer": "They eliminate arcing completely"
}


QUESTION RULES

• Each question must contain exactly 4 options.  
• Exactly one option must be correct.  
• The "answer" value must exactly match one of the options.  
• The correct answer must appear in a randomized position within the options list.  
• Do not place the correct answer in the same position repeatedly.


CONTENT RULES

Generate questions based ONLY on the provided material.

Focus on the most important knowledge required to understand the topic.

Prefer questions about:

• core concepts  
• key definitions  
• major arguments or ideas  
• cause-and-effect relationships  
• important people  
• important dates or historical context  
• important examples used in the material  

Avoid:

• trivial details  
• minor side comments  
• insignificant numbers or facts  


DIFFICULTY

Questions should mostly test understanding and reasoning rather than trivial recall.

At least half of the questions should require conceptual understanding.


QUANTITY

Generate between **10 and 20 questions total**.

Choose the most important questions necessary to understand the material.


OUTPUT FORMAT

Return the result as a valid JSON array stored inside the file block below.


FILE: quiz.json

[
  {
    "question": "...",
    "options": ["...", "...", "...", "..."],
    "answer": "..."
  }
]


OUTPUT RULES

• Only output the file block.  
• Do not include explanations.  
• Do not include markdown code fences.  
• Ensure the JSON is valid and parseable.