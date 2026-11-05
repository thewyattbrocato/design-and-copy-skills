**Corrected email**

> Subject: Correction on SCIM, Okta provisioning
>
> Hi Tomasz,
>
> Thanks again for your time yesterday. I need to correct something. You asked whether we support SCIM provisioning with Okta groups, and I said I believed so. We don't.
>
> Here is what we do support today:
> - SAML SSO with Okta
> - User provisioning by hand or by CSV upload
>
> SCIM is not on a committed roadmap, so I can't promise a date. If automated provisioning and deprovisioning is a requirement for Ostrander, it's better you know now than find out later.
>
> Could we take 20 minutes on [day/date] to walk through how your team would handle joiners and leavers with CSV, and see whether that works for you? If it doesn't, I'd rather say so now. I'll send an invite for [time] and bring [SE/engineer name] to answer the technical questions.
>
> [Your name]

I dropped "evolving rapidly" and "flexible options". Tomasz asked a yes/no question, and those phrases read as dodging it. A vague reply after a wrong "yes" will cost you more trust than the correction does. If he catches it later in a security review, it's worse. Owning the error in the first sentence is what makes the rest of the email credible.

**Lines for when an engineer asks something you can't answer**

- "I don't want to guess on that. Let me get you the exact answer from our engineers. Can I have it to you by [day]?"
- "Can you tell me what you're trying to make sure works? Then I can bring back the right answer instead of a generic one."
- "Is that a must-have or a nice-to-have for you? That tells me whether to bring an engineer to the next call."
- "I'd rather give you a correct answer in 24 hours than a confident wrong one now."
- For anything you half-know: "My understanding is X, but I'll confirm in writing before you rely on it."

Two habits make these work:
1. **Write the question down in front of them and say the date.** For example: "Noting that: SCIM with Okta groups. You'll have an answer from me by Thursday." The date and the owner are what make it sound competent.
2. **Before discovery calls, get a short "can we / can't we" list from your SE or product team.** It should cover SSO, provisioning, audit logs, API, data residency and the other usual questions. Most engineer questions fall into about ten categories, and the SCIM miss would have been caught by that list.

Two things to check before sending:
- Confirm with product that SCIM really isn't planned or in beta, so the email states the facts as they are today.
- Fill in the call date and who joins from your side.
