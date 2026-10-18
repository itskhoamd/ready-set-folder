## 8. Rules for client work
1. **One folder per client**, copied from `clients/_CLIENT-TEMPLATE/`, named `<PREFIX>_<client-name>`. The prefix comes from the initials (clash → add a number). Use it in file names and codes.
2. **Client data stays in its own client folder.** Never copy one client's data into another client's folder or into `templates/`: turn it into placeholders first.
3. **Client keys live in the client's own accounts or a credential store.** The client card only says where they are.
4. **Client-facing documents are written in the client's language**, in your brand's look, and checked by the human.
5. **Nothing goes to a client** (message, file, invoice, price) without the human's OK.
6. **Each client folder has its own `HANDOFF.md` and `CHANGELOG.md`.** `_system/HANDOFF.md` sums up across clients.
7. **Leads live in `pipeline/LEADS.md`** until they say yes; then they get a client folder.
8. **Never share or publish this workspace with real client folders in it.** `.gitignore` keeps real client folders out of git, but `pipeline/LEADS.md` and your notes are still personal: keep any repo of this workspace **private**.
