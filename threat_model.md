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
- the only attack vector considered in our system is by sending (arbitrary, i.e. not restricted by quality or quantity) data to one or more peers.

## Potential threats

The first attack is a Denial of Service by overflowing the system. The idea is as follow: when a correct replica receives an update, it first stores it in remotes/\<origin\>, then tries to validate it. If the update is trusted, the update is moved to valids/\<origin\>. This can potentially leads to 2 different Denial of Service attacks: one is memory overflow (sending so many updates that the receiving node cannot store them) and the second is computing exhaustion (the receiving node cannot check all updates because of limited computation power).

## Mitigation actions for the new implementation

The intention for our project is to couple the replication and validation protocols in order to detect nodes that send invalid updates and blacklist them.

## Measures and validations


## Analysis under the STRIDE model

The [STRIDE model](https://en.wikipedia.org/wiki/STRIDE_%28security%29) is a model for identifying computer security threats. We look into the different threats and argue whether they apply to our model and how.

### Spoofing

Spoofing is when someone is pretending to be someone else, breaching authenticity. In our system, encryption provides authenticity by binding an update to a key. An attacker can create arbitrary many keys but cannot craft a signature from a key it did not create. Thus Spoofing is excluded by assumption

### Tampering

Tampering is the modification of data on disk, network, memory or elsewhere. As all messages are signed, a modified message will not go unnoticed for its signature will not match the content. This is also based on the cryptographic primitives assumptions. An attacker could delete a complete message but the "previous message" field in a message makes sure this does not go unnoticed, and the eventual consistency assumption of the system implies that all messages will be retransmitted at some (arbitrary) point in time. This leaves us with 2 potential attack: 1) deleting a complete log and 2) deleting or modifying (making it incorrect) a message on all machines. The later would imply that the information is not available anywhere.

### Repudiation

Repudiation is the claim from a participant that it didn't do something, in our case that it didn't write a message (we do not consider the link between an author (the possessor and user of a key pair) and a physical person). This is excpected from byzantin authors and is part of our mechanism to expose them, as the cryptographic primitives make sure no one can forge nor repudiate a signature.

### Information disclosure

Information disclosure is the procurement of information by somebody not authorized to access it. In our system, no information is assumed to be secret, except the author's secret key, which confidentiality is an assumption. All other information are meant to be shared, preventing any information disclosure.

### Denial of service

Denial of service is the exhaustion of resources needed to provide the service. We assume in our system that the only attack vector is by sending data to peers. Thus a DoS attack on the correct replica's side could happen in 3 ways: 1) a technical failure of the process, arising when an attacker can reach and exploit a (software) bug, 2) a memory exhaustion and 3) a computation exhaustion.

### Elevation of privilege

Elevation of privilege arises when someone gains the ability to do something they are not authorized to do. Although this cannot be ruled out, the likelihood of such an attack being possible is low. Reasons for this include the lack of direct communication between replicas and the ease of implementation of a compartmentalisation isolating the receiving, storing and validating parts of the protocol.

