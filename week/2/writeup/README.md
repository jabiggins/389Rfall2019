# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)


#### Name
Eric Norman

#### Where does ejnorman84 work? 
What is the URL to their website? Controls Specialist for Wattsamp Energy

#### List all personal information (including social media accounts, contacts, etc) you can find about ejnorman84. For each, briefly detail how you discovered them. 

* reddit: https://www.reddit.com/user/ejnorman84
* IG: https://www.instagram.com/ejnorman84/ he likes Texas, especially Texas football
* LinkedIn: https://www.linkedin.com/in/eric-norman-304550192/ He used to be a junior engineer at BP he used to be an electrical engineering intern at Koch

* Whois command on Kali: 
  * Registrant Street: 1300 Adabel Dr Registrant City: El Paso 
  * Registrant State/Province: TX 
  * Registrant Postal Code: 79835 Registrant Country: 
  * US Registrant Phone: +1.2026562837 
  * Registrant Email: ejnorman84@gmail.com

#### List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information. 
I found on securitytrails.com 
* A record::: 
 * 157.230.179.99 
* others::: ns-cloud-d4.googledomains.com 
 * ns-cloud-d3.googledomains.com 
 * ns-cloud-d2.googledomains.com 
 * ns-cloud-d1.googledomains.com
 
#### List any hidden files or directories you found on this website. 
* When I inspected the admin link, I found that the page redirected me to view/admin. 
* When I just searched the page: http://wattsamp.net/views/ I found the index page with the three links. The css is another visible page. 
*When I inspected the login page, I saw it referenced ../assets which allowed me to get in that folder and see all the pictures

#### What ports are open on the website? What services are running behind these ports? How did you discover this? 
Found using nmap: 
* 22/tcp  open     ssh
* 25/tcp  filtered smtp
* 80/tcp  open     http
* 110/tcp filtered pop3
* 135/tcp filtered msrpc
* 139/tcp filtered netbios-ssn
* 445/tcp filtered microsoft-ds

#### Which operating system is running on the server that is hosting the website? How did you discover this? 
* When I inspected the admin link, I found that the page redirected me to view/admin. 
* When I just searched the page: http://wattsamp.net/views/ underneath the three links I found: 
 * Apache/2.4.29 (Ubuntu) Server at wattsamp.net Port 80

#### BONUS: Did you find any other flags on your OSINT mission? Note: the standard flag format for bonus flags is *CMSC389R-{}. (Up to 9 pts!) 
* *CMSC389R-{Do_you-N0T_See_this} 
* *CMSC389R-{n0_indexing_pls} 
* *CMSC389R-{html_h@x0r_lulz}


### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
