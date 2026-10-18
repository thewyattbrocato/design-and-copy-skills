**Not ready to send yet. The biggest problem is that the page doesn't save anything.** The submit handler only updates the text on screen, so every sign-up is lost, but the page says "You are on the list." Everything else is close.

What already works: the layout and labels are clear, focus outlines are kept, dark mode uses its own colors with readable contrast, the error appears next to the field and is announced to screen readers, focus moves to the problem field, and the name is inserted as text, not HTML.

**Ranked findings**

1. **Sign-ups go nowhere (blocks the purpose).** You need a destination before sending: a form endpoint, a Google Form, or your mailing-list tool's embed. Once you tell me which, I'll wire it in. Until then, don't say "You are on the list" in the success message. Also show a busy state on the button while sending, and if sending fails, keep what they typed and show a retry message.

2. **Missing event facts (a member can't act on this page).** The page doesn't say when, where, or what to bring. Add these, and fill in the placeholders yourself: `[date and start time]`, `[location / parking note]`, `[what to bring, e.g. warm layers]`, `[contact for questions]`, and `[what happens if weather cancels]`. I did not invent any of these.

3. **Blank name passes validation.** Submitting with no name shows "You are on the list: , party of 2." Fix:

   Markup, after the name input:
   ```html
   <input id="name" name="name" autocomplete="name" required aria-describedby="name-err">
   <p class="err" id="name-err" hidden>Please enter your name so we know who to expect.</p>
   ```

   Script, replacing the existing `<script>` block:
   ```html
   <script>
   const f=document.getElementById('f'),name=document.getElementById('name'),nameErr=document.getElementById('name-err'),
   n=document.getElementById('n'),e=document.getElementById('n-err'),s=document.getElementById('status');
   f.addEventListener('submit',ev=>{ev.preventDefault();
   const who=name.value.trim(),v=n.value.trim()===''?NaN:Number(n.value),
   nameBad=!who,bad=!(Number.isInteger(v)&&v>=1&&v<=8);
   nameErr.hidden=!nameBad;name.setAttribute('aria-invalid',nameBad);
   e.hidden=!bad;n.setAttribute('aria-invalid',bad);s.textContent='';
   if(nameBad){name.focus();return}
   if(bad){n.focus();return}
   s.textContent='You are on the list: '+who+', party of '+v+'. See you under the stars.'});
   </script>
   ```

4. **Fractional headcounts pass.** "2.5" is accepted because the check only tests the range. The new `Number.isInteger` check above fixes this.

5. **No way to withdraw or change a sign-up.** Leaving should be as easy as joining. Add a line such as "To change or cancel, email [contact]," or decide that a second sign-up is the way to change it. This is a decision for you.

6. **The "sign up in two parts" rule.** Groups over 8 are told to submit twice. Confirm that's what you want, since each part will be recorded as a separate entry with the same name.

**Not checked:** I read the code but did not run it in a browser, with a screen reader, on a phone, or at 200% zoom. I also did not test the dark theme visually.
