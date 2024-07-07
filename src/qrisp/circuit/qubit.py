"""
\********************************************************************************
* Copyright (c) 2023 the Qrisp authors
*
* This program and the accompanying materials are made available under the
* terms of the Eclipse Public License 2.0 which is available at
* http://www.eclipse.org/legal/epl-2.0.
*
* This Source Code may also be made available under the following Secondary
* Licenses when the conditions for such availability set forth in the Eclipse
* Public License, v. 2.0 are satisfied: GNU General Public License, version 2
* with the GNU Classpath Exception which is
* available at https://www.gnu.org/software/classpath/license.html.
*
* SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
********************************************************************************/
"""
import numpy as np
from jax.core import AbstractValue, Primitive, raise_to_shaped_mappings

class Qubit:
    """
    This class describes qubits. Qubits are created by supplying the identifier string.

    Attributes
    ----------
    identifier : str
        A string to identify the Qubit.

    Examples
    --------

    We create a Qubit and add it to a :ref:`QuantumCircuit`:

    >>> from qrisp import QuantumCircuit, Qubit
    >>> qb = Qubit("alphonse")
    >>> qc = QuantumCircuit()
    >>> qc.add_qubit(qb)
    >>> qc.x(qb)
    >>> print(qc)
    
    ::
    
                  ┌───┐
        alphonse: ┤ X ├
                  └───┘


    """
    qubit_hash = np.zeros(1)
    def __init__(self, identifier):
        self.identifier = identifier
        self.hash_value = int(self.qubit_hash[0])
        self.qubit_hash += 1
        self.lock = False
        self.perm_lock = False

    def __str__(self):
        return self.identifier

    def __repr__(self):
        return "Qubit(" + self.identifier + ")"

    def __hash__(self):
        return self.hash_value

    def __eq__(self, other):
        return self.hash_value == other.hash_value
    

"""
from jax import tree_util

class QBNameContainer:
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    def __hash__(self):
        return hash(type(self))
    
    def __eq__(self, other):
        return isinstance(other, QBNameContainer)
        
def flatten_qb(qb):
    # return the tracers and auxiliary data (structure of the object)
    children = (qb.abstract,)
    aux_data = (QBNameContainer(qb.identifier),)
    return children, aux_data

def unflatten_qb(aux_data, children):
    # reconstruct the object from children and auxiliary data
    res = Qubit.__new__(Qubit)
    
    res.abstract = children[0]
    res.identifier = aux_data[0].identifier
    
    return res

# Register as a PyTree with JAX
tree_util.register_pytree_node(Qubit, flatten_qb, unflatten_qb)
"""
pass