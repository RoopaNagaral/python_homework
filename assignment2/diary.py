import traceback

#Task 1
try:
    with open('diary.txt','a') as file:
        message = ""
        i = 0
        while i < 2:
            if message == "done for now":
                break
            elif i == 0:
                message = input("What happened today?")
                file.write(message + '\n')
                i += 1
            else:
                message = input("What else?")
                file.write(message + '\n')
            
                
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")