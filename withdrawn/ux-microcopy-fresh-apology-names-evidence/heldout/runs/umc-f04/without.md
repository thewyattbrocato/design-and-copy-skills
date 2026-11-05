I can't write it exactly as the CEO asked, because one of the three lines is false and another is misleading. I've drafted a version that's still calm and that you can send today.

**Problems with the requested wording**
- **"Fully resolved"** is false. You haven't found the entry point or closed it. If the attacker gets back in, or more comes out, you'll have told 38,000 people it was over. That is the most damaging line to be wrong about, and it could expose the company to deceptive-statement claims from regulators.
- **"No evidence your data has been misused"** is misleading when you've been investigating for one day and the data was stolen. Nobody has looked yet, so "no evidence" says nothing. Credential stuffing and phishing typically start within days. If you use the line at all, qualify it: "we have not yet seen..."
- **"Your security is our top priority"** is fine as a closing line. As an opener, it reads as boilerplate right before bad news, and readers tend to distrust it. Leading with what happened and what to do reads as more competent, and that is what calms people.

**Suggested draft**

**Subject: Important security notice about your Pinecone Notes account**

Hi,

We're writing to tell you about a security incident that affected your Pinecone Notes account.

**What happened**
On [date], we discovered that an unauthorized party had accessed an older database and copied account information. Your email address and your hashed (scrambled) password were included. Your notes were not stored in that database. [Confirm this before sending.]

**What we're doing**
We're investigating how the access happened, and that work is still under way. We have not yet confirmed how the person got in, and we will update you when we know more. [Add any containment steps you've actually taken.]

**What you should do**
- Change your Pinecone Notes password now: [link]. We've [required / will require] a reset for affected accounts.
- If you use the same password on other sites, change it there too.
- Be cautious with emails that appear to come from us or ask for your password. We will never ask for your password by email.
- Turn on two-factor authentication: [link]. [Only include this if you offer it.]

Passwords were stored in hashed form, which makes them harder to use, but hashing isn't a guarantee, especially for simple passwords. That's why we recommend changing yours.

**More information**
We'll post updates at [URL]. Questions: [security contact]. We're sorry this happened, and we take responsibility for protecting your information.

[Name, title]
Pinecone Notes

**Before you send**
1. **Have counsel review it today.** Breach notification laws probably apply, such as state laws in the US and the GDPR 72-hour regulator deadline if you have EU users. The clock may have started when you found out yesterday. Counsel may require specific content or a regulator notice alongside this one.
2. **Verify every factual claim**, especially that notes and other data weren't in that database, and the hash algorithm. Say "bcrypt-hashed" only if it's true.
3. **Force a password reset** for the 38,000 accounts, or at least invalidate their sessions, so the advice in the notice is backed by action.
4. **Send a short update** once the entry point is closed. "Resolved" can go in that message, once it's true.

For the CEO: a notice that says "resolved" and is later contradicted will cost more trust than an honest "we're still investigating." The draft above keeps the tone calm without making any claim you'd have to retract.

I can also write a shorter in-app banner version, or a tighter version that follows her wording as closely as the facts allow.
