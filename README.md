# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain
The domain is on-campus dining guide at UC Davis. The information is available to find online if you are willing to to the research but since there are so many options it becomes difficult to navigate and find the answer that you are looking for. The domain will cover the different dining options and includes some reddit reviews in order to have more opinions in case the users wants recommendations.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | UCD official website | descriptor of UCD dining commons | https://housing.ucdavis.edu/dining/dining-commons/ |
| 2 | UCD official website | list of available dining options | https://housing.ucdavis.edu/dining/menus/ |
| 3 | UCD official website | main dining hall | https://housing.ucdavis.edu/dining/dining-commons/segundo/ |
| 4 | UCD official website | main dining hall | https://housing.ucdavis.edu/dining/dining-commons/cuarto/ |
| 5 | UCD official website | main dining hall | https://housing.ucdavis.edu/dining/dining-commons/tercero/ |
| 6 | UCD news | article talking about dining | https://aggiereader.ucdavis.edu/news/lets-talk-eating-campus |
| 7 | Scrubs cafe | menu of scrubs cafe | https://scrubscafe.ucdavis.edu/menus |
| 8 | reddit r/UCDavis | reddit review thread | https://www.reddit.com/r/UCDavis/comments/1n8zuem/diningcampus_food/ |
| 9 | reddit r/UCDavis | reddit review thread | https://www.reddit.com/r/UCDavis/comments/1nxjuiy/what_is_the_best_food_item_on_campus_and_where/ |
| 10 | reddit r/UCDavis | reddit review thread | https://www.reddit.com/r/UCDavis/comments/1dlosaj/dining_commons_food/ |
| 11 | ucd official | on campus restaurant | https://housing.ucdavis.edu/dining/the-gunrock/ |
| 12 | ucd official | on campus restaurant | https://housing.ucdavis.edu/dining/spokes/ |
| 13 | ucd official | on campus cafe | https://housing.ucdavis.edu/dining/coffee/ |
| 14 | ucd official | on campus convenience store | https://housing.ucdavis.edu/dining/markets/residential-markets/ |
| 15 | ucd official | on campus quick food | https://housing.ucdavis.edu/dining/latitude-market/ |
| 16 | ucd official | on campus convenience store | https://housing.ucdavis.edu/dining/markets/silo-market/ |
| 17 | ucd official | on campus food trucks | https://housing.ucdavis.edu/dining/food-trucks/ |
| 18 | ucd official | meal plans | https://housing.ucdavis.edu/dining/meal-plans/residential/ |
| 19 | ucd official | aggie cash | https://housing.ucdavis.edu/dining/aggie-cash/ |
| 20 | ucd official | vegan & vegetarian info | https://housing.ucdavis.edu/dining/nutrition/vegan-and-vegetarian-options/ |
| 21 | ucd official | halal and kosher info | https://housing.ucdavis.edu/dining/nutrition/halal-and-kosher-dining-options/ |
| 22 | ucd official | allergy info | https://housing.ucdavis.edu/dining/nutrition/food-allergens-and-ingredients-of-concern/ |
| 23 | ucd official | yogurt shop | https://housing.ucdavis.edu/dining/yoloberry-yogurt/ |
| 24 | ucd official | aggie swipe plus meal plan | https://housing.ucdavis.edu/dining/meal-plans/aggie-swipe-plus/ |

---

## Chunking Strategy

**Chunk size:**
500 character chunks

**Overlap:**
50 character overlap between chunks

**Why these choices fit your documents:**
My documents are mostly written in small paragraphs that are losely related, I believe that my current chunk size will return chunks that have appropiate context while not being too large that they lose semantic meaning. I chose a 50 character overlap as a baseline value since I am splitting by tokens I want to make sure that the boundries don't lose too much meaning. It also improves retrieval as it would make chunks that are part of the same section embed more closely if they have overlapped sections.

**Final chunk count:**
245 chunks across all sources.

**Sample chunks:**

