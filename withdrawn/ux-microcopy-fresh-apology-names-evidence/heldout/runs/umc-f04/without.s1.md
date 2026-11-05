I haven't written it as the CEO asked, because "has been fully resolved" is false. You told me the hole isn't closed and you don't know how they got in. If the attacker still has access, or gets back in, you will have told 38,000 people they're safe when they aren't, and they won't take protective steps like changing passwords elsewhere. It also creates legal exposure. Regulators and plaintiffs treat a false "resolved" statement in a breach notice as a serious aggravating factor, and it could make you miss your notification obligations. "No evidence of misuse" has a similar problem. When you don't yet know how the breach happened, absence of evidence tells people very little, so it's better to say what you've actually seen.

The CEO's goal of keeping people calm is reasonable, and a clear, specific, action-oriented notice usually does that better than reassurance does. Here is a draft:

---

**Subject: Security incident affecting your Pinecone Notes account**

Hi [First name],

We're writing to tell you about a security incident that involved your Pinecone Notes account information.

**What happened**
On [date], we discovered that an unauthorized party had accessed one of our older databases. The data taken includes your **email address and your hashed (scrambled) password**. About 38,000 accounts are affected. [Confirm: the database did not contain your notes or payment information.]

**What we're doing**
We're investigating how the access happened, and that work is still under way. We haven't yet closed the vulnerability, and we'll update you when we have. [Replace with actual containment steps, e.g. "We have rotated credentials, restricted access to the affected system, and brought in outside security specialists."] [If true: "We have not seen reports of your data being misused, but we can't rule it out."]

**What you should do**
- **Change your Pinecone Notes password now**: [link]. We've also [logged you out of all sessions / will require a reset at next login].
- **If you use the same password anywhere else, change it there too.** Hashed passwords can sometimes be cracked, especially weak ones.
- **Be alert to phishing.** Someone with your email address may send messages pretending to be us. We will never ask for your password by email. Treat unexpected links with caution.
- Consider turning on two-factor authentication [if available: link].

**Questions**
Contact us at [security@ address] or [link to FAQ]. We're sorry this happened, and we'll keep you updated as we learn more.

[Name, title]
Pinecone Notes

---

**Before you send it:**
- **Fill in the brackets with facts only.** Cut anything you can't confirm, such as what the database did and didn't contain.
- **Talk to counsel today.** Notification deadlines vary by jurisdiction (GDPR is 72 hours to the regulator, and many US states have their own rules), and you found out yesterday.
- **Say the notice will be updated.** That is the honest way to handle the open investigation, and it lets you send a follow-up when you do close the hole.
- **For the CEO:** "We're telling you what we know, what we don't, and exactly what to do" is calming, and it holds up if the investigation turns up something worse. A "fully resolved" claim that later proves wrong would do far more damage to trust than an honest notice does now.

If you want, I can write a short version for the in-app banner, or a one-page internal note you can use to make this case to the CEO.
