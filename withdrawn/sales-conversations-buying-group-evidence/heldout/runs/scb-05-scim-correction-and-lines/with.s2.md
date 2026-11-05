**Your draft:** "Evolving rapidly" and "flexible options" dodge the question. Tomasz will read it as a yes-ish answer or as a dodge, and either one hurts you more when he finds out. A short correction now costs much less than a surprise during security review or rollout.

**Revised email**

> Subject: Correction on SCIM: Ostrander demo follow-up
>
> Hi Tomasz,
>
> Thanks again for your time yesterday. I need to correct something I said. You asked whether we support SCIM provisioning with Okta groups, and I told you I believed we did. We don't.
>
> Here is what we do support today:
> - SAML SSO with Okta
> - User provisioning by manual creation or CSV upload
>
> SCIM is not on a committed roadmap, so I can't promise a date. I'd rather you hear that from me now than find it later.
>
> If automated provisioning and deprovisioning is a requirement for Ostrander, I'd like to know how you'd handle it. How many users would you be provisioning, and how often does your team onboard or offboard? That will show whether the CSV route is workable or a dealbreaker. I can also pass your use case to our product team as a formal request.
>
> Are you free for 20 minutes on [day/date] to go through it? If SCIM is a hard requirement, I'd rather say so on that call than waste your time.
>
> [Name]

Two things to do before you send it:
- Check with product or engineering that "no SCIM, SAML only, CSV or manual provisioning" is exactly right, including any API you could offer as a workaround. Add it if there is one.
- Only offer to log the request if you'll actually do it. Don't imply it influences the roadmap.

**Lines for when you don't know the answer on a call**

The aim is to be precise about what you know and to commit to a time for the rest. Don't bluff, and don't deflect.

- "I don't want to guess on that. I'll confirm with our engineers and send you the answer by [day]."
- "Good question. I know the SSO side well, but I'd rather get you the exact answer on that from someone who knows it than give you a fuzzy one."
- "Here's what I know for certain: [fact]. For the rest, I'll bring an engineer in. Can I get your email and the specifics of what you need?"
- "Is that a requirement or a nice-to-have for you? That tells me how fast to get you the answer."
- "Let me repeat the question back so I get it to the right person exactly as you asked it."
- For anything that sounds like a yes/no commitment: "I want to be sure before I say yes, because it matters to you if I'm wrong."

Habits that help:
- **Keep a "known / not supported / need to check" sheet** for the top 15 or 20 technical questions (SSO, provisioning, API, data residency, uptime, compliance). SCIM would have been on it.
- **Ask why they're asking.** "What are you trying to do with it?" often shows the need is smaller than the question sounded, and it buys you thinking time.
- **Bring an engineer to technical calls** when you can.
- **Send the written answer within 24 hours,** with a named owner and date, so every "I'll check" turns into a visible next step.

A caught gap that you correct yourself makes buyers trust you more. A guess that gets exposed later doesn't.
