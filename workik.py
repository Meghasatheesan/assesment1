import google.generativeai as genai
def getanswers(question):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(question+ "plan my day with the given information")
    output=response.text
    print(output)

if __name__=="__main__":
    
    s=input("what are your plans for today: ")
    n=0
    genai.configure(api_key="AIzaSyDs19MSWDaGOHkTgUAVakSgWXqpHTrB_jY")
    getanswers(s)
    
    while True:
        choice= input("do you need more help: ")
        if choice.lower()=="yes":
            s=input("provide me with more information :")
            getanswers(s)
        else :
            getanswers("generate my schedule based on the provided information only")
            break
        
            