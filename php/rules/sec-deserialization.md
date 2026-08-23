---
title: Unsafe Deserialization
impact: CRITICAL
impactDescription: Unserializing attacker-controlled data enables remote code execution (POP chains)
tags: security, serialization, php8
---

# Unsafe Deserialization

Never call `unserialize()` on input an attacker can influence. Use `json_decode()` for data exchange; when PHP serialization is unavoidable, use `allowed_classes: false`.

## Bad Example

```php
<?php

// RCE gadget chains: any class in the autoload graph with magic methods
// (__destruct, __wakeup, __toString) becomes a weapon:
$cart = unserialize($_COOKIE['cart']);          // attacker-controlled payload

$state = unserialize($requestBody);             // same, from POST body

// allow_classes does not help here - default is ALL classes allowed
$config = unserialize(base64_decode($row['blob']));
```

## Good Example

```php
<?php

declare(strict_types=1);

// Data exchange: JSON carries values, never executable object graphs
$cart = json_decode($_COOKIE['cart'] ?? '{}', true, flags: JSON_THROW_ON_ERROR);
assert(is_array($cart));

// Validate decoded structure against your schema before use
if (!isset($cart['items']) || !is_array($cart['items'])) {
    throw new ValidationException(['cart' => 'malformed']);
}

// Legacy PHP-serialized blobs you cannot migrate yet - forbid instantiation:
$data = unserialize($row['blob'], ['allowed_classes' => false]);
// Result contains only __PHP_Incomplete_Class placeholders - safe values only

// Signing does not replace the above, but detects tampering of stored blobs:
$mac = hash_hmac('sha256', $blob, $key);
if (!hash_equals($mac, $storedMac)) {
    throw new SecurityException('Blob signature mismatch');
}
```

## Why

- **`unserialize()` triggers magic methods** (`__wakeup`, `__destruct`) during reconstruction — attackers chain these "gadgets" through popular libraries into file writes or command execution. This is PHP's most notorious RCE class.
- **`json_decode()`** produces plain arrays/scalars — there is no object graph to weaponize.
- **`['allowed_classes' => false]`** keeps legacy blobs readable while eliminating instantiation entirely.
- **HMAC-signing stored serialized blobs** prevents substitution attacks but does not make `unserialize()` safe for user input — it protects storage integrity only.

Reference: [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