> **Chunk 1** (source: ucd-halal-kosher.txt)
> "ckaged meal options that meet Kosher requirements. Please visit our Accessible Housing and Dining webpage for more information on requesting catered Kosher meals. Options in Retail Dining — We currently offer a variety of select fresh produce and pre-packaged Kosher items at our campus market locations."

> **Chunk 2** (source: ucd-aggie-cash.txt)
> "Inside The Silo — Tercero Dining Commons* — Tercero Market* Next to the Tercero Services Center and DC — ASUCD Coffee House Inside the Memorial Union — Campus Food Trucks+ At various food truck corrales on campus. * Receive a 10% discount when using Aggie Cash at these locations. + Receive a 10% discount at participating food trucks when using Aggie Cash."

> **Chunk 3** (source: reddit-dining-campus-food.txt)
> "ll consistent variety and quality during the week. Davis has all the standard college food( pasta, burgers, pizza, rice + meat + veggies), but usually also has other options that rotate, such as bulgogi, mozzarella chicken parm, nachos, etc. Latitude will also have nice staples that add a lot more variety in terms of flavor and spices. fresh omelettes for breakfast ( it's worth getting up at 6 for them in my opinion)"

> **Chunk 4** (source: ucd-meal-plans.txt)
> "r from week to week and expire every Sunday night. Meal swipes may be used to purchase up to $12 in goods per swipe at most Dining Services retail locations**; guests will need to pay the difference for purchases over $12; no credit or change returned for purchases under $12. *Please note that unlimited access is provided during hours of operation."

> **Chunk 5** (source: ucd-allergens.txt)
> "e for lunch and dinner at the Purple Zone, our allergy-friendly platform featuring a variety of tasty dishes made without any of the top major allergens, (wheat/gluten, soy, dairy, fish, shellfish, eggs, tree nuts, peanuts, and sesame) as well as coconut, soybean oil, soy lecithin, peanut oil, or fried items prepared in a shared fryer."

---

## Embedding Model

**Model used:**
all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:**
I used the all-MiniLM-L6-v2 via sentence-transformers embedding model since it is small and lightweight runs locally and doesn't need an API key or cost. If I was deploying this system for real users I would likely use a more powerful API-hosted model like from Open-AI. It would be better since users have lots of different hardware and running it locally will have issues with latency depending on the user. It would also support more context and I could embed a larger corpus of sources. I would also consider improving the domain specific sections by adding more meta data to the chunks so the embedding model has more context when generating vectors.

---

## Retrieval Test Results

**Query 1: "Does UC Davis dining offer halal or kosher options?"**

| Rank | Source | Distance | Chunk preview |
|------|--------|----------|---------------|
| 1 | ucd-vegan-vegetarian.txt | 0.2250 | "At UC Davis Dining Services, we are committed to meeting the diverse dietary needs and preferences of our student community..." |
| 2 | ucd-halal-kosher.txt | 0.2330 | "Kosher Dining Options — 'Kosher-Friendly' Meals in our DC's — UC Davis Dining Services was approached by student leaders from the Jewish community..." |
| 3 | ucd-halal-kosher.txt | 0.2703 | "Halal and Kosher Dining Options — Halal Dining Options — At UC Davis Dining Services, the 'H' icon is used to help our dining patrons easily identify dishes..." |

**Why these chunks are relevant:** The top results correctly identify the dietary accommodation documents. Chunks 2 and 3 come directly from the halal/kosher source and contain the specific "H" icon labeling system and the Kosher-Friendly program details. Chunk 1 from the vegan/vegetarian source is also relevant because the embedding model recognizes the semantic similarity between different dietary accommodation topics. All distances are well below 0.3, indicating strong semantic matches.

**Query 2: "What is Aggie Cash and how does it work?"**

