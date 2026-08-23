---
title: Session Security
impact: CRITICAL
impactDescription: Fixated or hijacked sessions grant full account takeover without ever touching passwords
tags: security, sessions, cookies, php8
---

# Session Security

Configure session cookies defensively, regenerate IDs at privilege changes, and rely on PHP's strict mode — session fixation and hijacking are prevented by configuration, not by hope.

## Bad Example

```php
<?php

session_start(); // defaults: cookie flags off, ID accepted from URL/cookie as-is

// After login, keep the same session id -> fixation succeeds:
// attacker plants ?PHPSESSID=attacker-known-id, victim logs in,
// attacker replays the now-authenticated id.

setcookie('remember', $token, time() + 31536000); // no Secure/HttpOnly flags
```

## Good Example

```php
<?php

declare(strict_types=1);

$secure = [
    'cookie_httponly' => '1',          // JS cannot read the session cookie
    'cookie_secure'   => '1',          // HTTPS only
    'cookie_samesite' => 'Strict',     // CSRF surface reduction
    'use_strict_mode' => '1',          // reject uninitialized/attacker-supplied IDs
    'cookie_lifetime' => '0',          // browser-session cookie; server-side TTL governs
    'gc_maxlifetime'  => '1800',       // 30 min idle timeout for authenticated apps
];
session_start($secure);

// Regenerate on every privilege change - kills fixation:
session_regenerate_id(true);

// Bind to a fingerprint and re-check (defense in depth, not a substitute for TLS):
$expected = hash('sha256', $_SERVER['HTTP_USER_AGENT'] ?? '');
if (!isset($_SESSION['fingerprint'])) {
    $_SESSION['fingerprint'] = $expected;
} elseif (hash_equals($_SESSION['fingerprint'], $expected) === false) {
    session_unset();
    session_destroy();
    throw new SecurityException('Session fingerprint mismatch');
}

// Logout = destroy server-side, not just unset client array:
$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $p = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000, $p['path'], $p['domain'], (bool)$p['secure'], (bool)$p['httponly']);
}
session_destroy();
```

## Why

- **`use_strict_mode=1`** is the single most effective anti-fixation setting: PHP rejects uninitialized session identifiers instead of adopting them.
- **`session_regenerate_id(true)`** after login and after any permission elevation invalidates pre-authentication tokens an attacker may know.
- **`HttpOnly` + `Secure` + `SameSite`** remove the three cheapest hijack vectors: XSS cookie theft, plain-HTTP sniffing, cross-site sending.
- Server-side storage of session data (`Redis`/DB handlers) lets you invalidate a specific session immediately — file sessions make remote revocation impractical.

Reference: [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
