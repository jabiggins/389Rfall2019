# Writeup 2 - OSINT

Name: James Biggins
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: James Biggins

## Assignment Writeup

### Part 1 (45 pts)


#### Name
Eric Norman

#### Where does ejnorman84 work? 
Controls Specialist for Wattsamp Energy

#### What is the URL to their website? 
wattsamp.net

#### List all personal information (including social media accounts, contacts, etc) you can find about ejnorman84. For each, briefly detail how you discovered them. 

* reddit: https://www.reddit.com/user/ejnorman84
 * my partner in class found this one, very little information
* IG: https://www.instagram.com/ejnorman84/ 
 * He likes Texas, especially Texas football
* LinkedIn: https://www.linkedin.com/in/eric-norman-304550192/ 
 * He used to be a junior engineer at BP he used to be an electrical engineering intern at Koch

* Whois command on Kali: 
  * Registrant Street: 1300 Adabel Dr Registrant City: El Paso 
  * Registrant State/Province: TX 
  * Registrant Postal Code: 79835 Registrant Country: 
  * US Registrant Phone: +1.2026562837 
  * Registrant Email: ejnorman84@gmail.com

#### List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information. 
I found on securitytrails.com and confirmed in dns dumpster
* A record::: 
 * 157.230.179.99 
* others::: ns-cloud-d4.googledomains.com 
 * ns-cloud-d3.googledomains.com 
 * ns-cloud-d2.googledomains.com 
 * ns-cloud-d1.googledomains.com
 I asked the TA's and they said this was good enough
 
#### List any hidden files or directories you found on this website. 
* When I inspected the admin link, I found that the page redirected me to view/admin. 
* When I just searched the page: http://wattsamp.net/views/ I found the index page with the three links. The css is another visible page. 
* When I inspected the login page, I saw it referenced ../assets which allowed me to get in that folder and see all the pictures

#### What ports are open on the website? What services are running behind these ports? How did you discover this? 
Found using nmap: 
* 22/tcp   open     ssh
* 25/tcp   filtered smtp
* 80/tcp   open     http
* 110/tcp  filtered pop3
* 135/tcp  filtered msrpc
* 136/tcp  filtered profile
* 137/tcp  filtered netbios-ns
* 138/tcp  filtered netbios-dgm
* 139/tcp  filtered netbios-ssn
* 445/tcp  filtered microsoft-ds
* 1337/tcp open     waste


#### Which operating system is running on the server that is hosting the website? How did you discover this? 
* When I inspected the admin link, I found that the page redirected me to view/admin. 
* When I just searched the page: http://wattsamp.net/views/ underneath the three links I found: 
 * Apache/2.4.29 (Ubuntu) Server at wattsamp.net Port 80

#### BONUS: Did you find any other flags on your OSINT mission? Note: the standard flag format for bonus flags is *CMSC389R-{}. (Up to 9 pts!) 
* *CMSC389R-{Do_you-N0T_See_this} 
* *CMSC389R-{n0_indexing_pls} 
* *CMSC389R-{html_h@x0r_lulz}


### Part 2 (75 pts)

I first had to come into office hours to get my github set properly. I then had to come in again to figure out what part 2 was trying to accomplish, because I was completely lost. Then I broke the work down into the steps that I was told to do:
* loop through lines of file
* get captcha 
* extract the math problem 
  * Wes suggested using .split() instead of pattern matching
  * This made things cleaner, but it also meant that I think I needed to sleep longer since my array ws longer
* determine operator
* get UN prompt and return UN
* get PW prompt and return PW
* get result and quit program if correct

I finally got the code running through a couple times, and then played with the sleep times to make it as fast as possible, because multi-threading seemed excessive. When I got the password, I nc-ed manually and then cd-ed to the home directory to find the flag CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}
