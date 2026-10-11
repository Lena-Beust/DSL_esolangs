import subprocess 
for prog in range(1,4):
    print(f"****** p{prog}.rock")
    prog_name = "p" + str(prog) + ".rock"
    for i in range(1,5):
        print(f"test {i}")
        filename = "0" + str(i)
        with open(f"tests/{filename}.in") as input_test:
            p = subprocess.run(['./binaries/rockstar', prog_name], input=input_test.read(), capture_output=True, text=True)
            res = p.stdout
        
        with open(f"tests/{filename}.out") as output_test:
            wanted = output_test.read()
            
        print(res == wanted)
        
    print("\n")
    
