I wouldn't send the notice as your CEO worded it. I've written one that keeps the calm tone without the problems below.

**Why not the requested wording**
- **"Has been fully resolved"** is false today. You haven't found the entry point or closed the hole. If the attacker gets back in, or you later find more was taken, this line becomes the headline.
- **"No evidence of misuse"** is technically true of any breach found a day ago, but it reads as "nothing bad has happened." Stolen emails and hashed passwords are mainly used for credential stuffing and phishing, and those happen on other sites and out of your sight. Saying it now invites the criticism that you implied safety you couldn't know.
- **Regulators:** a notice that overstates the situation can create legal exposure beyond the breach itself. Have counsel review it before it goes out. Depending on where your users are, you may have notification deadlines (GDPR is 72 hours to the regulator, and US state laws vary), and the clock may already be running.

Calm comes from being clear and giving people something concrete to do. Here is a version for that.

---

**Email subject:** Security incident affecting your Pinecone Notes account

Hi [First name],

We're writing to tell you about a security incident that involved your Pinecone Notes account.

**What happened**
On [date], we discovered that someone gained unauthorized access to an older database and copied account information. For your account, this was your **email address and your hashed (scrambled) password**. [Confirm: your notes and payment information were not stored in this database.]

**What we don't know yet**
We're still investigating how the attacker got in, and we haven't yet confirmed that the access has been fully shut off. We have not found evidence that the stolen data has been used, but it's early, and we can't rule it out. We'll update you by [date], or sooner if we learn something important.

**What we're doing**
- [Investigating with (internal team / outside forensic firm)]
- [Resetting passwords for affected accounts. Edit this to match what you actually do.]
- [Notifying the relevant authorities]

**What you should do**
1. **Change your Pinecone Notes password** here: [link]. Hashing makes passwords hard to read, but not impossible to crack, especially weak ones.
2. **Change it anywhere else you've used the same password**, and consider a password manager.
3. **Be cautious of emails that appear to come from us.** We will never ask for your password by email. If a message seems off, go directly to [site] rather than clicking links.
4. [Turn on two-factor authentication: link, if available.]

We're sorry. You trusted us with your information and we fell short. Questions can go to [security@address], and updates will be posted at [status page URL].

[Name], [Title]
Pinecone Notes

---

**In-app banner**

> **Security incident:** An unauthorized party copied account emails and hashed passwords from an older database. Please change your password now. We're still investigating and will share updates here. [Change password] [Learn more]

---

**To raise with the CEO**
- Her goal of keeping people calm is better served by this version. If the hole stays open, a "fully resolved" notice followed by a second incident does far more damage to trust than an honest first one.
- When the hole is actually closed and verified, you can send a follow-up that says so. That message will land well.
- The bracketed items must be confirmed before sending. In particular, check whether notes content or other data lived in that database, and whether you're forcing resets.

If you tell me what you're doing about passwords and where your users are, I can tighten the details and draft the follow-up.
