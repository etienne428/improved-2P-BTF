# improved-2P-BTF
etienne.mettaz@epfl.ch
06.03.2024

## Description

In this project, we first analyze the 2P-BFT-Log protocol and look for threat models assuming a byzantine attacker. We then implement a protocol that couples git's replication protocol and 2P-BFT-Log's validation protocol in order to mitigate some of the threat models found. This protocol should be transparent to the user, i.e., should be intuitively similar to git's command line interface. Finally, we analyze and when possible measure the security features and the performance of the implementation and compare it with existing implementations.
