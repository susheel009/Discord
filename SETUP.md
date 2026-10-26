# Private Discord setup and review checklist

This deployment is **Hermes**, with the supplied bot identity **HermesBot#9321**, for the private **Hermes Cornerstone** team. The human/account operator is GitHub user **susheel009**; the bot is not a legal person. These pages are not a legal opinion, security certification, or Discord approval.

## What is actually required?

- **App verification:** Discord says verification is required to scale past 100 servers. A personal/private deployment does not need to pursue that scale merely to use the gateway.[1]
- **Privacy policy:** Discord requires an accurate, publicly available, up-to-date policy describing collection, use, sharing, storage/retention, and how users request deletion.[2]
- **Terms of Service:** Discord lists connected public Terms of Service and Privacy Policy among App Directory requirements. Directory discovery is separate from private bot access.[3]
- **Support Server:** a Discord community support-server link is an App Directory requirement; an HTML support page is not a replacement for that field.[3]
- **Interactions Endpoint:** do not point this at a static page. The standard Hermes Discord integration uses the Discord Gateway, not a stateless HTTP interaction webhook.[4]
- **Linked Roles Verification URL:** leave it empty unless you separately implement Discord Linked Roles. This policy site implements no such endpoint.

## Links to paste into General Information

| Portal field | Value |
| --- | --- |
| Terms of Service URL | https://susheel009.github.io/Discord/terms.html |
| Privacy Policy URL | https://susheel009.github.io/Discord/privacy.html |
| Interactions Endpoint URL | Leave blank for the standard Hermes Gateway |
| Linked Roles Verification URL | Leave blank; linked roles are not implemented |

Optional website/support references:

- Overview: https://susheel009.github.io/Discord/
- Support: https://susheel009.github.io/Discord/support.html
- Data deletion: https://susheel009.github.io/Discord/data-deletion.html

Suggested application description, after you have configured the gateway:

> Private AI assistant for the Hermes Cornerstone team, powered by Hermes Agent. Helps explicitly authorized users with questions, research, files, and approved tool-based tasks through Discord.

## Private gateway checklist — not completed by publishing the site

Hermes documents the following setup steps and security controls.[4]

- [ ] Confirm the bot identity and application name in the Developer Portal.
- [ ] Enable the intents required by the installed Hermes adapter; the current Hermes guide calls for Message Content and Server Members. Presence is optional. Save changes.
- [ ] Use Guild Install with `bot` and `applications.commands` scopes. Grant only the permissions needed; do not grant Administrator simply to make setup easier.
- [ ] For a private bot, leave Public Bot off and use the documented manual invite method. Leave Require OAuth2 Code Grant off for the normal bot gateway. A Discord-provided install link requires Public Bot on; do not accidentally open the bot just to obtain that link.
- [ ] Configure the bot token securely in Hermes's messaging setup. Never send it to chat, put it in a policy page, or commit it to GitHub.
- [ ] Authorize only your Discord user ID and any individually approved teammates. Review any role/channel-based authorizations too. Do not enable `GATEWAY_ALLOW_ALL_USERS` or `DISCORD_ALLOW_ALL_USERS` for this private deployment.
- [ ] Prefer a dedicated private bot channel. Review channel-history backfill: nearby messages may enter AI context when the bot is mentioned. Disable backfill if it is not needed, and inform everyone in any channel the bot can read.
- [ ] Run the gateway, send a DM or authorized channel mention, and verify a reply. Then confirm an unapproved account cannot invoke the assistant.
- [ ] Restrict tool permissions and connected accounts. An admin/user slash-command split is not a full tool sandbox; ordinary authorized chat can still cause tool use.
- [ ] Make the policy links easy to find in the private server, such as a pinned message.

## Operational/privacy review before real team data

Discord requires good privacy and security practices, including deletion when API data is no longer necessary and encryption of stored API data at rest. Publishing words is not evidence that these controls are active.[2]

- [ ] Review the Terms and Privacy Policy and adopt them only if they match actual operation and applicable law. Obtain qualified legal advice if needed.
- [ ] Ensure authorized users have a working private route to the human operator. No public email was supplied, so the pages use the existing team administrator plus a minimal public GitHub contact request. Monitor repository issues. A dedicated privacy email would make this easier.
- [ ] Verify the actual AI-provider account's data-use, training, retention, and transfer terms/settings before sending Discord data. Do not assume OpenAI API-specific controls apply identically to a Codex/OAuth account. Configure providers consistently with Discord's restrictions.
- [ ] Inventory optional tools that can receive prompt/context data and inform teammates of enabled providers. Update the policy before material processing changes.
- [ ] Verify encryption at rest for the runtime disk and any backups, restrict filesystem/account access, and secure credentials. None of these controls was certified by creating this site.
- [ ] Define a retention review schedule. Persistent transcripts and memories do not disappear on `/new`, `/reset`, or a gateway restart.
- [ ] Exercise a deletion request using non-sensitive test content. Locate the account's session data, transcripts, memories, attachment cache, files, logs, exports, and any backups. Remove only the intended data with the installed Hermes version's supported procedures; do not delete the entire shared profile to satisfy one user's request.
- [ ] Confirm the operator can acknowledge and complete requests within the deadlines applicable to the request. Do not promise automatic erasure or a fixed retention period without implementing it.
- [ ] Keep bot configuration, runtime data, and secrets out of this public repository.

## Publication is not verification

These pages provide public policy links and instructions only. They do **not** verify identity, enable privileged intents, submit a Discord application review, configure or start the Hermes gateway, prove provider compliance, or certify the app's runtime behavior. If you later pursue App Directory discovery, use the live Developer Portal checklist; additional requirements include the description, tags, install URL, support server, and app verification.[1][3]

## Sources

[1] https://support-dev.discord.com/hc/en-us/articles/23926564536471-How-Do-I-Get-My-App-Verified
[2] https://support-dev.discord.com/hc/en-us/articles/8562894815383-Discord-Developer-Terms-of-Service
[3] https://support-dev.discord.com/hc/en-us/articles/6378525413143-App-Directory-App-profile-pages
[4] https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord
