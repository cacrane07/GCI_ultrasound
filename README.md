# GCI_ultrasound

**Author(s):**

Carrie Crane 

Hannah Anderson 

Kayla Kim 

Juliana Jordan

Lindsay Ross 

Marin Morrison

## Background of Grand Challenge 

Toxic algal blooms, specifically those caused by increased reproduction of cyanobacteria, have become a growing concern for freshwater systems. When conditions tend to support their explosive growth, these blooms produce potent cyanotoxins which include: hepatotoxins, neurotoxins, and dermatoxins. These all-harm fish, wildlife, and even humans. Besides the  immediate toxins, very dense algal blooms block sunlight from reaching plants in the water. This disrupts photosynthesis and weakens aquatic habitats. As the algae begins to die and decompose, they start to release dissolved oxygen levels, leading to dead zones in fresh water systems that can kill fish and destabilize entire food webs. Toxic algal blooms pose a serious threat to ecosystem balance and highlight the urgent need for effective mitigation strategies.

## Approach

Our group has proposed using an ultrasonic sensor that emits ultrasound waves to treat cyanobacteria. The ultrasound waves disrupt the buoyancy of the blooms by bursting their gas vesicles. This apporach allows the blooms to be slowly treated without further harming the environment. We want out sensor to emit an adjustable range of frequencies that can be adjusted to operate in a range that does not cause harm to local freshwater organisms. 

## Specification

We created a schematic of a system that has 2 components: a transducer as a signal input, and a bandpass filter composed of a simple RLC circuit. In this case, the transducer is the hardware responsible for emitting the ultrasound waves.  

The marimo notebook includes the graph of the transfer function which is a ratio of input vs output signal. It shows how the filter will focus on allowing frequencies only in the range of 20kHz, which is one of our desired frequenies for treating the cyanobacteria. 

The schematic is included as an image which shows the RLC circuit and the values of the resistor, inductor, and capacitor all in practice. The final schematic is what we will build in GCI 250. The bandpass filter is necessary to prevent environmental noise from changing the applied signal. This schematic was generated in LTSpice and samples over frequencies from 1kHz to 200 kHz.

The 20kHz peak shown is an example of how we can control frequencies we would like to use. To have an adjustable range of frequencies we can create a multipeak bandpass filter which is more advanced and will allow certain chosen frequencies to pass through. 

## Teamwork Reflection 

Our team worked well together and regularly attended our group meetings. Each of our meetings were very efficient and we maintained communication throughout the semester. Each individual group member did their part of the work in a timely manner and their work always met the standards of other group members. 

Carrie Crane: I maintained a general knowledge of each aspect of the project to connect the tasks necessary for each part of the group. I worked heavily on the engineering side of the project and created the final schematic. I also created this GitHub repository containing our final deliverable. I worked with each person in the group to ensure everyones work would contribute to the final deliverable in some form. 

Hannah Anderson: I helped out in the engineering side of the project. I worked with Carrie and Kayla to download new software and read new research papers to change up our design.Throughout the project, I communicated with my teammates through our weekly meetings and our group chat.

Kayla Kim: My main role in our team was to help out on the engineering side of our ultrasonic sensor. I worked with Carrie and Hannah to learn the software we were using and also researched papers about the best frequencies to use for toxic algae blooms. Throughout the project, I collaborated well with my teammates by attending meetings, communicating through messages, and offering help where it was needed.

Juliana Jordan: I took the lead on researching valid frequency ranges and identifying the optimal output frequency for minimizing neurotoxic emissions in the algae. I also conducted comparative research on freshwater versus saltwater algae to determine how their biological differences might affect our results. Throughout the project, I collaborated closely with my teammates to integrate these findings into our overall design.

Lindsay Ross: I took the lead on the biology side of the project, researching places where the toxic blooms reside, how they can affect different species, and how we can collect to test. I also assisted Juliana on finding safe frequencies for different species of marine life. Throughout the project, I made sure to communicate clearly and effectively with my teammates, making sure we are(were) on the right track to test the sensor in GCI 250.

Marin Morrison: 

## Acknowledgement 

The values in the schematic were calculated based on prior knowledge from the course EENG300 (Electronics & Circuits II). The structure of this notebook was generated based on knowledge from the course PHY323 (Scientific Computing II). All research for the necessary frequency range was done prior and presented in our final presentation. 

## References

Litaker, R. W., Krause, J., Lindo-Atichati, D., Vandersea, M. W., Dyble, J., Tester, P. A., … Baden, D. G. (2022). The effects of the harmful algal bloom species Karenia brevis on fish larvae: A case study. https://pmc.ncbi.nlm.nih.gov/articles/PMC10051689/ 

Vaughan, L., Barnett, D., Bourke, E., Burrows, H., Robertson, F., Smith, B., … Zamyadi, A. (2023). Evaluating ultrasonicator performance for cyanobacteria management at freshwater sources. Toxins, 15(3), 186. https://doi.org/10.3390/toxins15030186 (PMC10051689) 

Haolian Xu, Zhenzhen Tang, Zixuan Liang, Hongbin Chen, Xiaohu Dai Neglected methane production and toxicity risk in low-frequency ultrasound for controlling harmful algal blooms. ScienceDirect, (2023). https://www.sciencedirect.com/science/article/pii/S0013935123012264?via%3Dihub  

Huang, H., Wu, G., Sheng, C., Jiannan, W., Li, D., Wang, H., & … (2020). Improved cyanobacteria removal from harmful algae blooms by two-cycle, low-frequency, low-density and short-duration ultrasonic radiation. Water, 12(9), 2431.https://www.researchgate.net/publication/343978855_Improved_Cyanobacteria_Removal_from_Harmful_Algae_Blooms_by_Two-Cycle_Low-Frequency_Low-Density_and_Short-Duration_Ultrasonic_Radiatio 

