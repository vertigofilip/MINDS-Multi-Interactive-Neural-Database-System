The simple version of MINDS is based on SQL database that contains data in the format explained below. 
The first part os MINDS AI that should be created is simple text input. This will then allow us to create materials for the next parts of this AI.

List of elements to do:
in progress:
- user input

main To Do:
- memory to data converter
- memory to task converter
- data analyser
- task analyser
- text output

additional To Do:
- text input
- comaln line input
- comand line output
- screen input
- immage input
- immage output
- GPIO input
- GPIO output

Database element:
| type (of element) | title (helps in finding right element) | content () | source (who or where is it from) | timestamp | (comment) |
|----------|----------|----------|----------|----------|----------|
| memory | topic of memory | message or conversation | who said, or sides of conversation | when did the think happen | It is holding individual information from input or other sources |
| information | topic | information | list of sources | when did the information was last updated | Well supported general information, that the AI uses in generation iof response |
| grammar | gametic word or symbol | pattern | na | date of last update | Used for structuring output, and perhaps for input, not in first version |
| user | name | info about user | na | date of creation | It holds information about user |
| feedback | summary | opinion | who said opinion | date of creation | It holds opinions on AI from users. It can be used to improve the AI |
| intentions | type of intention | content | for who | date of creation | Those are the things, that AI will do. It is holding more and less abstract tasks based on user requests, and other intentions |

The input for text:
| username | massage | timestamp |
|----------|----------|----------|
| vertigp | How tall is the Eiffel tower? | 1710014077 |
| added by interface, or by input AI (default "unknown") | from user | added by input AI |

The segments are going to be separated by "•".

example filling missing data:
| input | output | comment |
|----------|----------|----------|
| Sherlok Holms•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m. | Sherlok Holms•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m.•1710071499 |  |
| 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m. | unknown•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m.•1710071499 |  |

| input | output | comment |
|----------|----------|----------|
| Sherlok Holms•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m.•1710071499 | INSERT INTO table_name VALUES (memory, Nevile Henderson position, Nevile Henderson was British ambassador to Berlin ,Sherlok Holms, 1710071499); INSERT INTO table_name VALUES (memory, Nevile Henderson task, Nevile Henderson was instructed by the Cabinet to deliver an ultimatum to Germany, Sherlok Holms, 1710071499); INSERT INTO table_name VALUES (memory, reacrion to ultimatum, ultimatum send from Nevile Henderson to Germany expired at 11:00 without reply, Sherlok Holms, 1710071499);
 |  |
