The simple version of MINDS is based on SQL database that contains data in the format explained below. 
The first part os MINDS AI that should be created is simple text input. This will then allow us to create materials for the next parts of this AI.

List of elements to do:

in progress:
- user input

main To Do:
- memory to data converter
- memory to intentions converter
- data analyser
- intentions analyser
- text output

additional To Do:
- text input
- comand line input
- comand line output
- immage input
- immage output
- screen input
- GPIO input
- GPIO output
- scheduler

Database element:
| type (of element) | title (helps in finding right element) | content () | source (who or where is it from) | timestamp | (comment) |
|----------|----------|----------|----------|----------|----------|
| memory | topic of memory | message or conversation | who said, or sides of conversation | when did the think happen | It is holding individual information from input or other sources |
| information | topic | information | list of sources | when did the information was last updated | Well supported general information, that the AI uses in generation iof response |
| grammar | gametic word or symbol | pattern | n/a | date of last update | Used for structuring output, and perhaps for input, not in first version |
| user | name | info about user | n/a | date of creation | It holds information about user |
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
| Mahatma Gandhi•Explain the principles of satyagraha (nonviolent resistance) and its role in the Indian independence movement.•2407031545 | INSERT INTO work_space VALUES (memory, User wants to generate explanation of the principles of satyagraha (nonviolent resistance) and its role in the Indian independence movement, user/Mahatma Gandhi, 2407031545); |

 | element | function | comment |
|----------|----------|----------|
| user input | generates memories mased on text input, they can contain tasks for M.I.N.D.S. system, this input can cuse generatipon of task element |  |
| memory to data converter | this scripts is generating small pices of informations based on memories |  |
| memory to intentions converter | this scripts is generating intentions based on memories |  |
| data analyser | compairs, modify, and combines informations into networks of wikipedia like definitions, and additional mrta informations | there are going to be more than one |
| intentions analyser | checks if user is allowed to ask for something and splits intentions into smaller intentions necesery for thei complitions |  |
| text output | this scripts is generating text oiutput based on intentions, and informations |  |
| text input | This input is ment wot inputing data without sreating tasaks, it function is to get informations, and ignore any potencial comands | might be removed, and replaced with something else |
| comaln line input | spesific, and relativliy simple and low cost method of interacting with operating system |  |
| comand line output | spesific, and relativliy simple and low cost method of interacting with operating system |  |
| immage input | this input is ment to accept files, and camera input for use to identify objects, and other immage oriented tasks |  |
| immage output | immage generating script | the description of immage is going to be build using descriptions of element of that immage until description is detailed enouth for that script |
| screen input | is specific OS interface for interacting with GUI | alternative specific interfaces are going to be added, this is generic interface |
| GPIO input | relativliy simple and low cost method of controling simple electronics like servo mechanism, leds, etc  |  |
| GPIO output | relativliy simple and low cost method of reciving data from electronics like distance sensors, co2 detectors, load cels, etc |  |
| scheduler | this is going to be cost effective whay of setting tasks to be done in the future using seperete database using timer to put correct tasks back to main database at the right moment | this is going to prevent tasks scheduled from taking up time of other scripts |
