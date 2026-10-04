import ollama
name =  input("enter the name: ")
branch = input('enter the subject: ')
print(f"Hi {name} from {branch}")

SYSTEM = '''
You expalin programming error messages to a 2nd year engineering student.Reply in 3 parts.
1) what it means in plain english.
2) the likly cause
3) how to fix
keep it under 120 words.
'''
while True:
    data = input("Enter the error message or'exit' to stop: ")
    data = ("Enter the")
    if data.lower() == "exit":
        print("goodbye")
        break

    elif question.lower() == "history":
        print("\n----chat history---")
        for message in messages:
            if message["role"]=="user":
                print("you:",message["content"])
            elif message["role"] == "assistant":
                print("Bot: ",message["content"])
            print("---------------\n")

response = ollama.chat
(model-"gemma3:1b",
    messages=[
    {
         "role":"system",
         "content":"SYSTEM"
    },
    {
             "role":"user",
             "content":"python error-NameError: name 'x' is not defined"
    }
]
)
print(response.message.content)