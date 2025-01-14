
## Part 1
First, I would use OSINT to find some online account or subscription that Ericâ€™s mom has. Ideally, it would be something that she has, that Eric does not, like a pool membership or a senior citizens club. For the sake of simplicity, letâ€™s assume that is a pool membership. Judging by the age of Eric, it is safe to say that she is middle-aged to senior. As such, I think that it is credible to go off the premise that the mom is not very familiar with online technology. 
My persona will be an â€œaccount security specialistâ€ from the pool. I will contact Eric and tell him that the pool is instituting a new multi-factor security system for middle age customers. This will allow them to have a trusted family member have limited account access if she forgot her password or has a health emergency and canâ€™t cancel the subscription service. As I pretend to set up this account, I will hopefully get all of the required information.
First, when I call, I will tell him that his mother elected to have him sign up for the account, as he is more familiar with technology. The first hurdle is going to be establishing trust before he gets suspicious and calls his mother to double check. Luckily, we did some good OSINT last week, and I can go down the list of information that we gathered to have him confirm that it is correct. When I say all this personal information, it would seem more credible that I got it from someone who knows him well, his mother.
Second, I will say that in order to set up this service, I need to check that her browser can support our new service. I will ask him the browser he and his mom use, in order to confirm that everything works correctly.
Next up, I will have him confirm his identity, by answering two questions about his mother. I will say that because we need to confirm that this number his mother gave us is correct, he has to answer:
* His mothers maiden name
* And the city she was born in
The reason for having these two pieces of information here, is that they are difficult to get at any other way, and are common enough knowledge to not be inherently suspicious. On top of that, I put the more common one first, to utilize the â€œfoot in the door phenomenon.â€
Next, I will have him login to a fake page. To do so, I will need to throw together a quick, reputable looking webpage that has a â€œconfirm an accountâ€ option. I give him a fake username that has something to do with her name, and then tell him that his mom already set an initial password for the account, and all he has to do is login. I will then say, her hint for the password is â€œthe name of her first petâ€ because that is apparently something that they should both know. I will then say for security reasons, she has been instructed to change the password to be more secure later, after we have initialized everything on our end.
Finally, on the next page of the website, I will say that the account needs a 4 digit pin, so that both of you can access it quickly on browsers you trust, like your home desktop. I will tell Eric that he should make it something easy for his mom to remember, like a pin she is used to using frequently using so she wonâ€™t forget. Hopefully this is enough to have him enter the ATM pin number.
The last two steps really deal with very personal/obscure information, so I thought having a webpage that just stores the results for me in something like a SQL database is the best option.
 
 ## Part 2
#### 1)	Vulnerability 1: Exposed ports
This is a problem, because without an exposed port, the hackers would never have had access to the file system. That means that by securing this entry-point, you would severely limit the number of people who would even have access to the login in the first place.
To prevent this vulnerability, I would suggest setting up automatic scans of your system, to ensure that no port that is supposed to be closed is open. Next, I would close the backdoor port that the hackers used, and direct employees to a VPN instead, if they need access. Finally, but establishing a firewall, attackers could be severely slowed if they try to get in via any port, or be unable to get in at all.
https://nmap.org/book/defenses.html

#### 2)	Vulnerability: Weak Password
This is a problem, because once the hackers were inside the system, they were able to find the correct password fairly quickly by a dictionary aided brute force attack. Once found, they have free access to view the files on the system.
To prevent this vulnerability, I would first require users to have longer and more complicated passwords. Many websites do this already, and it removes many of the passwords along the lines of â€œhello1.â€ When I interned at NIST, I heard amount many additional security recommendations that their research discovered, some of which are detailed here:
https://www.alvaka.net/new-password-guidelines-us-federal-government-via-nist/
Secondly, I would institute progressive delays, where â€œuser accounts are locked out for a set period of time after a few failed login attempts. The lock-out time increases with each subsequent failed attempt.â€ This would ensure that any script that tries to automate a brute force attack would not succeed in any reasonable amount of time.
https://www.computerweekly.com/answer/Techniques-for-preventing-a-brute-force-login-attack

#### 3)	Vulnerability: Operating System Information
When the hackers were able to navigate away from the pages of the website that were meant to be public, they discovered the name and version of the OS listed at the bottom of the page. Stopping this listing is the easiest way to hide the operating system from plain sight. Although many consider preventing the general type of OS from being discoverable as an impossible task, you can make it more difficult by using technologies like TOR browser or TCP/IP fingerprinting.
https://security.stackexchange.com/questions/173233/how-do-i-hide-the-os-i-am-using-from-internet-sites
https://www.torproject.org/download/
https://en.wikipedia.org/wiki/TCP/IP_stack_fingerprinting
In this security case, by implementing these steps, you may make the task of finding the OS more difficult than it is worth, which in many cases is enough to at least direct the attackers attention elsewhere to a more visible attack, or stop attacks from occurring altogether.