| Rank | Source | Distance | Chunk preview |
|------|--------|----------|---------------|
| 1 | ucd-aggie-cash.txt | 0.3754 | "Aggie Cash is a declining balance (debit) account students, faculty and staff use to purchase food at UC Davis Dining Services locations..." |
| 2 | ucd-aggie-cash.txt | 0.4156 | "Aggie Cash balance rolls from quarter to quarter. Aggie Cash will be deactivated if the account is inactive for more than a 12-month period..." |
| 3 | ucd-aggie-cash.txt | 0.4684 | "gieCard just as one would using a bank debit card. Balance transactions are deducted from the Aggie Cash account, until the account is exhausted..." |

**Why these chunks are relevant:** All three top results come from the correct source document (ucd-aggie-cash.txt). The retrieval correctly prioritized the chunk containing the definition of Aggie Cash first, followed by chunks covering rollover policy and how payments work. Together these three chunks give the LLM everything it needs to explain the system comprehensively.

**Query 3: "At Gunrock cafe are there TVs available for watch parties?"**

| Rank | Source | Distance | Chunk preview |
|------|--------|----------|---------------|
| 1 | ucd-dining-article.txt | 0.4212 | "...community through the love of sports and good food. Here at The Gunrock, your students can play games, chill and attend events..." |
| 2 | ucd-gunrock.txt | 0.4217 | "...ining room to host your next meeting or gathering. Sign up Online. Host Your Next Event or Meeting With Us..." |
| 3 | ucd-gunrock.txt | 0.4416 | "...popular local brewery in town, Sudwerk Brewing Co. Even though we serve from Sudwerk, people of any age can dine with us. Want to watch your favorite sports game? We have 7 TVs..." |

---

## Grounded Generation

**System prompt grounding instruction:**
I use a system prompt that tells the LLM to: Answer the user's question using ONLY the information in the provided documents below. Do NOT use any outside knowledge. If the documents do not contain enough information to answer the question, say 'I don't have enough information on that.'" The temperature is set to 0.3 to reduce creative generation and keep responses closer to the source text. Each retrieved chunk is labeled with its source filename (e.g., [Source: ucd-aggie-cash.txt]) in the context block, so the LLM can reference specific documents in its answer.

**How source attribution is surfaced in the response:**
Source attribution works at two levels. First, the system prompt instructs the LLM to cite which documents it draws from. Second, sources are programmatically guaranteed, the ask() function extracts the unique filenames from the retrieved chunks and returns them separately in the response, independent of what the LLM generates. The Gradio UI displays these in a dedicated "Retrieved from" textbox beneath the answer, so the user always sees which documents were used regardless of whether the LLM remembered to cite them.

**Example response 1:**

> **Query:** "Does UC Davis dining offer halal or kosher options?"
>
> **Answer:** Yes, UC Davis dining offers both halal and kosher options. According to the ucd-halal-kosher.txt document, halal dining options are available and identified with an "H" icon, indicating that the dishes do not contain certain non-halal ingredients. Additionally, the same document mentions "Kosher-Friendly" meals in the dining commons, although it notes that this is a stylistic designation rather than one based on the laws of Kashrut. Furthermore, it is mentioned that all food served at Hillel is kosher. (Source: ucd-halal-kosher.txt)
>
> **Retrieved from:** ucd-vegan-vegetarian.txt, ucd-halal-kosher.txt, reddit-dining-campus-food.txt

**Example response 2:**

> **Query:** "What is Aggie Cash and how does it work?"
>
> **Answer:** Aggie Cash is a declining balance (debit) account that students, faculty, and staff use to purchase food at UC Davis Dining Services locations. It works by transforming the AggieCard (UC Davis ID card) into a debit card with a finite amount of available funds. Account holders make purchases at on-campus retail food locations using their AggieCard, and balance transactions are deducted from the Aggie Cash account until it is exhausted. (Source: ucd-aggie-cash.txt)
>
> **Retrieved from:** ucd-aggie-cash.txt, ucd-dining-article.txt

**Out-of-scope query (refusal response):**

