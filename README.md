## Introduction to Encryption in Cryptocurrency

From encryption, we will have hopefully built a solid foundation of computers, and how encryption works on a basic level. 
Afterwards, it is important to also build a healthy foundation of financial and economical systems, to truly understand modern defi systems.
and as we merge the two concepts together, we will devlop deeper understandings of how they merge themselves. 🖥️ 

The history is long and complex but there has always been a desire to store secretive information.

The earliest use of cryptography is hieroglyphs. 

A great example was Edgar Allen Poes “The Gold-Bug” which uses a simple substitution cipher.
(For more on that: http://csc.columbusstate.edu/summers/NOTES/1301/lab8-f12.pdf)

You can agree to rearrange every 3rd letter in a series of texts 3 times. 
People could get ahold of how a party decrypted a message or could figure it out themselves.
The game changed when computer based encryption came along, with complex algorithms that could encrypt messages one way,
but not decrypt them without a certain key. The key behind this was using exponents, and prime numbers. 
Before we get ahead of ourselves let's get a better understanding of this concept, with this abstract picture of paints:

![image](https://user-images.githubusercontent.com/49100995/226060626-fea1ae60-1792-4259-a377-dd5420d2b01d.png)

Say you and your friend, either Alice or Bob, are hanging around one day playing with paint.
 Life is tough at your boarding school, and you just want to communicate to your crush without having to worry about some 
bully pretending to be Alice, or Bob. You guys think you have found a way to communicate with the confidence 
that one another wrote the letter themselves, and nobody is pretending to be one another!! :Direct_Hit~1: 

You both agree to use your schools color; Egg-White that you both have access to. 
On your own though, you each make a unique red, and blue paint; (perhaps a paint separator
 could allow someone to make the same paint, but for this purpose lets assume that doesn't exist yet) 
With your own unique colors, you both take a portion and mix it with some of the white paint, 
getting a pink, and baby blue color, both still unique, since they were mixed with your unique paint.
 We will then send a vial of the new lighter color to one another. Alice will mix the baby blue from 
Bob with her pink, and get a distinct purple, as will Bob, with his baby blue. You will both now have 
a distinct and unique purple. You can send your letters with a small vial of purple paint, and
 if it matches the paint you can make with your color, you know its your friend.

When we send cryptocurrencies (let's say Alice is sending Bob some bitcoin),
 we are typically sending a message to several computers; in Alice's case she
will be asking those computers to take bitcoin from her hot pink paint color,
 and send it to Bob, and you can prove that you are hot pink, because you are
 able to make the distinct purple, while the egg-white color is really just the 
"network protocol" all the computers use to agree on being able to tell if the 
purple is the distinct purple your hot pink should be able to make. The trick to 
why computers cant separate the paint, or break the encryption, comes down to RSA-256, 
and elliptical curve cryptography, which at it's true roots is possibly because of the Euler-Zeta formula. 
(Proof: https://riemannhypothesis.info/2013/09/in-the-beginning-there-was-eulers-formula/)
(More on encryption: https://medium.com/coinmonks/private-and-public-key-cryptography-explained-simply-4c374d371736)

![image](https://user-images.githubusercontent.com/49100995/226060874-f890d5e5-e535-49df-97cb-3ed28ad7c8ba.png)

Now to the nitty gritty; 
if you would like to see private key encryption in action above, we will be encrypting the message 22621,
 and then decrypting it using the private key. double asterisk indicates an exponent (example: 3 to the power of 2 is 9) 
and % is modulus which indicates the amount left over after dividing.

![image](https://user-images.githubusercontent.com/49100995/226060886-bde5ed30-b7a0-4cc1-a367-105cf8e77aa2.png)

The reason we use primes reverts back to our Euler-Zeta formula.

Now with a more solid understanding of how encryption works, tomorrow we will look at Satoshi Nakomoto's Bitcoin White paper,
 as well as look into some of the references, to understand how encryption built up to this point, why Bitcoin was invented, and how the technology
 integrated with blockchain, and the key concepts of decentralization, how it is achieved through network consensus algorithms, and how it can change the future. 

