---
title: Security Headers & CSP
impact: HIGH
impactDescription: Missing response headers leaves XSS, clickjacking, and sniffing defenses switched off at the browser
tags: security, headers, csp, php8
---

# Security Headers & CSP

Send defensive headers on every response — they cost one line each and switch on browser-side protections your application code cannot provide alone. A Content-Security-Policy is the strongest XSS mitigation available.

## Bad Example

```php
<?php

// No security headers at all - browser defaults apply (i.e., almost none)
echo "<h1>{$_GET['name']}</h1>";   // reflected XSS now executes freely

// Inline scripts + inline handlers everywhere make a strict CSP impossible later
echo '<button onclick="track()">Buy</button>';
```

## Good Example

```php
<?php

declare(strict_types=1);

final class SecurityHeaders
{
    public static function send(string $cspNonce): void
    {
        header('Content-Security-Policy: '
            . "default-src 'self'; "
            . 'script-src \'self\' \'nonce-' . $cspNonce . '\'; '
            . "style-src 'self'; "
            . 'img-src \'self\' data:; '
            . "object-src 'none'; "
            . 'frame-ancestors \'none\'; '
            . 'base-uri \'self\'');
        header('X-Content-Type-Options: nosniff');
        header('Referrer-Policy: strict-origin-when-cross-origin');
        // Only if the site is fully HTTPS and stays that way:
        header('Strict-Transport-Security: max-age=31536000; includeSubDomains');
        // Permissions policy: deny everything not explicitly used
        header('Permissions-Policy: camera=(), microphone=(), geolocation=()');
    }
}

// Nonce per response for the inline scripts you genuinely need:
$cspNonce = bin2hex(random_bytes(16));
SecurityHeaders::send($cspNonce);
?>
<script nonce="<?= htmlspecialchars($cspNonce, ENT_QUOTES, 'UTF-8') ?>">
    initPage();
</script>
```

## Why

- **CSP with nonces** replaces the blocklist game of XSS filtering: injected `<script>` tags simply do not execute without the per-response nonce.
- **`frame-ancestors 'none'`** (or `SAMEORIGIN`) is the modern anti-clickjacking control — `X-Frame-Options` remains only as legacy support.
- **`nosniff`** stops MIME-confusion attacks where user uploads are reinterpreted as scripts or stylesheets.
- Start in report-only mode (`Content-Security-Policy-Report-Only`) when retrofitting CSP to an existing app, collect violation reports, then enforce.

Reference: [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) · [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)
