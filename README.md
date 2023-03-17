## Introduction to Encryption in Cryptocurrency

From encryption, we will have hopefully built a solid foundation of computers, and how encryption works on a basic level. 
Afterwards, it is important to also build a healthy foundation of financial and economical systems, to truly understand modern defi systems.
and as we merge the two concepts together, we will devlop deeper understandings of how they merge themselves. 🖥️ 

The history is long and complex but there has always been a desire to store secretive information.

The earliest use of cryptography is hieroglyphs. 

A great example was Edgar Allen Poes “The Gold-Bug” which uses a simple substitution cipher.
(For more on that: http://csc.columbusstate.edu/summers/NOTES/1301/lab8-f12.pdf)

Here is a python file that will re-arrange a phrase for you with a simple Caesar algorithm:
https://github.com/MekailTheMachine/Encryptedkiss/blob/master/examples/Caesar.py
If you run the file, you can input a message, and a key value to shift the letters by. 

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
 
 
 ----------------------------------------------------------------------------------------------------------------------------------
 
 ## Part 2
 
 -----------------------------------------------------------------------------------------------------------------------------------
 
 ## Blockchain, Tokenomics, Value Theory, and Modern Economics 

we dove into encryption and started building a foundation for understanding how it works. 
To deepen your knowledge, feel free to explore this guide 
(https://hackernoon.com/how-does-rsa-work-f44918df914b). 
Now, let's dive into the core of our topic: blockchain technology and Bitcoin!

Follow along as we review Satoshi Nakamoto's groundbreaking Bitcoin whitepaper:
 https://bitcoin.org/en/bitcoin-paper.

#Traditional systems
like Facebook, Twitter, and YouTube,
 store data in centralized locations controlled by server administrators or entities.
  Decentralization removes this central storage, spreading data across computers worldwide. 
  People are incentivized to help carry and add to this data through mining fees or, 
  in the case of Bitcoin, block rewards.

The data structure we'll focus on is the blockchain, 
which stores data in "blocks" containing transactions.
Once all data is verified and certain random requirements are met, 
the data is "hashed" - run through an algorithm that condenses it into an 
unpredictable 256-character string. This string starts the sequence for each 
subsequent block, linking the data together.

If any computer tries to alter past data, the hash would change, 
causing a mismatch and making the network reject the block and node. 
Blockchain technology's decentralized nature is exemplified by Bitcoin, 
as the blockchain ledger is distributed among numerous computers.

![image](https://user-images.githubusercontent.com/49100995/226064330-cb704499-c4c6-411d-9cb1-ef563464cbde.png)


Satoshi's whitepaper outlines the problems with financial institutions 
and how they can be resolved through Bitcoin. The Merkle tree concept, 
combined with decreasing inflation rates, forces nations to develop protocols 
for situations like emergency relief programs instead of relying on inflation-based taxation.

Debates over intrinsic and extrinsic values between fiat and cryptocurrencies 
can get complicated. Money, as a representation of value, varies in importance 
between individuals. It's crucial to question whether our collective beliefs and 
values are still beneficial compared to alternative options. Over the past decade, 
we've seen an increase in Bitcoin's perceived value.

Before we delve into philosophy, let's discuss some definitions:

Intrinsic value: The value inherent in something.
Extrinsic value: The value attributed to an item, separate from its composition.

The US dollar is a good example. What are its intrinsic and extrinsic 
values before and after the Nixon-era gold standard? Currently, 
the intrinsic value of the dollar is the cotton it's made from, 
while its extrinsic value is the societal agreement on its worth.

As a society, we must question whether our current values and beliefs 
continue to benefit us compared to alternatives. We will host in-depth 
classes on financial systems and structures. If you're curious to learn more, 
feel free to reach out to our admins for recommended resources.

Centralized networks can easily store and access data in a single location. 
However, decentralized blockchain networks face challenges in efficiently 
accessing and sharing vast amounts of data among nodes. This data must be 
verified and shared with receiving nodes. By utilizing Merkle trees and cryptography, 
we arrive at the first public blockchain network, as implemented by Satoshi Nakamoto.

-------------------------------------------------------------

## part 3

--------------------------------------------------------------

## To understand Crypto we must first understand it's origins. 🎒 

Now that we have taken a glimpse into the crypto-graphical origins or crypto, let's take a look at the other driving forces that brought forth this behemoth of a network. That is community, government, and economy.
From the creators perspective, there was a growing number of problems, but as technology advances, the tools became available to pose a possible solution.

What were these problems? 

In Satoshi's terms, Bitcoin was invented to remove / provide an alternative to third parties, such as Visa, and Western Union. These third parties make a hefty some for conducting money transferring services. In Satoshi's words, 

“The root problem with conventional currency is all the trust that’s required to make it work. The central bank must be trusted not to debase the currency, but the history of fiat currencies is full of breaches of that trust. Banks must be trusted to hold our money and transfer it electronically, but they lend it out in waves of credit bubbles with barely a fraction in reserve.”

These transaction fees are largely sized based, and wouldn't be much reason for smaller transactions. Perhaps there were deeper motives...

Relying on the standard financial systems has other implications as well that can cause us to take a step back and view how our financial system truly functions as a whole, and the role many governments play in controlling the monetary supply. This may have even been an underlying goal of Satoshi's. 

Satoshi wanted to build a trustless system.

What does this mean?

With our current financial system, there is a lot of trust in specific parties, or "Central entities". One particular area of trust is typically within banks. Trusting that they wont use the money they are holding to extend credit, and loans; precisely what caused the Great Recession of 2008. The underlying issues lead several entities becoming incentivized to take risky actions, such as giving out risky loans. From a direct perspective, it does not appear that these entities have the general populations interest at heart, but hey. Technically that's not their job. 

When these banks over extend their credit, and can't pay back the money they owe to clients, and investors. The insurance agencies, and investment banks, all get bailed out by the government, in whom we must also trust with our money. 

Fun fact, addressing the issue of how organized political finances get spent is, and mitigating corruption through that spending is what inspired Cushy Crypto, and the Crypto Conductors. 

Beyond government bailouts, and transaction fees, these are just some of many simplified examples of the ways our financial system as a whole, is ridden with a moral hazard problem. 

 Central Banks to the rescue  

Luckily, the banks came up with a monetary policy to mitigate the negative economic affects deriving from the risky behavior that continuously takes course. This includes setting limits on loans, and creating restrictions; requiring banks hold a certain reserve, as well as other criteria. This all derives from Keynesian economics dating back to 1930. 
(Read more here: https://www.imf.org/external/pubs/ft/fandd/2014/09/pdf/basics.pdf)

(Read more on monetary and fiscal policy here:
 https://www.freefacts.org/ftf-blog/monetary-policy-explained )

If it weren't for government intervention, and increasing the monetary supply, the US may not have been able to recover as well from the 2008 recession. However motivation to print money has not always been the most "fiscally conservative". America for example has continued to print money to pay off their debt despite long debate.

Although the US dollar is much stronger than the Venezeulan Bolívar, or the many other countries experiencing hyper inflation, Rome was quite strong as well during the Roman Empire, both had very similar military budgets as well. Many would argue that Rome had over budgeted  military being one of the many catalysts of their economic downfall.
