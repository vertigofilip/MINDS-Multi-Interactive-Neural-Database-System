# MINDS-Multi-Interactive-Neural-Database-System
I have decided to start AI project based on hierarchical database containing elements such as memories, intencions, etc and relativly simple AI models and scripts. Scripts are planed to be in 3 categories: input creating "memory elements" in database, procesing taking allready created database elements and modifying, deleting, ang creating new onese, and output creating rturning content.
The idea behind this architecture is, that the AI chatbot wil breakdown problem in database using AI scripts, other AI scripts will be cheacking is there are enouth informations to finish the request, and all of hir will create stem by step plan to follow for other scripts, that are going to make this plan reality.
Learninf for that AI is going to invove AI scripts analising memories and allready existing elements. The scripst analising those database elements are going to divide, modify, and compair existing database elements in order to determine if information are internali consistant, and it are good enouth to support themself. If this won't be the case the AI will loock for aswers.


This multi model neural network is in very early development. The idea of this AI is changing constantly. Current two files are retraining data for existing AI I want to used to accelerate progress. They separate understanding of text from understanding of tasks required from AI in order to create different input modes for safety. In its current form input text is intended to be provided to both neural networks, however it is going to be changed in the future to working in line in order to allow this one neural network to interact with different forms of input. The entire AI is going to work based on database containing elements with fields 'type', 'name', 'information', and 'source'. The types of those are going to be: 'goal', 'memory, 'knolage'. The networks and scripts working on them are going to be decided into input, maintenance and output nodes. Input nodes are going to create database elements based on input, maintenance are going to create, delete, and modify them in order to process information, analyze them and modify behavior of AI, and output are going to generate output based on the database elements.
