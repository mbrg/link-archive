---
title: "AI in Software Engineering at Facebook ◆ IEEE Journals & Magazine ◆ IEEE Xplore"
tags:
   - Software Engineering
   - Artificial Intelligence
   - Code Recommendation
   - Machine Learning
   - Natural Language Processing
link: https://ieeexplore.ieee.org/document/9360852
date: 2025-07-20
summary: "Facebook's integration of AI into software engineering highlights advancements in developer productivity through three key tools: Neural Code Search (NCS), Aroma, and Getafix. NCS enables natural language-based querying of code repositories, utilizing embeddings for efficient snippet retrieval. Aroma clusters similar code snippets for idiomatic recommendations, enhancing coding practices. Getafix automates bug-fix suggestions by learning from historical commit patterns, streamlining the debugging process. These ML techniques not only improve code editing but also target code review and production stages, indicating significant potential for further optimization in the software development lifecycle."
---

Loading web-font TeX/Size4/Regular

AI in Software Engineering at Facebook \| IEEE Journals & Magazine \| IEEE Xplore

[close message button](https://ieeexplore.ieee.org/document/)

Skip to Main Content

# AI in Software Engineering at Facebook

Publisher: IEEE

Cite This

[PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9360852)

[Johannes Bader](https://ieeexplore.ieee.org/author/38113805600); [Sonia Seohyun Kim](https://ieeexplore.ieee.org/author/37088894158)[Open Researcher and Contributor Identifier (ORCID)](https://orcid.org/0000-0002-1654-3902); [Frank Sifei Luan](https://ieeexplore.ieee.org/author/37088892612)[Open Researcher and Contributor Identifier (ORCID)](https://orcid.org/0000-0001-8709-6823); [Satish Chandra](https://ieeexplore.ieee.org/author/37335309000)[Open Researcher and Contributor Identifier (ORCID)](https://orcid.org/0000-0003-2546-9000); [Erik Meijer](https://ieeexplore.ieee.org/author/37086462048)

All Authors

View Document

10

Cites in

Papers

7617

Full

Text Views

Open Access

- Alerts



[Manage Content Alerts](https://ieeexplore.ieee.org/alerts/citation)



Add to Citation Alerts


Under a [Creative Commons License](https://creativecommons.org/licenses/by-nc-nd/4.0/)

* * *

- [Download PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9360852)

- Download References
- Request Permissions
- Save to
- Alerts

## Abstract:

How can artificial intelligence help software engineers better do their jobs and advance the state of the practice? We describe three productivity tools that learn patter...Show More

## Metadata

## Abstract:

How can artificial intelligence help software engineers better do their jobs and advance the state of the practice? We describe three productivity tools that learn patterns from software artifacts: code search using natural language, code recommendation, and automatic bug fixing.

**Published in:** [IEEE Software](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=52) ( Volume: 38, [Issue: 4](https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=9460976&punumber=52), July-Aug. 2021)

**Page(s):** 52 \- 61

**Date of Publication:** 23 February 2021 [Get help with using Publication Dates](http://ieeexplore.ieee.org/Xplorehelp/Help_Pubdates.html)

## ISSN Information:

**DOI:** [10.1109/MS.2021.3061664](https://doi.org/10.1109/MS.2021.3061664)

Publisher: IEEE

![](https://ieeexplore.ieee.org/assets/img/document/toc-icon.png) Contents

* * *

[![](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/38ms04-bader-opener-3061664-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/38ms04-bader-opener-3061664-large.gif)

Artificial intelligence (AI) and, more specifically, the machine learning (ML) subarea of AI, has had a transformative impact on almost every major industry today, ranging from retail, to pharmaceuticals, to finance. Not surprisingly, it is beginning to transform the software development industry as well, though significant potential remains untapped.

The underlying basis for the transformative impact of ML is the vast amount of data that are available to be analyzed and mined, from which clever ML algorithms can extract patterns and insights. In software engineering, one of the most easily accessible data are source code itself. For example, GitHub hosts millions of projects, which, together, add up to billions of lines of code; most companies have large proprietary code repositories as well. Other examples of sources of data include the following:

- incremental changes between repository versions of code

- a large number of tests and their outcomes during continuous integration

- online forums, such as Stack Overflow, in which developers interact with each other.


What are some of the useful insights to be extracted from these data? How can we use ML to extract those insights? Since software engineering is a lot about developer productivity, in the rest of this introduction, we give several examples of scenarios in which we have used ML to help developers work more efficiently; in later sections, we give technical details of how these tools work. Toward the end of the article, we present a broader picture of additional ways in which ML-based insights can help in software engineering.

Consider the life of a developer who has to implement a function, for example, for hiding the Android soft keyboard programmatically. One way to tackle this problem is to study Android application programming interfaces (APIs) and then implement the function, but APIs may take a long time to comprehend. It would be much more efficient to derive inspiration from existing code that serves a related purpose. One way to find a relevant code snippet is with a quick search on Stack Overflow. However, if the question is not already answered on Stack Overflow, posting a new question and waiting for a response has a long latency.

On the other hand, copious amounts of relevant Android code are available on GitHub. The problem is that it is hard to find such relevant snippets directly from a collection of repositories. We have created a technique that can help retrieve a pertinent code snippet directly from source code, starting with just rough keywords. While the search does not come with the explanation that a Stack Overflow post has, it retrieves potentially useful information in real time.

Even when one does have a start on which APIs to use for a certain task at hand, the task is not done. When writing code, developers are curious about how other programmers have written similar code, to get reassured or discover considerations they might have missed. If they directly search on a large code corpus for an API name, they might get tens of thousands of results. What they instead want is a small set of sample usages from the repository that gives them some additional information.

Consider an example usage of an Android API method decodeStream:

**Bitmap** bitmap = **BitmapFactory**.

decodeStream(input);

However, if one were to look at related code elsewhere in the repository, one variation is to make sure the app does not crash on an exception:

**try** {

**Bitmap** bitmap = **BitmapFactory**.decode

      Stream(input); …

} catch ( **IOException** e) {…}

This is a different search scenario that we call _code recommendation_. The input is a code snippet, and the output is a small list of related code fragments that show only a few representative variations of information that occur commonly enough. We will discuss our approach to building such a code recommendation engine in the “Code Recommendation” section.

When writing code, developers are curious about how other programmers have written similar code, to get reassured or discover considerations they might have missed.

Code evolves constantly. At Facebook, the Android app repository alone sees thousands of commits per week. Since many of these commits are fixes to various issues, we can use ML to figure out the patterns to these fixes and automatically suggest an appropriate fix.

More specifically, we have found that fixes to static analysis warnings often come from a large palette of code patterns. The following shows an example fix (inserted code in green) of Infer’s warning on potential NullPointerException (NPE) (null dereferences) in Java:

**if** ( **this**.lazyProvider == **null** \|\| shouldSkip) {

**return false**;

}

**Provider** p = **this**.lazyProvider.get();

The notable point is that developers have a strong preference for a certain way to fix a warning, even though there might exist alternate, semantically equivalent ways. A tool that recommends fixes must suggest the one that the developer finds natural in a given context. We will talk about a tool that discovers and learns bug-fixing patterns from data.

These are just some of the many initiatives we have started and incorporated into practice at Facebook. Additional work includes predictive regression test selection,1 triaging for crashes,2 and code autocompletion. Our F8 presentation3 demonstrates how these tools are integrated into the Facebook development environment.

Our thesis is that even simple ML methods can help remove a lot of inefficiencies in the day-to-day life of a developer. No longer should they spend a lot of time looking for information over a repository, finding relevant information from hundreds of code fragments, or fixing simple, predictable bugs manually. In the next section, we describe technical details for the three topics we have introduced.

### Background

The ability to search over large code corpora can be a powerful productivity booster. Therefore, we have explored ways to search directly over the provided code corpora using basic natural language processing and information-retrieval techniques.

There have been previous works in code search, such as CoCaBu4 (a code-search tool that augments natural language queries by adding correlated code vocabulary from Internet forums) and Sourcerer5 (a code-search framework that searches over open source projects available on the Internet). However, these tools are not applicable for internal use since most of our developers work with proprietary APIs and frameworks, which are rarely discussed on the Internet.

Thus, we came up with an approach to directly search over the given corpus. Our tool, called _neural code search_ ( _NCS_),6 aims to find relevant code snippet examples given a query in natural language.

### How Does It Work?

NCS is built using the idea of embeddings, which are vector representations of code that aim to capture the intent of a piece of code in a form suitable for ML. Our hypothesis is that the tokens in source code are generally meaningful, and embeddings derived from these tokens can capture the intent of the code snippet well enough for a code search. NCS creates embeddings at the granularity of a method body.

As shown in Figure 1, NCS works in the following steps.

[![Figure 1. - The NCS model training and search retrieval. NCS extracts information from the source code, builds word embeddings, and uses TF-IDF weighting to get a document embedding for each code snippet. The query is mapped to the shared vector space, and the most relevant code snippets are ranked with cosine similarity.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/bader01-3061664-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/bader01-3061664-large.gif)

**Figure 1.**

The NCS model training and search retrieval. NCS extracts information from the source code, builds word embeddings, and uses TF-IDF weighting to get a document embedding for each code snippet. The query is mapped to the shared vector space, and the most relevant code snippets are ranked with cosine similarity.

Show All

#### Extract Information

NCS first extracts relevant tokens from source code to create a “natural language” document. The information NCS extracts includes method names, comments, class names, and string literals.

#### Build Word Embeddings

NCS then builds word embeddings using FastText,7 which gives vector representations for each word in the corpus. Similar to Word2Vec,8 FastText performs unsupervised training such that words appearing in similar contexts have similar vector representations. For example, the embedding of _button_ is the closest with the embeddings of _click_, _popup_, and _dismissible_ when trained on an Android code corpus.

#### Build Document Embeddings

Finally, to create a document embedding for each method body in the corpus, NCS computes a weighted average from its tokenized words and its respective word embeddings, as shown in [(1)](https://ieeexplore.ieee.org/document/#deqn1), where {d}d is a set of words in a document, {C}C is the corpus containing all documents, and {u}u is a normalizing function. This document embedding serves to capture the overall semantic meaning of the method body. NCS weights the words using term frequency–inverse document frequency (TF-IDF) [(2)](https://ieeexplore.ieee.org/document/#deqn2), a well-known weighting technique in information retrieval. The top portion of Figure 1 shows the NCS model training part.
{v}\_{d} = {u} \\left(\\mathop{\\sum}\\limits\_{{w},{\\in}\\,{d}}{u}\\left({v}\_{w}\\right),\\cdot\\,{\\text{tfidf}} \\left({w},{d},{C}\\right)\\right) \\tag{1}

View Source![Right-click on figure for MathML and additional features.](https://ieeexplore.ieee.org/assets/img/icon.support.gif)\\\[{v}\_{d} = {u} \\left(\\mathop{\\sum}\\limits\_{{w},{\\in}\\,{d}}{u}\\left({v}\_{w}\\right),\\cdot\\,{\\text{tfidf}} \\left({w},{d},{C}\\right)\\right) \\tag{1} \\\]{\\text{tfidf}}\\left({w},{d},{C}\\right) = \\frac{{1} + {\\log}{\\text{tf}}\\left. \\left({w},{d}\\right)\\right)}{{\\log}{\\left\\vert{C}\\right\\vert}\\,{\\cdot}\\,{\\text{df}}\\left({w},{C}\\right)}. \\tag{2}

View Source![Right-click on figure for MathML and additional features.](https://ieeexplore.ieee.org/assets/img/icon.support.gif)\\\[{\\text{tfidf}}\\left({w},{d},{C}\\right) = \\frac{{1} + {\\log}{\\text{tf}}\\left. \\left({w},{d}\\right)\\right)}{{\\log}{\\left\\vert{C}\\right\\vert}\\,{\\cdot}\\,{\\text{df}}\\left({w},{C}\\right)}. \\tag{2} \\\]

#### Search Retrieval

Upon receiving a search query, NCS tokenizes the query and uses the same trained word embeddings to represent it as a vector. It is important to note that the tokenization will turn the natural language query to a series of main keywords that captures the essence of the query. For example, the query “How to get the ActionBar height?” will be tokenized to “get action bar height.” NCS then compares this vector to the document embeddings, as discussed previously. NCS ranks the document embeddings by cosine similarity using Facebook AI Similarity Search,9 a standard similarity search algorithm that operates on high-dimensional data, and returns the top results. The bottom portion of Figure 1 shows the search retrieval part.

NCS is built using the idea of embeddings, which are vector representations of code that aim to capture the intent of a piece of code in a form suitable for ML.

### Evaluation

We evaluated the effectiveness of NCS on a set of Stack Overflow questions, with the post title as the query and a code snippet from the accepted answer as the desired code answer. Given a query, we measured whether NCS was able to retrieve a correct answer from a large search corpus (GitHub repositories). Out of 287 questions, NCS correctly answered 98 questions in the top 10 results. This evaluation data set, along with the search corpus, is publicly available from Li et al.10

Some examples of Stack Overflow questions that NCS answers well are as follows:

- “How to delete a whole folder and content?”

- “How to convert an image into Base64 string?”

- “How to get the ActionBar height?”

- “How to find MAC address of an Android device programmatically?”


Sachdev et al.6 include more details on the training and evaluation of NCS. We further investigated whether deep learning models lead to better code-search results.11

### Developer Feedback

The usage of NCS at Facebook was somewhat different from the way we had envisioned it. Developers did not often write Stack Overflow-style questions; instead, they mostly searched with keyword queries, such as “contract number amount.” Although the raw query types were different, with the tokenization step where we break down both code snippets and the queries into keywords, we were able to deploy NCS with no adaptations to the model at Facebook.

At Facebook, NCS is integrated into the main code-search tools (e.g., the website and IDE) as a complement to the existing exact-match code-search capabilities. Initially, the NCS results and the exact-match (grep-like) results were shown together. Sometimes, though, developers were looking only for exact matches and got confused by the interleaving of results. Consequently, exact-match results (from the raw queries) were shown separately from the NCS results (from the tokenized queries).

### Background

NCS answers the first question that every developer has—how do I do something?—by enabling natural language search directly over a large code corpus. Using NCS, a developer can find this API for writing code to load a bitmap image:

**Bitmap** bitmap = **BitmapFactory**.decode

Stream(input);

However, real-world coding does not end here. This line of code, if written and deployed, can run on millions of devices in a variety of different environments. The developer needs to make sure that the code will not crash on people’s phones. Often, this would mean adding additional code for a safety check, error handling, and so on. In other words, the developer has a new question: is there anything else to add?

Since there are millions of open source repositories available, it is highly likely that, given a particular task, some code already exists somewhere doing it. The challenge is, given a query code snippet and a large code corpus, how to find similar code and offer concise, idiomatic coding patterns to developers.

There exist many coding assistant tools that differ in their design and model: API recommenders suggest APIs given a coding context, but they do not provide usage examples to help with integration. API documentation tools provide helpful usage templates, but these are limited to API queries rather than arbitrary code snippets. Code-to-code search engines return exhaustive code matches, whereas our goal is to provide concise recommendations by clustering together similar results. Aroma is able to overcome all of these shortcomings.

### How Does Aroma Work?

Aroma indexes the code corpus by creating sparse vector representations of each method body. To do so, it first parses the source code to get a simplified parse tree. Aroma uses this representation because it allows the rest of the algorithm to be language agnostic.

Aroma then extracts features (presented in Figure 2) from the parse tree to capture the code structure and semantics. Aroma creates the feature set of a code snippet by aggregating the features of all tokens in that code snippet. After obtaining the vocabulary of all features, Aroma assigns a unique index to each feature, then converts the feature set to a sparse vector. Given a query code snippet, Aroma runs the following phases to create recommendations.

[![Figure 2. - The features extracted by Aroma from a parse tree. The leaf nodes represent code tokens, which are extracted as token features; the internal nodes represent syntactic structures and are concatenated with leaf nodes as syntactic features. The different colors represent different features extracted for the bottom-most node view. Refer to Luan et al.12 for more details.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/bader02-3061664-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/bader02-3061664-large.gif)

**Figure 2.**

The features extracted by Aroma from a parse tree. The leaf nodes represent code tokens, which are extracted as token features; the internal nodes represent syntactic structures and are concatenated with leaf nodes as syntactic features. The different colors represent different features extracted for the bottom-most node view. Refer to Luan et al.12 for more details.

Show All

#### Feature-Based Search

Aroma takes the query code snippet and creates a vector representation using the same steps in indexing. It then computes a list of top (e.g., 1,000) candidate methods that have the most overlap with the query. This computation is very efficient by utilizing parallel sparse matrix multiplication.

#### Clustering

Aroma then clusters together similar-looking method bodies. Instead of showing similar or duplicate code, we want to create a single, idiomatic code recommendation from them. Aroma performs a fine-grained analysis on the candidate methods and finds clusters based on similarities among the method bodies.

Code-to-code search engines return exhaustive code matches, whereas our goal is to provide concise recommendations by clustering together similar results.

#### Intersecting

The final step is to create one code recommendation for each cluster of method bodies. The intersecting algorithm works by taking the first code snippet as the “base” code and then iteratively pruning it with respect to every other method in the cluster. Its goal is to return only the common coding idiom among the cluster, by removing extraneous lines that may be just situational in a specific method. Refer to our paper12 for full algorithm details.

As a concrete example, suppose the following two code snippets are in one cluster and that the first one is the “base” code snippet:

//Base snippet

InputStream is =…;

final BitmapFactory.Options **options** = new

    BitmapFactory.Options();

**options.inSampleSize = 2**;

Bitmap **bmp** = **BitmapFactory**. **decodeStream**

**(is**, null, **options)**;

ImageView **imageView** =…;

//2nd snippet

BitmapFactory.Options **options** = new Bitmap

    Factory.Options();

while (…) {

**options.inSampleSize = 2;**

**options.inJustDecodeBounds =…**

**bitmap** = BitmapFactory. **decodeStream(in**,

        null, **options)**;

}

Both snippets contain a few lines of similar code but also different lines specific to themselves. Aroma’s intersection algorithm compares the base snippet with the second snippet, keeping only the lines that are common in both. It then compares these lines with the next method body. The remaining lines are returned as a code recommendation:

//A code recommendation

final BitmapFactory.Options **options** = new

    BitmapFactory.Options();

**options.inSampleSize = 2**;

Bitmap **bmp** = BitmapFactory. **decodeStream**

**(is**, null, **options)**;

Other code recommendations are created from other clusters in the same way. Aroma’s algorithm ensures that these recommendations are substantially different from one another, so developers can learn a diverse range of coding patterns.

### Results

We instantiated Aroma on a large code corpus of Android GitHub repositories and performed Aroma searches with code snippets chosen from the 500 most popular Stack Overflow questions with the Android tag. We observed that Aroma provided useful recommendations for a majority of these snippets. Moreover, when we used half of the snippet as the query, Aroma exactly recommended the second half of the code snippet in 37 out of 50 cases.

### Developer Feedback

At Facebook, Aroma is integrated into the Visual Studio Code IDE. The developer selects a portion of code to be used as a query, and, in response, Aroma presents a set of code recommendations. From Aroma’s feedback workgroups, this integration received mixed feedback: developers were unsure about the use case. Is it a “teacher” to show better code? Is it warning about potential code duplication? In the end, developers were most interested in seeing examples of API usage. We have since developed a new tool for generating code examples13 to address this need.

### Background

Large code repositories also come with a long history of commits (i.e., code changes), recording how the code base evolved into its current state. If we can find repetitive patterns using ML among these changes, then we can automate the routine work that engineers repetitively do. At Facebook, we have found that one common class of repetitive changes encompasses bug fixes. Therefore, we built a tool called _Getafix_, which learns bug-fixing patterns and automatically offers fix suggestions.

Getafix has goals similar to those of existing automated program repair techniques, but it fills a previously unoccupied spot in the design space: single/few shot prediction of natural-looking fixes, but for specific kinds of bugs. In contrast to generate-and-validate approaches,14 we focus on learning patterns from past fixes for specific bug types and leverage information known about bug instances (e.g., blamed variable). Getafix does not attempt to find generic solutions from any sort of ingredient space or by generically mutating the code. It tends to produce actual, human-like fixes by construction, as it takes nothing but past human fixes as inspiration.

### How Does It Work?

For clarity, we focus on a specific type of bug that can crash Android apps: Java NPE. The following code snippet shows an example of an NPE and a possible fix:

public int **getWidth()** {

    @Nullable View **v** = this. **getView**();

    return **v.getWidth()**;  // **Bug: NPE if v is null**

    return **v** !=null ? **v.getWidth**() : 0;

}

At Facebook, we use the Infer15 static analyzer to detect and warn about potential NPEs (the line highlighted in red). From the Infer records, we identify commits that fix the potential NPE (the line highlighted in green). We scrape hundreds of such bug-fixing commits from the version history and use them as training data for Getafix.

#### Edit Extraction

To find repetitive patterns of bug fixes (“fix patterns”) from these training data, Getafix splits commits into fine-grained abstract syntax tree (AST) edits. Getafix first parses each file touched by a commit into a pair of ASTs: one for the source code before the changes made, and another for after the change. Getafix then applies a tree differencing algorithm similar to GumTree16 to each pair of ASTs to predict the edits (insertions, deletions, moves, or updates) that likely represent the difference. For the example fix described, Getafix will extract the following edit: v.getWidth() " v!=null? v.getWidth(): 0.

#### Clustering

Getafix takes a data-driven approach, called _antiunification_, by clustering the set of AST edits yielded by the previous step by similarity: it merges the most similar pair of edits in the set into a new edit pattern, abstracting away details only where necessary. An example follows:

Edit A:     v.getWidth() ⟶ "v!=null

? v.getWidth(): 0

Edit B:     lst.size() ⟶ **l** st!=null

? lst.size():  0

Antiunification:     α.β() ⟶ α !=null

? α.β():   0

Antiunification has the desirable property of merging edit patterns in the most information-preserving way possible. Getafix repeats this step as often as possible, putting the resulting edit pattern back into the set in place of its constituents, hence reducing the size of the set and allowing edit patterns to be merged and abstracted even further. This process results in a hierarchy of edit patterns, with the original edits as leaf nodes and increasingly abstract edit patterns closer to the roots.

#### Fix Prediction

With such a hierarchy of fix patterns for NPE warnings, Getafix can automatically fix future warnings: when Infer produces a new, previously unseen NPE warning, Getafix retrieves all patterns that are applicable from our hierarchy of fix patterns. It then applies those candidate patterns to the code, generating candidate fixes, which are ranked statistically using a metric comparable to TF-IDF. To limit computational cost, one or, at most, a few of the top-ranked candidate patterns are then validated (e.g., by running Infer and making sure the warning disappeared).

The best passing candidate fix is offered to the engineer as a suggestion he or she can accept or reject at the click of a button. Getafix suggests only one fix to limit the cognitive load and provide a straightforward user experience. We do require a final human confirmation since Getafix uses statistical learning and ranking techniques, so there is no formal guarantee of correctness despite certain forms of validation. For more details about Getafix, refer to Bader et al.17

### Results

Of the Infer NPE warnings fixed by Facebook engineers since the Getafix service was rolled out, 42% were fixed by accepting our fix suggestion, and, in 9% of the cases, engineers wrote a semantically identical fix (which goes to show that developers are very particular about the fix suggestions they accept). Note that our pattern-learning phase takes any set of changes as input, so a different scenario we have successfully started automating is the discovery and application of “lint” rules. Changes made in response to code review are often fixes to common antipatterns that were pointed out by a reviewer, and finding and fixing these antipatterns can be baked into a lint rule.

### Developer Feedback

We show fix suggestions for warnings during code review and in the IDE wherever possible. We found that warnings that came with a fix suggestion were more actionable and addressed (whether via accepting the suggested fix or hand-writing one) more often than plain warnings. Individual reactions ranged from ignoring our suggestions to expressing excitement about their level of sophistication in internal feedback groups.

We found that semantic equivalence is insufficient to our engineers and that syntactic differences do matter to them: for instance, we sometimes predict using a ternary conditional and, in several cases, observed developers adopt this fix but negating the condition and swapping the “then” and “else” expressions. At this point, the “accept with one click” experience we provide is ineffective, so we strive to suggest natural-looking fixes exactly as our engineers expect, so syntax and even details like idiomatic white space must be human-like. Our ML-based approach learns patterns that look natural by construction (learned from real fixes) and also learns how to rank among them in a principled way, which would be strenuous to replicate manually.

We now take a step back to discuss how these ML-based techniques fit in the broader picture of the software development process. In fact, these techniques have the potential to influence not just writing or fixing code but almost all stages of the software lifecycle.

Figure 3 shows a way to think about modern software development, as organized in three stages, recurring in a cycle (not depicted). The workflow begins with an individual developer’s work, which involves editing the code to implement new functionality, or in response to an issue and making sure the code compiles and passes at least some lightweight quality control (e.g., linters or unit tests). Next is the team stage: once the developer is satisfied with a code change he or she is making, it is sent in for code review, and, perhaps simultaneously, more extensive testing and verification are kicked off. Either of these can require the jumping back into the individual workflow.

[![Figure 3. - The common workflows in software development.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/bader03-3061664-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/52/9460976/9360852/bader03-3061664-large.gif)

**Figure 3.**

The common workflows in software development.

Show All

Once code gets released and enters production, new issues can arise that were not caught by previous stages. The process must account for how such issues are tracked. The production stage would typically also include some telemetry that helps with bug isolation. Feedback from production kicks off a new cycle, starting again from the individual stage.

The previous sections talked about concepts that are primarily applicable in the code-editing phase of the individual workflow. In addition to those ideas, the most visible developer-facing use of ML in the code-editing phase is autocomplete, which has been widely studied and deployed. More ambitiously, ML techniques can also help developers complete code via program synthesis.

Significant opportunities exist in the other states—for example, we had previously mentioned our own work on predictive regression test selection1 and triaging crashes2—but a detailed discussion of these is outside the scope of this brief article. Here, in our view, are some of the most promising but relatively untapped opportunities for using ML pertinent to aspects of the team and production states.

- _Code review_: Code review, while widely regarded as essential for maintaining software quality, is also a significant time commitment for software engineers. ML techniques can help automate routine code reviews (such as formatting and best coding practices). More ambitiously, perhaps ML can also automatically resolve a routine code-review comment.

- _Assessing the risk of a code change_: In principle, any code change increases the riskiness of an application. Arguably, the entire testing and verification pipeline exists essentially to reduce this risk. Can we design ML-based techniques that provide a quantitative assessment of the risk of a code change, complementing the usual testing and verification pipeline? Advances here will impact both testing (by prioritizing tests related to riskier changes) and release management (by carrying out additional quality control for riskier code releases). By comparison, techniques for assessing the impact of a change (e.g., Reb et al.18) take a binary view of affectedness and, due to the limitations of static analysis, often would be overly pessimistic in their assessment.

- _Troubleshooting_: For widely deployed applications, customers send their feedback implicitly (telemetry or crashes) and, sometimes, explicitly by sending comments. The volume of this feedback can be huge. This is another area where ML can help in multiple ways: not only in triaging these reports, but clustering them to identify common issues, finding important clues from telemetry logs and code changes that could be connected to the issue at hand.


With renewed interest in ML and an emerging uniformity of software development processes (common repositories as well as continuous integration and release), industry is ripe for absorbing these ideas into the mainstream. At Facebook, we certainly are transforming our development process to be as data driven as possible.

## Authors

## Figures

## References

## Citations

## Keywords

## Metrics

More Like This

[Video-Based Empathy Training for Software Engineers](https://ieeexplore.ieee.org/document/11024334/)

2025 IEEE/ACM 37th International Conference on Software Engineering Education and Training (CSEE&T)

Published: 2025

[Data mining: A tool for knowledge discovery in human aspect of software engineering](https://ieeexplore.ieee.org/document/7124792/)

2015 2nd International Conference on Electronics and Communication Systems (ICECS)

Published: 2015

Show More

**References is not available for this document.**

### IEEE Account

- [Change Username/Password](https://www.ieee.org/profile/changeusrpwd/showChangeUsrPwdPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
- [Update Address](https://www.ieee.org/profile/address/getAddrInfoPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)

### Purchase Details

- [Payment Options](https://www.ieee.org/profile/payment/showPaymentHome.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
- [Order History](https://www.ieee.org/profile/vieworder/showOrderHistory.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
- [View Purchased Documents](https://ieeexplore.ieee.org/articleSale/purchaseHistory.jsp)

### Profile Information

- [Communications Preferences](https://www.ieee.org/ieee-privacyportal/app/ibp?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
- [Profession and Education](https://www.ieee.org/profile/profedu/getProfEduInformation.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
- [Technical Interests](https://www.ieee.org/profile/tips/getTipsInfo.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)

### Need Help?

- **US & Canada:** +1 800 678 4333
- **Worldwide:** +1 732 981 0060

- [Contact & Support](https://ieeexplore.ieee.org/xpl/contact)

- [About IEEE _Xplore_](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/about-ieee-xplore)
- [Contact Us](https://ieeexplore.ieee.org/xpl/contact)
- [Help](https://ieeexplore.ieee.org/Xplorehelp)
- [Accessibility](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/accessibility-statement)
- [Terms of Use](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/terms-of-use)
- [Nondiscrimination Policy](http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html)
- [Sitemap](https://ieeexplore.ieee.org/xpl/sitemap.jsp)
- [Privacy & Opting Out of Cookies](http://www.ieee.org/about/help/security_privacy.html)

A not-for-profit organization, IEEE is the world's largest technical professional organization dedicated to advancing technology for the benefit of humanity.

© Copyright 2025 IEEE - All rights reserved. Use of this web site signifies your agreement to the terms and conditions.


The Identity Selector: Persistence Service
