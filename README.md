# zalgo-cli
A command line zalgo text generator.

I created this because I wanted to use a zalgo-text nickname on Discord. 
But the online generators that I found tended to generate text of a rediculous
length if you wanted it to look good. There was also the problem of having to 
generate it multiple times to find one that looked good.

This program solves both of these issues. You can choose a maximum character limit, and the
program will evenly distribute the combining characters across the string. You can also
choose how many different strings to generate, so you can look through them and find
the one that you like the most.

## Sample usage
```
$ python zalgo.py 
Initial string: fydrenak
Character limit [0 for no limit, min 16]: 32
Amount to generate: 64
f̥͋͟ẙ̨̡ď̢̚r̺͎͞e̻̾͋n͔ͯ͟â̭ͯk̸̨̍	f͒̔̍y̯͐ͥḓ̛̈́ŗ̀͊ḛ̾́n̅ͥ͞á̭̼k̭̇͒	f̵̍͟y̷ͮͫd͒ͨ̕r̽͛ͭé́́n͉̱ͪa͍͚͓k͇͓͋	f̧ͪͩy̅ͩͨd́͆̚r̮̿̓e̶͍̯n̠͎͊a͖̾͗k̝̀̈́
f͖ͭ̇y̟̤̖ḓ̝̇ṛ͇ͅe̬̓͢n͊̕͡ả̘̄k̼ͣͅ	f͕ͬ͘ÿ́̒ͦd̩̣ͨr̴͒͠e̠̬ͬn͇̾ͥà͑͐k̨̓̕	f͖͋̈́y̴͈̽d̗̋̔ŕ̩̭e͙ͤͮñ͛͊ą̠ͨk̷̺ͣ	f̢ͣ̉y̸͕̻d̓̄͜ŗͬ̓eͧ̌͠nͧ͆̕a̟ͭͯk̟̺̽
f̟͂͡y̮͔͞d͔̣̚r͐͟ͅe̸͙͡ṉ͂ͧà̛ͧk̃ͬ͡	f̛̳͡ÿ̷͎́ď̛̬r̸̢͑e͎̍̐n̤͊̕a̱̠͊k͎ͮ̕	f͇̽̈y̖̤ͨd̖͆́r͖̻̉e̖ͮ͡n̯̣̼a͎̝̍k̜̿ͯ	f̿ͬ̓y̳̜͊dͪ͋̉r̴̠ͧe̝̩͢n̷̞̰ă̔͞k̙̍͑
f̟ͩ̈́y̭ͮ̎d̙͓ͣr̥͎̄ẽ̝̾ņ̸͗ạ̅͠kͧ̔͜	f̯ͨ̾y̡̹̞d̫͇̽ȑ͎̟e̢̯̽n͏̷͗ȧ̰ͫk̻̅͆	f̡͋̏ŷ̦ͤd̨͙̒rͫ͌̕ĕ͌͒ņ̦͑ã͇̽k̀ͣ̊	f̧͇̤y̻̟̜d̠ͨ̓r̥̄͏e͕ͬ̈́n̘͒̚a͚̍̄k̘̰̬
f̲̫̉ȳ̟͋ḑ̓͒r̗ͨ͆ê̶̠n̘͐̄a̗̐̇k̟̻̉	f̢ͩ̆ÿ́̑̈́d̾ͮ͊ṛ̮̌e̬ͯ͟n̠̉̏a͎̍̇k̬ͫ̓	f̍̏̑ỳ̞̳d̉͋̕r͛ͧ͟e̠̞̽n͉̿͡a͔͒ͥķ̥̅	f̢̪ͯy̜ͧ͜d͎̑̃r̝͊̓e̦͔̩n͖͙͆a̞͑ͧk̩̉͟
f̛̙͋y̑̔͜d̠́̂r̦̙͍eͨ̇̎n̳̫ͮa̓͌̂k̪̀̕	f̶̮͖y̮̗̽d͙ͩ͡r̩͎͖eͩ́̒n͔͐͡à̲̀ǩ͔͘	f͓͋̕y̵̒͟d͓̺̔r̮ͩ͡é̶̜nͭͪ̐à͓̩ḱ͐͢	f̱̖̠y͙͉̍d͖ͮ̊r̬ͯ̒e̗ͮ̇n̓̀̆aͬͧ͛kͫ͐͠
f̬͑ͬy͊ͩ̉d̸̈́̏r̡͔ͫe̡͌ͨṅ̶͔ȁ͙̫k̺̂̾	f̢̼ͣÿ͍͞d͒̆̀r̪̆͡e̖̰͋n̨͇ͅa͎ͩ͊k̵͞͞	f̾̎́y͖͚̚d̛̺̓r̭̳̈́e͓͇ͩn͇̤ͫa̗̤̋k̨̈͝	f̡̐͞y̢̼͌d̺̓̔r͍̖͒e͎̙ͦn̳͂͌a̴̕͟k̘͆͏
ḟ̹̀yͮ̓̃d̹͍̊r̐̅ͧe̢̬̓n͔̮̾à̂̕k͇̬̍	f́͊͗y͇̣͕d͕ͮ͑r̴̩ͮẻ̷̘n̫̋̿a̔ͮ̌ǩͦ͛	f̷̵̭y̨̝͌d̹̑ͯrͤ͗̑e̸̠̽n͎̰̆a͏̳ͯk͇ͨ͠	f̱̪ͅy͏̵̓d̦̖́r̋̅̄ĕ̹̇n̞͜͞ǎ̇̋k̸̦̒
f̶ͨ͜yͦ̈̽d̦̺̗r̲̲̓e̴͕̾n͍͋̕ȁ̰͜k̛͓͟	f̶̳͈y̫̐̈́d͚͔͑ŕ̘͙ě̛̜n̬͉͛aͦͤ͜k̛̔̓	f̢ͭͅy̷̫̒d̪̫͆r̶̕͡e̖̿͐n̗ͪ͟aͭͩ̕k̞̚͝	f̶̶̡y̷̯̅d̴ͭ̑r̨̀͠ë͈̳́n̦̒͠a̘̓ͅk̰̝̍
f̸̼ͩỳ͇͚d̟̔ͯr̙̮̩ḛ͇͑n̨̲ͅả̩̫k̸͙ͫ	f̼̜͇y͉̿͋d͏̆̕r̬̣̔ë͖́̂nͫ͋ͧa̟̰̱ḵ̶̢	f̉ͤ͜y̓͊͌dͥ͏ͮrͯͯ̔e̶͉ͨn̖̣ͥa̴̘̋k̴͔̕	f̤̾̀y̍͏ͫḏ̟ͦr͖̯̼eͯ͢͡ǹ̛̩ả͉̽k̋ͦ̃
f͙ͮ͢y̗ͦ̾d̷̵͇ȓ̯ͯȇ̝ͫn̢̲͆a͈̋̀k͇̺̇	f̶͇̰y̠̮͊d͌ͬ͜r͙̍͂e̙͗̔n̪̺̐a̵͔̦k̨͒͜	f̺̣͢y̨͔ͮd̳̆̆r̛̍̽e̼̰̟ǹ͎͠a̶̗̠k͙͈͇	f̛̈́̓y͉͍͡d͙͖̿r̶̪͛e̢̪̣n̞̬̽a͏̔̈ķͩͪ
f̡͍͚y̷̓͠ḑͪ̀r̗̈̽e͙̪̎ǹ̢͎a͈̘̓ḱ̻̋	f̙̜̬y̝͔͌d̩̻̈r̠̩ͧe͉̹̝n͈͂̕a̮̋ͥḳ̄̅	f͊̈́͟ý̩̕d̗̬̤r͙̟̃e̊̇́n̪̊ͬä̤̱k͍̯ͣ	f̶̩͙y̠ͤ͡d̯̥̊ŕ̥͉ḙ̴̘ṇͪͣa̋ͦ̽ķ̟ͣ
f̗́͒y̘̓̕d̫̫͟rͦͥ͜e͖ͨ́ñ̆͘a̼̼͆ḳ̵͎	f̨̞̄ŷ̾ͯd̢̋͞r͈ͩ͞ẹ͇̅n̟͆͝a̗ͩ̚k̵͇̓	f̷̃ͥy̙̐ͤd̮̘ͩr̞͒͝e̐͏̓n͓͒ͬă̩̼k̴̒̾	f̖͑̀y̭ͬ̇d̸ͨ̕r̫̈́̀ĕ̒ͩń̜ͧá̧͇k̪ͣ̐
fͪ͏ͥy̸ͤ̚d̴̻͋r̤͆͟e̯͈̲n̵̒ͨã̭̀ḱ̶ͅ	f͔̎̒y̓̊͢d̏ͧ͢ŗ̨͌e͎͚̊n͚̒̎a͈͑ͣk̡̮ͪ	fͥ́͟y̨̗͗d̡̓ͤr͓ͣ̆e̥͋ͨn̝͜͏a͈͌̑kͥ̂͂	f̟͍͑y̮̗͑ď̮̗r̭ͨ̋e͚̫̭ṅ͖̠aͭ̏̊k̮̐͐
f͎̞̓y͙̥͠d̼̹́r̷͢͢é͗̎n͈͗ͤa̮̽͟k̗͟͢	f̧̤͎y͎̏̉d̷̳̄r̩͑͋ḛ̼͗n͏͉ͤȃͬ̚k̈́̈́͝	f̞͖ͤy̖̓̉d̥ͣ̓r̥͉̖e̶̡̕nͦ̈̐à̚͠k̬͈̂	f̰̤͗ŷ͚͑d͈̜̑r͔ͣ́e̜ͩ̾n̐́͘à̡ͯk̻ͭͅ
f̙̣͍y̥̔ͅd̎̽ͥṟ̲̠eͥ̇͠n͍̆́ā̑ͥk̘͈̊	f̭̅̒ý̡̑d̔́͞r̬̋ͯe͍̾ͩn̻̂ͅḁͧ̏ķ̝̐	f̛̀̆y̴̜̘d͔̓̚r͍̝͐è̱͞n͎̓͠a̶̻̗ǩ̝͞	f̵̑ͤy̺͍͘d̵̡̘r̀͛̚ê̷̿n̻̓͂a͍̍̽ḵ͗̓
```
