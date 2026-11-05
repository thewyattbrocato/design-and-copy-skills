Your draft dodges the question, and a bank IT lead will notice. "Evolving rapidly" and "flexible options" read as a no, and they make you look evasive. A short, straight correction will do more for your credibility than the draft would. It also matters because Tomasz may be relying on your "yes" in their evaluation.

**Revised email**

> Subject: Correction on SCIM: Ostrander Bank demo
>
> Hi Tomasz,
>
> Thanks again for your time yesterday. I need to correct something I said. You asked about SCIM provisioning with Okta groups, and I said I believed we supported it. We don't currently.
>
> Here's where we are today:
> - **SAML SSO with Okta:** fully supported.
> - **User provisioning:** manual, or bulk via CSV import.
> - **SCIM:** not available, and I don't have a committed date to share.
>
> I'd rather you have the accurate picture now than find out mid-evaluation. If automated provisioning and deprovisioning is a requirement, I'd like to understand how you'd handle it (for example, how many users and how often they change) so we can see whether the CSV workflow is workable for you. I'm also happy to bring in someone from our product team to talk through where SCIM sits.
>
> Do you have 20 minutes this week?
>
> Best,
> [Name]

Before you send it, check with your product or engineering lead on two things:
- Whether you can say anything about SCIM timing. I wrote "no committed date" because that's what you told me.
- Whether you can offer a product person for the call.

If you can't offer either, cut those lines.

**Lines for discovery calls**

These work because they're honest and they keep control of the conversation.

- "I don't want to guess on that. Let me confirm with engineering and get you a written answer by end of day tomorrow."
- "Good question. Can you tell me what you're trying to accomplish? That way I can get you the right answer, not just a yes or no."
- "I know we support X. I'm not certain about Y, so I'll verify rather than risk giving you wrong information."
- "That's a detail I'd rather have our solutions engineer walk you through. Can I bring them to the next call?"
- For yes/no questions on integrations: "Here's what I know is supported today: [list]. Is [their ask] a must-have or a nice-to-have?" That also qualifies the deal.

Two habits help more than any line:
1. **Never say "I believe so."** It sounds like a yes to them and it's a liability for you. Use "Let me confirm" instead.
2. **Keep a one-page cheat sheet** of the questions that come up most: SSO/SCIM, encryption, data residency, SOC 2, API limits, uptime SLA. Ask your SE or product team to help write it, and update it after each call where you got stumped.

If you paste the questions you've been stumped on, I can help draft that sheet.
