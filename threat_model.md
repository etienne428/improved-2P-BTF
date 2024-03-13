# Threat model analysis of 2P BFT Log

etienne.mettaz@epfl.ch
10.03.2024

## Description

This document is a threat model of the [2 Phases Byzantine Fault Tolerant log protocol](./2P_BFT_Log.pdf) based on the standard git protocol.

## Assumption of the system

The system assumes that:
- there is an arbitrary large set of replicas, of which at least 2 are correct (the rest are Byzantine)
- every correct replica is connected to at least another correct replica in such a way that all correct replicas form a connected graph (the Byzantine nodes do not split the graph of correct nodes in 2)
- we have eventual consistency: each correct node receive every update by correct replicas after some (arbitrary long) time. This does not assume in-order update nor that all updates from one replica arrive trhough the same node
- correct replicas always reject invalid messages
- an attacker cannot break the encryption used to sign the updates
- signing keys from correct updates are not compromised

## Potential threats

The first attack is a Denial of Service by overflowing the system. The idea is as follow: when a correct replica receives an update, it first stores it in remotes/\<origin\>, then tries to validate it. If the update is trusted, the update is moved to valids/\<origin\>. This can potentially leads to 2 different Denial of Service attacks: one is memory overflow (sending so many updates that the receiving node cannot store them) and the second is computing exhaustion (the receiving node cannot check all updates because of limited computation power).

## Mitigation actions for the new implementation

The intention for our project is to couple the replication and validation protocols in order to detect nodes that send invalid updates and blacklist them.

## Measures and validations


## Analysis under the STRIDE model

The [STRIDE model](https://en.wikipedia.org/wiki/STRIDE_%28security%29) is a model for identifying computer security threats. We look into the different threats and argue whether they apply to our model and how.

### Spoofing

Spoofing is when someone is pretending to be someone else, breaching authenticity. In our system, encryption provides authenticity by binding an update to a key. An attacker can create arbitrary many keys but cannot craft a signature from a key it did not create.
