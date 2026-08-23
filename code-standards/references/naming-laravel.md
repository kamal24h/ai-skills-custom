# Laravel Naming Conventions

Laravel's documented conventions (framework defaults + docs). Base standard: PHP PSR — class/method/property casing follows [`php.md`](php.md).

## Element table

| Element | Convention | Example |
|---|---|---|
| Model | singular PascalCase | `User`, `OrderItem` |
| Table (auto-derived) | snake_case plural of model | `users`, `order_items` |
| Pivot table | alphabetical singular names joined by `_` | `post_user` |
| Primary / foreign key | `id` / `{snake_model}_id` | `order_id` |
| Controller | PascalCase + `Controller` suffix, actions per resource verbs | `OrderController::store()` |
| Migration file | snake_case with verb phrases | `create_users_table`, `add_votes_to_users_table` |
| Seeder | PascalCase + `Seeder` | `UserSeeder` |
| Factory | PascalCase + `Factory` | `OrderFactory` |
| Event | PascalCase, present/past tense noun | `OrderShipped` |
| Listener | PascalCase + role suffix | `SendShipmentNotification` |
| Job | PascalCase + verb phrase | `ProcessPodcast` |
| Policy | PascalCase + `Policy` matching model | `OrderPolicy` |
| Request (form) | PascalCase + `Request` | `StoreOrderRequest` |
| Resource (API) | PascalCase + `Resource` | `OrderResource` |
| Command class / signature | PascalCase + `Command` / kebab-case signature | `SendEmailsCommand`, `mail:send {user}` |
| Config file & keys | snake_case filename and keys | `config/services.php` → `'stripe' => [...]` |
| Env variable | UPPER_SNAKE_CASE | `STRIPE_SECRET_KEY` |
| Blade view | snake_case path | `emails/orders/shipped.blade.php` |
| Route URI | kebab-case, plural nouns | `/pending-orders` |
| Route name | dot notation, lowercase | `orders.show` |
| Artisan command options | kebab-case flags | `--force`, `--queue=` |

## Rules worth remembering

- Eloquent derives table names automatically (`OrderItem` → `order_items`) — deviating means naming the table explicitly; prefer staying on the default.
- Relationship methods read as the relation: `belongsTo(User::class)` in `author()`; collections plural (`comments()`), single camelCase (`latestComment`).
- Accessor/mutator attribute names are camelCase matching the virtual attribute (`full_name` column ↔ `getFullNameAttribute()` legacy style).

## Sources

- [Laravel Directory Structure](https://laravel.com/docs/13.x/structure)
- [Laravel Eloquent: Conventions](https://laravel.com/docs/13.x/eloquent#eloquent-model-conventions)
- [Laravel Migrations](https://laravel.com/docs/13.x/migrations)
- [Laravel Routing](https://laravel.com/docs/13.x/routing)
- [Laravel Artisan Console](https://laravel.com/docs/13.x/artisan)
