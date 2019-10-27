import hashlib
import pyfiglet
import argparse
from time import time

global result 

def figlet(text):
    a = pyfiglet.figlet_format(text)
    print(a)

def get_arguments():
    parser = argparse.ArgumentParser(description='Brute.MD5.# v1.0')
    parser._optionals.title = "Optional Arguments"
    parser.add_argument("-o", "--output", dest="output", help="Output file name to save Result in Text")

    required_arguments = parser.add_argument_group('Required Arguments')
    required_arguments.add_argument("-p", "--pass_hash", dest="pass_hash", help="MD5 Hash to Crack it.", required=True)
    required_arguments.add_argument("-w", "--wordlist", dest="wordlist", help="Wordlist for Bruteforce Attack.", required=True)
    return parser.parse_args()

def crack_md5(wordlist, pass_hash):
    flag = 0
    attempts = 0

    try:
        pass_file = open(wordlist, 'r') 
    except Exception as e:
        print("[+] No File Found!")
        quit()

    print("[*] Attempting to Crack Password Hash...")
    print("[*] Please wait for a while!")
    
    current_time = time()
    
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()    #One liner md5 encoder using hashlib.md5()
        
        attempts += 1   #To count total no. of attempts done by program.
        
        if digest == pass_hash:
            global result
            result = word     #Updating Result for save_result() function
            print(f"[+] Password Found : {word}")
            print(f"Total Attempts to Crack MD5 Hash: {attempts}")
            flag = 1
            break     #Want to break "for loop" after finding correct answer.
        
    if flag == 0:
        print("[-] Sorry! Unable to find correct password :(")
        print(f"Total Attempts to Crack MD5 Hash: {attempts}\n")

        
def save_result(pass_hash, result, file_name):
    if result == "":
        failed_result = f"[*] MD5 Hash : {pass_hash}\n[!] Result : Password Not Found in Wordlist"     
        with open(file_name, 'w') as f:
            f.write(failed_result)

    else:
        cracked_result = f"[*] MD5 Hash : {pass_hash}\n[+] Cracked Password : " + result
        with open(file_name, 'w') as f:
            f.write(cracked_result)            

if __name__ == '__main__':
    #==================================================================================================================
    #For Fancy Styling 
    #==================================================================================================================
    figlet('Brute.MD5.#')   
    print("Author: Pushpender  |  Website: https://technowlogy.tk\n")
    print("-"*70,"\n")
    #==================================================================================================================
    run_save_result_function = 0
    
    arguments = get_arguments()   #Taking Arguments from the Function
    #==================================================================================================================    
    if arguments.output == None:
        print("[!] Output File Not Defined, Result will Not Going to be saved!")

    else:
        print(f"[*] Output File Specified, Saving Result in \"{arguments.output}\" file.")
        run_save_result_function = 1
    
    crack_md5(arguments.wordlist, arguments.pass_hash)   #Calling Main Cracker Function
    #==================================================================================================================
    if run_save_result_function == 1:
        save_result(arguments.pass_hash, result, arguments.output)

    else:
        pass
        
    print("-"*70,)   
    