from qiskit import QuantumCircuit, Aer, execute

# Create a 2-qubit circuit
qc = QuantumCircuit(2)

# Create a Bell State (Entanglement)
qc.h(0)         # Put qubit 0 in superposition
qc.cx(0, 1)     # Apply CNOT gate

# Measure the qubits
qc.measure_all()

# Simulate the result
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print("\nEntanglement Measurement Results:")
print(counts)
# Expecting nearly 50% for '00' and 50% for '11'
