---
title: Command Injection Prevention
impact: CRITICAL
impactDescription: A single unescaped shell argument yields full server takeover under the PHP user
tags: security, exec, shell, php8
---

# Command Injection Prevention

Avoid spawning shells entirely. When unavoidable, pass arguments through `escapeshellarg()` and use the array-form `proc_open()` — never interpolate variables into command strings.

## Bad Example

```php
<?php

// $filename = "report.pdf; rm -rf /" or "report.pdf && cat .env"
exec("pdftotext {$filename} out.txt");

shell_exec("convert {$_GET['image']} -resize 100x100 thumb.png");

system("git pull origin " . $_POST['branch']);

passthru("ffmpeg -i {$input} -v quiet {$output}");  // spaces alone break this too
```

## Good Example

```php
<?php

declare(strict_types=1);

// Preferred: no shell at all - native extensions and process arrays
$imagick = new Imagick();
$imagick->readImage($uploadPath);
$imagick->thumbnailImage(100, 100);
$imagick->writeImage($thumbPath);

// Unavoidable external binary: array argv + escapeshellarg per argument
function pdfToText(string $filename, string $workDir): string
{
    if (str_contains($filename, "\0") || !is_file("$workDir/$filename")) {
        throw new ValidationException(['file' => 'invalid']);
    }
    $cmd = [
        '/usr/bin/pdftotext',          // absolute path - no PATH hijacking
        escapeshellarg("$workDir/$filename"),
        '-',
    ];
    $proc = proc_open($cmd, [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes);
    if (!is_resource($proc)) {
        throw new RuntimeException('pdftotext failed to start');
    }
    $text = stream_get_contents($pipes[1]);
    $stderr = stream_get_contents($pipes[2]);
    $code = proc_close($proc);
    if ($code !== 0) {
        throw new RuntimeException("pdftotext exited {$code}: {$stderr}");
    }
    return $text;
}
```

## Why

- **`escapeshellarg()`** wraps the value in single quotes and escapes embedded quotes, making metacharacter injection (`;`, `&&`, backticks) inert.
- **Array-form `proc_open()`** bypasses `sh -c` string parsing entirely on POSIX — argument boundaries are structural, not parsed.
- **Absolute binary paths** prevent a manipulated `PATH` from substituting a malicious executable.
- Best of all is not shelling out: prefer native PHP libraries (`Imagick`, `php-gpg`) or queue binaries behind an internal API that validates input types itself.

Reference: [OWASP Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Command_Injection_Defense_Cheat_Sheet.html)
