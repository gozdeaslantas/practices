s = input().strip()
sArr = s.split('.')
sentences = []
sentence = ''

'''
    sArr[0] = 'In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance'
    sArr[1] = 'Such were Willarski and even the Grand Master of the principal lodge'
    ..
    sArr[2] = 'What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that'
'''
for i in range(len(sArr)):
    sentence = sArr[i]
    if len(sentence) > 2 and len(sentence) < 10000:
        sentences.append(sentence +'.')
        sentences.append('\n')
        
    if sentence.find('!') > -1 and not sentence.startswith('"'):
        excArr = sentence.split('!')
        for exc in excArr:
            sentences.append(exc + '!')
            sentences.append('\n')
    elif sentence.find('?') > -1 and not sentence.startswith('"'):
        quesArr = sentence.split('?')
        for ques in quesArr:
            sentences.append(ques + '?')
            sentences.append('\n')
    elif sentence.startswith('"'):
        quotesArr = sentence.split('"')
        for quotes in quotesArr:
            sentences.append('"' + str(quotes) + '"')
            sentences.append('\n')
    else:
        sentences.append(sentence + '.')
    
    
print(''.join(sentences))
