# PHP Naming Conventions (PSR-1 / PSR-12)

The baseline for plain PHP and the base standard that Laravel and Symfony inherit. From the PHP-FIG official standards.

## Element table

| Element | Convention | Example |
|---|---|---|
| Namespace | `Vendor\Package\...` StudlyCaps segments | `Acme\Billing\Invoice` |
| Class | StudlyCase (PascalCase) | `InvoiceRepository` |
| File | MUST end with the class it contains (PSR-4 autoload) | `src/Billing/InvoiceRepository.php` |
| Method | camelCase | `getTotalAmount()` |
| Class constant | UPPER_SNAKE_CASE | `self::STATUS_PAID` |
| Property | camelCase; **no `_` prefix for private/protected** (PSR-12 explicitly forbids) | `$this->totalAmount` |
| Local variable | camelCase (community default; PSR-12 leaves it open) | `$invoiceTotal` |
| Interface | StudlyCase, suffixed per project convention (`-Interface` common in legacy) | `PaymentGatewayInterface` |
| Trait | StudlyCase, `-Trait` suffix common | `LoggableTrait` |
| Enum | StudlyCase, cases PascalCase or UPPER_SNAKE (project choice — be consistent) | `InvoiceStatus::Paid` |

## Rules worth remembering

- One class per file by PSR-1 side effects rule: files either declare symbols **or** execute logic, never both.
- `declare(strict_types=1)` on line 1, then namespace — the modern file skeleton.
- Abstract classes carry no mandated prefix (`AbstractMapper` is a common project choice).

## Sources

- [PSR-1: Basic Coding Standard](https://www.php-fig.org/psr/psr-1/)
- [PSR-12: Extended Coding Style](https://www.php-fig.org/psr/psr-12/)
- [PSR-4: Autoloading](https://www.php-fig.org/psr/psr-4/)
