# GCI_ultrasound

**Author(s):**

Carrie Crane 

Hannah Anderson 

Kayla Kim 

Juliana Jordan

Lindsay Ross 

Marin Morrison

## Background of Grand Challenge 



## Specification

We created a schematic of a system that has 2 components: a transducer as a signal input, and a bandpass filter composed of a simple RLC circuit. 

The marimo notebook includes the graph of the transfer function which is a ratio of input vs output signal. It shows how the filter will focus on allowing frequencies only in the range of 20kHz, which is one of our desired frequenies for treating the cyanobacteria. 

The schematic is included as an image which shows the RLC circuit and the values of the resistor, inductor, and capacitor all in practice. The final schematic is what we will build in GCI 250. The bandpass filter is necessary to prevent environmental noise from changing the applied signal. This schematic was generated in LTSpice and samples over frequencies from 1kHz to 200 kHz.

The 20kHz peak shown is an example of how we can control frequencies we would like to use. To have an adjustable range of frequencies we can create a multipeak bandpass filter which is more advanced and will allow certain chosen frequencies to pass through. 

## Teamwork Reflection 


## Acknowledgement 

The values in the schematic were calculated based on prior knowledge from the course EENG300 (Electronics & Circuits II). The structure of this notebook was generated based on knowledge from the course PHY323 (Scientific Computing II). All research for the necessary frequency range was done prior and presented in our final presentation. 
