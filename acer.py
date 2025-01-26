# use someones data who has already done the work for you
from gemini import get_gemini_response

while True: # read input from user and print response
    inp = input('Please enter: ')
    result = get_gemini_response(inp)
    if inp == 'bye':
        break
    print('reponse:' , result['candidates'][0]['content']['parts'][0]['text']) 
   