> **Query:** "What are the best CS professors at UC Davis?"
>
> **Answer:** I don't have enough information on that. The provided documents do not mention CS professors at UC Davis. They discuss dining options, coffee, and food variety on campus, but do not provide information about professors or the Computer Science department.
>
> **Retrieved from:** ucd-coffee.txt, reddit-dining-campus-food.txt, ucd-dining-commons-overview.txt, ucd-vegan-vegetarian.txt

---

## Query Interface

The system uses a Gradio web UI launched with `python app.py` at `http://localhost:7860`.

**Input fields:**
- A text box labeled "Your question" where the user types a plain-language question about UC Davis dining

**Output fields:**
- "Answer" — an 8-line scrollable text box displaying the LLM's grounded response with source citations
- "Retrieved from" — a 4-line text box listing the source document filenames that the retrieved chunks came from

**Sample interaction transcript:**

> **Input:** "What is Aggie Cash and how does it work?"
>
> **Answer:** Aggie Cash is a declining balance (debit) account that students, faculty, and staff use to purchase food at UC Davis Dining Services locations. It works by transforming the AggieCard (UC Davis ID card) into a debit card with a finite amount of available funds. Account holders make purchases at on-campus retail food locations using their AggieCard, and balance transactions are deducted from the Aggie Cash account until it is exhausted. (Source: ucd-aggie-cash.txt)
>
> **Retrieved from:**
> - ucd-aggie-cash.txt
> - ucd-dining-article.txt

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 |Which dining locations accepts student meal plans? |The are 3 dining commons Segundo, Tercero and Cuarto as well as the Latitude Restaurant |1. The three main dining commons (Source: reddit-dining-campus-food.txt, ucd-dining-commons-overview.txt) 2. Latitude Restaurant (Source: reddit-dining-campus-food.txt, ucd-meal-plans.txt) 3. A variety of campus dining and coffee locations (Source: ucd-meal-plans.txt) |Relevant |Partially accurate |
| 2 |Does UC Davis dining offer halal or kosher options? |Yes, at UC Davis Dining Services, the "H" icon is used to help our dining patrons easily identify dishes that meet Halal dietary guidelines and they also offer meals designated as "Kosher-Friendly". |Yes, UC Davis dining offers both halal and kosher options. According to the ucd-halal-kosher.txt document, UC Davis Dining Services uses an "H" icon to identify dishes that meet Halal dietary guidelines, and they also offer "Kosher-Friendly" meals in their dining commons. Additionally, the document mentions that all food served at Hillel is kosher. (Source: ucd-halal-kosher.txt) |Relevant |Accurate |
| 3 |What is Aggie Cash and how does it work? |Aggie Cash is a declining balance (debit) account students, faculty and staff use to purchase food at UC Davis Dining Services locations. It also comes with a variety of benefits such as 10% discount on most UCD dining locations |Aggie Cash is a declining balance (debit) account that students, faculty, and staff use to purchase food at UC Davis Dining Services locations. It transforms the AggieCard (UC Davis ID card) into a debit card with a finite amount of available funds. According to the ucd-aggie-cash.txt document, Aggie Cash account holders make purchases at on-campus retail food locations using their AggieCard, just as one would using a bank debit card. Balance transactions are deducted from the Aggie Cash account until the account is exhausted. (Source: ucd-aggie-cash.txt) |Relevant |Accurate |
| 4 |At Gunrock cafe are there TV's available for watch parties? |Yes they have 7 TV's that are available for watch parties. |Yes, at The Gunrock, there are 7 TVs available for watch parties. (Source: ucd-gunrock.txt, ucd-dining-article.txt) |Relevant |Accurate |
| 5 |How does pricing work at the dining common's and latitude? |It is all-you-care-to-eat you pay a flat cost if not on a meal plan or 1 meal swipe if on one. They are welcome to eat dishes freely and stay as long as you want. |According to the provided documents, meal plans may be used at any of the dining commons, and they provide access to all three dining commons (Source: ucd-dining-commons-overview.txt). The 9-Meals-A-Week Plan allows for up to nine meals per week, and it can be used at any of the three dining commons and Latitude (Source: ucd-meal-plans.txt). As for pricing, meal swipes can be used to purchase up to $12 in goods per swipe at most Dining Services retail locations, including Latitude. If a purchase exceeds $12, the guest will need to pay the difference, and no credit or change will be returned for purchases under $12 (Source: ucd-meal-plans.txt). It's also worth noting that paying at the door is an option for those without a meal plan, but the exact pricing for this option is not specified in the provided documents. |Partially Relevant |Partially Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:**
How does pricing work at the dining common's and latitude?

