# IR-Assign02

# CSCI 4030/ CSCI 6030/ DASC 6030: IR
# Programming Assignment No: 02
## 1 Assignment Goal  
Develop expertise in constructing positional indexes and processing phrase and proximity queries.  

## 2 Problem Statement  
Given a text corpus, develop a positional index. Process phrase and proximity queries using the positional index.  

## 3 Text Corpus  
You will be provided a large document corpus (about 50,000 documents). The corpus will be provided in ASCII file format. Each document will come in a separate physical file. You are responsible for normalizing the text.   

## 4 Solution Steps  
Following are high-level solution steps. You may need to make several decisions in each step related to low-level implementation details. Think about alternatives, articulate their pros and cons, reason about their algorithmic correctness and efficiency, and make informed decisions. It is strongly encouraged that hold one or two brainstorming sessions with your team members to strategize a solution before you delve into code-level details.  
1) Normalize text – address punctuation characters, stemming/lemmatization, and lowercasing. Do not throw away stop words.  
2) Extract tokens and identify vocabulary for the dictionary.  
3) Scan the corpus and build a positional index.  
4) Implement the algorithm for processing phrase/proximity queries (page 39 of textbook, Figure 2.12). However, if you choose to, you may use a different algorithm.  
5) Proximity queries are limited to only one parameter type: maximum distances between words. For example, consider the query: united /0 states /3 enraged /2 actions. Proximity queries of this assignment are not required to handle parameters such as: within the same sentence, and within the same paragraph.  
6) Develop a simple interface for users to specify phrase/proximity queries. The interface can be as simple as prompting the user for a phrase/proximity query (i.e., a text string). You may also read a phrase/proximity query through command line arguments.
7) Design test cases and execute them. Document execution results.  
8) Submit your source code files, instructions for compiling and running your program, and results from execution of your test cases. Upload all documents to Blackboard.  

**This is an involved project. It is essential that all your team members actively contribute to the project. Get started early. Spend upfront time on your algorithm and data structure choices. Seek help from course TAs in addition to the instructor. Course TAs are also available for phone appointments.**
