### Day 1 notes
1. Looking at the Diode scan, it's almost impossible to tell what makes them 
different than anything else. The images are extremely low quality, but my guess
is that anything other than a white scan is not correct.
2. Looking at the cracking scan, I see a white square in the top right, but 
nothing that seems way out of the ordinary. 
3. Soiling looks just as dark as the cracking one, and I can't really tell 
what distinguishes each. but I guess they know.
4. Most of the entries are no-anomaly, which means that most of the work will be
easy.

## Day 2:

Nice work. Next is Day 2: get your own API answering in a browser. It uses the metadata file you just explored, and there’s still no database or React yet.

Checklist

[x] Open the FastAPI tutorial and follow its first pages: create a virtual environment, install FastAPI, and run the dev server. Type the tutorial’s hello-world example yourself, then change the message to something else and confirm it updates.
[x] Open the auto-generated docs page in your browser. The dev server prints a docs address (the /docs page) next to the server address. Click around and try the endpoint from there. 
tiangolo
[ ] Replace hello-world with your first real endpoint: one that loads your metadata JSON and returns the first handful of entries. Decide for yourself how many, and what each entry should contain.
[ ] Add a query parameter that lets the caller choose how many entries to get back. The tutorial’s query parameters page covers this.
[ ] Add a second query parameter that filters by anomaly class. Test it in the docs page with at least two different classes.

Done when: you can type a URL in your browser, ask for 5 cracked modules, and get back exactly 5 entries as JSON, all with the class you asked for. Add a few lines to your notes.md about what confused you and how you fixed it.

Hint if you get stuck: decide where your metadata gets loaded. Loading the file inside the endpoint on every request works but is wasteful. See if you can figure out why, and what you’d change. That question is worth thinking about even if you don’t fix it today.

Also, I never saw your Day 1 answers. Paste your class counts when you get a chance. I want to see how uneven they are, because it affects the ML phase later.
