The draft dodges the question. Tomasz will probably read "evolving rapidly" and "flexible options" as a yes or a maybe, and an IT lead will notice that the email never answers him. If he finds out later that SCIM isn't supported, it will cost you more than a correction now. A short, direct correction usually helps with technical buyers.

**Revised email**

> Subject: Correction on SCIM, Okta provisioning
>
> Hi Tomasz,
>
> Thanks again for your time yesterday. I need to correct something I said about SCIM. I told you I believed we support it, and that was wrong. Here's where we stand:
>
> - **Supported today:** SAML SSO with Okta
> - **User provisioning:** manual, or bulk via CSV upload
> - **SCIM / Okta group-based provisioning:** not currently supported, and I don't have a committed date to share
>
> I'd rather you have the accurate picture now than find out mid-evaluation. If automated provisioning is a requirement for Ostrander, I'm happy to set up a short call with our product team so you can talk through your needs, and I can share how other customers manage provisioning with SAML in the meantime.
>
> Sorry for the confusion, and thanks for the sharp question.
>
> [Name]

Before you send it, check two things:
- Only offer the product call if you can actually arrange it.
- Only mention how other customers handle provisioning if you know that's true. Otherwise cut that clause.

**Lines for discovery calls**

- "Good question. I don't want to guess on that one. Let me get you a precise answer from our engineers by end of day tomorrow."
- "I know the business-level answer, but that's an implementation detail I want to confirm. Can I bring an SE to the next call?"
- "Help me understand what you're trying to accomplish. Is it [X] or [Y]? That will tell me who to loop in."
- "I'd rather get you a correct answer than a fast one."
- When you half-know: "My understanding is X, but I'll verify before you rely on it."

Two habits that help more than any line:
- **Write down every question you can't answer, then send the answers in a follow-up within 24 hours.** Buyers often remember that more favorably than an instant answer.
- **Build a one-page "supported / not supported / roadmap" cheat sheet** for SSO, provisioning, API, data residency, and compliance. Ask your SE to help. Most of the questions engineers ask fall into a handful of categories, and "I believe so" is much less likely to come out of your mouth when you have the sheet in front of you.
