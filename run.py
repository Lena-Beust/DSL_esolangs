import subprocess 
for prog in range(0,4):
    if prog == 0 :      # our program
        prog_name = "p.rock"
        print(f"****** {prog_name}")
    else :      # generated program by the AI
        prog_name = f"llm/p{prog}.rock"
        print(f"****** {prog_name}")
    
    for i in range(1,5):
        filename = "0" + str(i)
        with open(f"tests/{filename}.in") as input_test:
            p = subprocess.run(['./binaries/rockstar', prog_name], input=input_test.read(), capture_output=True, text=True)
            res = p.stdout
                
        
        with open(f"tests/{filename}.out") as output_test:
            wanted = output_test.read()
            
        status = "Pass" if res == wanted else "Fail"
        print(f"test {i} : {status}")
        
    print("\n")
    
