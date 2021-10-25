# This code is part of QType.
#
# Copyright 2021 Antonio Párraga Navarro
#
# This code is licensed under the MIT License. You may obtain
# a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at https://opensource.org/licenses/MIT.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
from qtype.circuit.circuit import Circuit
from qtype.circuit.circuitcommand import CircuitCommand
from qtype.gates.quantumgate import QuantumGate
from qtype.types.qtype import QType


class GateCommand(CircuitCommand):

    def __init__(self, gate: QuantumGate):
        self.gate = gate

    def execute(self, circuit: Circuit):
        circuit.addGate(self.gate)

