from qiskit import QuantumCircuit

# 3-qubit Bit-Flip Error Correction Code
qc = QuantumCircuit(3)

# Encoding: Copying the state of qubit 0 to qubit 1 and 2
qc.cx(0, 1)
qc.cx(0, 2)

qc.barrier()
# --- SIMULATING AN ERROR ---
# Imagine an unwanted X gate (error) happens on qubit 0
qc.x(0) 
qc.barrier()

# Decoding/Syndrome Measurement
qc.cx(0, 1)
qc.cx(0, 2)
qc.ccx(1, 2, 0) # Majority vote to fix the error

print("Bit-flip Correction Circuit:")
print(qc.draw())
