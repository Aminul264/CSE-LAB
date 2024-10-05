Cryptography and Network Security Lab
Course Code: CSE-4232P
Program: B.Sc. Engg. Part 4, Even Semester
Session: 2018-2019, Examination 2022
Department: Computer Science and Engineering, University of Rajshahi

Lab Overview
This lab covers various cryptographic algorithms and techniques for securing information. The exercises involve encrypting and decrypting plaintext using different ciphers and cryptographic methods, as well as implementing prime-checking algorithms and hash functions.

Instructor
Md. Tohidul Islam
Associate Professor, Dept. of CSE, University of Rajshahi

Lab Exercises
1. Caesar Cipher
Objective:
Encrypt a given line of text using the Caesar Cipher (shift by 3 modulo 26). Then reverse the process to recover the original plaintext.

2. Polygram Substitution Cipher
Objective:
Encrypt a given plaintext using a Polygram Substitution Cipher (block size of 3). Then reverse the process to recover the original plaintext.

3. Transposition Cipher
Objective:
Encrypt the plaintext message "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH" using the Transposition Cipher (width provided as input). Reverse the process to get the original plaintext.

4. Double Transposition Cipher
Objective:
Encrypt the above plaintext using the Double Transposition Cipher. Then reverse the process to recover the original plaintext.

5. One-Time Pad Cipher
Objective:
Encrypt a plaintext using a truly random, non-repeating key from a file using the One-Time Pad technique. Reverse the operation to retrieve the original plaintext.

6. Lehmann Algorithm for Primality Testing
Objective:
Write a program to check whether a given number 
𝑃
P is prime using the Lehmann primality test algorithm.

7. Rabin-Miller Primality Test
Objective:
Write a program to check whether a given number 
𝑃
P is prime using the Rabin-Miller primality test algorithm.

8. MD5 Hash Function
Objective:
Write a program to implement the MD5 one-way hash function.

9. Secure Hash Algorithm (SHA)
Objective:
Write a program to implement the Secure Hash Algorithm (SHA).

10. RSA Algorithm
Objective:
Encrypt a plaintext message using the RSA algorithm. Reverse the process to recover the original plaintext.

11. Diffie-Hellman Key Exchange
Objective:
Write a program to implement the Diffie-Hellman Key Exchange protocol.











(Md. Tohidul Islam)
Associate Professor
Dept. of CSE
University of Rajshahi









Certainly! The Diffie-Hellman Key Exchange algorithm is a foundational cryptographic protocol used to securely exchange cryptographic keys over an insecure channel. Here's a detailed explanation of how it works:

Overview
The Diffie-Hellman Key Exchange allows two parties to establish a shared secret key that can be used for encrypting subsequent communications. The beauty of the protocol is that even though the parties exchange their keys over an insecure channel, the shared secret remains secure.

How It Works
Public Parameters:

Prime Number (p): A large prime number.
Base (g): A primitive root modulo p.
Private Keys:

Each party selects a private key that is kept secret.
Public Keys:

Each party computes a public key using their private key and the public parameters.
Shared Secret:

Both parties use their private key and the public key of the other party to compute a shared secret.
Detailed Steps
Setup:

Alice and Bob agree on a large prime number p and a base g. These values are public and can be shared openly.
Private Keys:

Alice chooses a private key 
𝑎
a.
Bob chooses a private key 
𝑏
b.
Compute Public Keys:

Alice computes her public key 
𝐴
A as follows:
𝐴
=
𝑔
𝑎
m
o
d
 
 
𝑝
A=g 
a
 modp
Bob computes his public key 
𝐵
B as follows:
𝐵
=
𝑔
𝑏
m
o
d
 
 
𝑝
B=g 
b
 modp
Alice and Bob then exchange their public keys.
Compute Shared Secret:

Alice computes the shared secret using Bob's public key 
𝐵
B:
Shared Secret
Alice
=
𝐵
𝑎
m
o
d
 
 
𝑝
Shared Secret 
Alice
​
 =B 
a
 modp
Bob computes the shared secret using Alice's public key 
𝐴
A:
Shared Secret
Bob
=
𝐴
𝑏
m
o
d
 
 
𝑝
Shared Secret 
Bob
​
 =A 
b
 modp
Both computations will yield the same result, which is the shared secret.
Why It’s Secure
Public Key Exposure: Even though the public keys 
𝐴
A and 
𝐵
B are exchanged openly, the private keys 
𝑎
a and 
𝑏
b are never shared.
Mathematical Hardness: The security of the Diffie-Hellman protocol relies on the difficulty of solving the discrete logarithm problem. Given 
𝑔
𝑎
m
o
d
 
 
𝑝
g 
a
 modp, it is computationally hard to determine 
𝑎
a.
Example
Let’s go through a simple example with small numbers to illustrate the Diffie-Hellman Key Exchange:

Public Parameters:

Prime 
𝑝
=
23
p=23
Base 
𝑔
=
5
g=5
Private Keys:

Alice: 
𝑎
=
6
a=6
Bob: 
𝑏
=
15
b=15
Compute Public Keys:

Alice computes her public key 
𝐴
A:
𝐴
=
5
6
m
o
d
 
 
23
=
8
A=5 
6
 mod23=8
Bob computes his public key 
𝐵
B:
𝐵
=
5
15
m
o
d
 
 
23
=
2
B=5 
15
 mod23=2
Alice and Bob exchange their public keys.
Compute Shared Secret:

Alice computes the shared secret using Bob’s public key 
𝐵
B:
Shared Secret
Alice
=
2
6
m
o
d
 
 
23
=
2
Shared Secret 
Alice
​
 =2 
6
 mod23=2
Bob computes the shared secret using Alice’s public key 
𝐴
A:
Shared Secret
Bob
=
8
15
m
o
d
 
 
23
=
2
Shared Secret 
Bob
​
 =8 
15
 mod23=2
Both Alice and Bob end up with the shared secret 
2
2, which they can now use for secure communication.

Key Points
Choice of Parameters: In practice, p and g should be large primes to ensure security.
Private Key Security: Private keys must be kept secret.
Public Key Computation: Involves modular exponentiation, which is computationally feasible.
This protocol is the basis for many cryptographic systems and secure communication methods.