{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Building Quantum Circuits and a Visualizer using Rigetti's Quantum Computer and PyQuil"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this tutorial, we will learn how to create, run, and visualize quantum circuits using Rigetti's quantum computer. It is recommended that you follow this tutorial along by running the code in your own Jupyter Notebook. As we go deeper, you will be required to sign up for Rigetti's Quantum Processing Unit (QPU) or Rigetti's Quantum Virtual Machine (QVM).\n",
    "<br>\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing Modules/Libraries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We first start off programing our quantum circuit by importing a few important libraries. We first import **Program**, **get_qc**, and **list_quantum_computers** from PyQuil by running: ```from pyquil import Program, get_qc, list_quantum_computers```. These will allow us to build the quantum circuit, call a quantum computer, and list quantum computers that we can use.\n",
    "\n",
    "After importing these, we need to import the standard quantum gates from PyQuil by running: ```from pyquil.gates import *```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyquil import Program, get_qc, list_quantum_computers     # Here we import the class and functions needed\n",
    "from pyquil.gates import *     # Here we import the quantum gates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Secondly, we ```import numpy as np``` to help us organize data from our results from the quantum computer, as well as ```import matplotlib.pyplot as plt```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np     # This will allow us to organize our data (results)\n",
    "import matplotlib.pyplot as plt     # This will help us will making the graph (visualization tool)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### If everything was done correctly, the code should look like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyquil import Program, get_qc, list_quantum_computers\n",
    "from pyquil.gates import *\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Building the Quantum Circuit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. We first create an empty quantum circuit, and assign in the the variable **p** by running: ```p = Program()```\n",
    "2. We now need something for us to store the data we collect from running the quantum circuit. We can do this by running ```ro = p.declare('ro', 'BIT', 2)```. We assign the variable \"ro\" to the program's memory slot and set the following parameters: **name:** \"ro\", **memory type:** \"BIT\", and **memory size**: 2\n",
    "\n",
    "##### We are now done building an empty quantum circuit. Below is a picture/visualization of the quantum circuit that you've made. Now we can start to apply quantum gates to the qubits."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**|q0>** --------------------------------------------------------------------------------------  \n",
    "\n",
    "**|q1>** --------------------------------------------------------------------------------------  \n",
    "\n",
    "**ro** -----------------------------------------------------------------------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "p = Program()    # Set up a circuit\n",
    "ro = p.declare('ro', 'BIT', 2)     # Declare memory space ro"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Applying and Running Quantum Gates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's start of by applying some simple gates to our qubits. We'll start off by applying a Pauli-X gate and a Pauli-Y gate to the first qubit, notated by ```|q0>```, followed by a CNOT gate.\n",
    "\n",
    "Before we offically apply our quantum gates, we need to denote that we are applying a quantum gate to **p**, the quantum circuit by notating ```p +=```.\n",
    "\n",
    "1. We can now apply our first quantum gate by writing ```X(0)``` into our code, beside the ```p +=```, such that we write ```p += X(0)```. Notice that we used \"0\" as our parameter of the Pauli-X gate function. The \"0\" signifies that we are applying the gate to the first qubit (notated by ```|q0>```).\n",
    "\n",
    "2. Now, we repeat the previous step, but use ```Y(0)``` rather than ```X(0)``` since we're applying the Pauli-Y gate instead of the Pauli-X gate. This will now give us ```p += Y(0) ```.\n",
    "\n",
    "3. Onto our third and final gate, we will apply the CNOT gate with ```|q0>``` as the control, and ```|q1>``` as the target. Similar to before, we first write ```p += ```, followed by our gate. Since the CNOT gate requires 2 qubits; 1 as the control and the other as the target, we will bring ```|q1>``` in. We use the CNOT function and use ```|q0>``` for the control parameter and ```|q1>``` for the target parameter. In all, this will make the code look like this: ```p += CNOT(0, 1)```."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "p += X(0)     # Apply Pauli-X gate on qubit 0\n",
    "p += Y(0)     # Apply Pauli-Y gate on qubit 0\n",
    "p += CNOT(0, 1)     # Apply CNOT gate with qubit 0 as the control and qubit 1 as the target"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Now here is a picture/visualization of the quantum circuit that you've made with the quantum gates applied:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**|q0>** ----[ X ]----[ Y ]-----o---------------------------------------------------------------  \n",
    "&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;|   \n",
    "**|q1>** ---------------------(X)--------------------------------------------------------------  \n",
    "\n",
    "  \n",
    "**ro** -----------------------------------------------------------------------------------------\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's measure the qubits that we ran in the quantum circuit. We'll do this by using the ```MEASURE``` function. I will visually represent this gate as **[ M ]**. We start off with ```p +=```, following it with the ```MEASURE``` function. The ```MEASURE``` function has 2 parameters. The first parameter is which qubit you want to measure, and the second parameter is where you want to store you data (recall \"```ro```\"). The ```MEASURE``` function looks like this: ```MEASURE(qubit, name of memory space[slot number within memory space])```.\n",
    "\n",
    "Since Python is zero-based, our first memory slot is ```ro[0]```, and our second slot is ```ro[1]```. We write the line of code: ```p += MEASURE(0, ro[0]``` for measuring qubit 1. We do the same thing but for the memory slot, we use ```ro[1]``` so that the data on ```ro[0]``` doesn't get overwritten. Therefore, the code for measuring qubit 2 is ```p += MEASURE(1, ro[1])```.  \n",
    "\n",
    "Overall, our code should be:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "p += MEASURE(0, ro[0])     # Measure qubit 1\n",
    "p += MEASURE(1, ro[1])     # Measure qubit 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "... and our quantum circuit should look like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**|q0>** ----[ X ]----[ Y ]-----o--------------[ M ]--------------------------------------------  \n",
    "&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;|   \n",
    "**|q1>** ---------------------(X)----[ M ] -----|-----------------------------------------------  \n",
    "&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;|&emsp;&emsp;&emsp;&nbsp;|   \n",
    "**ro** -------------------------------- V-------V----------------------------------------\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now lets run it by writing: ```print(p)```. This will print out the operations of our quantum circuit. **But this does not run our quantum curcuit**. If you followed everything correctly, the following will be displayed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DECLARE ro BIT[2]\n",
      "X 0\n",
      "Y 0\n",
      "CNOT 0 1\n",
      "MEASURE 0 ro[0]\n",
      "MEASURE 1 ro[1]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(p) # This will \"run\" our quantum circuit and display the operation of the gates on our qubits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
