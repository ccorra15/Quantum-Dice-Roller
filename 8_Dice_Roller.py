import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3)

# Put 3 qubits in superposition
circuit.h(0)
circuit.h(1)
circuit.h(2)

# Collapse the qubits from superposition
circuit.measure_all()

# Simulate the circuit once
job = execute(circuit, simulator, shots = 1)

# Retrieve the result from the job
result = job.result()

# Retrieve the number in binary
number_binary = list(result.get_counts(circuit).keys())[0]

# Turn the binary number to decimal
def binaryToDecimal(n): 
    num = n
    dec_value = 0
      
    # Initializing base  
    # value to 1, i.e 2 ^ 0 
    base1 = 1
      
    len1 = len(num)
    for i in range(len1 - 1, -1, -1): 
        if (num[i] == '1'):      
            dec_value += base1
        base1 = base1 * 2
      
    return dec_value
  
# Print the number in decimal form
print("Your Quantum number is: " + str(binaryToDecimal(number_binary))) 