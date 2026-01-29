import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector

# Create a 1-qubit quantum circuit
qc = QuantumCircuit(1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Visualize the circuit
print("Quantum Circuit for Superposition:")
print(qc.draw())

# This demonstrates the fundamental concept of a qubit being in 0 and 1 simultaneously.
