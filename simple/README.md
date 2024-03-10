This version is utilising siple version of this arhitecture. Text input is just plain text. Nex the ai element modifies it ading 

Database element:
| type (of element) | title (helps in finding right element) | content () | source (who or where is it from) | (comment) |
|----------|----------|----------|----------|----------|
| memory | topic of memory | message or conversation | who said, or sides of conversation | It is holding individual information from input or other sources |
| information | topic | information | list of sources | Well supported general information, that the AI uses in generation iof response |
| grammar | gametic word or symbol | pattern | na | Used for structuring output, and perhaps for input, not in first version |
| user | name | info about user | na | It holds information about user |
| feedback | summary | opinion | who said opinion | It holds opinions on AI from users. It can be used to improve the AI |
| intentions | type of intention | content | for who | Those are the things, that AI will do. It is holding more and less abstract tasks based on user requests, and other intentions |

The input for text:
| username | massage | timestamp |
|----------|----------|----------|
| vertigp | How tall is the Eiffel tower? | 1710014077 |
| added by interface, or by input AI (default "unknown") | from user | added by input AI |

The segments are going to be separated by "•".

example filling nissing data:
| input | output | comment |
|----------|----------|----------|
| Sherlok Holms•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m. | Sherlok Holms•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m.•1710071499 |  |
| 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m. | unknown•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m.•1710071499 |  |

| input | output | comment |
|----------|----------|----------|
| Sherlok Holms•At 9:00 a.m. the British ambassador to Berlin Nevile Henderson is instructed by the Cabinet to deliver an ultimatum to Germany which expired without answer at 11:00 a.m.•1710071499 | memory•Nevile Henderson position•Nevile Henderson was British ambassador to Berlin•Sherlok Holms••memory•Nevile Henderson task•Nevile Henderson was instructed by the Cabinet to deliver an ultimatum to Germany•Sherlok Holms••memory•reacrion to ultimatum•ultimatum send from Nevile Henderson to Germany expired at 11:00 without reply•Sherlok Holms |  |