**What the system returned:**
It is supposed to explain that either a meal swipe or a flat fee is to be paid for an all you can eat experience at the dining common's and latitude. It accurately responded these are valid options but it was unable to return the pricing information even though that information is available in the sources. It also mistakened a section from the information about meal plans for retail swipes which are basically $12 dollar vouchers to be used at dining service locations that are not latitude and the dining commons. It fails to explain that the meals are all you can eat and instead gets it confused with the $12 retail swipes.

**Root cause (tied to a specific pipeline stage):**
I believe that the error comes from my chunking method. Its possible that my chunks are too short making them lose meaning and since it only returns 5 chunks contextual information. There is also the embedding model treating the mealswipes and retail swipes similarly but in reality they are quite different which causes the retrieval to grab the chunk about retail swipes instead of looking that the sources for the actual dining commons.

**What you would change to fix it:**
I would like to try changing the chunk size either by increasing it from 500 -> 800-1000 to improve the context behind the chunks or to switch to recursive chunking to split on paragraph boundries since this will create more sematically meaningful chunks. I would also consider changing the top-k from 5->8 this gives the LLM a better chance to get the chunks it needs to properly answer the question.

---

## Spec Reflection

**One way the spec helped you during implementation:**
The spec helped me to clearly define the chunking strategy and retrival approach before prompting any tools. Claude code was able to use the concrete parameters to generate the logic to be as I expected it. The architecture diagram also helped to establish how each stage connects to each other and I am able to clearly understand how the separate modules feed into each other.

**One way your implementation diverged from the spec, and why:**
The spec did not specify what is the distance metric to be used for ChromaDB. The default is L2 (Euclidean) distance. During testing for retrieval all the distance scores where above 0.5 on even with relevant chunks. After some research I switched to using cosine distance since all-MiniLM-L6-v2 is trained to optimize for cosine similarity. This made the scores below 0.5 and made them more relevant for evaluating the retrieval quality. 

---

## AI Usage

**Instance 1**

- *What I gave the AI:*

     My Chunking Strategy section from planning.md (500-character chunks, 50-character overlap), the Documents table listing my 24 sources, and the requirement to build a custom Python splitter that breaks at sentence/word boundaries.

- *What it produced:*

     A complete ingest.py with load_documents(), clean_text(), and chunk_text() functions that loaded all .txt files from documents/, normalized whitespace, and split text into chunks with metadata.

- *What I changed or overrode:*

     The initial chunk_text() function had a bug where the start variable could move backwards when a word boundary was found close to the start position, causing an infinite loop that crashed the program. I had Claude Code diagnose the issue and fix it by adding a guard (start = max(start + 1, end - overlap)) to guarantee forward progress.
     
**Instance 2**

- *What I gave the AI:*

     My Retrieval Approach section from planning.md use embedding model all-MiniLM-L6-v2, Chromadb with top-k=5, the architecture diagram, and the chunk output format from ingest.py.

- *What it produced:*

     embed.py with build_vector_store() and retrieve() functions that embedded all chunks into ChromaDB with source metadata and returned results with distance scores.

- *What I changed or overrode:*

     The generated code used ChromaDB's default L2 distance metric. After testing, distance scores were all above 0.5 even on relevant results. I switched the collection to use cosine distance (metadata={"hnsw:space": "cosine"}) since that's what all-MiniLM-L6-v2 was trained to optimize for, which brought scores into the expected range.

