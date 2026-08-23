# Symfony Naming Conventions

From Symfony's official coding standards and framework defaults. Base standard: PHP PSR — see [`php.md`](php.md).

## Element table

| Element | Convention | Example |
|---|---|---|
| Class | PascalCase | `InvoiceCalculator` |
| Controller class | PascalCase + `Controller` suffix; action `__invoke` preferred | `BlogController`, action `show()` |
| Service id | FQCN by default (autowiring); snake_case for named ids | `App\Service\InvoiceCalculator` / `'app.invoice_calculator'` |
| Entity (Doctrine) | PascalCase singular, in `Entity/` | `User`, `BlogPost` |
| Repository | PascalCase + `Repository` | `BlogPostRepository` |
| Table / column | snake_case (Doctrine default naming strategy) | `blog_post.created_at` |
| Form type | PascalCase + `Type` | `OrderType` |
| Twig template | snake_case + `.html.twig`; bundle layout: `bundles/AcmeBlogBundle/Blog/index.html.twig` | `blog/index.html.twig` |
| Event name (string) | dot-namespaced lowercase | `kernel.request`, `order.placed` |
| Event class | PascalCase past tense | `OrderPlaced` |
| Command class / name | PascalCase + `Command` / colon-namespace signature | `CreateUserController`, `app:create-user` |
| Twig extension / voter | PascalCase + role suffix (`Extension`, `Voter`) | `RoleVoter` |
| Bundle | PascalCase + `Bundle` (only when distributing reusable code) | `AcmeBlogBundle` |
| YAML config keys | snake_case | `default_locale: tr` |
| Route path | kebab/snake lowercase segments | `/blog/{slug}` |

## Rules worth remembering

- Modern Symfony apps rely on autowiring by type: name classes well and you rarely hand-write service ids at all.
- Voter attribute names are simple verbs/strings agreed with the domain (`EDIT`, `VIEW`) — checked literally via `is_granted('EDIT', $post)`.
- Template naming mirrors controller/action: `BlogController::show()` → `templates/blog/show.html.twig`.

## Sources

- [Symfony Coding Standards](https://symfony.com/doc/current/contributing/code/standards.html)
- [Symfony Service Container conventions](https://symfony.com/doc/current/service_container.html)
- [Symfony Templates (naming/placement)](https://symfony.com/doc/current/templates.html)
- [Symfony Console commands](https://symfony.com/doc/current/console.html)
