
import requests
import pprint
 
i = 0
for i in range(1,255):
    r = requests.get('https://pubgleague.dmm.com/team/profile/' + str(i))

    print(r.text)
    
    source = r.text
    with open(str(i) + '.html', 'w', encoding='utf-8') as w:
        w.write(source)
    i += 1
w.closed
 
 
 
