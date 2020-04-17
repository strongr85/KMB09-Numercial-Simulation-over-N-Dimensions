# ctrl+K+C  /   ctrl+K+U

import csv
import math 
import random
import string
import re

## Time code
#import time
#t0 = time.time()

no_of_qubits = 10
no_of_dimensions = 2


def check_state(element):
    if element.find("e") == 0:
        bit =1
    else:
        bit = 0
    return bit

def check_index(element):
    number = re.search(r'\d+', element).group()

    return int(number)

print(" ************************* KMB09 NUMERICAL SIMULATION *************************")

print('Input number of Dimensions : ')
tmp_dimensions = input()  # read a single line and store it in the variable "name"

if int(tmp_dimensions)<2:
    print('Wrong input, Simuating on 2 Dimensions.')
    no_of_dimensions = 2
else:
    no_of_dimensions = int(tmp_dimensions)

print('Input number of Photons : ')
tmp_photon = input()  # read a single line and store it in the variable "name"

if int(tmp_photon)<10:
    print('Wrong input, Simuating on 2 Dimensions.')
    no_of_qubits = 10
else:
    no_of_qubits = int(tmp_photon)

print("input: ",int(tmp_dimensions),no_of_dimensions)

basis_e =  [string for i in range(no_of_dimensions)]
basis_f =  [string for i in range(no_of_dimensions)]

for x in range(no_of_dimensions):
    basis_e[x] = "e_"+str(x)
    basis_f[x] = "f_"+str(x)

#for x in range(no_of_dimensions):
#    print (basis_e[x],basis_f[x])


Alice_elements =  [string for i in range(no_of_qubits)]
Bob_elements =  [string for i in range(no_of_qubits)]

index_data_alice = [int for i in range(no_of_qubits)]
index_data_bob = [int for i in range(no_of_qubits)]

bits_bob = [int for i in range(no_of_qubits)]
key_data = [int for i in range(no_of_qubits)]
final_key = [int for i in range(no_of_qubits)]

#/////////////////////////////// Random states generation at ALICE//////////////////////////////////
for qbits in range(no_of_qubits):
    x = random.randint(0, 1)
    if x == 0:
        tmp_state = random.randint(0, no_of_dimensions-1)
        Alice_elements[qbits] = basis_e[tmp_state]
        index_data_alice[qbits] = tmp_state
    else:
        tmp_state = random.randint(0, no_of_dimensions-1)
        Alice_elements[qbits] = basis_f[tmp_state]
        index_data_alice[qbits] = tmp_state


#/////////////////////////////// Random Basis mesurement at BOB //////////////////////////////////
for qbits in range(no_of_qubits):
    x = random.randint(0, 1)
    if x==0:   #
        if Alice_elements[qbits].find("e")==0:
            #print("DONE")
            Bob_elements[qbits] = Alice_elements[qbits]
            index_data_bob[qbits] = check_index(Alice_elements[qbits])
        else:
            #Bob_elements[qbits] = "K"
            state = random.randint(0,no_of_dimensions-1)
            Bob_elements[qbits] = basis_e[state]
            index_data_bob[qbits] = check_index(basis_e[state])
    else:
        if Alice_elements[qbits].find("f")==0:
            #print("DONE")
            Bob_elements[qbits] = Alice_elements[qbits]
            index_data_bob [qbits]= check_index(Alice_elements[qbits])
        else:
            #Bob_elements[qbits] = "K"
            state = random.randint(0,no_of_dimensions-1)
            Bob_elements[qbits] = basis_f[state]
            index_data_bob[qbits] = check_index(basis_f[state])


    #print(qbits,Alice_elements[qbits],Bob_elements[qbits],index_data_alice[qbits],index_data_bob[qbits])



print("Alice_elements \t Bob_elements \t Alice Index \t Bob Index")
for qbits in range(no_of_qubits):
    print(Alice_elements[qbits]," \t\t ",Bob_elements[qbits]," \t\t ",index_data_alice[qbits]," \t\t ",index_data_bob[qbits])

#/////////////////////////////////////////// key generation ///////////////////////////////////////////////////
print("\n\n =============================================================================================== \t")
no_of_key_bits = 0
for qbits in range(no_of_qubits):
    if(index_data_alice[qbits]!=index_data_bob[qbits]):
        #print(qbits)
        key_data[no_of_key_bits] = check_state(Bob_elements[qbits])
        no_of_key_bits = no_of_key_bits +  1


print("\n\n Key generated : ")

for qubit in range(no_of_key_bits):
    print(key_data[qubit], end=" ")

#f = open('KMB09_Numerical.csv', 'a')
#with f:

#    writer = csv.writer(f) 
#    writer.writerow(str(no_of_dimensions))
#    #writer.writerow(key_data)
#    writer.writerow(str(no_of_qubits))
#    writer.writerow(str((no_of_key_bits/no_of_qubits)*100))
#f.close()

#for x in range(no_of_key_bits):
#    print(key_data[x])

print("\n\n ===============================================================================================")

print("\n\n\t\t Efficinecy : ",(no_of_key_bits/no_of_qubits)*100," %")

print("\n\n\t\t No of Qubits : ",no_of_qubits,"\t with ",no_of_dimensions," Dimenions.")


#for qbits in range(no_of_qubits):
#    print (Bob_elements[qbits],index_data_bob[qbits])



