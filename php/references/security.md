# PHP Security

Input validation, output escaping, SQL, password storage, and file uploads — mapped to OWASP Top 10.

## When to Load

- Handling any value that originated outside the process (request, file, queue, third-party API)
- Writing or reviewing SQL, especially anything built with string concatenation
- Implementing authentication, password storage, or session handling
- Accepting file uploads
- Performing a security review or audit

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Injection (SQL, command, path) | CRITICAL | `sec-` |
| 2 | Output escaping (XSS) | CRITICAL | `sec-` |
| 3 | Authentication & password storage | CRITICAL | `sec-` |
| 4 | Input validation & file uploads | CRITICAL | `sec-` |

## Rule Index

- [`sec-sql-prepared`](../rules/sec-sql-prepared.md) — Prepared statements with bound parameters, always
- [`sec-output-escaping`](../rules/sec-output-escaping.md) — Escape at output, per context
- [`sec-input-validation`](../rules/sec-input-validation.md) — Validate against an allow-list at the boundary
- [`sec-password-hashing`](../rules/sec-password-hashing.md) — `password_hash()` / `password_verify()`
- [`sec-file-uploads`](../rules/sec-file-uploads.md) — Verify type, size, and storage location

## Key Principles

### Validate on input, escape on output

These are different jobs and both are required.

- **Validation** answers "is this acceptable at all?" — an email that is not an email is rejected at the boundary.
- **Escaping** answers "how must this be encoded for where it is going?" — the same string needs different treatment in HTML, in an attribute, in JavaScript, in SQL, and in a shell command.

Sanitising on input and storing the mangled value is the common mistake: it corrupts legitimate data (`O'Brien` becomes `O\'Brien` in the database) and still does not protect the contexts you forgot.

### SQL — parameters are not string interpolation

```php
// ❌ injectable regardless of how the value was "cleaned"
$pdo->query("SELECT * FROM users WHERE email = '{$email}'");

// ✅ the value never becomes part of the parsed statement
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $email]);
```

Two details that matter:

1. **Emulated prepares.** With `PDO::ATTR_EMULATE_PREPARES` on (the historical default for MySQL), PDO interpolates client-side. Turn it off so the driver sends a real prepared statement:
   ```php
   new PDO($dsn, $user, $pass, [
       PDO::ATTR_EMULATE_PREPARES   => false,
       PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
       PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
   ]);
   ```
2. **Identifiers cannot be bound.** Table names, column names, and `ORDER BY` direction are not parameterisable. Validate them against an allow-list:
   ```php
   $column = match ($request->sort) {
       'name', 'created_at', 'total' => $request->sort,
       default => 'created_at',
   };
   ```

### Escaping is context-dependent

| Output context | Function |
|---|---|
| HTML body | `htmlspecialchars($v, ENT_QUOTES \| ENT_SUBSTITUTE, 'UTF-8')` |
| HTML attribute | Same, and always quote the attribute |
| URL query parameter | `rawurlencode()` |
| JavaScript data | `json_encode($v, JSON_HEX_TAG \| JSON_HEX_AMP \| JSON_HEX_APOS \| JSON_HEX_QUOT)` |
| Shell argument | `escapeshellarg()` — or avoid shelling out |
| SQL value | Bound parameter (not a function) |

`ENT_QUOTES` matters — without it single quotes pass through and break out of `attr='…'`. `ENT_SUBSTITUTE` replaces invalid UTF-8 instead of returning an empty string, which otherwise silently blanks the whole output.

Never place user data inside a `<script>` block, an event handler attribute, or a `javascript:` URL. There is no escaping function that makes that safe in general.

### Passwords

```php
$hash = password_hash($plain, PASSWORD_DEFAULT);      // bcrypt today, follows the language forward
if (password_verify($plain, $hash)) {
    if (password_needs_rehash($hash, PASSWORD_DEFAULT)) {
        $repository->updateHash($user, password_hash($plain, PASSWORD_DEFAULT));
    }
}
```

- `PASSWORD_DEFAULT` is deliberately not pinned — it moves as the language's recommendation moves, and `password_needs_rehash()` is how existing hashes migrate. Pin an algorithm only if you must match an external system.
- `PASSWORD_ARGON2ID` is available where libargon2 is compiled in and is the stronger choice when you control the deployment.
- `password_verify()` is constant-time. Never compare hashes with `===`; for other secrets use `hash_equals()`.
- Never truncate or pre-hash passwords with `md5`/`sha1`, and never store a reversible encryption of them.

Rate-limit authentication attempts per account **and** per IP, and make the failure response identical for "unknown user" and "wrong password" — a differing message or timing is a user-enumeration oracle.

### File uploads

The dangerous default is trusting `$_FILES['x']['type']` and the client-supplied filename. Both are attacker-controlled.

```php
$file = $request->files->get('avatar');

// 1. did the upload actually succeed
if ($file->getError() !== UPLOAD_ERR_OK) { … }

// 2. determine type from content, not from the request
$mime = (new finfo(FILEINFO_MIME_TYPE))->file($file->getPathname());
if (!in_array($mime, ['image/jpeg', 'image/png', 'image/webp'], true)) { … }

// 3. generate the stored name — never reuse the client's
$name = bin2hex(random_bytes(16)) . '.' . $extensionFromMime[$mime];

// 4. store outside the web root, serve through a controller
$file->move($this->privateUploadDir, $name);
```

Additional requirements: enforce a size limit in application code as well as `upload_max_filesize`/`post_max_size`; strip or regenerate image metadata; never `include`/`require` an uploaded path; and if uploads must live under the web root, disable script execution for that directory at the web-server level.

### Other essentials

- **Randomness**: `random_bytes()` / `random_int()` for anything security-relevant. `rand()`, `mt_rand()`, and `uniqid()` are predictable.
- **Sessions**: `session_regenerate_id(true)` on privilege change; cookies `HttpOnly`, `Secure`, `SameSite=Lax` or `Strict`.
- **Mass assignment**: never hydrate an entity straight from `$_POST`; list the fields you accept.
- **Path traversal**: `realpath()` the resolved path and verify it is still inside the intended base directory.
- **Deserialization**: never `unserialize()` untrusted input — use `json_decode()`.
- **Secrets**: environment variables or a secret manager; never committed, never in a client-reachable file.
- **Error output**: `display_errors=Off` in production; log instead. Stack traces name file paths, library versions, and query fragments.

## OWASP Top 10 Mapping

| OWASP | Rule |
|---|---|
| A01 Broken Access Control | Authorisation checks per action (see the framework skill) |
| A02 Cryptographic Failures | [`sec-password-hashing`](../rules/sec-password-hashing.md) |
| A03 Injection | [`sec-sql-prepared`](../rules/sec-sql-prepared.md), [`sec-output-escaping`](../rules/sec-output-escaping.md) |
| A04 Insecure Design | [`solid-dip`](../rules/solid-dip.md), boundary validation |
| A05 Security Misconfiguration | `display_errors`, session flags, upload dirs |
| A08 Data Integrity Failures | [`sec-file-uploads`](../rules/sec-file-uploads.md), no `unserialize()` |

## Sources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [OWASP — Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [PHP Manual — Password hashing](https://www.php.net/manual/en/book.password.php)
- [PHP Manual — Handling file uploads](https://www.php.net/manual/en/features.file-upload.php)
- [PHP Manual — PDO prepared statements](https://www.php.net/manual/en/pdo.prepared-statements.php)
