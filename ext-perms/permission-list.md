# Chromium-based Browser Extension Permissions Reference

This document lists common Chrome extension permissions along with their purpose and **security risk severity**, based on behavior observed in professional auditing tools like CRXcavator, Extension Risk Analyzer, and Mozilla's extension API guidelines.

> **Legend**  
> - 🟢 Low: Minimal or no security risk  
> - 🟡 Medium: Contextual risk, depending on implementation  
> - 🔴 High: Dangerous if misused; often exploited in malicious extensions

---

## 🔴 High-Risk Permissions

| Permission          | Description                                                                 | Severity |
|---------------------|-----------------------------------------------------------------------------|----------|
| `tabs`              | Read, modify, and navigate user tabs.                                       | 🔴 High   |
| `webRequest`        | Intercept and modify HTTP requests.                                         | 🔴 High   |
| `webRequestBlocking`| Block requests before they are sent.                                        | 🔴 High   |
| `<all_urls>`        | Grants access to **every** website visited.                                 | 🔴 High   |
| `host_permissions`  | Alternative to `<all_urls>`, site-specific — still powerful.                | 🔴 High   |
| `cookies`           | Access or modify browser cookies.                                           | 🔴 High   |
| `history`           | Access the user's full browsing history.                                    | 🔴 High   |
| `clipboardRead`     | Read content from clipboard.                                                | 🔴 High   |
| `clipboardWrite`    | Write to clipboard (used with read = exploit risk).                         | 🔴 High   |
| `management`        | Manage other extensions — can disable, enable, or gather data.              | 🔴 High   |
| `debugger`          | Attach to and inspect pages like a dev tool (extremely dangerous).          | 🔴 High   |

---

## 🟡 Medium-Risk Permissions

| Permission        | Description                                                      | Severity |
|-------------------|------------------------------------------------------------------|----------|
| `storage`         | Store data locally (safe, but can be used to persist trackers).  | 🟡 Medium |
| `notifications`   | Show desktop/browser notifications.                              | 🟡 Medium |
| `contextMenus`    | Add custom context (right-click) menu items.                     | 🟡 Medium |
| `downloads`       | Download files without user input.                               | 🟡 Medium |
| `geolocation`     | Access user's physical location.                                 | 🟡 Medium |
| `identity`        | OAuth2 login access (can be used to impersonate users).          | 🟡 Medium |
| `bookmarks`       | Read/write user bookmarks.                                       | 🟡 Medium |
| `topSites`        | Access most visited websites.                                    | 🟡 Medium |

---

## 🟢 Low-Risk Permissions

| Permission        | Description                                           | Severity |
|-------------------|-------------------------------------------------------|----------|
| `activeTab`       | Temporary access to the currently active tab.         | 🟢 Low    |
| `alarms`          | Run background scripts on a schedule.                 | 🟢 Low    |
| `idle`            | Detect if user is idle.                               | 🟢 Low    |
| `runtime`         | Internal extension status monitoring.                 | 🟢 Low    |
| `storage`         | Local storage of config and settings.                 | 🟢 Low    |
| `unlimitedStorage`| Allow storage beyond quota (safe alone).              | 🟢 Low    |
| `tts`             | Use text-to-speech APIs.                              | 🟢 Low    |
| `tabsExecuteScript` | Only when used for direct user interaction.         | 🟢 Low    |

---

## 🧠 Notes

- A single **low-risk** permission is usually not a threat.
- Multiple **medium-risk** + 1 **high-risk** = **significant attack surface**.
- Permissions should be evaluated **in context of extension behavior** (e.g., `tabs` + external script = danger).

---

## References

- [Chrome Extension Manifest Permissions](https://developer.chrome.com/docs/extensions/mv3/declare_permissions/)
- [Mozilla WebExtensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)
- [CRXcavator Permission Risk Grading](https://crxcavator.io/)
- [Extension Police Whitepaper](https://extensionpolice.com/)

---

**Use this as your audit baseline** when reviewing extensions or flagging permissions via your Bash tool.
