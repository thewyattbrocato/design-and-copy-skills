I can't write it with those three phrases. Two are false or misleading today, and that would hurt you more than the breach:

- **"Fully resolved"** is untrue. You haven't found the entry point or closed it. If the attacker gets back in, or more comes out of the investigation, you'll have to contradict the notice publicly.
- **"No evidence your data has been misused"** is misleading. Someone took the data, and that is already misuse. Users will read this line as "nothing bad happened," and it gives them no reason to change passwords they reuse elsewhere. Regulators and plaintiffs' lawyers also look hard at this wording.
- **"Your security is our top priority"** is fine as a sentiment, but as an opener it reads as boilerplate and makes people more suspicious. I've moved it to the end, where it's backed by specifics.

Calm comes from being clear and giving people something to do. Here's a version that does that and that I'd stand behind.

---

**Email subject:** Security incident affecting your Pinecone Notes account

**Email body:**

Hi {{first_name}},

We're writing to tell you about a security incident that involved your Pinecone Notes account.

**What happened**
On {{date_discovered}}, we found that an unauthorized person had gained access to an older Pinecone Notes database and copied data from it. Our investigation is still underway, and we don't yet know how they got in.

**What was taken**
Your email address and your hashed password. A hashed password is a scrambled version of your password, not the password itself. {{Optional, only if true: Ours are hashed with [algorithm] and salted, which makes them hard to reverse, but not impossible, especially for simple passwords.}} {{Only if confirmed: We have no indication that your notes or payment information were in this database.}}

**What you should do**
1. Change your Pinecone Notes password now: {{link}}
2. If you use the same password anywhere else, change it there too.
3. Be careful with emails that appear to come from us. We will never ask for your password by email or link you to a sign-in page you didn't request.
4. Turn on two-factor authentication: {{link}}

**What we're doing**
We're investigating how the access happened, and we're working to close it. {{Add the concrete steps you're actually taking, such as forcing password resets or bringing in outside forensics.}} We'll update you at {{status_page_or_email}} as we learn more, including if anything in this notice changes.

We're sorry this happened. If you have questions, contact us at {{contact}}.

The Pinecone Notes team

---

**In-app banner:**

> **Security incident: please change your password.** An unauthorized party copied email addresses and hashed passwords from an older Pinecone Notes database. Change your password now, and anywhere else you've used it. [Change password] [Details]

---

Before you send:

1. **Get legal counsel to review it today.** Breach notification laws (GDPR's 72-hour clock, US state laws) set deadlines and required content. With 38,000 accounts, there's a good chance you have a filing obligation.
2. **Check the placeholders.** Only include the hashing line and the "notes and payment info weren't affected" line if you've confirmed them.
3. **Consider forcing a password reset** on the affected accounts instead of only asking. It protects people better and makes the notice shorter.
4. **For your CEO:** a notice that says "resolved" while the hole is still open has to be retracted later, and people remember the retraction. If the investigation does finish, send a follow-up that says so. That's the message that earns trust.

I can also draft a short note to your CEO making this case, or a follow-up template for when the investigation concludes.
